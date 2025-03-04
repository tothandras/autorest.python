import { getPagedResult, getLroMetadata } from "@azure-tools/typespec-azure-core";
import {
    getDoc,
    getSummary,
    ignoreDiagnostics,
    isErrorModel,
    ModelProperty,
    Namespace,
    Operation,
    EmitContext,
    listServices,
    Type,
    getNamespaceFullName,
} from "@typespec/compiler";
import {
    getAuthentication,
    getHttpOperation,
    getServers,
    HttpOperationParameter,
    HttpOperationResponse,
    HttpServer,
    HttpOperation,
} from "@typespec/http";
import { getAddedOnVersions } from "@typespec/versioning";
import {
    SdkClient,
    listClients,
    listOperationGroups,
    listOperationsInOperationGroup,
    isApiVersion,
    getDefaultApiVersion,
    getClientNamespaceString,
    createSdkContext,
    SdkContext,
    getLibraryName,
    getAllModels,
    isInternal,
    getPropertyNames,
    getEffectivePayloadType,
    getAccess,
} from "@azure-tools/typespec-client-generator-core";
import { getResourceOperation } from "@typespec/rest";
import { resolveModuleRoot, saveCodeModelAsYaml } from "./external-process.js";
import { dirname } from "path";
import { fileURLToPath } from "url";
import { execFileSync } from "child_process";
import { PythonEmitterOptions } from "./lib.js";
import { camelToSnakeCase } from "./utils.js";
import {
    CredentialType,
    CredentialTypeUnion,
    getConstantType,
    getType,
    KnownTypes,
    simpleTypesMap,
    typesMap,
} from "./types.js";

interface HttpServerParameter {
    type: "endpointPath";
    name: string;
    param: ModelProperty;
}

const defaultOptions = {
    "basic-setup-py": true,
    "package-version": "1.0.0b1",
};

let isArm: boolean = false;
export let modelsMode: string | undefined = undefined;

function setGlobalFlag(options: Record<string, any>, clients: SdkClient[]) {
    isArm = clients[0].arm;
    modelsMode = options["models-mode"] ?? (isArm ? "msrest" : "dpg");
    options["models-mode"] = modelsMode;
}

export async function $onEmit(context: EmitContext<PythonEmitterOptions>) {
    const program = context.program;
    const resolvedOptions = { ...defaultOptions, ...context.options };
    const sdkContext = createSdkContext(context);
    const clients = listClients(sdkContext);
    setGlobalFlag(resolvedOptions, clients);

    const root = await resolveModuleRoot(program, "@autorest/python", dirname(fileURLToPath(import.meta.url)));
    const outputDir = context.emitterOutputDir;
    const yamlMap = emitCodeModel(sdkContext, clients);
    const yamlPath = await saveCodeModelAsYaml("typespec-python-yaml-map", yamlMap);
    const commandArgs = [
        `${root}/run-python3.js`,
        `${root}/run_cadl.py`,
        `--output-folder=${outputDir}`,
        `--cadl-file=${yamlPath}`,
    ];

    for (const [key, value] of Object.entries(resolvedOptions)) {
        commandArgs.push(`--${key}=${value}`);
    }
    if (resolvedOptions.debug) {
        commandArgs.push("--debug");
    }
    if (isArm === true) {
        commandArgs.push("--azure-arm=true");
    }
    commandArgs.push("--from-typespec=true");
    if (!program.compilerOptions.noEmit && !program.hasError()) {
        execFileSync(process.execPath, commandArgs);
    }
}

const endpointPathParameters: Record<string, any>[] = [];
let apiVersionParam: Record<string, any> | undefined = undefined;
let subscriptionIdParam: Record<string, any> | undefined = undefined;

function getDocStr(context: SdkContext, target: Type): string {
    return getDoc(context.program, target) ?? "";
}

// To pass the yaml dump
function getAddedOnVersion(context: SdkContext, t: Type): string | undefined {
    const versions = getAddedOnVersions(context.program as any, t as any);
    if (versions !== undefined && versions.length > 0) {
        return versions[0].value;
    }
    return undefined;
}

type ParamBase = {
    optional: boolean;
    description: string;
    addedOn: string | undefined;
    clientName: string;
    inOverload: boolean;
};

