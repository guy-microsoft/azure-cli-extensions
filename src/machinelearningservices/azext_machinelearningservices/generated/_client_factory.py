# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def cf_machinelearningservices(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.machinelearningservices import AzureMachineLearningWorkspaces
    return get_mgmt_service_client(cli_ctx, AzureMachineLearningWorkspaces)


def cf_workspace(cli_ctx, *_):
    return cf_machinelearningservices(cli_ctx).workspace


def cf_workspace_feature(cli_ctx, *_):
    return cf_machinelearningservices(cli_ctx).workspace_feature


def cf_usage(cli_ctx, *_):
    return cf_machinelearningservices(cli_ctx).usage


def cf_virtual_machine_size(cli_ctx, *_):
    return cf_machinelearningservices(cli_ctx).virtual_machine_size


def cf_quota(cli_ctx, *_):
    return cf_machinelearningservices(cli_ctx).quota


def cf_machine_learning_compute(cli_ctx, *_):
    return cf_machinelearningservices(cli_ctx).machine_learning_compute


def cf_private_endpoint_connection(cli_ctx, *_):
    return cf_machinelearningservices(cli_ctx).private_endpoint_connection


def cf_private_link_resource(cli_ctx, *_):
    return cf_machinelearningservices(cli_ctx).private_link_resource


def cf_linked_workspace(cli_ctx, *_):
    return cf_machinelearningservices(cli_ctx).linked_workspace
