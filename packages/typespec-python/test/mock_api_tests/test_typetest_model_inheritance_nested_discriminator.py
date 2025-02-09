# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the proasync def ject root for
# license information.
# --------------------------------------------------------------------------
import pytest
from typetest.model.nesteddiscriminator import NestedDiscriminatorClient
from typetest.model.nesteddiscriminator.models import GoblinShark, Salmon, Fish


@pytest.fixture
def client():
    with NestedDiscriminatorClient() as client:
        yield client


@pytest.fixture
def valid_body():
    return GoblinShark(age=1)


def test_get_model(client, valid_body):
    assert client.get_model() == valid_body


def test_put_model(client, valid_body):
    client.put_model(valid_body)


@pytest.fixture
def valid_recursive_body():
    return Salmon(
        {
            "age": 1,
            "kind": "salmon",
            "partner": {"age": 2, "kind": "shark", "sharktype": "saw"},
            "friends": [
                {
                    "age": 2,
                    "kind": "salmon",
                    "partner": {"age": 3, "kind": "salmon"},
                    "hate": {
                        "key1": {"age": 4, "kind": "salmon"},
                        "key2": {"age": 2, "kind": "shark", "sharktype": "goblin"},
                    },
                },
                {"age": 3, "kind": "shark", "sharktype": "goblin"},
            ],
            "hate": {
                "key3": {"age": 3, "kind": "shark", "sharktype": "saw"},
                "key4": {
                    "age": 2,
                    "kind": "salmon",
                    "friends": [{"age": 1, "kind": "salmon"}, {"age": 4, "kind": "shark", "sharktype": "goblin"}],
                },
            },
        }
    )


def test_get_recursive_model(client, valid_recursive_body):
    assert valid_recursive_body == client.get_recursive_model()


def test_put_recursive_model(client, valid_recursive_body):
    client.put_recursive_model(valid_recursive_body)


def test_get_missing_discriminator(client):
    assert client.get_missing_discriminator() == Fish(age=1)


def test_get_wrong_discriminator(client):
    assert client.get_wrong_discriminator() == Fish(age=1, kind="wrongKind")
