#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# This script is used to execute pyright within a tox environment. Depending on which package is being executed against,
# a failure may be suppressed.

from subprocess import check_call, CalledProcessError
import logging
import sys
from util import run_check, AUTOREST_PACKAGE_DIR

logging.getLogger().setLevel(logging.INFO)


def _single_dir_verifytypes(mod):
    inner_class = next(
        d for d in mod.iterdir() if d.is_dir() and not str(d).endswith("egg-info")
    )

    try:
        check_call(
            [
                sys.executable,
                "-m",
                "pyright",
                "--verifytypes",
                str(AUTOREST_PACKAGE_DIR),
                str(inner_class.absolute()),
                "--ignoreexternal"
            ]
        )
    except CalledProcessError as e:
        pass

if __name__ == "__main__":
    run_check("verifytypes", _single_dir_verifytypes, "verifytypes")
