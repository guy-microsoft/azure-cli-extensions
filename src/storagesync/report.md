# Azure CLI Module Creation Report

### storagesync cloud-endpoint create

create a storagesync cloud-endpoint.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--sync_group_name**|string|Name of Sync Group resource.|sync_group_name|sync_group_name|
|**--cloud_endpoint_name**|string|Name of Cloud Endpoint object.|cloud_endpoint_name|cloud_endpoint_name|
|**--storage_account_resource_id**|string|Storage Account Resource Id|storage_account_resource_id|properties_storage_account_resource_id|
|**--azure_file_share_name**|string|Azure file share name|azure_file_share_name|properties_azure_file_share_name|
|**--storage_account_tenant_id**|string|Storage Account Tenant Id|storage_account_tenant_id|properties_storage_account_tenant_id|
|**--friendly_name**|string|Friendly Name|friendly_name|properties_friendly_name|
### storagesync cloud-endpoint delete

delete a storagesync cloud-endpoint.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--sync_group_name**|string|Name of Sync Group resource.|sync_group_name|sync_group_name|
|**--cloud_endpoint_name**|string|Name of Cloud Endpoint object.|cloud_endpoint_name|cloud_endpoint_name|
### storagesync cloud-endpoint list

list a storagesync cloud-endpoint.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--sync_group_name**|string|Name of Sync Group resource.|sync_group_name|sync_group_name|
### storagesync cloud-endpoint post-backup

post-backup a storagesync cloud-endpoint.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--sync_group_name**|string|Name of Sync Group resource.|sync_group_name|sync_group_name|
|**--cloud_endpoint_name**|string|Name of Cloud Endpoint object.|cloud_endpoint_name|cloud_endpoint_name|
|**--azure_file_share**|string|Azure File Share.|azure_file_share|azure_file_share|
### storagesync cloud-endpoint post-restore

post-restore a storagesync cloud-endpoint.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--sync_group_name**|string|Name of Sync Group resource.|sync_group_name|sync_group_name|
|**--cloud_endpoint_name**|string|Name of Cloud Endpoint object.|cloud_endpoint_name|cloud_endpoint_name|
|**--partition**|string|Post Restore partition.|partition|partition|
|**--replica_group**|string|Post Restore replica group.|replica_group|replica_group|
|**--request_id**|string|Post Restore request id.|request_id|request_id|
|**--azure_file_share_uri**|string|Post Restore Azure file share uri.|azure_file_share_uri|azure_file_share_uri|
|**--status**|string|Post Restore Azure status.|status|status|
|**--source_azure_file_share_uri**|string|Post Restore Azure source azure file share uri.|source_azure_file_share_uri|source_azure_file_share_uri|
|**--failed_file_list**|string|Post Restore Azure failed file list.|failed_file_list|failed_file_list|
|**--restore_file_spec**|array|Post Restore restore file spec array.|restore_file_spec|restore_file_spec|
### storagesync cloud-endpoint pre-backup

pre-backup a storagesync cloud-endpoint.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--sync_group_name**|string|Name of Sync Group resource.|sync_group_name|sync_group_name|
|**--cloud_endpoint_name**|string|Name of Cloud Endpoint object.|cloud_endpoint_name|cloud_endpoint_name|
|**--azure_file_share**|string|Azure File Share.|azure_file_share|azure_file_share|
### storagesync cloud-endpoint pre-restore

pre-restore a storagesync cloud-endpoint.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--sync_group_name**|string|Name of Sync Group resource.|sync_group_name|sync_group_name|
|**--cloud_endpoint_name**|string|Name of Cloud Endpoint object.|cloud_endpoint_name|cloud_endpoint_name|
|**--partition**|string|Pre Restore partition.|partition|partition|
|**--replica_group**|string|Pre Restore replica group.|replica_group|replica_group|
|**--request_id**|string|Pre Restore request id.|request_id|request_id|
|**--azure_file_share_uri**|string|Pre Restore Azure file share uri.|azure_file_share_uri|azure_file_share_uri|
|**--status**|string|Pre Restore Azure status.|status|status|
|**--source_azure_file_share_uri**|string|Pre Restore Azure source azure file share uri.|source_azure_file_share_uri|source_azure_file_share_uri|
|**--backup_metadata_property_bag**|string|Pre Restore backup metadata property bag.|backup_metadata_property_bag|backup_metadata_property_bag|
|**--restore_file_spec**|array|Pre Restore restore file spec array.|restore_file_spec|restore_file_spec|
|**--pause_wait_for_sync_drain_time_period_in_seconds**|integer|Pre Restore pause wait for sync drain time period in seconds.|pause_wait_for_sync_drain_time_period_in_seconds|pause_wait_for_sync_drain_time_period_in_seconds|
### storagesync cloud-endpoint restoreheartbeat

