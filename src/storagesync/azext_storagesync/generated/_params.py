# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from knack.arguments import CLIArgumentType
from azure.cli.core.commands.parameters import (
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azext_storagesync.action import AddRestoreFileSpec


def load_arguments(self, _):

    with self.argument_context('storagesync storage-sync-service list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')

    with self.argument_context('storagesync storage-sync-service show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')

    with self.argument_context('storagesync storage-sync-service create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='Required. Gets or sets the location of the resource. This will be one of the supported and registered Azure Geo Regions (e.g. West US, East US, Southeast Asia, etc.). The geo region of a resource cannot be changed once it is created, but if an identical geo region is specified on update, the request will succeed.')
        c.argument('tags', tags_type, help='Gets or sets a list of key value pairs that describe the resource. These tags can be used for viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key with a length no greater than 128 characters and a value with a length no greater than 256 characters.')
        c.argument('properties', help='Any object')

    with self.argument_context('storagesync storage-sync-service update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('tags', tags_type, help='The user-specified tags associated with the storage sync service.')

    with self.argument_context('storagesync storage-sync-service delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')

    with self.argument_context('storagesync sync-group list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')

    with self.argument_context('storagesync sync-group show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')

    with self.argument_context('storagesync sync-group create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')

    with self.argument_context('storagesync sync-group delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')

    with self.argument_context('storagesync cloud-endpoint list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')

    with self.argument_context('storagesync cloud-endpoint show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('cloud_endpoint_name', help='Name of Cloud Endpoint object.')

    with self.argument_context('storagesync cloud-endpoint create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('cloud_endpoint_name', help='Name of Cloud Endpoint object.')
        c.argument('properties_storage_account_resource_id', help='Storage Account Resource Id')
        c.argument('properties_azure_file_share_name', help='Azure file share name')
        c.argument('properties_storage_account_tenant_id', help='Storage Account Tenant Id')
        c.argument('properties_friendly_name', help='Friendly Name')

    with self.argument_context('storagesync cloud-endpoint delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('cloud_endpoint_name', help='Name of Cloud Endpoint object.')

    with self.argument_context('storagesync cloud-endpoint pre-restore') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('cloud_endpoint_name', help='Name of Cloud Endpoint object.')
        c.argument('partition', help='Pre Restore partition.')
        c.argument('replica_group', help='Pre Restore replica group.')
        c.argument('request_id', help='Pre Restore request id.')
        c.argument('azure_file_share_uri', help='Pre Restore Azure file share uri.')
        c.argument('status', help='Pre Restore Azure status.')
        c.argument('source_azure_file_share_uri', help='Pre Restore Azure source azure file share uri.')
        c.argument('backup_metadata_property_bag', help='Pre Restore backup metadata property bag.')
        c.argument('restore_file_spec', action=AddRestoreFileSpec, nargs='+', help='Pre Restore restore file spec array.')
        c.argument('pause_wait_for_sync_drain_time_period_in_seconds', help='Pre Restore pause wait for sync drain time period in seconds.')

    with self.argument_context('storagesync cloud-endpoint post-restore') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('cloud_endpoint_name', help='Name of Cloud Endpoint object.')
        c.argument('partition', help='Post Restore partition.')
        c.argument('replica_group', help='Post Restore replica group.')
        c.argument('request_id', help='Post Restore request id.')
        c.argument('azure_file_share_uri', help='Post Restore Azure file share uri.')
        c.argument('status', help='Post Restore Azure status.')
        c.argument('source_azure_file_share_uri', help='Post Restore Azure source azure file share uri.')
        c.argument('failed_file_list', help='Post Restore Azure failed file list.')
        c.argument('restore_file_spec', action=AddRestoreFileSpec, nargs='+', help='Post Restore restore file spec array.')

    with self.argument_context('storagesync cloud-endpoint trigger-change-detection') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('cloud_endpoint_name', help='Name of Cloud Endpoint object.')
        c.argument('directory_path', help='Relative path to a directory Azure File share for which change detection is to be performed.')
        c.argument('change_detection_mode', arg_type=get_enum_type(['Default', 'Recursive']), help='Change Detection Mode. Applies to a directory specified in directoryPath parameter.')
        c.argument('paths', nargs='+', help='Array of relative paths on the Azure File share to be included in the change detection. Can be files and directories.')

    with self.argument_context('storagesync cloud-endpoint pre-backup') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('cloud_endpoint_name', help='Name of Cloud Endpoint object.')
        c.argument('azure_file_share', help='Azure File Share.')

    with self.argument_context('storagesync cloud-endpoint post-backup') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('cloud_endpoint_name', help='Name of Cloud Endpoint object.')
        c.argument('azure_file_share', help='Azure File Share.')

    with self.argument_context('storagesync cloud-endpoint restoreheartbeat') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('cloud_endpoint_name', help='Name of Cloud Endpoint object.')

    with self.argument_context('storagesync server-endpoint list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')

    with self.argument_context('storagesync server-endpoint show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('server_endpoint_name', help='Name of Server Endpoint object.')

    with self.argument_context('storagesync server-endpoint create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('server_endpoint_name', help='Name of Server Endpoint object.')
        c.argument('properties_server_local_path', help='Server folder used for data synchronization')
        c.argument('properties_cloud_tiering', arg_type=get_enum_type(['on', 'off']), help='Type of the Feature Status')
        c.argument('properties_volume_free_space_percent', help='Level of free space to be maintained by Cloud Tiering if it is enabled.')
        c.argument('properties_tier_files_older_than_days', help='Tier files older than days.')
        c.argument('properties_friendly_name', help='Friendly Name')
        c.argument('properties_server_resource_id', help='Arm resource identifier.')
        c.argument('properties_offline_data_transfer', arg_type=get_enum_type(['on', 'off']), help='Type of the Feature Status')
        c.argument('properties_offline_data_transfer_share_name', help='Offline data transfer share name')

    with self.argument_context('storagesync server-endpoint update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('server_endpoint_name', help='Name of Server Endpoint object.')
        c.argument('properties_cloud_tiering', arg_type=get_enum_type(['on', 'off']), help='Type of the Feature Status')
        c.argument('properties_volume_free_space_percent', help='Level of free space to be maintained by Cloud Tiering if it is enabled.')
        c.argument('properties_tier_files_older_than_days', help='Tier files older than days.')
        c.argument('properties_offline_data_transfer', arg_type=get_enum_type(['on', 'off']), help='Type of the Feature Status')
        c.argument('properties_offline_data_transfer_share_name', help='Offline data transfer share name')

    with self.argument_context('storagesync server-endpoint delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('server_endpoint_name', help='Name of Server Endpoint object.')

    with self.argument_context('storagesync server-endpoint recall-action') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('server_endpoint_name', help='Name of Server Endpoint object.')
        c.argument('pattern', help='Pattern of the files.')
        c.argument('recall_path', help='Recall path.')

    with self.argument_context('storagesync registered-server list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')

    with self.argument_context('storagesync registered-server show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('server_id', help='GUID identifying the on-premises server.')

    with self.argument_context('storagesync registered-server create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('server_id', help='GUID identifying the on-premises server.')
        c.argument('properties_server_certificate', help='Registered Server Certificate')
        c.argument('properties_agent_version', help='Registered Server Agent Version')
        c.argument('properties_server_osversion', help='Registered Server OS Version')
        c.argument('properties_last_heart_beat', help='Registered Server last heart beat')
        c.argument('properties_server_role', help='Registered Server serverRole')
        c.argument('properties_cluster_id', help='Registered Server clusterId')
        c.argument('properties_cluster_name', help='Registered Server clusterName')
        c.argument('properties_server_id', help='Registered Server serverId')
        c.argument('properties_friendly_name', help='Friendly Name')

    with self.argument_context('storagesync registered-server delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('server_id', help='GUID identifying the on-premises server.')

    with self.argument_context('storagesync registered-server trigger-rollover') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('server_id', help='GUID identifying the on-premises server.')
        c.argument('server_certificate', help='Certificate Data')

    with self.argument_context('storagesync workflow list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')

    with self.argument_context('storagesync workflow show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('workflow_id', help='workflow Id')

    with self.argument_context('storagesync workflow abort') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('workflow_id', help='workflow Id')

    with self.argument_context('storagesync operation-status show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group. The name is case insensitive.')
        c.argument('location_name', help='The desired region for the name check.')
        c.argument('workflow_id', help='workflow Id')
        c.argument('operation_id', help='operation Id')
