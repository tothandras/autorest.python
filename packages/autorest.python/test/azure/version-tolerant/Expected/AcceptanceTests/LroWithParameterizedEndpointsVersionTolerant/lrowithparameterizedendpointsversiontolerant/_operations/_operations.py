# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, Optional, TypeVar, Union, cast

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.polling.base_polling import LROBasePolling
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .._serialization import Serializer
from .._vendor import LROWithParamaterizedEndpointsMixinABC

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_lro_with_paramaterized_endpoints_poll_with_parameterized_endpoints_request(  # pylint: disable=name-too-long
    **kwargs: Any,
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/lroParameterizedEndpoints"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_lro_with_paramaterized_endpoints_poll_with_constant_parameterized_endpoints_request(  # pylint: disable=name-too-long
    **kwargs: Any,
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    constant_parameter: Literal["iAmConstant"] = kwargs.pop("constant_parameter", "iAmConstant")
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/lroConstantParameterizedEndpoints/{constantParameter}"
    path_format_arguments = {
        "constantParameter": _SERIALIZER.url("constant_parameter", constant_parameter, "str", skip_quote=True),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


class LROWithParamaterizedEndpointsOperationsMixin(  # pylint: disable=name-too-long
    LROWithParamaterizedEndpointsMixinABC
):
    def _poll_with_parameterized_endpoints_initial(  # pylint: disable=name-too-long
        self, account_name: str, **kwargs: Any
    ) -> Optional[str]:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[Optional[str]] = kwargs.pop("cls", None)

        request = build_lro_with_paramaterized_endpoints_poll_with_parameterized_endpoints_request(
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
            "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        response_headers = {}
        if response.status_code == 200:
            if response.content:
                deserialized = response.json()
            else:
                deserialized = None

        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    @distributed_trace
    def begin_poll_with_parameterized_endpoints(self, account_name: str, **kwargs: Any) -> LROPoller[str]:
        """Poll with method and client level parameters in endpoint.

        :param account_name: Account Name. Pass in 'local' to pass test. Required.
        :type account_name: str
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns str
        :rtype: ~azure.core.polling.LROPoller[str]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[str] = kwargs.pop("cls", None)
        polling: Union[bool, PollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = self._poll_with_parameterized_endpoints_initial(
                account_name=account_name, cls=lambda x, y, z: x, headers=_headers, params=_params, **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            if response.content:
                deserialized = response.json()
            else:
                deserialized = None
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        path_format_arguments = {
            "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
            "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
        }

        if polling is True:
            polling_method: PollingMethod = cast(
                PollingMethod,
                LROBasePolling(
                    lro_delay,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=path_format_arguments,
                    **kwargs,
                ),
            )
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    def _poll_with_constant_parameterized_endpoints_initial(  # pylint: disable=name-too-long
        self, account_name: str, **kwargs: Any
    ) -> Optional[str]:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        constant_parameter: Literal["iAmConstant"] = kwargs.pop("constant_parameter", "iAmConstant")
        cls: ClsType[Optional[str]] = kwargs.pop("cls", None)

        request = build_lro_with_paramaterized_endpoints_poll_with_constant_parameterized_endpoints_request(
            constant_parameter=constant_parameter,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
            "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        response_headers = {}
        if response.status_code == 200:
            if response.content:
                deserialized = response.json()
            else:
                deserialized = None

        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    @distributed_trace
    def begin_poll_with_constant_parameterized_endpoints(  # pylint: disable=name-too-long
        self, account_name: str, **kwargs: Any
    ) -> LROPoller[str]:
        """Poll with method and client level parameters in endpoint, with a constant value.

        :param account_name: Account Name. Pass in 'local' to pass test. Required.
        :type account_name: str
        :keyword constant_parameter: Next link for the list operation. Default value is "iAmConstant".
         Note that overriding this default value may result in unsupported behavior.
        :paramtype constant_parameter: str
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns str
        :rtype: ~azure.core.polling.LROPoller[str]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        constant_parameter: Literal["iAmConstant"] = kwargs.pop("constant_parameter", "iAmConstant")
        cls: ClsType[str] = kwargs.pop("cls", None)
        polling: Union[bool, PollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = self._poll_with_constant_parameterized_endpoints_initial(
                account_name=account_name,
                constant_parameter=constant_parameter,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs,
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            if response.content:
                deserialized = response.json()
            else:
                deserialized = None
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        path_format_arguments = {
            "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
            "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
        }

        if polling is True:
            polling_method: PollingMethod = cast(
                PollingMethod, LROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
            )
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore
