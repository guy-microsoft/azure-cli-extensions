# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_hardware_security_modules(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.hardwaresecuritymodules import AzureDedicatedHSMResourceProvider
    return get_mgmt_service_client(cli_ctx, AzureDedicatedHSMResourceProvider)


def cf_dedicated_hsm(cli_ctx, *_):
    return cf_hardware_security_modules(cli_ctx).dedicated_hsm
