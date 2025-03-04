# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import functools

import pytest

from specialheaders.clientrequestid import ClientRequestIdClient
from .test_header_utils import check_client_request_id_header


@pytest.fixture
def client():
    with ClientRequestIdClient() as client:
        yield client


def test_get(client: ClientRequestIdClient):
    checked = {}
    result, resp = client.get(
        cls=lambda x, y, z: (y, x),
        raw_request_hook=functools.partial(
            check_client_request_id_header, header="client-request-id", checked=checked
        ),
    )
    assert result is None
    assert (
        resp.http_response.headers["client-request-id"]
        == checked["client-request-id"]
    )
    pass
