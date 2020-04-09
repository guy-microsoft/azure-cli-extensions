# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def cf_storagesync(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.storagesync import MicrosoftStorageSync
    return get_mgmt_service_client(cli_ctx, MicrosoftStorageSync)


def cf_storage_sync_service(cli_ctx, *_):
    return cf_storagesync(cli_ctx).storage_sync_service


def cf_sync_group(cli_ctx, *_):
    return cf_storagesync(cli_ctx).sync_group


def cf_cloud_endpoint(cli_ctx, *_):
    return cf_storagesync(cli_ctx).cloud_endpoint


def cf_server_endpoint(cli_ctx, *_):
    return cf_storagesync(cli_ctx).server_endpoint


def cf_registered_server(cli_ctx, *_):
    return cf_storagesync(cli_ctx).registered_server


def cf_workflow(cli_ctx, *_):
    return cf_storagesync(cli_ctx).workflow


def cf_operation_status(cli_ctx, *_):
    return cf_storagesync(cli_ctx).operation_status
