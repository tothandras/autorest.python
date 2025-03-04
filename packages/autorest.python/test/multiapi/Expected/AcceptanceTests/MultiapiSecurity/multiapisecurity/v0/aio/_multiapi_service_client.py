# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest

from .. import models as _models
from ..._serialization import Deserializer, Serializer
from ._configuration import MultiapiServiceClientConfiguration
from .operations import OperationGroupOneOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class MultiapiServiceClient:  # pylint: disable=client-accepts-api-version-keyword
    """Service client for multiapi client testing.

    :ivar operation_group_one: OperationGroupOneOperations operations
    :vartype operation_group_one: multiapisecurity.v0.aio.operations.OperationGroupOneOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param base_url: Service URL. Default value is "http://localhost:3000".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "0.0.0". Note that overriding this default
     value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self, credential: "AsyncTokenCredential", base_url: str = "http://localhost:3000", **kwargs: Any
    ) -> None:
        self._config = MultiapiServiceClientConfiguration(credential=credential, **kwargs)
        self._client: AsyncPipelineClient = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.operation_group_one = OperationGroupOneOperations(
            self._client, self._config, self._serialize, self._deserialize, "0.0.0"
        )

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "MultiapiServiceClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
