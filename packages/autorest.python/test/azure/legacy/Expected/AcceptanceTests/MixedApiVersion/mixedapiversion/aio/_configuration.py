# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, TYPE_CHECKING, cast

from azure.core.configuration import Configuration
from azure.core.pipeline import policies
from azure.core.rest import HttpRequest, HttpResponse

from .._version import VERSION

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class MixedApiVersionClientConfiguration(  # pylint: disable=too-many-instance-attributes
    Configuration[HttpRequest, HttpResponse]
):
    """Configuration for MixedApiVersionClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The subscription id, which appears in the path, always modeled in
     credentials. The value is always '1234-5678-9012-3456'. Required.
    :type subscription_id: str
    """

    def __init__(self, credential: "AsyncTokenCredential", subscription_id: str, **kwargs: Any) -> None:
        super(MixedApiVersionClientConfiguration, self).__init__(**kwargs)
        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")

        self.credential = credential
        self.subscription_id = subscription_id
        self.credential_scopes = kwargs.pop("credential_scopes", [])
        kwargs.setdefault("sdk_moniker", "mixedapiversion/{}".format(VERSION))
        self._configure(**kwargs)

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get("user_agent_policy") or cast(
            policies.SansIOHTTPPolicy[HttpRequest, HttpResponse], policies.UserAgentPolicy(**kwargs)
        )
        self.headers_policy = kwargs.get("headers_policy") or cast(
            policies.SansIOHTTPPolicy[HttpRequest, HttpResponse], policies.HeadersPolicy(**kwargs)
        )
        self.proxy_policy = kwargs.get("proxy_policy") or cast(
            policies.SansIOHTTPPolicy[HttpRequest, HttpResponse], policies.ProxyPolicy(**kwargs)
        )
        self.logging_policy = kwargs.get("logging_policy") or cast(
            policies.SansIOHTTPPolicy[HttpRequest, HttpResponse], policies.NetworkTraceLoggingPolicy(**kwargs)
        )
        self.http_logging_policy = kwargs.get("http_logging_policy") or cast(
            policies.SansIOHTTPPolicy[HttpRequest, HttpResponse], policies.HttpLoggingPolicy(**kwargs)
        )
        self.retry_policy = kwargs.get("retry_policy") or cast(
            policies.AsyncHTTPPolicy[HttpRequest, HttpResponse], policies.AsyncRetryPolicy(**kwargs)
        )
        self.custom_hook_policy = kwargs.get("custom_hook_policy") or cast(
            policies.SansIOHTTPPolicy[HttpRequest, HttpResponse], policies.CustomHookPolicy(**kwargs)
        )
        self.redirect_policy = kwargs.get("redirect_policy") or cast(
            policies.AsyncHTTPPolicy[HttpRequest, HttpResponse], policies.AsyncRedirectPolicy(**kwargs)
        )
        self.authentication_policy = kwargs.get("authentication_policy")
        if not self.credential_scopes and not self.authentication_policy:
            raise ValueError("You must provide either credential_scopes or authentication_policy as kwargs")
        if self.credential and not self.authentication_policy:
            self.authentication_policy = cast(
                policies.SansIOHTTPPolicy[HttpRequest, HttpResponse],
                policies.AsyncBearerTokenCredentialPolicy(self.credential, *self.credential_scopes, **kwargs),
            )