function emitParamBase(context: SdkContext, parameter: ModelProperty | Type): ParamBase {
    let optional: boolean;
    let name: string;
    let description: string = "";
    let addedOn: string | undefined;

    if (parameter.kind === "ModelProperty") {
        optional = parameter.optional;
        name = getLibraryName(context, parameter);
        description = getDocStr(context, parameter);
        addedOn = getAddedOnVersion(context, parameter);
    } else {
        optional = false;
        name = "body";
    }

    return {
        optional,
        description,
        addedOn,
        clientName: camelToSnakeCase(name),
        inOverload: false,
    };
}

type BodyParameter = ParamBase & {
    contentTypes: string[];
    type: any;
    wireName: string;
    location: "body";
    defaultContentType: string;
};

function getBodyType(context: SdkContext, route: HttpOperation): Record<string, any> {
    let bodyModel = route.parameters.body?.type;
    if (bodyModel && bodyModel.kind === "Model" && route.operation) {
        const resourceType = getResourceOperation(context.program, route.operation)?.resourceType;
        if (resourceType && route.responses && route.responses.length > 0) {
            const resp = route.responses[0];
            if (resp && resp.responses && resp.responses.length > 0) {
                const responseBody = resp.responses[0]?.body;
                if (responseBody?.type?.kind === "Model") {
                    const bodyTypeInResponse = getEffectivePayloadType(context, responseBody.type);
                    // response body type is reosurce type, and request body type (if templated) contains resource type
                    if (
                        bodyTypeInResponse === resourceType &&
                        bodyModel.templateMapper &&
                        bodyModel.templateMapper.args.some((it) => {
                            return it.kind === "Model" || it.kind === "Union" ? it === bodyTypeInResponse : false;
                        })
                    ) {
                        bodyModel = resourceType;
                    }
                }
            }
        }
        if (resourceType && bodyModel.name === "") {
            bodyModel = resourceType;
        }
    }
    if (bodyModel && bodyModel.kind === "Scalar") {
        return getType(context, route.parameters.body!.parameter!);
    }
    return getType(context, bodyModel!);
}

function emitBodyParameter(context: SdkContext, httpOperation: HttpOperation): BodyParameter {
    const params = httpOperation.parameters;
    const body = params.body!;
    const base = emitParamBase(context, body.parameter ?? body.type);
    let contentTypes = body.contentTypes;
    if (contentTypes.length === 0) {
        contentTypes = ["application/json"];
    }
    const type = getBodyType(context, httpOperation);

    if (type.type === "model" && type.name === "") {
        type.name = capitalize(httpOperation.operation.name) + "Request";
    }

    return {
        contentTypes,
        type,
        wireName: body.parameter?.name ?? "body",
        location: "body",
        ...base,
        defaultContentType:
            body.parameter?.default ?? contentTypes.includes("application/json") ? "application/json" : contentTypes[0],
    };
}

function isSubscriptionId(param: Record<string, any>): boolean {
    return isArm && param.wireName === "subscriptionId";
}

function getDefaultApiVersionValue(context: SdkContext): string | undefined {
    const defaultApiVersion = getDefaultApiVersion(context, getServiceNamespace(context));
    if (!defaultApiVersion) {
        if (isArm) {
            const services = listServices(context.program);
            return services.length > 0 ? services[0].version : undefined;
        }
        return defaultApiVersion;
    }
    return defaultApiVersion.value;
}

