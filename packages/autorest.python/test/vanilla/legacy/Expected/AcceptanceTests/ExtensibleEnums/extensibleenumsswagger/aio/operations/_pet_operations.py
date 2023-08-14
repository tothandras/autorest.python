# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

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
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._configuration import PetStoreIncConfiguration
from ..._serialization import Deserializer, Serializer
from ..._vendor import _convert_request
from ...operations._pet_operations import build_add_pet_request, build_get_by_pet_id_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PetOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~extensibleenumsswagger.aio.PetStoreInc`'s
        :attr:`pet` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient[HttpRequest, AsyncHttpResponse] = (
            input_args.pop(0) if input_args else kwargs.pop("client")
        )
        self._config: PetStoreIncConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get_by_pet_id(self, pet_id: str, **kwargs: Any) -> _models.Pet:
        """get pet by id.

        :param pet_id: Pet id. Required.
        :type pet_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Pet or the result of cls(response)
        :rtype: ~extensibleenumsswagger.models.Pet
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

        cls: ClsType[_models.Pet] = kwargs.pop("cls", None)

        request = build_get_by_pet_id_request(
            pet_id=pet_id,
            template_url=self.get_by_pet_id.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("Pet", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_by_pet_id.metadata = {"url": "/extensibleenums/pet/{petId}"}

    @overload
    async def add_pet(
        self, pet_param: Optional[_models.Pet] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Pet:
        """add pet.

        :param pet_param: pet param. Default value is None.
        :type pet_param: ~extensibleenumsswagger.models.Pet
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Pet or the result of cls(response)
        :rtype: ~extensibleenumsswagger.models.Pet
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def add_pet(
        self, pet_param: Optional[IO] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Pet:
        """add pet.

        :param pet_param: pet param. Default value is None.
        :type pet_param: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Pet or the result of cls(response)
        :rtype: ~extensibleenumsswagger.models.Pet
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def add_pet(self, pet_param: Optional[Union[_models.Pet, IO]] = None, **kwargs: Any) -> _models.Pet:
        """add pet.

        :param pet_param: pet param. Is either a Pet type or a IO type. Default value is None.
        :type pet_param: ~extensibleenumsswagger.models.Pet or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Pet or the result of cls(response)
        :rtype: ~extensibleenumsswagger.models.Pet
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
        cls: ClsType[_models.Pet] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(pet_param, (IOBase, bytes)):
            _content = pet_param
        else:
            if pet_param is not None:
                _json = self._serialize.body(pet_param, "Pet")
            else:
                _json = None

        request = build_add_pet_request(
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.add_pet.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("Pet", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    add_pet.metadata = {"url": "/extensibleenums/pet/addPet"}
