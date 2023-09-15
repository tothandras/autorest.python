# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ..._model_base import _deserialize
from ...operations._operations import (
    build_internal_operation_internal_decorator_in_internal_request,
    build_internal_operation_no_decorator_in_internal_request,
    build_internal_operation_public_decorator_in_internal_request,
    build_public_operation_no_decorator_in_public_request,
    build_public_operation_public_decorator_in_public_request,
    build_relative_model_in_operation_discriminator_request,
    build_relative_model_in_operation_operation_request,
    build_shared_model_in_operation_internal_request,
    build_shared_model_in_operation_public_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PublicOperationOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~_specs_.azure.clientgenerator.core.access.aio.AccessClient`'s
        :attr:`public_operation` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def no_decorator_in_public(self, *, name: str, **kwargs: Any) -> _models.NoDecoratorModelInPublic:
        """no_decorator_in_public.

        :keyword name: Required.
        :paramtype name: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: NoDecoratorModelInPublic. The NoDecoratorModelInPublic is compatible with
         MutableMapping
        :rtype: ~_specs_.azure.clientgenerator.core.access.models.NoDecoratorModelInPublic
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.NoDecoratorModelInPublic] = kwargs.pop("cls", None)

        request = build_public_operation_no_decorator_in_public_request(
            name=name,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.NoDecoratorModelInPublic, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def public_decorator_in_public(self, *, name: str, **kwargs: Any) -> _models.PublicDecoratorModelInPublic:
        """public_decorator_in_public.

        :keyword name: Required.
        :paramtype name: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: PublicDecoratorModelInPublic. The PublicDecoratorModelInPublic is compatible with
         MutableMapping
        :rtype: ~_specs_.azure.clientgenerator.core.access.models.PublicDecoratorModelInPublic
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.PublicDecoratorModelInPublic] = kwargs.pop("cls", None)

        request = build_public_operation_public_decorator_in_public_request(
            name=name,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.PublicDecoratorModelInPublic, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class InternalOperationOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~_specs_.azure.clientgenerator.core.access.aio.AccessClient`'s
        :attr:`internal_operation` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def _no_decorator_in_internal(  # pylint: disable=protected-access
        self, *, name: str, **kwargs: Any
    ) -> _models._models.NoDecoratorModelInInternal:
        """no_decorator_in_internal.

        :keyword name: Required.
        :paramtype name: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: NoDecoratorModelInInternal. The NoDecoratorModelInInternal is compatible with
         MutableMapping
        :rtype: ~_specs_.azure.clientgenerator.core.access.models.NoDecoratorModelInInternal
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models._models.NoDecoratorModelInInternal] = kwargs.pop(  # pylint: disable=protected-access
            "cls", None
        )

        request = build_internal_operation_no_decorator_in_internal_request(
            name=name,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(
                _models._models.NoDecoratorModelInInternal, response.json()  # pylint: disable=protected-access
            )

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def _internal_decorator_in_internal(  # pylint: disable=protected-access
        self, *, name: str, **kwargs: Any
    ) -> _models._models.InternalDecoratorModelInInternal:
        """internal_decorator_in_internal.

        :keyword name: Required.
        :paramtype name: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: InternalDecoratorModelInInternal. The InternalDecoratorModelInInternal is compatible
         with MutableMapping
        :rtype: ~_specs_.azure.clientgenerator.core.access.models.InternalDecoratorModelInInternal
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models._models.InternalDecoratorModelInInternal] = kwargs.pop(  # pylint: disable=protected-access
            "cls", None
        )

        request = build_internal_operation_internal_decorator_in_internal_request(
            name=name,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(
                _models._models.InternalDecoratorModelInInternal, response.json()  # pylint: disable=protected-access
            )

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def _public_decorator_in_internal(
        self, *, name: str, **kwargs: Any
    ) -> _models.PublicDecoratorModelInInternal:
        """public_decorator_in_internal.

        :keyword name: Required.
        :paramtype name: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: PublicDecoratorModelInInternal. The PublicDecoratorModelInInternal is compatible with
         MutableMapping
        :rtype: ~_specs_.azure.clientgenerator.core.access.models.PublicDecoratorModelInInternal
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.PublicDecoratorModelInInternal] = kwargs.pop("cls", None)

        request = build_internal_operation_public_decorator_in_internal_request(
            name=name,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.PublicDecoratorModelInInternal, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class SharedModelInOperationOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~_specs_.azure.clientgenerator.core.access.aio.AccessClient`'s
        :attr:`shared_model_in_operation` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def public(self, *, name: str, **kwargs: Any) -> _models.SharedModel:
        """public.

        :keyword name: Required.
        :paramtype name: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: SharedModel. The SharedModel is compatible with MutableMapping
        :rtype: ~_specs_.azure.clientgenerator.core.access.models.SharedModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.SharedModel] = kwargs.pop("cls", None)

        request = build_shared_model_in_operation_public_request(
            name=name,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.SharedModel, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def _internal(self, *, name: str, **kwargs: Any) -> _models.SharedModel:
        """internal.

        :keyword name: Required.
        :paramtype name: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: SharedModel. The SharedModel is compatible with MutableMapping
        :rtype: ~_specs_.azure.clientgenerator.core.access.models.SharedModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.SharedModel] = kwargs.pop("cls", None)

        request = build_shared_model_in_operation_internal_request(
            name=name,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.SharedModel, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class RelativeModelInOperationOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~_specs_.azure.clientgenerator.core.access.aio.AccessClient`'s
        :attr:`relative_model_in_operation` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def _operation(  # pylint: disable=protected-access
        self, *, name: str, **kwargs: Any
    ) -> _models._models.OuterModel:
        """Expected query parameter: name=:code:`<any string>`
        Expected response body:

        .. code-block:: json

           {
             "name": <any string>,
             "inner":
             {
               "name": <any string>
             }
           }.

        :keyword name: Required.
        :paramtype name: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: OuterModel. The OuterModel is compatible with MutableMapping
        :rtype: ~_specs_.azure.clientgenerator.core.access.models.OuterModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models._models.OuterModel] = kwargs.pop("cls", None)  # pylint: disable=protected-access

        request = build_relative_model_in_operation_operation_request(
            name=name,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models._models.OuterModel, response.json())  # pylint: disable=protected-access

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def _discriminator(  # pylint: disable=protected-access
        self, *, kind: str, **kwargs: Any
    ) -> _models._models.AbstractModel:
        """Expected query parameter: kind=:code:`<any string>`
        Expected response body:

        .. code-block:: json

           {
             "name": <any string>,
             "kind": "real"
           }.

        :keyword kind: Required.
        :paramtype kind: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: AbstractModel. The AbstractModel is compatible with MutableMapping
        :rtype: ~_specs_.azure.clientgenerator.core.access.models.AbstractModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models._models.AbstractModel] = kwargs.pop("cls", None)  # pylint: disable=protected-access

        request = build_relative_model_in_operation_discriminator_request(
            kind=kind,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(
                _models._models.AbstractModel, response.json()  # pylint: disable=protected-access
            )

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