function emitParameter(
    context: SdkContext,
    parameter: HttpOperationParameter | HttpServerParameter,
    implementation: string,
): Record<string, any> {
    const base = emitParamBase(context, parameter.param);
    base.clientName = camelToSnakeCase(getPropertyNames(context, parameter.param)[0]);
    let type = getType(context, parameter.param);
    let clientDefaultValue = undefined;
    if (parameter.name.toLowerCase() === "content-type" && type["type"] === "constant") {
        /// We don't want constant types for content types, so we make sure if it's
        /// a constant, we make it not constant
        clientDefaultValue = type["value"];
        type = type["valueType"];
    }
    const paramMap: Record<string, any> = {
        wireName: parameter.type === "path" ? parameter.param.name : parameter.name,
        location: parameter.type,
        type: type,
        implementation: implementation,
        skipUrlEncoding: parameter.type === "endpointPath",
    };
    if (type.type === "list" && (parameter.type === "query" || parameter.type === "header")) {
        if (parameter.format === "csv") {
            paramMap["delimiter"] = "comma";
        } else if ((parameter.format as string) === "ssv") {
            paramMap["delimiter"] = "space";
        } else if ((parameter.format as string) === "tsv") {
            paramMap["delimiter"] = "tab";
        } else if ((parameter.format as string) === "pipes") {
            paramMap["delimiter"] = "pipe";
        } else {
            paramMap["explode"] = true;
        }
    }

    if (paramMap.type.type === "constant") {
        clientDefaultValue = paramMap.type.value;
    }

    if (isApiVersion(context, parameter as HttpOperationParameter)) {
        const defaultApiVersion = getDefaultApiVersionValue(context);
        paramMap.type = defaultApiVersion ? getConstantType(defaultApiVersion) : KnownTypes.string;
        paramMap.implementation = "Client";
        paramMap.in_docstring = false;
        paramMap.isApiVersion = true;
        if (defaultApiVersion) {
            clientDefaultValue = defaultApiVersion;
        }
    }
    if (isSubscriptionId(paramMap)) {
        paramMap.implementation = "Client";
    }
    return { clientDefaultValue, ...base, ...paramMap };
}

function emitContentTypeParameter(
    bodyParameter: Record<string, any>,
    inOverload: boolean,
    inOverriden: boolean,
): Record<string, any> {
    return {
        checkClientInput: false,
        clientDefaultValue: bodyParameter.defaultContentType,
        clientName: "content_type",
        delimiter: null,
        description: `Body parameter Content-Type. Known values are: ${bodyParameter.contentTypes}.`,
        implementation: "Method",
        inDocstring: true,
        inOverload: inOverload,
        inOverriden: inOverriden,
        location: "header",
        optional: true,
        wireName: "Content-Type",
        type: KnownTypes.string,
    };
}

function emitFlattenedParameter(
    bodyParameter: Record<string, any>,
    property: Record<string, any>,
): Record<string, any> {
    return {
        checkClientInput: false,
        clientDefaultValue: null,
        clientName: property.clientName,
        delimiter: null,
        description: property.description,
        implementation: "Method",
        inDocstring: true,
        inFlattenedBody: true,
        inOverload: false,
        inOverriden: false,
        isApiVersion: bodyParameter["isApiVersion"],
        location: "other",
        optional: property["optional"],
        wireName: null,
        skipUrlEncoding: false,
        type: property["type"],
        defaultToUnsetSentinel: true,
    };
}

function emitAcceptParameter(inOverload: boolean, inOverriden: boolean): Record<string, any> {
    return {
        checkClientInput: false,
        clientDefaultValue: "application/json",
        clientName: "accept",
        delimiter: null,
        description: "Accept header.",
        explode: false,
        groupedBy: null,
        implementation: "Method",
        inDocstring: true,
        inOverload: inOverload,
        inOverriden: inOverriden,
        location: "header",
        optional: false,
        wireName: "Accept",
        skipUrlEncoding: false,
        type: getConstantType("application/json"),
    };
}

function emitResponseHeaders(context: SdkContext, response: HttpOperationResponse): Record<string, any>[] {
    const headers: Record<string, any>[] = [];
    for (const innerResponse of response.responses) {
        if (innerResponse.headers && Object.keys(innerResponse.headers).length > 0) {
            for (const [key, value] of Object.entries(innerResponse.headers)) {
                headers.push({
                    type: getType(context, value),
                    wireName: key,
                });
            }
        }
    }
    return headers;
}

function isAzureCoreModel(t: Type): boolean {
    return (
        t.kind === "Model" &&
        t.namespace !== undefined &&
        ["Azure.Core", "Azure.Core.Foundations"].includes(getNamespaceFullName(t.namespace))
    );
}

function hasDefaultStatusCode(response: HttpOperationResponse): boolean {
    return response.statusCode === "*";
}

function getBodyFromResponse(context: SdkContext, response: HttpOperationResponse): Type | undefined {
    let body: Type | undefined = undefined;
    for (const innerResponse of response.responses) {
        if (!body && innerResponse.body) {
            body = innerResponse.body.type;
        }
    }
    if (body && body.kind === "Model") {
        body = getEffectivePayloadType(context, body);
    }
    return body;
}

