# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, List, Optional, TypeVar

from azure.core import AsyncPipelineClient
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

from ..._configuration import AutoRestUrlMutliCollectionFormatTestServiceConfiguration
from ..._serialization import Deserializer, Serializer
from ...operations._operations import (
    build_queries_array_string_multi_empty_request,
    build_queries_array_string_multi_null_request,
    build_queries_array_string_multi_valid_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class QueriesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~urlmulticollectionformatversiontolerant.aio.AutoRestUrlMutliCollectionFormatTestService`'s
        :attr:`queries` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient[HttpRequest, AsyncHttpResponse] = (
            input_args.pop(0) if input_args else kwargs.pop("client")
        )
        self._config: AutoRestUrlMutliCollectionFormatTestServiceConfiguration = (
            input_args.pop(0) if input_args else kwargs.pop("config")
        )
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def array_string_multi_null(  # pylint: disable=inconsistent-return-statements
        self, *, array_query: Optional[List[str]] = None, **kwargs: Any
    ) -> None:
        """Get a null array of string using the multi-array format.

        :keyword array_query: a null array of string using the multi-array format. Default value is
         None.
        :paramtype array_query: list[str]
        :return: None
        :rtype: None
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

        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_queries_array_string_multi_null_request(
            array_query=array_query,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def array_string_multi_empty(  # pylint: disable=inconsistent-return-statements
        self, *, array_query: Optional[List[str]] = None, **kwargs: Any
    ) -> None:
        """Get an empty array [] of string using the multi-array format.

        :keyword array_query: an empty array [] of string using the multi-array format. Default value
         is None.
        :paramtype array_query: list[str]
        :return: None
        :rtype: None
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

        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_queries_array_string_multi_empty_request(
            array_query=array_query,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def array_string_multi_valid(  # pylint: disable=inconsistent-return-statements
        self, *, array_query: Optional[List[str]] = None, **kwargs: Any
    ) -> None:
        """Get an array of string ['ArrayQuery1', 'begin!*'();:@ &=+$,/?#[]end' , null, ''] using the
        mult-array format.

        :keyword array_query: an array of string ['ArrayQuery1', 'begin!*'();:@ &=+$,/?#[]end' , null,
         ''] using the mult-array format. Default value is None.
        :paramtype array_query: list[str]
        :return: None
        :rtype: None
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

        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_queries_array_string_multi_valid_request(
            array_query=array_query,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})
