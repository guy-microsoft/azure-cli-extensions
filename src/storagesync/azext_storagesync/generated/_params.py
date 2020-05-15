# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from knack.arguments import CLIArgumentType
from azure.cli.core.commands.parameters import (
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azext_storagesync.action import (
    AddPrivateEndpoint,
    AddPrivateLinkServiceConnectionState,
    AddStoragesyncCloudEndpointPostRestoreRestoreFileSpec,
    AddStoragesyncCloudEndpointPreRestoreRestoreFileSpec
)


def load_arguments(self, _):

    with self.argument_context('storagesync storage-sync-service list') as c:
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('storagesync storage-sync-service show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')

    with self.argument_context('storagesync storage-sync-service create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)
        c.argument('incoming_traffic_policy', arg_type=get_enum_type(['AllowAllTraffic', 'AllowVirtualNetworksOnly']),
                   help='Incoming Traffic Policy')

    with self.argument_context('storagesync storage-sync-service update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('tags', tags_type)
        c.argument('incoming_traffic_policy', arg_type=get_enum_type(['AllowAllTraffic', 'AllowVirtualNetworksOnly']),
                   help='Incoming Traffic Policy')

    with self.argument_context('storagesync storage-sync-service delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')

    with self.argument_context('storagesync private-link-resource list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='The name of the storage sync service name within the specified re'
                   'source group.')

    with self.argument_context('storagesync private-endpoint-connection list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')

    with self.argument_context('storagesync private-endpoint-connection show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='The name of the storage sync service name within the specified re'
                   'source group.')
        c.argument('private_endpoint_connection_name', help='The name of the private endpoint connection associated wit'
                   'h the Azure resource')

    with self.argument_context('storagesync private-endpoint-connection create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='The name of the storage sync service name within the specified re'
                   'source group.')
        c.argument('private_endpoint_connection_name', help='The name of the private endpoint connection associated wit'
                   'h the Azure resource')
        c.argument('private_endpoint', action=AddPrivateEndpoint, nargs='+', help='The resource of private end point. E'
                   'xpect value: KEY1=VALUE1 KEY2=VALUE2 ...')
        c.argument('private_link_service_connection_state', action=AddPrivateLinkServiceConnectionState, nargs='+',
                   help='A collection of information about the state of the connection between service consumer and pro'
                   'vider. Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: status, description, action-'
                   'required.')

    with self.argument_context('storagesync private-endpoint-connection delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='The name of the storage sync service name within the specified re'
                   'source group.')
        c.argument('private_endpoint_connection_name', help='The name of the private endpoint connection associated wit'
                   'h the Azure resource')

    with self.argument_context('storagesync sync-group list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')

    with self.argument_context('storagesync sync-group show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')

    with self.argument_context('storagesync sync-group create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('properties', arg_type=CLIArgumentType(options_list=['--properties'], help='The parameters used to c'
                   'reate the sync group Expected value: json-string/@json-file.'))

    with self.argument_context('storagesync sync-group delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')

    with self.argument_context('storagesync cloud-endpoint list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')

    with self.argument_context('storagesync cloud-endpoint show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('cloud_endpoint_name', help='Name of Cloud Endpoint object.')

    with self.argument_context('storagesync cloud-endpoint create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('cloud_endpoint_name', help='Name of Cloud Endpoint object.')
        c.argument('storage_account_resource_id', help='Storage Account Resource Id')
        c.argument('azure_file_share_name', help='Azure file share name')
        c.argument('storage_account_tenant_id', help='Storage Account Tenant Id')
        c.argument('friendly_name', help='Friendly Name')

    with self.argument_context('storagesync cloud-endpoint delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('cloud_endpoint_name', help='Name of Cloud Endpoint object.')

    with self.argument_context('storagesync cloud-endpoint post-backup') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('cloud_endpoint_name', help='Name of Cloud Endpoint object.')
        c.argument('azure_file_share', help='Azure File Share.')

    with self.argument_context('storagesync cloud-endpoint post-restore') as c:
        c.argument('resource_group_name', resource_group_name_type)
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
        c.argument('restore_file_spec', action=AddStoragesyncCloudEndpointPostRestoreRestoreFileSpec, nargs='+', help=
                   'Post Restore restore file spec array. Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs ar'
                   'e: path, isdir.')

    with self.argument_context('storagesync cloud-endpoint pre-backup') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('cloud_endpoint_name', help='Name of Cloud Endpoint object.')
        c.argument('azure_file_share', help='Azure File Share.')

    with self.argument_context('storagesync cloud-endpoint pre-restore') as c:
        c.argument('resource_group_name', resource_group_name_type)
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
        c.argument('restore_file_spec', action=AddStoragesyncCloudEndpointPreRestoreRestoreFileSpec, nargs='+', help='P'
                   're Restore restore file spec array. Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are:'
                   ' path, isdir.')
        c.argument('pause_wait_for_sync_drain_time_period_in_seconds', help='Pre Restore pause wait for sync drain time'
                   ' period in seconds.')

    with self.argument_context('storagesync cloud-endpoint restoreheartbeat') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('cloud_endpoint_name', help='Name of Cloud Endpoint object.')

    with self.argument_context('storagesync cloud-endpoint trigger-change-detection') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('cloud_endpoint_name', help='Name of Cloud Endpoint object.')
        c.argument('directory_path', help='Relative path to a directory Azure File share for which change detection is '
                   'to be performed.')
        c.argument('change_detection_mode', arg_type=get_enum_type(['Default', 'Recursive']), help='Change Detection Mo'
                   'de. Applies to a directory specified in directoryPath parameter.')
        c.argument('paths', nargs='+', help='Array of relative paths on the Azure File share to be included in the chan'
                   'ge detection. Can be files and directories. Expected value: json-string/@json-file.')

    with self.argument_context('storagesync server-endpoint list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')

    with self.argument_context('storagesync server-endpoint show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('server_endpoint_name', help='Name of Server Endpoint object.')

    with self.argument_context('storagesync server-endpoint create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('server_endpoint_name', help='Name of Server Endpoint object.')
        c.argument('server_local_path', help='Server Local path.')
        c.argument('cloud_tiering', arg_type=get_enum_type(['on', 'off']), help='Cloud Tiering.')
        c.argument('volume_free_space_percent', help='Level of free space to be maintained by Cloud Tiering if it is en'
                   'abled.')
        c.argument('tier_files_older_than_days', help='Tier files older than days.')
        c.argument('friendly_name', help='Friendly Name')
        c.argument('server_resource_id', help='Server Resource Id.')
        c.argument('offline_data_transfer', arg_type=get_enum_type(['on', 'off']), help='Offline data transfer')
        c.argument('offline_data_transfer_share_name', help='Offline data transfer share name')
        c.argument('initial_download_policy', arg_type=get_enum_type(['NamespaceOnly', 'NamespaceThenModifiedFiles', 'A'
                   'voidTieredFiles']), help='Policy for how namespace and files are recalled during FastDr.')
        c.argument('local_cache_mode', arg_type=get_enum_type(['DownloadNewAndModifiedFiles', 'UpdateLocallyCachedFiles'
                   '']), help='Policy for enabling follow-the-sun business models: link local cache to cloud behavior t'
                   'o pre-populate before local access.')

    with self.argument_context('storagesync server-endpoint update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('server_endpoint_name', help='Name of Server Endpoint object.')
        c.argument('cloud_tiering', arg_type=get_enum_type(['on', 'off']), help='Cloud Tiering.')
        c.argument('volume_free_space_percent', help='Level of free space to be maintained by Cloud Tiering if it is en'
                   'abled.')
        c.argument('tier_files_older_than_days', help='Tier files older than days.')
        c.argument('offline_data_transfer', arg_type=get_enum_type(['on', 'off']), help='Offline data transfer')
        c.argument('offline_data_transfer_share_name', help='Offline data transfer share name')
        c.argument('local_cache_mode', arg_type=get_enum_type(['DownloadNewAndModifiedFiles', 'UpdateLocallyCachedFiles'
                   '']), help='Policy for enabling follow-the-sun business models: link local cache to cloud behavior t'
                   'o pre-populate before local access.')

    with self.argument_context('storagesync server-endpoint delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('server_endpoint_name', help='Name of Server Endpoint object.')

    with self.argument_context('storagesync server-endpoint recall-action') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('sync_group_name', help='Name of Sync Group resource.')
        c.argument('server_endpoint_name', help='Name of Server Endpoint object.')
        c.argument('pattern', help='Pattern of the files.')
        c.argument('recall_path', help='Recall path.')

    with self.argument_context('storagesync registered-server list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')

    with self.argument_context('storagesync registered-server show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('server_id', help='GUID identifying the on-premises server.')

    with self.argument_context('storagesync registered-server create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('server_id', help='GUID identifying the on-premises server.')
        c.argument('server_certificate', help='Registered Server Certificate')
        c.argument('agent_version', help='Registered Server Agent Version')
        c.argument('server_osversion', help='Registered Server OS Version')
        c.argument('last_heart_beat', help='Registered Server last heart beat')
        c.argument('server_role', help='Registered Server serverRole')
        c.argument('cluster_id', help='Registered Server clusterId')
        c.argument('cluster_name', help='Registered Server clusterName')
        c.argument('properties_server_id', help='Registered Server serverId')
        c.argument('friendly_name', help='Friendly Name')

    with self.argument_context('storagesync registered-server delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('server_id', help='GUID identifying the on-premises server.')

    with self.argument_context('storagesync registered-server trigger-rollover') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('server_id', help='Server Id')
        c.argument('server_certificate', help='Certificate Data')

    with self.argument_context('storagesync workflow list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')

    with self.argument_context('storagesync workflow show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('workflow_id', help='workflow Id')

    with self.argument_context('storagesync workflow abort') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('storage_sync_service_name', help='Name of Storage Sync Service resource.')
        c.argument('workflow_id', help='workflow Id')

    with self.argument_context('storagesync operation-status show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('location_name', help='The desired region to obtain information from.')
        c.argument('workflow_id', help='workflow Id')
        c.argument('operation_id', help='operation Id')