function emitResponse(context: SdkContext, response: HttpOperationResponse): Record<string, any> {
    let type = undefined;
    const body = getBodyFromResponse(context, response);
    if (body) {
        if (body.kind === "Model") {
            if (body && body.decorators.find((d) => d.decorator.name === "$pagedResult")) {
                if (modelsMode !== "msrest") {
                    type = getType(context, Array.from(body.properties.values())[0]);
                } else {
                    type = getType(context, body);
                }
            } else if (body && !isAzureCoreModel(body)) {
                type = getType(context, body);
            }
        } else {
            type = getType(context, body);
        }
    }
    const statusCodes = [];
    if (hasDefaultStatusCode(response)) {
        statusCodes.push("default");
    } else {
        statusCodes.push(parseInt(response.statusCode));
    }
    return {
        headers: emitResponseHeaders(context, response),
        statusCodes: statusCodes,
        addedOn: getAddedOnVersion(context, response.type),
        discriminator: "basic",
        type: type,
    };
}

function emitOperation(context: SdkContext, operation: Operation, operationGroupName: string): Record<string, any>[] {
    const lro = getLroMetadata(context.program, operation);
    const paging = getPagedResult(context.program, operation);
    if (lro && paging) {
        return emitLroPagingOperation(context, operation, operationGroupName);
    } else if (paging) {
        return emitPagingOperation(context, operation, operationGroupName);
    } else if (lro) {
        return emitLroOperation(context, operation, operationGroupName);
    }
    return emitBasicOperation(context, operation, operationGroupName);
}

function addLroInformation(
    context: SdkContext,
    tspOperation: Operation,
    emittedOperation: Record<string, any>,
    initialOperation: Record<string, any>,
) {
    emittedOperation["discriminator"] = "lro";
    emittedOperation["initialOperation"] = initialOperation;
    emittedOperation["exposeStreamKeyword"] = false;
    const lroMeta = getLroMetadata(context.program, tspOperation);
    if (!isAzureCoreModel(lroMeta!.logicalResult)) {
        emittedOperation["responses"][0]["type"] = getType(context, lroMeta!.logicalResult);
        if (lroMeta!.logicalPath) {
            emittedOperation["responses"][0]["resultProperty"] = lroMeta!.logicalPath;
        }
        addAcceptParameter(context, tspOperation, emittedOperation["parameters"]);
        addAcceptParameter(context, lroMeta!.operation, emittedOperation["initialOperation"]["parameters"]);
    }
}
function addPagingInformation(context: SdkContext, operation: Operation, emittedOperation: Record<string, any>) {
    emittedOperation["discriminator"] = "paging";
    const pagedResult = getPagedResult(context.program, operation);
    if (pagedResult === undefined) {
        throw Error("Trying to add paging information, but not paging metadata for this operation");
    }
    if (!isAzureCoreModel(pagedResult.modelType)) {
        getType(context, pagedResult.modelType)["pageResultModel"] = true;
    }
    emittedOperation["itemName"] = pagedResult.itemsSegments ? pagedResult.itemsSegments.join(".") : null;
    emittedOperation["itemType"] = getType(context, pagedResult.itemsProperty!.type);
    emittedOperation["continuationTokenName"] = pagedResult.nextLinkSegments
        ? pagedResult.nextLinkSegments.join(".")
        : null;
    emittedOperation["exposeStreamKeyword"] = false;
}

function getLroInitialOperation(
    context: SdkContext,
    operation: Operation,
    operationGroupName: string,
): Record<string, any> {
    const initialTspOperation = getLroMetadata(context.program, operation)!.operation;
    const initialOperation = emitBasicOperation(context, initialTspOperation, operationGroupName)[0];
    initialOperation["name"] = `_${initialOperation["name"]}_initial`;
    initialOperation["isLroInitialOperation"] = true;
    initialOperation["wantTracing"] = false;
    initialOperation["exposeStreamKeyword"] = false;
    initialOperation["responses"].forEach((resp: Record<string, any>, index: number) => {
        if (
            getBodyFromResponse(
                context,
                ignoreDiagnostics(getHttpOperation(context.program, initialTspOperation)).responses[index],
            )
        ) {
            // if there's a body, even if it's an Azure.Core model, we want to use anyObject
            resp["type"] = KnownTypes.anyObject;
        }
    });
    return initialOperation;
}

