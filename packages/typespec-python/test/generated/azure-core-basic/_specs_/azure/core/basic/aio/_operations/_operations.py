# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import json
import sys
from typing import Any, AsyncIterable, Callable, Dict, IO, List, Optional, TypeVar, Union, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
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
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import AzureJSONEncoder, _deserialize
from ..._operations._operations import (
    build_basic_create_or_replace_request,
    build_basic_create_or_update_request,
    build_basic_delete_request,
    build_basic_export_request,
    build_basic_get_request,
    build_basic_list_request,
    build_basic_list_with_custom_page_model_request,
    build_basic_list_with_page_request,
)
from .._vendor import BasicClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class BasicClientOperationsMixin(BasicClientMixinABC):
    @overload
    async def create_or_update(
        self, id: int, resource: _models.User, *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.User:
        """Adds a user or updates a user's fields.

        Creates or updates a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Required.
        :type resource: ~_specs_.azure.core.basic.models.User
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: User. The User is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.basic.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self, id: int, resource: JSON, *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.User:
        """Adds a user or updates a user's fields.

        Creates or updates a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Required.
        :type resource: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: User. The User is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.basic.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self, id: int, resource: IO[bytes], *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.User:
        """Adds a user or updates a user's fields.

        Creates or updates a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Required.
        :type resource: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: User. The User is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.basic.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self, id: int, resource: Union[_models.User, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.User:
        """Adds a user or updates a user's fields.

        Creates or updates a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Is one of the following types: User, JSON, IO[bytes]
         Required.
        :type resource: ~_specs_.azure.core.basic.models.User or JSON or IO[bytes]
        :keyword content_type: This request has a JSON Merge Patch body. Default value is None.
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: User. The User is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.basic.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.User] = kwargs.pop("cls", None)

        content_type = content_type or "application/merge-patch+json"
        _content = None
        if isinstance(resource, (IOBase, bytes)):
            _content = resource
        else:
            _content = json.dumps(resource, cls=AzureJSONEncoder, exclude_readonly=True)  # type: ignore

        request = build_basic_create_or_update_request(
            id=id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.status_code == 200:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.User, response.json())

        if response.status_code == 201:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.User, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def create_or_replace(
        self, id: int, resource: _models.User, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.User:
        """Adds a user or replaces a user's fields.

        Creates or replaces a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Required.
        :type resource: ~_specs_.azure.core.basic.models.User
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: User. The User is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.basic.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_replace(
        self, id: int, resource: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.User:
        """Adds a user or replaces a user's fields.

        Creates or replaces a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Required.
        :type resource: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: User. The User is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.basic.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_replace(
        self, id: int, resource: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.User:
        """Adds a user or replaces a user's fields.

        Creates or replaces a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Required.
        :type resource: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: User. The User is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.basic.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_replace(
        self, id: int, resource: Union[_models.User, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.User:
        """Adds a user or replaces a user's fields.

        Creates or replaces a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Is one of the following types: User, JSON, IO[bytes]
         Required.
        :type resource: ~_specs_.azure.core.basic.models.User or JSON or IO[bytes]
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: User. The User is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.basic.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.User] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(resource, (IOBase, bytes)):
            _content = resource
        else:
            _content = json.dumps(resource, cls=AzureJSONEncoder, exclude_readonly=True)  # type: ignore

        request = build_basic_create_or_replace_request(
            id=id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.status_code == 200:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.User, response.json())

        if response.status_code == 201:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = _deserialize(_models.User, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def get(self, id: int, **kwargs: Any) -> _models.User:
        """Gets a user.

        Gets a User.

        :param id: The user's id. Required.
        :type id: int
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: User. The User is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.basic.models.User
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

        cls: ClsType[_models.User] = kwargs.pop("cls", None)

        request = build_basic_get_request(
            id=id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
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
            deserialized = _deserialize(_models.User, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def list(
        self,
        *,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        orderby: Optional[List[str]] = None,
        filter: Optional[str] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.User"]:
        """Lists all users.

        Lists all Users.

        :keyword top: The number of result items to return. Default value is None.
        :paramtype top: int
        :keyword skip: The number of result items to skip. Default value is None.
        :paramtype skip: int
        :keyword orderby: Expressions that specify the order of returned results. Default value is
         None.
        :paramtype orderby: list[str]
        :keyword filter: Filter the result list using the given expression. Default value is None.
        :paramtype filter: str
        :keyword select: Select the specified fields to be included in the response. Default value is
         None.
        :paramtype select: list[str]
        :keyword expand: Expand the indicated resources into the response. Default value is None.
        :paramtype expand: list[str]
        :return: An iterator like instance of User
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~_specs_.azure.core.basic.models.User]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.User]] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_basic_list_request(
                    top=top,
                    skip=skip,
                    orderby=orderby,
                    filter=filter,
                    select=select,
                    expand=expand,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request.url = self._client.format_url(request.url)

            return request

        async def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(List[_models.User], deserialized["value"])
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                if _stream:
                    await response.read()  # Load the body in memory and close the socket
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace
    def list_with_page(self, **kwargs: Any) -> AsyncIterable["_models.User"]:
        """List with Azure.Core.Page<>.

        :return: An iterator like instance of User
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~_specs_.azure.core.basic.models.User]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.User]] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_basic_list_with_page_request(
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request.url = self._client.format_url(request.url)

            return request

        async def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(List[_models.User], deserialized["value"])
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                if _stream:
                    await response.read()  # Load the body in memory and close the socket
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace
    def list_with_custom_page_model(self, **kwargs: Any) -> AsyncIterable["_models.User"]:
        """List with custom page model.

        :return: An iterator like instance of User
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~_specs_.azure.core.basic.models.User]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.User]] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_basic_list_with_custom_page_model_request(
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request.url = self._client.format_url(request.url)

            return request

        async def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(List[_models.User], deserialized["items"])
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                if _stream:
                    await response.read()  # Load the body in memory and close the socket
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace_async
    async def delete(self, id: int, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Deletes a user.

        Deletes a User.

        :param id: The user's id. Required.
        :type id: int
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
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

        request = build_basic_delete_request(
            id=id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def export(self, id: int, *, format: str, **kwargs: Any) -> _models.User:
        """Exports a user.

        Exports a User.

        :param id: The user's id. Required.
        :type id: int
        :keyword format: The format of the data. Required.
        :paramtype format: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: User. The User is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.basic.models.User
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

        cls: ClsType[_models.User] = kwargs.pop("cls", None)

        request = build_basic_export_request(
            id=id,
            format=format,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
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
            deserialized = _deserialize(_models.User, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
