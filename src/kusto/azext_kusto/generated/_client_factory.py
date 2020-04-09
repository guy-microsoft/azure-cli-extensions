# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def cf_kusto(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.kusto import KustoManagementClient
    return get_mgmt_service_client(cli_ctx, KustoManagementClient)


def cf_cluster(cli_ctx, *_):
    return cf_kusto(cli_ctx).cluster


def cf_cluster_principal_assignment(cli_ctx, *_):
    return cf_kusto(cli_ctx).cluster_principal_assignment


def cf_database(cli_ctx, *_):
    return cf_kusto(cli_ctx).database


def cf_database_principal_assignment(cli_ctx, *_):
    return cf_kusto(cli_ctx).database_principal_assignment


def cf_attached_database_configuration(cli_ctx, *_):
    return cf_kusto(cli_ctx).attached_database_configuration


def cf_data_connection(cli_ctx, *_):
    return cf_kusto(cli_ctx).data_connection