function emitLroPagingOperation(
    context: SdkContext,
    operation: Operation,
    operationGroupName: string,
): Record<string, any>[] {
    const retval: Record<string, any>[] = [];
    for (const emittedOperation of emitBasicOperation(context, operation, operationGroupName)) {
        const initialOperation = getLroInitialOperation(context, operation, operationGroupName);
        addLroInformation(context, operation, emittedOperation, initialOperation);
        addPagingInformation(context, operation, emittedOperation);
        emittedOperation["discriminator"] = "lropaging";
        retval.push(emittedOperation);
    }
    return retval;
}

function emitLroOperation(
    context: SdkContext,
    operation: Operation,
    operationGroupName: string,
): Record<string, any>[] {
    const retval = [];
    for (const emittedOperation of emitBasicOperation(context, operation, operationGroupName)) {
        const initialOperation = getLroInitialOperation(context, operation, operationGroupName);
        addLroInformation(context, operation, emittedOperation, initialOperation);
        retval.push(initialOperation);
        retval.push(emittedOperation);
    }
    return retval;
}

function emitPagingOperation(
    context: SdkContext,
    operation: Operation,
    operationGroupName: string,
): Record<string, any>[] {
    const retval = [];
    for (const emittedOperation of emitBasicOperation(context, operation, operationGroupName)) {
        addPagingInformation(context, operation, emittedOperation);
        retval.push(emittedOperation);
    }
    return retval;
}

function isAbstract(operation: HttpOperation): boolean {
    const body = operation.parameters.body;
    return body !== undefined && body.contentTypes.length > 1;
}

function addAcceptParameter(context: SdkContext, operation: Operation, parameters: Record<string, any>[]) {
    const httpOperation = ignoreDiagnostics(getHttpOperation(context.program, operation));
    if (
        getBodyFromResponse(context, httpOperation.responses[0]) &&
        parameters.filter((e) => e.wireName.toLowerCase() === "accept").length === 0
    ) {
        parameters.push(emitAcceptParameter(false, false));
    }
}

function emitBasicOperation(
    context: SdkContext,
    operation: Operation,
    operationGroupName: string,
): Record<string, any>[] {
    // Set up parameters for operation
    const parameters: Record<string, any>[] = [];
    if (endpointPathParameters) {
        for (const param of endpointPathParameters) {
            parameters.push(param);
        }
    }
    const httpOperation = ignoreDiagnostics(getHttpOperation(context.program, operation));
    for (const param of httpOperation.parameters.parameters) {
        const emittedParam = emitParameter(context, param, "Method");
        if (isApiVersion(context, param) && apiVersionParam === undefined) {
            apiVersionParam = emittedParam;
        }
        if (isSubscriptionId(emittedParam) && subscriptionIdParam === undefined) {
            subscriptionIdParam = emittedParam;
        }
        parameters.push(emittedParam);
    }

    // Set up responses for operation
    const responses: Record<string, any>[] = [];
    const exceptions: Record<string, any>[] = [];
    const isOverload: boolean = false;
    const isOverriden: boolean = false;
    for (const response of httpOperation.responses) {
        const emittedResponse = emitResponse(context, response);
        addAcceptParameter(context, operation, parameters);
        if (isErrorModel(context.program, response.type)) {
            // * is valid status code in cadl but invalid for autorest.python
            if (response.statusCode === "*") {
                exceptions.push(emittedResponse);
            }
        } else {
            responses.push(emittedResponse);
        }
    }

    let bodyParameter: Record<string, any> | undefined;
    if (httpOperation.parameters.body === undefined) {
        bodyParameter = undefined;
    } else {
        bodyParameter = emitBodyParameter(context, httpOperation);
        if (parameters.filter((e) => e.wireName.toLowerCase() === "content-type").length === 0) {
            parameters.push(emitContentTypeParameter(bodyParameter, isOverload, isOverriden));
        }
        if (bodyParameter.type.type === "model" && bodyParameter.type.base === "json") {
            bodyParameter["propertyToParameterName"] = {};
            if (!isOverload) {
                bodyParameter.defaultToUnsetSentinel = true;
            }
            for (const property of bodyParameter.type.properties) {
                bodyParameter["propertyToParameterName"][property["wireName"]] = property["clientName"];
                parameters.push(emitFlattenedParameter(bodyParameter, property));
            }
        }
    }
    const name = camelToSnakeCase(getLibraryName(context, operation));
    return [
        {
            name: name,
            description: getDocStr(context, operation),
            summary: getSummary(context.program, operation),
            url: httpOperation.path,
            method: httpOperation.verb.toUpperCase(),
            parameters: parameters,
            bodyParameter: bodyParameter,
            responses: responses,
            exceptions: exceptions,
            groupName: operationGroupName,
            addedOn: getAddedOnVersion(context, operation),
            discriminator: "basic",
            isOverload: false,
            overloads: [],
            apiVersions: [getAddedOnVersion(context, operation)],
            wantTracing: true,
            exposeStreamKeyword: true,
            abstract: isAbstract(httpOperation),
            internal: isInternal(context, operation) || getAccess(context, operation) === "internal",
        },
    ];
}

