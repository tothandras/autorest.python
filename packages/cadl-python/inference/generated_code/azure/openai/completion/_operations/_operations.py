# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import json
import sys
from typing import Any, Callable, Dict, IO, List, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from .._model_base import AzureJSONEncoder, _deserialize
from .._serialization import Serializer
from .._vendor import CompletionClientMixinABC, _format_url_section

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_completion_completions_request(deployment_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: Literal["2022-06-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2022-06-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/deployments/{deploymentId}/completions"
    path_format_arguments = {
        "deploymentId": _SERIALIZER.url("deployment_id", deployment_id, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class CompletionClientOperationsMixin(CompletionClientMixinABC):
    @overload
    def completions(
        self, deployment_id: str, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Completion:
        """Return the completions for a given prompt.

        :param deployment_id: deployment id of the deployed model. Required.
        :type deployment_id: str
        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Completion. The Completion is compatible with MutableMapping
        :rtype: ~azure.openai.models.Completion
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "best_of": 0,  # Optional. How many generations to create server side, and
                      display only the best. Will not"nstream intermediate progress if best_of > 1. Has
                      maximum value of 128.
                    "cache_level": 0,  # Optional. can be used to disable any server-side
                      caching, 0=no cache, 1=prompt prefix"nenabled, 2=full cache.
                    "completionConfig": "str",  # Optional. Completion configuration.
                    "echo": bool,  # Optional. Echo back the prompt in addition to the
                      completion.
                    "frequency_penalty": 0.0,  # Optional. How much to penalize new tokens based
                      on whether they appear in the text so"nfar. Increases the model's likelihood to
                      talk about new topics.
                    "logit_bias": {
                        "str": 0  # Optional. Defaults to null. Modify the likelihood of
                          specified tokens appearing in the"ncompletion. Accepts a json object that
                          maps tokens (specified by their token ID"nin the GPT tokenizer) to an
                          associated bias value from -100 to 100. You can use"nthis tokenizer tool
                          (which works for both GPT-2 and GPT-3) to convert text to"ntoken IDs.
                          Mathematically, the bias is added to the logits generated by the"nmodel prior
                          to sampling. The exact effect will vary per model, but values"nbetween -1 and
                          1 should decrease or increase likelihood of selection; values"nlike -100 or
                          100 should result in a ban or exclusive selection of the relevant"ntoken. As
                          an example, you can pass {"50256" &#58; -100} to prevent the"n<|endoftext|>
                          token from being generated.
                    },
                    "logprobs": 0,  # Optional. Include the log probabilities on the ``logprobs``
                      most likely tokens, as well the"nchosen tokens. So for example, if ``logprobs``
                      is 10, the API will return a list"nof the 10 most likely tokens. If ``logprobs``
                      is 0, only the chosen tokens will"nhave logprobs returned. Minimum of 0 and
                      maximum of 100 allowed.
                    "max_tokens": 0,  # Optional. The maximum number of tokens to generate. Has
                      minimum of 0.
                    "model": "str",  # Optional. The name of the model to use.
                    "n": 0,  # Optional. How many snippets to generate for each prompt. Minimum
                      of 1 and maximum of 128"nallowed.
                    "presence_penalty": 0.0,  # Optional. How much to penalize new tokens based
                      on their existing frequency in the text"nso far. Decreases the model's likelihood
                      to repeat the same line verbatim. Has"nminimum of -2 and maximum of 2.
                    "prompt": "str",  # Optional. An optional prompt to complete from, encoded as
                      a string, a list of strings, or"na list of token lists. Defaults to
                      <|endoftext|>. The prompt to complete from."nIf you would like to provide
                      multiple prompts, use the POST variant of this"nmethod. Note that <|endoftext|>
                      is the document separator that the model sees"nduring training, so if a prompt is
                      not specified the model will generate as if"nfrom the beginning of a new
                      document. Maximum allowed size of string list is"n2048. Is one of the following
                      types: string, list, list
                    "stop": "str",  # Optional. A sequence which indicates the end of the current
                      document. Is either a string type or a list type.
                    "stream": bool,  # Optional. Whether to enable streaming for this endpoint.
                      If set, tokens will be sent as"nserver-sent events as they become available.
                    "temperature": 0.0,  # Optional. What sampling temperature to use. Higher
                      values means the model will take more"nrisks. Try 0.9 for more creative
                      applications, and 0 (argmax sampling) for ones"nwith a well-defined answer."nWe
                      generally recommend using this or ``top_p`` but"nnot both."nMinimum of 0 and
                      maximum of 2 allowed.
                    "top_p": 0.0,  # Optional. An alternative to sampling with temperature,
                      called nucleus sampling, where the"nmodel considers the results of the tokens
                      with top_p probability mass. So 0.1"nmeans only the tokens comprising the top 10%
                      probability mass are"nconsidered."nWe generally recommend using this or
                      ``temperature`` but not"nboth."nMinimum of 0 and maximum of 1 allowed.
                    "user": "str"  # Optional. The ID of the end-user, for use in tracking and
                      rate-limiting.
                }
        """

    @overload
    def completions(
        self,
        deployment_id: str,
        *,
        content_type: str = "application/json",
        prompt: Optional[Union[str, List[str], List[List[str]]]] = None,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        logit_bias: Optional[Dict[str, int]] = None,
        user: Optional[str] = None,
        n: Optional[int] = None,
        stream: Optional[bool] = None,
        logprobs: Optional[int] = None,
        model: Optional[str] = None,
        echo: Optional[bool] = None,
        stop: Optional[Union[str, List[str]]] = None,
        completion_config: Optional[str] = None,
        cache_level: Optional[int] = None,
        presence_penalty: Optional[float] = None,
        frequency_penalty: Optional[float] = None,
        best_of: Optional[int] = None,
        **kwargs: Any
    ) -> _models.Completion:
        """Return the completions for a given prompt.

        :param deployment_id: deployment id of the deployed model. Required.
        :type deployment_id: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword prompt: An optional prompt to complete from, encoded as a string, a list of strings,
         or
         a list of token lists. Defaults to <|endoftext|>. The prompt to complete from.
         If you would like to provide multiple prompts, use the POST variant of this
         method. Note that <|endoftext|> is the document separator that the model sees
         during training, so if a prompt is not specified the model will generate as if
         from the beginning of a new document. Maximum allowed size of string list is
         2048. Is one of the following types: string, list, list Default value is None.
        :paramtype prompt: str or list[str] or list[list[str]]
        :keyword max_tokens: The maximum number of tokens to generate. Has minimum of 0. Default value
         is None.
        :paramtype max_tokens: int
        :keyword temperature: What sampling temperature to use. Higher values means the model will take
         more
         risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones
         with a well-defined answer.
         We generally recommend using this or ``top_p`` but
         not both.
         Minimum of 0 and maximum of 2 allowed. Default value is None.
        :paramtype temperature: float
        :keyword top_p: An alternative to sampling with temperature, called nucleus sampling, where the
         model considers the results of the tokens with top_p probability mass. So 0.1
         means only the tokens comprising the top 10% probability mass are
         considered.
         We generally recommend using this or ``temperature`` but not
         both.
         Minimum of 0 and maximum of 1 allowed. Default value is None.
        :paramtype top_p: float
        :keyword logit_bias: Defaults to null. Modify the likelihood of specified tokens appearing in
         the
         completion. Accepts a json object that maps tokens (specified by their token ID
         in the GPT tokenizer) to an associated bias value from -100 to 100. You can use
         this tokenizer tool (which works for both GPT-2 and GPT-3) to convert text to
         token IDs. Mathematically, the bias is added to the logits generated by the
         model prior to sampling. The exact effect will vary per model, but values
         between -1 and 1 should decrease or increase likelihood of selection; values
         like -100 or 100 should result in a ban or exclusive selection of the relevant
         token. As an example, you can pass {"50256" &#58; -100} to prevent the
         <|endoftext|> token from being generated. Default value is None.
        :paramtype logit_bias: dict[str, int]
        :keyword user: The ID of the end-user, for use in tracking and rate-limiting. Default value is
         None.
        :paramtype user: str
        :keyword n: How many snippets to generate for each prompt. Minimum of 1 and maximum of 128
         allowed. Default value is None.
        :paramtype n: int
        :keyword stream: Whether to enable streaming for this endpoint. If set, tokens will be sent as
         server-sent events as they become available. Default value is None.
        :paramtype stream: bool
        :keyword logprobs: Include the log probabilities on the ``logprobs`` most likely tokens, as
         well the
         chosen tokens. So for example, if ``logprobs`` is 10, the API will return a list
         of the 10 most likely tokens. If ``logprobs`` is 0, only the chosen tokens will
         have logprobs returned. Minimum of 0 and maximum of 100 allowed. Default value is None.
        :paramtype logprobs: int
        :keyword model: The name of the model to use. Default value is None.
        :paramtype model: str
        :keyword echo: Echo back the prompt in addition to the completion. Default value is None.
        :paramtype echo: bool
        :keyword stop: A sequence which indicates the end of the current document. Is either a string
         type or a list type. Default value is None.
        :paramtype stop: str or list[str]
        :keyword completion_config: Completion configuration. Default value is None.
        :paramtype completion_config: str
        :keyword cache_level: can be used to disable any server-side caching, 0=no cache, 1=prompt
         prefix
         enabled, 2=full cache. Default value is None.
        :paramtype cache_level: int
        :keyword presence_penalty: How much to penalize new tokens based on their existing frequency in
         the text
         so far. Decreases the model's likelihood to repeat the same line verbatim. Has
         minimum of -2 and maximum of 2. Default value is None.
        :paramtype presence_penalty: float
        :keyword frequency_penalty: How much to penalize new tokens based on whether they appear in the
         text so
         far. Increases the model's likelihood to talk about new topics. Default value is None.
        :paramtype frequency_penalty: float
        :keyword best_of: How many generations to create server side, and display only the best. Will
         not
         stream intermediate progress if best_of > 1. Has maximum value of 128. Default value is None.
        :paramtype best_of: int
        :return: Completion. The Completion is compatible with MutableMapping
        :rtype: ~azure.openai.models.Completion
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def completions(
        self, deployment_id: str, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Completion:
        """Return the completions for a given prompt.

        :param deployment_id: deployment id of the deployed model. Required.
        :type deployment_id: str
        :param body: Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Completion. The Completion is compatible with MutableMapping
        :rtype: ~azure.openai.models.Completion
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def completions(
        self,
        deployment_id: str,
        body: Union[JSON, IO],
        *,
        prompt: Optional[Union[str, List[str], List[List[str]]]] = None,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        logit_bias: Optional[Dict[str, int]] = None,
        user: Optional[str] = None,
        n: Optional[int] = None,
        stream: Optional[bool] = None,
        logprobs: Optional[int] = None,
        model: Optional[str] = None,
        echo: Optional[bool] = None,
        stop: Optional[Union[str, List[str]]] = None,
        completion_config: Optional[str] = None,
        cache_level: Optional[int] = None,
        presence_penalty: Optional[float] = None,
        frequency_penalty: Optional[float] = None,
        best_of: Optional[int] = None,
        **kwargs: Any
    ) -> _models.Completion:
        """Return the completions for a given prompt.

        :param deployment_id: deployment id of the deployed model. Required.
        :type deployment_id: str
        :param body: Is either a model type or a IO type. Required.
        :type body: JSON or IO
        :keyword prompt: An optional prompt to complete from, encoded as a string, a list of strings,
         or
         a list of token lists. Defaults to <|endoftext|>. The prompt to complete from.
         If you would like to provide multiple prompts, use the POST variant of this
         method. Note that <|endoftext|> is the document separator that the model sees
         during training, so if a prompt is not specified the model will generate as if
         from the beginning of a new document. Maximum allowed size of string list is
         2048. Is one of the following types: string, list, list Default value is None.
        :paramtype prompt: str or list[str] or list[list[str]]
        :keyword max_tokens: The maximum number of tokens to generate. Has minimum of 0. Default value
         is None.
        :paramtype max_tokens: int
        :keyword temperature: What sampling temperature to use. Higher values means the model will take
         more
         risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones
         with a well-defined answer.
         We generally recommend using this or ``top_p`` but
         not both.
         Minimum of 0 and maximum of 2 allowed. Default value is None.
        :paramtype temperature: float
        :keyword top_p: An alternative to sampling with temperature, called nucleus sampling, where the
         model considers the results of the tokens with top_p probability mass. So 0.1
         means only the tokens comprising the top 10% probability mass are
         considered.
         We generally recommend using this or ``temperature`` but not
         both.
         Minimum of 0 and maximum of 1 allowed. Default value is None.
        :paramtype top_p: float
        :keyword logit_bias: Defaults to null. Modify the likelihood of specified tokens appearing in
         the
         completion. Accepts a json object that maps tokens (specified by their token ID
         in the GPT tokenizer) to an associated bias value from -100 to 100. You can use
         this tokenizer tool (which works for both GPT-2 and GPT-3) to convert text to
         token IDs. Mathematically, the bias is added to the logits generated by the
         model prior to sampling. The exact effect will vary per model, but values
         between -1 and 1 should decrease or increase likelihood of selection; values
         like -100 or 100 should result in a ban or exclusive selection of the relevant
         token. As an example, you can pass {"50256" &#58; -100} to prevent the
         <|endoftext|> token from being generated. Default value is None.
        :paramtype logit_bias: dict[str, int]
        :keyword user: The ID of the end-user, for use in tracking and rate-limiting. Default value is
         None.
        :paramtype user: str
        :keyword n: How many snippets to generate for each prompt. Minimum of 1 and maximum of 128
         allowed. Default value is None.
        :paramtype n: int
        :keyword stream: Whether to enable streaming for this endpoint. If set, tokens will be sent as
         server-sent events as they become available. Default value is None.
        :paramtype stream: bool
        :keyword logprobs: Include the log probabilities on the ``logprobs`` most likely tokens, as
         well the
         chosen tokens. So for example, if ``logprobs`` is 10, the API will return a list
         of the 10 most likely tokens. If ``logprobs`` is 0, only the chosen tokens will
         have logprobs returned. Minimum of 0 and maximum of 100 allowed. Default value is None.
        :paramtype logprobs: int
        :keyword model: The name of the model to use. Default value is None.
        :paramtype model: str
        :keyword echo: Echo back the prompt in addition to the completion. Default value is None.
        :paramtype echo: bool
        :keyword stop: A sequence which indicates the end of the current document. Is either a string
         type or a list type. Default value is None.
        :paramtype stop: str or list[str]
        :keyword completion_config: Completion configuration. Default value is None.
        :paramtype completion_config: str
        :keyword cache_level: can be used to disable any server-side caching, 0=no cache, 1=prompt
         prefix
         enabled, 2=full cache. Default value is None.
        :paramtype cache_level: int
        :keyword presence_penalty: How much to penalize new tokens based on their existing frequency in
         the text
         so far. Decreases the model's likelihood to repeat the same line verbatim. Has
         minimum of -2 and maximum of 2. Default value is None.
        :paramtype presence_penalty: float
        :keyword frequency_penalty: How much to penalize new tokens based on whether they appear in the
         text so
         far. Increases the model's likelihood to talk about new topics. Default value is None.
        :paramtype frequency_penalty: float
        :keyword best_of: How many generations to create server side, and display only the best. Will
         not
         stream intermediate progress if best_of > 1. Has maximum value of 128. Default value is None.
        :paramtype best_of: int
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :return: Completion. The Completion is compatible with MutableMapping
        :rtype: ~azure.openai.models.Completion
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
        cls: ClsType[_models.Completion] = kwargs.pop("cls", None)

        if body is None:
            body = {
                "best_of": best_of,
                "cache_level": cache_level,
                "completionConfig": completion_config,
                "echo": echo,
                "frequency_penalty": frequency_penalty,
                "logit_bias": logit_bias,
                "logprobs": logprobs,
                "max_tokens": max_tokens,
                "model": model,
                "n": n,
                "presence_penalty": presence_penalty,
                "prompt": prompt,
                "stop": stop,
                "stream": stream,
                "temperature": temperature,
                "top_p": top_p,
                "user": user,
            }
        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IO, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=AzureJSONEncoder)  # type: ignore

        request = build_completion_completions_request(
            deployment_id=deployment_id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers["apim-request-id"] = self._deserialize("str", response.headers.get("apim-request-id"))

        deserialized = _deserialize(_models.Completion, response.json())

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore
