# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_machinelearningservices.generated._client_factory import cf_workspace
    machinelearningservices_workspace = CliCommandType(
        operations_tmpl='azext_machinelearningservices.vendored_sdks.machinelearningservices.operations._workspace_operations#WorkspaceOperations.{}',
        client_factory=cf_workspace)
    with self.command_group('machinelearningservices workspace', machinelearningservices_workspace, client_factory=cf_workspace) as g:
        g.custom_command('list', 'machinelearningservices_workspace_list')
        g.custom_show_command('show', 'machinelearningservices_workspace_show')
        g.custom_command('create', 'machinelearningservices_workspace_create', supports_no_wait=True)
        g.custom_command('update', 'machinelearningservices_workspace_update')
        g.custom_command('delete', 'machinelearningservices_workspace_delete')
        g.custom_command('list-key', 'machinelearningservices_workspace_list_key')
        g.custom_command('resync-key', 'machinelearningservices_workspace_resync_key')
        g.wait_command('wait')

    from azext_machinelearningservices.generated._client_factory import cf_workspace_feature
    machinelearningservices_workspace_feature = CliCommandType(
        operations_tmpl='azext_machinelearningservices.vendored_sdks.machinelearningservices.operations._workspace_feature_operations#WorkspaceFeatureOperations.{}',
        client_factory=cf_workspace_feature)
    with self.command_group('machinelearningservices workspace-feature', machinelearningservices_workspace_feature, client_factory=cf_workspace_feature) as g:
        g.custom_command('list', 'machinelearningservices_workspace_feature_list')

    from azext_machinelearningservices.generated._client_factory import cf_usage
    machinelearningservices_usage = CliCommandType(
        operations_tmpl='azext_machinelearningservices.vendored_sdks.machinelearningservices.operations._usage_operations#UsageOperations.{}',
        client_factory=cf_usage)
    with self.command_group('machinelearningservices usage', machinelearningservices_usage, client_factory=cf_usage) as g:
        g.custom_command('list', 'machinelearningservices_usage_list')

    from azext_machinelearningservices.generated._client_factory import cf_virtual_machine_size
    machinelearningservices_virtual_machine_size = CliCommandType(
        operations_tmpl='azext_machinelearningservices.vendored_sdks.machinelearningservices.operations._virtual_machine_size_operations#VirtualMachineSizeOperations.{}',
        client_factory=cf_virtual_machine_size)
    with self.command_group('machinelearningservices virtual-machine-size', machinelearningservices_virtual_machine_size, client_factory=cf_virtual_machine_size) as g:
        g.custom_command('list', 'machinelearningservices_virtual_machine_size_list')

    from azext_machinelearningservices.generated._client_factory import cf_quota
    machinelearningservices_quota = CliCommandType(
        operations_tmpl='azext_machinelearningservices.vendored_sdks.machinelearningservices.operations._quota_operations#QuotaOperations.{}',
        client_factory=cf_quota)
    with self.command_group('machinelearningservices quota', machinelearningservices_quota, client_factory=cf_quota) as g:
        g.custom_command('list', 'machinelearningservices_quota_list')
        g.custom_command('update', 'machinelearningservices_quota_update')

    from azext_machinelearningservices.generated._client_factory import cf_machine_learning_compute
    machinelearningservices_machine_learning_compute = CliCommandType(
        operations_tmpl='azext_machinelearningservices.vendored_sdks.machinelearningservices.operations._machine_learning_compute_operations#MachineLearningComputeOperations.{}',
        client_factory=cf_machine_learning_compute)
    with self.command_group('machinelearningservices machine-learning-compute', machinelearningservices_machine_learning_compute, client_factory=cf_machine_learning_compute) as g:
        g.custom_command('list', 'machinelearningservices_machine_learning_compute_list')
        g.custom_show_command('show', 'machinelearningservices_machine_learning_compute_show')
        g.custom_command('create', 'machinelearningservices_machine_learning_compute_create', supports_no_wait=True)
        g.custom_command('update', 'machinelearningservices_machine_learning_compute_update', supports_no_wait=True)
        g.custom_command('delete', 'machinelearningservices_machine_learning_compute_delete', supports_no_wait=True)
        g.custom_command('list-node', 'machinelearningservices_machine_learning_compute_list_node')
        g.custom_command('list-key', 'machinelearningservices_machine_learning_compute_list_key')
        g.wait_command('wait')

    from azext_machinelearningservices.generated._client_factory import cf_machinelearningservices
    machinelearningservices_ = CliCommandType(
        operations_tmpl='azext_machinelearningservices.vendored_sdks.machinelearningservices.operations.__operations#Operations.{}',
        client_factory=cf_machinelearningservices)
    with self.command_group('machinelearningservices ', machinelearningservices_, client_factory=cf_machinelearningservices) as g:
        g.custom_command('list', 'machinelearningservices__list')

    from azext_machinelearningservices.generated._client_factory import cf_private_endpoint_connection
    machinelearningservices_private_endpoint_connection = CliCommandType(
        operations_tmpl='azext_machinelearningservices.vendored_sdks.machinelearningservices.operations._private_endpoint_connection_operations#PrivateEndpointConnectionOperations.{}',
        client_factory=cf_private_endpoint_connection)
    with self.command_group('machinelearningservices private-endpoint-connection', machinelearningservices_private_endpoint_connection, client_factory=cf_private_endpoint_connection) as g:
        g.custom_show_command('show', 'machinelearningservices_private_endpoint_connection_show')
        g.custom_command('delete', 'machinelearningservices_private_endpoint_connection_delete')
        g.custom_command('put', 'machinelearningservices_private_endpoint_connection_put')

    from azext_machinelearningservices.generated._client_factory import cf_private_link_resource
    machinelearningservices_private_link_resource = CliCommandType(
        operations_tmpl='azext_machinelearningservices.vendored_sdks.machinelearningservices.operations._private_link_resource_operations#PrivateLinkResourceOperations.{}',
        client_factory=cf_private_link_resource)
    with self.command_group('machinelearningservices private-link-resource', machinelearningservices_private_link_resource, client_factory=cf_private_link_resource) as g:
        g.custom_command('list', 'machinelearningservices_private_link_resource_list')

    from azext_machinelearningservices.generated._client_factory import cf_linked_workspace
    machinelearningservices_linked_workspace = CliCommandType(
        operations_tmpl='azext_machinelearningservices.vendored_sdks.machinelearningservices.operations._linked_workspace_operations#LinkedWorkspaceOperations.{}',
        client_factory=cf_linked_workspace)
    with self.command_group('machinelearningservices linked-workspace', machinelearningservices_linked_workspace, client_factory=cf_linked_workspace) as g:
        g.custom_command('list', 'machinelearningservices_linked_workspace_list')
        g.custom_show_command('show', 'machinelearningservices_linked_workspace_show')
        g.custom_command('create', 'machinelearningservices_linked_workspace_create')
        g.custom_command('update', 'machinelearningservices_linked_workspace_update')
        g.custom_command('delete', 'machinelearningservices_linked_workspace_delete')
