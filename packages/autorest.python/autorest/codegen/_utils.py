# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

DEFAULT_HEADER_TEXT = (
    "Copyright (c) Microsoft Corporation. All rights reserved.\n"
    "Licensed under the MIT License. See License.txt in the project root for license information.\n"
    "Code generated by Microsoft (R) Python Code Generator.\n"
    "Changes may cause incorrect behavior and will be lost if the code is regenerated."
)

SWAGGER_PACKAGE_MODE = ["mgmtplane", "dataplane"]  # for backward compatibility
TYPESPEC_PACKAGE_MODE = ["azure-mgmt", "azure-dataplane", "generic"]
VALID_PACKAGE_MODE = SWAGGER_PACKAGE_MODE + TYPESPEC_PACKAGE_MODE