restoreheartbeat a storagesync cloud-endpoint.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--sync_group_name**|string|Name of Sync Group resource.|sync_group_name|sync_group_name|
|**--cloud_endpoint_name**|string|Name of Cloud Endpoint object.|cloud_endpoint_name|cloud_endpoint_name|
### storagesync cloud-endpoint show

show a storagesync cloud-endpoint.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--sync_group_name**|string|Name of Sync Group resource.|sync_group_name|sync_group_name|
|**--cloud_endpoint_name**|string|Name of Cloud Endpoint object.|cloud_endpoint_name|cloud_endpoint_name|
### storagesync cloud-endpoint trigger-change-detection

trigger-change-detection a storagesync cloud-endpoint.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--sync_group_name**|string|Name of Sync Group resource.|sync_group_name|sync_group_name|
|**--cloud_endpoint_name**|string|Name of Cloud Endpoint object.|cloud_endpoint_name|cloud_endpoint_name|
|**--directory_path**|string|Relative path to a directory Azure File share for which change detection is to be performed.|directory_path|directory_path|
|**--change_detection_mode**|choice|Change Detection Mode. Applies to a directory specified in directoryPath parameter.|change_detection_mode|change_detection_mode|
|**--paths**|array|Array of relative paths on the Azure File share to be included in the change detection. Can be files and directories.|paths|paths|
### storagesync operation-status show

show a storagesync operation-status.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--location_name**|string|The desired region for the name check.|location_name|location_name|
|**--workflow_id**|string|workflow Id|workflow_id|workflow_id|
|**--operation_id**|string|operation Id|operation_id|operation_id|
### storagesync registered-server create

create a storagesync registered-server.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--server_id**|string|GUID identifying the on-premises server.|server_id|server_id|
|**--server_certificate**|string|Registered Server Certificate|server_certificate|properties_server_certificate|
|**--agent_version**|string|Registered Server Agent Version|agent_version|properties_agent_version|
|**--server_os_version**|string|Registered Server OS Version|server_os_version|properties_server_osversion|
|**--last_heart_beat**|string|Registered Server last heart beat|last_heart_beat|properties_last_heart_beat|
|**--server_role**|string|Registered Server serverRole|server_role|properties_server_role|
|**--cluster_id**|string|Registered Server clusterId|cluster_id|properties_cluster_id|
|**--cluster_name**|string|Registered Server clusterName|cluster_name|properties_cluster_name|
|**--server_id**|string|Registered Server serverId|server_id|properties_server_id|
|**--friendly_name**|string|Friendly Name|friendly_name|properties_friendly_name|
### storagesync registered-server delete

delete a storagesync registered-server.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--server_id**|string|GUID identifying the on-premises server.|server_id|server_id|
### storagesync registered-server list

list a storagesync registered-server.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
### storagesync registered-server show

show a storagesync registered-server.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--server_id**|string|GUID identifying the on-premises server.|server_id|server_id|
### storagesync registered-server trigger-rollover

trigger-rollover a storagesync registered-server.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--server_id**|string|GUID identifying the on-premises server.|server_id|server_id|
|**--server_certificate**|string|Certificate Data|server_certificate|server_certificate|
### storagesync server-endpoint create

create a storagesync server-endpoint.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--sync_group_name**|string|Name of Sync Group resource.|sync_group_name|sync_group_name|
|**--server_endpoint_name**|string|Name of Server Endpoint object.|server_endpoint_name|server_endpoint_name|
|**--server_local_path**|string|Server folder used for data synchronization|server_local_path|properties_server_local_path|
|**--cloud_tiering**|choice|Type of the Feature Status|cloud_tiering|properties_cloud_tiering|
|**--volume_free_space_percent**|integer|Level of free space to be maintained by Cloud Tiering if it is enabled.|volume_free_space_percent|properties_volume_free_space_percent|
|**--tier_files_older_than_days**|integer|Tier files older than days.|tier_files_older_than_days|properties_tier_files_older_than_days|
|**--friendly_name**|string|Friendly Name|friendly_name|properties_friendly_name|
|**--server_resource_id**|string|Arm resource identifier.|server_resource_id|properties_server_resource_id|
|**--offline_data_transfer**|choice|Type of the Feature Status|offline_data_transfer|properties_offline_data_transfer|
|**--offline_data_transfer_share_name**|string|Offline data transfer share name|offline_data_transfer_share_name|properties_offline_data_transfer_share_name|
### storagesync server-endpoint delete

