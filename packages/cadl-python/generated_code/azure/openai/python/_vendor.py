# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from abc import ABC
from typing import List, TYPE_CHECKING, cast

from ._configuration import AuthoringClientConfiguration, InferenceClientConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core import PipelineClient

    from ._serialization import Deserializer, Serializer


def _format_url_section(template, **kwargs):
    components = template.split("/")
    while components:
        try:
            return template.format(**kwargs)
        except KeyError as key:
            # Need the cast, as for some reasons "split" is typed as list[str | Any]
            formatted_components = cast(List[str], template.split("/"))
            components = [c for c in formatted_components if "{}".format(key.args[0]) not in c]
            template = "/".join(components)


class AuthoringClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "PipelineClient"
    _config: AuthoringClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


class InferenceClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "PipelineClient"
    _config: InferenceClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"
