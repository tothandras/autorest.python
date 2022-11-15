# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ArrayOptionalWrapper
from ._models_py3 import ArrayWrapper
from ._models_py3 import ClassOptionalWrapper
from ._models_py3 import ClassWrapper
from ._models_py3 import Error
from ._models_py3 import IntOptionalWrapper
from ._models_py3 import IntWrapper
from ._models_py3 import Product
from ._models_py3 import StringOptionalWrapper
from ._models_py3 import StringWrapper
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ArrayOptionalWrapper",
    "ArrayWrapper",
    "ClassOptionalWrapper",
    "ClassWrapper",
    "Error",
    "IntOptionalWrapper",
    "IntWrapper",
    "Product",
    "StringOptionalWrapper",
    "StringWrapper",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
