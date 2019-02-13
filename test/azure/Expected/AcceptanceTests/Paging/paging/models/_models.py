# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class CustomParameterGroup(Model):
    """Additional parameters for
    get_multiple_pages_fragment_with_grouping_next_link operation.

    All required parameters must be populated in order to send to Azure.

    :param api_version: Required. Sets the api version to use.
    :type api_version: str
    :param tenant: Required. Sets the tenant to use.
    :type tenant: str
    """

    _validation = {
        'api_version': {'required': True},
        'tenant': {'required': True},
    }

    _attribute_map = {
        'api_version': {'key': '', 'type': 'str'},
        'tenant': {'key': '', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CustomParameterGroup, self).__init__(**kwargs)
        self.api_version = kwargs.get('api_version', None)
        self.tenant = kwargs.get('tenant', None)


class OperationResult(Model):
    """OperationResult.

    :param status: The status of the request. Possible values include:
     'Succeeded', 'Failed', 'canceled', 'Accepted', 'Creating', 'Created',
     'Updating', 'Updated', 'Deleting', 'Deleted', 'OK'
    :type status: str or ~paging.models.enum
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OperationResult, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)


class PagingGetMultiplePagesLroOptions(Model):
    """Additional parameters for get_multiple_pages_lro operation.

    :param maxresults: Sets the maximum number of items to return in the
     response.
    :type maxresults: int
    :param timeout: Sets the maximum time that the server can spend processing
     the request, in seconds. The default is 30 seconds. Default value: 30 .
    :type timeout: int
    """

    _attribute_map = {
        'maxresults': {'key': '', 'type': 'int'},
        'timeout': {'key': '', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(PagingGetMultiplePagesLroOptions, self).__init__(**kwargs)
        self.maxresults = kwargs.get('maxresults', None)
        self.timeout = kwargs.get('timeout', 30)


class PagingGetMultiplePagesOptions(Model):
    """Additional parameters for get_multiple_pages operation.

    :param maxresults: Sets the maximum number of items to return in the
     response.
    :type maxresults: int
    :param timeout: Sets the maximum time that the server can spend processing
     the request, in seconds. The default is 30 seconds. Default value: 30 .
    :type timeout: int
    """

    _attribute_map = {
        'maxresults': {'key': '', 'type': 'int'},
        'timeout': {'key': '', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(PagingGetMultiplePagesOptions, self).__init__(**kwargs)
        self.maxresults = kwargs.get('maxresults', None)
        self.timeout = kwargs.get('timeout', 30)


class PagingGetMultiplePagesWithOffsetOptions(Model):
    """Additional parameters for get_multiple_pages_with_offset operation.

    All required parameters must be populated in order to send to Azure.

    :param maxresults: Sets the maximum number of items to return in the
     response.
    :type maxresults: int
    :param offset: Required. Offset of return value
    :type offset: int
    :param timeout: Sets the maximum time that the server can spend processing
     the request, in seconds. The default is 30 seconds. Default value: 30 .
    :type timeout: int
    """

    _validation = {
        'offset': {'required': True},
    }

    _attribute_map = {
        'maxresults': {'key': '', 'type': 'int'},
        'offset': {'key': '', 'type': 'int'},
        'timeout': {'key': '', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(PagingGetMultiplePagesWithOffsetOptions, self).__init__(**kwargs)
        self.maxresults = kwargs.get('maxresults', None)
        self.offset = kwargs.get('offset', None)
        self.timeout = kwargs.get('timeout', 30)


class PagingGetOdataMultiplePagesOptions(Model):
    """Additional parameters for get_odata_multiple_pages operation.

    :param maxresults: Sets the maximum number of items to return in the
     response.
    :type maxresults: int
    :param timeout: Sets the maximum time that the server can spend processing
     the request, in seconds. The default is 30 seconds. Default value: 30 .
    :type timeout: int
    """

    _attribute_map = {
        'maxresults': {'key': '', 'type': 'int'},
        'timeout': {'key': '', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(PagingGetOdataMultiplePagesOptions, self).__init__(**kwargs)
        self.maxresults = kwargs.get('maxresults', None)
        self.timeout = kwargs.get('timeout', 30)


class Product(Model):
    """Product.

    :param properties:
    :type properties: ~paging.models.ProductProperties
    """

    _attribute_map = {
        'properties': {'key': 'properties', 'type': 'ProductProperties'},
    }

    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)
        self.properties = kwargs.get('properties', None)


class ProductProperties(Model):
    """ProductProperties.

    :param id:
    :type id: int
    :param name:
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ProductProperties, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)


class ProductResult(Model):
    """ProductResult.

    :param values:
    :type values: list[~paging.models.Product]
    :param next_link:
    :type next_link: str
    """

    _attribute_map = {
        'values': {'key': 'values', 'type': '[Product]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ProductResult, self).__init__(**kwargs)
        self.values = kwargs.get('values', None)
        self.next_link = kwargs.get('next_link', None)