function capitalize(name: string): string {
    return name[0].toUpperCase() + name.slice(1);
}

function emitOperationGroups(context: SdkContext, client: SdkClient): Record<string, any>[] {
    const operationGroups: Record<string, any>[] = [];
    for (const operationGroup of listOperationGroups(context, client)) {
        let operations: Record<string, any>[] = [];
        const name = operationGroup.type.name;
        for (const operation of listOperationsInOperationGroup(context, operationGroup)) {
            operations = operations.concat(emitOperation(context, operation, name));
        }
        operationGroups.push({
            className: name,
            propertyName: name,
            operations: operations,
        });
    }
    const clientOperations: Map<string, Record<string, any>> = new Map<string, Record<string, any>>();
    for (const operation of listOperationsInOperationGroup(context, client)) {
        const groupName = isArm ? operation.interface?.name ?? "" : "";
        const emittedOperation = emitOperation(context, operation, groupName);
        if (!clientOperations.has(groupName)) {
            clientOperations.set(groupName, {
                className: groupName,
                propertyName: groupName,
                operations: [],
            });
        }
        const og = clientOperations.get(groupName) as Record<string, any>;
        og.operations = og.operations.concat(emittedOperation);
    }
    for (const value of clientOperations.values()) {
        operationGroups.push(value);
    }
    return operationGroups;
}

function getServerHelper(context: SdkContext, namespace: Namespace): HttpServer | undefined {
    const servers = getServers(context.program, namespace);
    if (servers === undefined) {
        return undefined;
    }
    return servers[0];
}

function hostParam(clientName: string = "endpoint", clientDefaultValue: string | null = null): Record<string, any> {
    return {
        optional: false,
        description: "Service host",
        clientName: clientName,
        clientDefaultValue: clientDefaultValue,
        wireName: "$host",
        location: "path",
        type: KnownTypes.string,
        implementation: "Client",
        inOverload: false,
    };
}

function emitServerParams(context: SdkContext, namespace: Namespace): Record<string, any>[] {
    const server = getServerHelper(context, namespace);
    if (server === undefined) {
        return [hostParam()];
    }
    if (server.parameters.size > 0) {
        const params: Record<string, any>[] = [];
        for (const param of server.parameters.values()) {
            const serverParameter: HttpServerParameter = {
                type: "endpointPath",
                name: param.name,
                param: param,
            };
            const emittedParameter = emitParameter(context, serverParameter, "Client");
            if (!endpointPathParameters.some((p) => p.clientName === emittedParameter.clientName)) {
                endpointPathParameters.push(emittedParameter);
            }
            if (isApiVersion(context, serverParameter as any) && apiVersionParam === undefined) {
                apiVersionParam = emittedParameter;
                continue;
            }
            params.push(emittedParameter);
        }
        return params;
    } else {
        return [hostParam(isArm ? "base_url" : "endpoint", server.url)];
    }
}

