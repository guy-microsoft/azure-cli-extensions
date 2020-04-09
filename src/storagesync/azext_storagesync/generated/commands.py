# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_storagesync.generated._client_factory import cf_storage_sync_service
    storagesync_storage_sync_service = CliCommandType(
        operations_tmpl='azext_storagesync.vendored_sdks.storagesync.operations._storage_sync_service_operations#StorageSyncServiceOperations.{}',
        client_factory=cf_storage_sync_service)
    with self.command_group('storagesync storage-sync-service', storagesync_storage_sync_service, client_factory=cf_storage_sync_service) as g:
        g.custom_command('list', 'storagesync_storage_sync_service_list')
        g.custom_show_command('show', 'storagesync_storage_sync_service_show')
        g.custom_command('create', 'storagesync_storage_sync_service_create')
        g.custom_command('update', 'storagesync_storage_sync_service_update')
        g.custom_command('delete', 'storagesync_storage_sync_service_delete')

    from azext_storagesync.generated._client_factory import cf_sync_group
    storagesync_sync_group = CliCommandType(
        operations_tmpl='azext_storagesync.vendored_sdks.storagesync.operations._sync_group_operations#SyncGroupOperations.{}',
        client_factory=cf_sync_group)
    with self.command_group('storagesync sync-group', storagesync_sync_group, client_factory=cf_sync_group) as g:
        g.custom_command('list', 'storagesync_sync_group_list')
        g.custom_show_command('show', 'storagesync_sync_group_show')
        g.custom_command('create', 'storagesync_sync_group_create')
        g.custom_command('delete', 'storagesync_sync_group_delete')

    from azext_storagesync.generated._client_factory import cf_cloud_endpoint
    storagesync_cloud_endpoint = CliCommandType(
        operations_tmpl='azext_storagesync.vendored_sdks.storagesync.operations._cloud_endpoint_operations#CloudEndpointOperations.{}',
        client_factory=cf_cloud_endpoint)
    with self.command_group('storagesync cloud-endpoint', storagesync_cloud_endpoint, client_factory=cf_cloud_endpoint) as g:
        g.custom_command('list', 'storagesync_cloud_endpoint_list')
        g.custom_show_command('show', 'storagesync_cloud_endpoint_show')
        g.custom_command('create', 'storagesync_cloud_endpoint_create', supports_no_wait=True)
        g.custom_command('delete', 'storagesync_cloud_endpoint_delete', supports_no_wait=True)
        g.custom_command('pre-restore', 'storagesync_cloud_endpoint_pre_restore', supports_no_wait=True)
        g.custom_command('post-restore', 'storagesync_cloud_endpoint_post_restore', supports_no_wait=True)
        g.custom_command('trigger-change-detection', 'storagesync_cloud_endpoint_trigger_change_detection', supports_no_wait=True)
        g.custom_command('pre-backup', 'storagesync_cloud_endpoint_pre_backup', supports_no_wait=True)
        g.custom_command('post-backup', 'storagesync_cloud_endpoint_post_backup', supports_no_wait=True)
        g.custom_command('restoreheartbeat', 'storagesync_cloud_endpoint_restoreheartbeat')
        g.wait_command('wait')

    from azext_storagesync.generated._client_factory import cf_server_endpoint
    storagesync_server_endpoint = CliCommandType(
        operations_tmpl='azext_storagesync.vendored_sdks.storagesync.operations._server_endpoint_operations#ServerEndpointOperations.{}',
        client_factory=cf_server_endpoint)
    with self.command_group('storagesync server-endpoint', storagesync_server_endpoint, client_factory=cf_server_endpoint) as g:
        g.custom_command('list', 'storagesync_server_endpoint_list')
        g.custom_show_command('show', 'storagesync_server_endpoint_show')
        g.custom_command('create', 'storagesync_server_endpoint_create', supports_no_wait=True)
        g.custom_command('update', 'storagesync_server_endpoint_update', supports_no_wait=True)
        g.custom_command('delete', 'storagesync_server_endpoint_delete', supports_no_wait=True)
        g.custom_command('recall-action', 'storagesync_server_endpoint_recall_action', supports_no_wait=True)
        g.wait_command('wait')

    from azext_storagesync.generated._client_factory import cf_registered_server
    storagesync_registered_server = CliCommandType(
        operations_tmpl='azext_storagesync.vendored_sdks.storagesync.operations._registered_server_operations#RegisteredServerOperations.{}',
        client_factory=cf_registered_server)
    with self.command_group('storagesync registered-server', storagesync_registered_server, client_factory=cf_registered_server) as g:
        g.custom_command('list', 'storagesync_registered_server_list')
        g.custom_show_command('show', 'storagesync_registered_server_show')
        g.custom_command('create', 'storagesync_registered_server_create', supports_no_wait=True)
        g.custom_command('delete', 'storagesync_registered_server_delete', supports_no_wait=True)
        g.custom_command('trigger-rollover', 'storagesync_registered_server_trigger_rollover', supports_no_wait=True)
        g.wait_command('wait')

    from azext_storagesync.generated._client_factory import cf_workflow
    storagesync_workflow = CliCommandType(
        operations_tmpl='azext_storagesync.vendored_sdks.storagesync.operations._workflow_operations#WorkflowOperations.{}',
        client_factory=cf_workflow)
    with self.command_group('storagesync workflow', storagesync_workflow, client_factory=cf_workflow) as g:
        g.custom_command('list', 'storagesync_workflow_list')
        g.custom_show_command('show', 'storagesync_workflow_show')
        g.custom_command('abort', 'storagesync_workflow_abort')

    from azext_storagesync.generated._client_factory import cf_operation_status
    storagesync_operation_status = CliCommandType(
        operations_tmpl='azext_storagesync.vendored_sdks.storagesync.operations._operation_status_operations#OperationStatusOperations.{}',
        client_factory=cf_operation_status)
    with self.command_group('storagesync operation-status', storagesync_operation_status, client_factory=cf_operation_status) as g:
        g.custom_show_command('show', 'storagesync_operation_status_show')