delete a storagesync server-endpoint.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--sync_group_name**|string|Name of Sync Group resource.|sync_group_name|sync_group_name|
|**--server_endpoint_name**|string|Name of Server Endpoint object.|server_endpoint_name|server_endpoint_name|
### storagesync server-endpoint list

list a storagesync server-endpoint.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--sync_group_name**|string|Name of Sync Group resource.|sync_group_name|sync_group_name|
### storagesync server-endpoint recall-action

recall-action a storagesync server-endpoint.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--sync_group_name**|string|Name of Sync Group resource.|sync_group_name|sync_group_name|
|**--server_endpoint_name**|string|Name of Server Endpoint object.|server_endpoint_name|server_endpoint_name|
|**--pattern**|string|Pattern of the files.|pattern|pattern|
|**--recall_path**|string|Recall path.|recall_path|recall_path|
### storagesync server-endpoint show

show a storagesync server-endpoint.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--sync_group_name**|string|Name of Sync Group resource.|sync_group_name|sync_group_name|
|**--server_endpoint_name**|string|Name of Server Endpoint object.|server_endpoint_name|server_endpoint_name|
### storagesync server-endpoint update

update a storagesync server-endpoint.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--sync_group_name**|string|Name of Sync Group resource.|sync_group_name|sync_group_name|
|**--server_endpoint_name**|string|Name of Server Endpoint object.|server_endpoint_name|server_endpoint_name|
|**--cloud_tiering**|choice|Type of the Feature Status|cloud_tiering|properties_cloud_tiering|
|**--volume_free_space_percent**|integer|Level of free space to be maintained by Cloud Tiering if it is enabled.|volume_free_space_percent|properties_volume_free_space_percent|
|**--tier_files_older_than_days**|integer|Tier files older than days.|tier_files_older_than_days|properties_tier_files_older_than_days|
|**--offline_data_transfer**|choice|Type of the Feature Status|offline_data_transfer|properties_offline_data_transfer|
|**--offline_data_transfer_share_name**|string|Offline data transfer share name|offline_data_transfer_share_name|properties_offline_data_transfer_share_name|
### storagesync storage-sync-service create

create a storagesync storage-sync-service.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--location**|string|Required. Gets or sets the location of the resource. This will be one of the supported and registered Azure Geo Regions (e.g. West US, East US, Southeast Asia, etc.). The geo region of a resource cannot be changed once it is created, but if an identical geo region is specified on update, the request will succeed.|location|location|
|**--tags**|dictionary|Gets or sets a list of key value pairs that describe the resource. These tags can be used for viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key with a length no greater than 128 characters and a value with a length no greater than 256 characters.|tags|tags|
|**--properties**|any|Any object|properties|properties|
### storagesync storage-sync-service delete

delete a storagesync storage-sync-service.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
### storagesync storage-sync-service list

list a storagesync storage-sync-service.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
### storagesync storage-sync-service show

show a storagesync storage-sync-service.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
### storagesync storage-sync-service update

update a storagesync storage-sync-service.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--tags**|dictionary|The user-specified tags associated with the storage sync service.|tags|tags|
### storagesync sync-group create

create a storagesync sync-group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--sync_group_name**|string|Name of Sync Group resource.|sync_group_name|sync_group_name|
### storagesync sync-group delete

delete a storagesync sync-group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--sync_group_name**|string|Name of Sync Group resource.|sync_group_name|sync_group_name|
### storagesync sync-group list

list a storagesync sync-group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
### storagesync sync-group show

show a storagesync sync-group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--sync_group_name**|string|Name of Sync Group resource.|sync_group_name|sync_group_name|
### storagesync workflow abort

abort a storagesync workflow.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--workflow_id**|string|workflow Id|workflow_id|workflow_id|
### storagesync workflow list

list a storagesync workflow.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
### storagesync workflow show

show a storagesync workflow.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resource_group_name|
|**--storage_sync_service_name**|string|Name of Storage Sync Service resource.|storage_sync_service_name|storage_sync_service_name|
|**--workflow_id**|string|workflow Id|workflow_id|workflow_id|