function emitCredentialParam(context: SdkContext, namespace: Namespace): Record<string, any> | undefined {
    const auth = getAuthentication(context.program, namespace);
    if (auth) {
        const credential_types: CredentialType[] = [];
        for (const option of auth.options) {
            for (const scheme of option.schemes) {
                const type: CredentialType = {
                    kind: "Credential",
                    scheme: scheme,
                };
                credential_types.push(type);
            }
        }
        if (credential_types.length > 0) {
            let type: CredentialType | CredentialTypeUnion;
            if (credential_types.length === 1) {
                type = credential_types[0];
            } else {
                type = {
                    kind: "CredentialTypeUnion",
                    types: credential_types,
                };
            }
            return {
                type: getType(context, type),
                optional: false,
                description: "Credential needed for the client to connect to Azure.",
                clientName: "credential",
                location: "other",
                wireName: "credential",
                implementation: "Client",
                skipUrlEncoding: true,
                inOverload: false,
            };
        }
    }
    return undefined;
}

function emitGlobalParameters(context: SdkContext, namespace: Namespace): Record<string, any>[] {
    const clientParameters = emitServerParams(context, namespace);
    const credentialParam = emitCredentialParam(context, namespace);
    if (credentialParam) {
        clientParameters.push(credentialParam);
    }

    return clientParameters;
}

function getApiVersionParameter(context: SdkContext): Record<string, any> | void {
    const version = getDefaultApiVersionValue(context);
    if (apiVersionParam) {
        return apiVersionParam;
    } else if (version !== undefined) {
        return {
            clientName: "api_version",
            clientDefaultValue: version,
            description: "Api Version",
            implementation: "Client",
            location: "query",
            wireName: "api-version",
            skipUrlEncoding: false,
            optional: false,
            inDocString: true,
            inOverload: false,
            inOverridden: false,
            type: getConstantType(version),
            isApiVersion: true,
        };
    }
}

function emitClients(context: SdkContext, namespace: string, clients: SdkClient[]): Record<string, any>[] {
    const retval: Record<string, any>[] = [];
    for (const client of clients) {
        if (getNamespace(context, client.name) !== namespace) {
            continue;
        }
        const server = getServerHelper(context, client.service);
        const emittedClient = {
            name: client.name.split(".").at(-1),
            description: getDocStr(context, client.type),
            parameters: emitGlobalParameters(context, client.service),
            operationGroups: emitOperationGroups(context, client),
            url: server ? server.url : "",
            apiVersions: [],
            arm: client.arm,
        };
        const emittedApiVersionParam = getApiVersionParameter(context);
        if (emittedApiVersionParam) {
            emittedClient.parameters.push(emittedApiVersionParam);
        }
        if (subscriptionIdParam) {
            const idx = emittedClient.parameters.findIndex((p) => p.clientName === "credential");
            emittedClient.parameters = [
                ...emittedClient.parameters.slice(0, idx + 1),
                subscriptionIdParam,
                ...emittedClient.parameters.slice(idx + 1),
            ];
        }
        retval.push(emittedClient);
    }
    return retval;
}

function getServiceNamespace(context: SdkContext): Namespace {
    return listServices(context.program)[0].type;
}

function getNamespace(context: SdkContext, clientName: string): string {
    // We get client namespaces from the client name. If there's a dot, we add that to the namespace
    const submodule = clientName.split(".").slice(0, -1).join(".").toLowerCase();
    if (!submodule) {
        return getClientNamespaceString(context)!.toLowerCase();
    }
    return submodule;
}

function getNamespaces(context: SdkContext): Set<string> {
    const namespaces = new Set<string>();
    for (const client of listClients(context)) {
        namespaces.add(getNamespace(context, client.name));
    }
    return namespaces;
}

function emitCodeModel(sdkContext: SdkContext, clients: SdkClient[]) {
    const clientNamespaceString = getClientNamespaceString(sdkContext)?.toLowerCase();
    // Get types
    const codeModel: Record<string, any> = {
        namespace: clientNamespaceString,
        subnamespaceToClients: {},
    };
    for (const model of getAllModels(sdkContext)) {
        if (model.name !== "") {
            getType(sdkContext, model);
        }
    }
    for (const namespace of getNamespaces(sdkContext)) {
        if (namespace === clientNamespaceString) {
            codeModel["clients"] = emitClients(sdkContext, namespace, clients);
        } else {
            codeModel["subnamespaceToClients"][namespace] = emitClients(sdkContext, namespace, clients);
        }
    }
    codeModel["types"] = [...typesMap.values(), ...Object.values(KnownTypes), ...simpleTypesMap.values()];
    return codeModel;
}
