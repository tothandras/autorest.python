# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from azure.core import PipelineClient
from azure.core.rest import HttpRequest, HttpResponse

from .._configuration import BodyFormsDataURLEncodedConfiguration
from .._serialization import Deserializer, Serializer
from .._vendor import raise_if_not_implemented


class FormdataurlencodedOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~bodyformurlencodeddataversiontolerant.BodyFormsDataURLEncoded`'s
        :attr:`formdataurlencoded` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client: PipelineClient[HttpRequest, HttpResponse] = (
            input_args.pop(0) if input_args else kwargs.pop("client")
        )
        self._config: BodyFormsDataURLEncodedConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        raise_if_not_implemented(
            self.__class__,
            [
                "update_pet_with_form",
                "partial_constant_body",
            ],
        )
