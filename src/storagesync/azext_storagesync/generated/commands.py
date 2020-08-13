# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_storagesync.generated._client_factory import cf_storage_sync_service
    storagesync_storage_sync_service = CliCommandType(
        operations_tmpl='azext_storagesync.vendored_sdks.storagesync.operations._storage_sync_service_operations#Storag'
        'eSyncServiceOperations.{}',
        client_factory=cf_storage_sync_service)
    with self.command_group('storagesync storage-sync-service', storagesync_storage_sync_service,
                            client_factory=cf_storage_sync_service, is_experimental=True) as g:
        g.custom_command('list', 'storagesync_storage_sync_service_list')
        g.custom_show_command('show', 'storagesync_storage_sync_service_show')
        g.custom_command('create', 'storagesync_storage_sync_service_create', supports_no_wait=True)
        g.custom_command('update', 'storagesync_storage_sync_service_update', supports_no_wait=True)
        g.custom_command('delete', 'storagesync_storage_sync_service_delete', supports_no_wait=True)
        g.custom_wait_command('wait', 'storagesync_storage_sync_service_show')

    from azext_storagesync.generated._client_factory import cf_private_link_resource
    storagesync_private_link_resource = CliCommandType(
        operations_tmpl='azext_storagesync.vendored_sdks.storagesync.operations._private_link_resource_operations#Priva'
        'teLinkResourceOperations.{}',
        client_factory=cf_private_link_resource)
    with self.command_group('storagesync private-link-resource', storagesync_private_link_resource,
                            client_factory=cf_private_link_resource, is_experimental=True) as g:
        g.custom_command('list', 'storagesync_private_link_resource_list')

    from azext_storagesync.generated._client_factory import cf_private_endpoint_connection
    storagesync_private_endpoint_connection = CliCommandType(
        operations_tmpl='azext_storagesync.vendored_sdks.storagesync.operations._private_endpoint_connection_operations'
        '#PrivateEndpointConnectionOperations.{}',
        client_factory=cf_private_endpoint_connection)
    with self.command_group('storagesync private-endpoint-connection', storagesync_private_endpoint_connection,
                            client_factory=cf_private_endpoint_connection, is_experimental=True) as g:
        g.custom_command('list', 'storagesync_private_endpoint_connection_list')
        g.custom_show_command('show', 'storagesync_private_endpoint_connection_show')
        g.custom_command('create', 'storagesync_private_endpoint_connection_create', supports_no_wait=True)
        g.custom_command('delete', 'storagesync_private_endpoint_connection_delete', supports_no_wait=True)
        g.custom_wait_command('wait', 'storagesync_private_endpoint_connection_show')

    from azext_storagesync.generated._client_factory import cf_sync_group
    storagesync_sync_group = CliCommandType(
        operations_tmpl='azext_storagesync.vendored_sdks.storagesync.operations._sync_group_operations#SyncGroupOperati'
        'ons.{}',
        client_factory=cf_sync_group)
    with self.command_group('storagesync sync-group', storagesync_sync_group, client_factory=cf_sync_group,
                            is_experimental=True) as g:
        g.custom_command('list', 'storagesync_sync_group_list')
        g.custom_show_command('show', 'storagesync_sync_group_show')
        g.custom_command('create', 'storagesync_sync_group_create')
        g.custom_command('delete', 'storagesync_sync_group_delete')

    from azext_storagesync.generated._client_factory import cf_cloud_endpoint
    storagesync_cloud_endpoint = CliCommandType(
        operations_tmpl='azext_storagesync.vendored_sdks.storagesync.operations._cloud_endpoint_operations#CloudEndpoin'
        'tOperations.{}',
        client_factory=cf_cloud_endpoint)
    with self.command_group('storagesync cloud-endpoint', storagesync_cloud_endpoint, client_factory=cf_cloud_endpoint,
                             is_experimental=True) as g:
        g.custom_command('list', 'storagesync_cloud_endpoint_list')
        g.custom_show_command('show', 'storagesync_cloud_endpoint_show')
        g.custom_command('create', 'storagesync_cloud_endpoint_create', supports_no_wait=True)
        g.custom_command('delete', 'storagesync_cloud_endpoint_delete', supports_no_wait=True)
        g.custom_command('post-backup', 'storagesync_cloud_endpoint_post_backup', supports_no_wait=True)
        g.custom_command('post-restore', 'storagesync_cloud_endpoint_post_restore', supports_no_wait=True)
        g.custom_command('pre-backup', 'storagesync_cloud_endpoint_pre_backup', supports_no_wait=True)
        g.custom_command('pre-restore', 'storagesync_cloud_endpoint_pre_restore', supports_no_wait=True)
        g.custom_command('restoreheartbeat', 'storagesync_cloud_endpoint_restoreheartbeat')
        g.custom_command('trigger-change-detection', 'storagesync_cloud_endpoint_trigger_change_detection',
                         supports_no_wait=True)
        g.custom_wait_command('wait', 'storagesync_cloud_endpoint_show')

    from azext_storagesync.generated._client_factory import cf_server_endpoint
    storagesync_server_endpoint = CliCommandType(
        operations_tmpl='azext_storagesync.vendored_sdks.storagesync.operations._server_endpoint_operations#ServerEndpo'
        'intOperations.{}',
        client_factory=cf_server_endpoint)
    with self.command_group('storagesync server-endpoint', storagesync_server_endpoint,
                            client_factory=cf_server_endpoint, is_experimental=True) as g:
        g.custom_command('list', 'storagesync_server_endpoint_list')
        g.custom_show_command('show', 'storagesync_server_endpoint_show')
        g.custom_command('create', 'storagesync_server_endpoint_create', supports_no_wait=True)
        g.custom_command('update', 'storagesync_server_endpoint_update', supports_no_wait=True)
        g.custom_command('delete', 'storagesync_server_endpoint_delete', supports_no_wait=True)
        g.custom_command('recall-action', 'storagesync_server_endpoint_recall_action', supports_no_wait=True)
        g.custom_wait_command('wait', 'storagesync_server_endpoint_show')

    from azext_storagesync.generated._client_factory import cf_registered_server
    storagesync_registered_server = CliCommandType(
        operations_tmpl='azext_storagesync.vendored_sdks.storagesync.operations._registered_server_operations#Registere'
        'dServerOperations.{}',
        client_factory=cf_registered_server)
    with self.command_group('storagesync registered-server', storagesync_registered_server,
                            client_factory=cf_registered_server, is_experimental=True) as g:
        g.custom_command('list', 'storagesync_registered_server_list')
        g.custom_show_command('show', 'storagesync_registered_server_show')
        g.custom_command('create', 'storagesync_registered_server_create', supports_no_wait=True)
        g.custom_command('delete', 'storagesync_registered_server_delete', supports_no_wait=True)
        g.custom_command('trigger-rollover', 'storagesync_registered_server_trigger_rollover', supports_no_wait=True)
        g.custom_wait_command('wait', 'storagesync_registered_server_show')

    from azext_storagesync.generated._client_factory import cf_workflow
    storagesync_workflow = CliCommandType(
        operations_tmpl='azext_storagesync.vendored_sdks.storagesync.operations._workflow_operations#WorkflowOperations'
        '.{}',
        client_factory=cf_workflow)
    with self.command_group('storagesync workflow', storagesync_workflow, client_factory=cf_workflow,
                            is_experimental=True) as g:
        g.custom_command('list', 'storagesync_workflow_list')
        g.custom_show_command('show', 'storagesync_workflow_show')
        g.custom_command('abort', 'storagesync_workflow_abort')

    from azext_storagesync.generated._client_factory import cf_operation_status
    storagesync_operation_status = CliCommandType(
        operations_tmpl='azext_storagesync.vendored_sdks.storagesync.operations._operation_status_operations#OperationS'
        'tatusOperations.{}',
        client_factory=cf_operation_status)
    with self.command_group('storagesync operation-status', storagesync_operation_status,
                            client_factory=cf_operation_status, is_experimental=True) as g:
        g.custom_show_command('show', 'storagesync_operation_status_show')
