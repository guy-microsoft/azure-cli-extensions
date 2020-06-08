# Azure CLI Module Creation Report

### containerregistry agent-pool create

create a containerregistry agent-pool.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--agent-pool-name**|string|The name of the agent pool.|agent_pool_name|
|**--location**|string|The location of the resource. This cannot be changed after the resource is created.|location|
|**--tags**|dictionary|The tags of the resource.|tags|
|**--count**|integer|The count of agent machine|count|
|**--tier**|string|The Tier of agent machine|tier|
|**--os**|choice|The OS of agent machine|os|
|**--virtual-network-subnet-resource-id**|string|The Virtual Network Subnet Resource Id of the agent machine|virtual_network_subnet_resource_id|
### containerregistry agent-pool delete

delete a containerregistry agent-pool.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--agent-pool-name**|string|The name of the agent pool.|agent_pool_name|
### containerregistry agent-pool get-queue-status

get-queue-status a containerregistry agent-pool.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--agent-pool-name**|string|The name of the agent pool.|agent_pool_name|
### containerregistry agent-pool list

list a containerregistry agent-pool.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
### containerregistry agent-pool show

show a containerregistry agent-pool.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--agent-pool-name**|string|The name of the agent pool.|agent_pool_name|
### containerregistry agent-pool update

update a containerregistry agent-pool.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--agent-pool-name**|string|The name of the agent pool.|agent_pool_name|
|**--tags**|dictionary|The ARM resource tags.|tags|
|**--count**|integer|The count of agent machine|count|
### containerregistry export-pipeline create

create a containerregistry export-pipeline.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--export-pipeline-name**|string|The name of the export pipeline.|export_pipeline_name|
|**--target**|object|The target properties of the export pipeline.|target|
|**--options**|array|The list of all options configured for the pipeline.|options|
|**--identity-principal-id**|string|The principal ID of resource identity.|principal_id|
|**--identity-tenant-id**|string|The tenant ID of resource.|tenant_id|
|**--identity-type**|sealed-choice|The identity type.|type_identity_type|
|**--identity-user-assigned-identities**|dictionary|The list of user identities associated with the resource. The user identity 
dictionary key references will be ARM resource ids in the form: 
'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/
    providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|
### containerregistry export-pipeline delete

delete a containerregistry export-pipeline.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--export-pipeline-name**|string|The name of the export pipeline.|export_pipeline_name|
### containerregistry export-pipeline list

list a containerregistry export-pipeline.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
### containerregistry export-pipeline show

show a containerregistry export-pipeline.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--export-pipeline-name**|string|The name of the export pipeline.|export_pipeline_name|
### containerregistry import-pipeline create

create a containerregistry import-pipeline.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--import-pipeline-name**|string|The name of the import pipeline.|import_pipeline_name|
|**--source**|object|The source properties of the import pipeline.|source|
|**--options**|array|The list of all options configured for the pipeline.|options|
|**--trigger-source-trigger-status**|choice|The current status of the source trigger.|status|
|**--identity-principal-id**|string|The principal ID of resource identity.|principal_id|
|**--identity-tenant-id**|string|The tenant ID of resource.|tenant_id|
|**--identity-type**|sealed-choice|The identity type.|type_identity_type|
|**--identity-user-assigned-identities**|dictionary|The list of user identities associated with the resource. The user identity 
dictionary key references will be ARM resource ids in the form: 
'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/
    providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|
### containerregistry import-pipeline delete

delete a containerregistry import-pipeline.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--import-pipeline-name**|string|The name of the import pipeline.|import_pipeline_name|
### containerregistry import-pipeline list

list a containerregistry import-pipeline.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
### containerregistry import-pipeline show

show a containerregistry import-pipeline.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--import-pipeline-name**|string|The name of the import pipeline.|import_pipeline_name|
### containerregistry pipeline-run create

create a containerregistry pipeline-run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--pipeline-run-name**|string|The name of the pipeline run.|pipeline_run_name|
|**--force-update-tag**|string|How the pipeline run should be forced to recreate even if the pipeline run configuration has not changed.|force_update_tag|
|**--request-pipeline-resource-id**|string|The resource ID of the pipeline to run.|pipeline_resource_id|
|**--request-artifacts**|array|List of source artifacts to be transferred by the pipeline. 
Specify an image by repository ('hello-world'). This will use the 'latest' tag.
Specify an image by tag ('hello-world:latest').
Specify an image by sha256-based manifest digest ('hello-world@sha256:abc123').|artifacts|
|**--request-source**|object|The source properties of the pipeline run.|source|
|**--request-target**|object|The target properties of the pipeline run.|target|
|**--request-catalog-digest**|string|The digest of the tar used to transfer the artifacts.|catalog_digest|
### containerregistry pipeline-run delete

delete a containerregistry pipeline-run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--pipeline-run-name**|string|The name of the pipeline run.|pipeline_run_name|
### containerregistry pipeline-run list

list a containerregistry pipeline-run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
### containerregistry pipeline-run show

show a containerregistry pipeline-run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--pipeline-run-name**|string|The name of the pipeline run.|pipeline_run_name|
### containerregistry private-endpoint-connection create

create a containerregistry private-endpoint-connection.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--private-endpoint-connection-name**|string|The name of the private endpoint connection.|private_endpoint_connection_name|
|**--private-link-service-connection-state**|object|A collection of information about the state of the connection between service consumer and provider.|private_link_service_connection_state|
|**--private-endpoint-id**|string|This is private endpoint resource created with Microsoft.Network resource provider.|id_properties_private_endpoint_id|
### containerregistry private-endpoint-connection delete

delete a containerregistry private-endpoint-connection.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--private-endpoint-connection-name**|string|The name of the private endpoint connection.|private_endpoint_connection_name|
### containerregistry private-endpoint-connection list

list a containerregistry private-endpoint-connection.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
### containerregistry private-endpoint-connection show

show a containerregistry private-endpoint-connection.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--private-endpoint-connection-name**|string|The name of the private endpoint connection.|private_endpoint_connection_name|
### containerregistry private-endpoint-connection update

create a containerregistry private-endpoint-connection.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--private-endpoint-connection-name**|string|The name of the private endpoint connection.|private_endpoint_connection_name|
|**--private-link-service-connection-state**|object|A collection of information about the state of the connection between service consumer and provider.|private_link_service_connection_state|
|**--private-endpoint-id**|string|This is private endpoint resource created with Microsoft.Network resource provider.|id_properties_private_endpoint_id|
### containerregistry registry create

create a containerregistry registry.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--location**|string|The location of the resource. This cannot be changed after the resource is created.|location|
|**--sku-name**|choice|The SKU name of the container registry. Required for registry creation.|name_sku_name|
|**--tags**|dictionary|The tags of the resource.|tags|
|**--admin-user-enabled**|boolean|The value that indicates whether the admin user is enabled.|admin_user_enabled|
|**--storage-account**|object|The properties of the storage account for the container registry. Only applicable to Classic SKU.|storage_account|
|**--network-rule-set**|object|The network rule set for a container registry.|network_rule_set|
|**--policies**|object|The policies for a container registry.|policies|
|**--encryption**|object|The encryption settings of container registry.|encryption|
|**--data-endpoint-enabled**|boolean|Enable a single data endpoint per region for serving data.|data_endpoint_enabled|
|**--public-network-access**|choice|Whether or not public network access is allowed for the container registry.|public_network_access|
|**--identity-principal-id**|string|The principal ID of resource identity.|principal_id|
|**--identity-tenant-id**|string|The tenant ID of resource.|tenant_id|
|**--identity-type**|sealed-choice|The identity type.|type_identity_type|
|**--identity-user-assigned-identities**|dictionary|The list of user identities associated with the resource. The user identity 
dictionary key references will be ARM resource ids in the form: 
'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/
    providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|
### containerregistry registry delete

delete a containerregistry registry.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
### containerregistry registry generate-credentials

generate-credentials a containerregistry registry.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--token-id**|string|The resource ID of the token for which credentials have to be generated.|token_id|
|**--expiry**|date-time|The expiry date of the generated credentials after which the credentials become invalid.|expiry|
|**--name**|choice|Specifies name of the password which should be regenerated if any -- password1 or password2.|name|
### containerregistry registry get-build-source-upload-url

get-build-source-upload-url a containerregistry registry.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
### containerregistry registry import-image

import-image a containerregistry registry.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--source-source-image**|string|Repository name of the source image.
Specify an image by repository ('hello-world'). This will use the 'latest' tag.
Specify an image by tag ('hello-world:latest').
Specify an image by sha256-based manifest digest ('hello-world@sha256:abc123').|source_image|
|**--target-tags**|array|List of strings of the form repo[:tag]. When tag is omitted the source will be used (or 'latest' if source tag is also omitted).|target_tags|
|**--untagged-target-repositories**|array|List of strings of repository names to do a manifest only copy. No tag will be created.|untagged_target_repositories|
|**--mode**|choice|When Force, any existing target tags will be overwritten. When NoForce, any existing target tags will fail the operation before any copying begins.|mode|
|**--source-resource-id**|string|The resource identifier of the source Azure Container Registry.|resource_id|
|**--source-registry-uri**|string|The address of the source registry (e.g. 'mcr.microsoft.com').|registry_uri|
|**--source-credentials**|object|Credentials used when importing from a registry uri.|credentials|
### containerregistry registry list

list a containerregistry registry.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
### containerregistry registry list-credentials

list-credentials a containerregistry registry.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
### containerregistry registry list-private-link-resource

list-private-link-resource a containerregistry registry.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
### containerregistry registry list-usage

list-usage a containerregistry registry.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
### containerregistry registry regenerate-credential

regenerate-credential a containerregistry registry.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--name**|sealed-choice|Specifies name of the password which should be regenerated -- password or password2.|name|
### containerregistry registry schedule-run

schedule-run a containerregistry registry.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--run-request**|object|The parameters of a run that needs to scheduled.|run_request|
### containerregistry registry show

show a containerregistry registry.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
### containerregistry registry update

update a containerregistry registry.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--tags**|dictionary|The tags for the container registry.|tags|
|**--admin-user-enabled**|boolean|The value that indicates whether the admin user is enabled.|admin_user_enabled|
|**--network-rule-set**|object|The network rule set for a container registry.|network_rule_set|
|**--policies**|object|The policies for a container registry.|policies|
|**--encryption**|object|The encryption settings of container registry.|encryption|
|**--data-endpoint-enabled**|boolean|Enable a single data endpoint per region for serving data.|data_endpoint_enabled|
|**--public-network-access**|choice|Whether or not public network access is allowed for the container registry.|public_network_access|
|**--identity-principal-id**|string|The principal ID of resource identity.|principal_id|
|**--identity-tenant-id**|string|The tenant ID of resource.|tenant_id|
|**--identity-type**|sealed-choice|The identity type.|type_identity_type|
|**--identity-user-assigned-identities**|dictionary|The list of user identities associated with the resource. The user identity 
dictionary key references will be ARM resource ids in the form: 
'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/
    providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|
|**--sku-name**|choice|The SKU name of the container registry. Required for registry creation.|name_sku_name|
### containerregistry replication create

create a containerregistry replication.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--replication-name**|string|The name of the replication.|replication_name|
|**--location**|string|The location of the resource. This cannot be changed after the resource is created.|location|
|**--tags**|dictionary|The tags of the resource.|tags|
|**--region-endpoint-enabled**|boolean|Specifies whether the replication's regional endpoint is enabled. Requests will not be routed to a replication whose regional endpoint is disabled, however its data will continue to be synced with other replications.|region_endpoint_enabled|
### containerregistry replication delete

delete a containerregistry replication.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--replication-name**|string|The name of the replication.|replication_name|
### containerregistry replication list

list a containerregistry replication.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
### containerregistry replication show

show a containerregistry replication.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--replication-name**|string|The name of the replication.|replication_name|
### containerregistry replication update

update a containerregistry replication.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--replication-name**|string|The name of the replication.|replication_name|
|**--tags**|dictionary|The tags for the replication.|tags|
|**--region-endpoint-enabled**|boolean|Specifies whether the replication's regional endpoint is enabled. Requests will not be routed to a replication whose regional endpoint is disabled, however its data will continue to be synced with other replications.|region_endpoint_enabled|
### containerregistry run cancel

cancel a containerregistry run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--run-id**|string|The run ID.|run_id|
### containerregistry run get-log-sas-url

get-log-sas-url a containerregistry run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--run-id**|string|The run ID.|run_id|
### containerregistry run list

list a containerregistry run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--filter**|string|The runs filter to apply on the operation. Arithmetic operators are not supported. The allowed string function is 'contains'. All logical operators except 'Not', 'Has', 'All' are allowed.|filter|
|**--top**|integer|$top is supported for get list of runs, which limits the maximum number of runs to return.|top|
### containerregistry run show

show a containerregistry run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--run-id**|string|The run ID.|run_id|
### containerregistry run update

update a containerregistry run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--run-id**|string|The run ID.|run_id|
|**--is-archive-enabled**|boolean|The value that indicates whether archiving is enabled or not.|is_archive_enabled|
### containerregistry scope-map create

create a containerregistry scope-map.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--scope-map-name**|string|The name of the scope map.|scope_map_name|
|**--description**|string|The user friendly description of the scope map.|description|
|**--actions**|array|The list of scoped permissions for registry artifacts.
E.g. repositories/repository-name/content/read,
repositories/repository-name/metadata/write|actions|
### containerregistry scope-map delete

delete a containerregistry scope-map.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--scope-map-name**|string|The name of the scope map.|scope_map_name|
### containerregistry scope-map list

list a containerregistry scope-map.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
### containerregistry scope-map show

show a containerregistry scope-map.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--scope-map-name**|string|The name of the scope map.|scope_map_name|
### containerregistry scope-map update

update a containerregistry scope-map.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--scope-map-name**|string|The name of the scope map.|scope_map_name|
|**--description**|string|The user friendly description of the scope map.|description|
|**--actions**|array|The list of scope permissions for registry artifacts.
E.g. repositories/repository-name/pull, 
repositories/repository-name/delete|actions|
### containerregistry task create

create a containerregistry task.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--task-name**|string|The name of the container registry task.|task_name|
|**--location**|string|The location of the resource. This cannot be changed after the resource is created.|location|
|**--tags**|dictionary|The tags of the resource.|tags|
|**--status**|choice|The current status of task.|status|
|**--platform**|object|The platform properties against which the run has to happen.|platform|
|**--agent-pool-name**|string|The dedicated agent pool for the task.|agent_pool_name|
|**--timeout**|integer|Run timeout in seconds.|timeout|
|**--docker-build-step**|object|The Docker build step.|docker_build_step|
|**--file-task-step**|object|The properties of a task step.|file_task_step|
|**--encoded-task-step**|object|The properties of a encoded task step.|encoded_task_step|
|**--credentials-custom-registries**|dictionary|Describes the credential parameters for accessing other custom registries. The key
for the dictionary item will be the registry login server (myregistry.azurecr.io) and
the value of the item will be the registry credentials for accessing the registry.|custom_registries|
|**--credentials-source-registry-login-mode**|choice|The authentication mode which determines the source registry login scope. The credentials for the source registry
will be generated using the given scope. These credentials will be used to login to
the source registry during the run.|login_mode|
|**--trigger-timer-triggers**|array|The collection of timer triggers.|timer_triggers|
|**--trigger-source-triggers**|array|The collection of triggers based on source code repository.|source_triggers|
|**--trigger-base-image-trigger**|object|The trigger based on base image dependencies.|base_image_trigger|
|**--agent-configuration-cpu**|integer|The CPU configuration in terms of number of cores required for the run.|cpu|
|**--identity-principal-id**|string|The principal ID of resource identity.|principal_id|
|**--identity-tenant-id**|string|The tenant ID of resource.|tenant_id|
|**--identity-type**|sealed-choice|The identity type.|type_identity_type|
|**--identity-user-assigned-identities**|dictionary|The list of user identities associated with the resource. The user identity 
dictionary key references will be ARM resource ids in the form: 
'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/
    providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|
### containerregistry task delete

delete a containerregistry task.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--task-name**|string|The name of the container registry task.|task_name|
### containerregistry task get-detail

get-detail a containerregistry task.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--task-name**|string|The name of the container registry task.|task_name|
### containerregistry task list

list a containerregistry task.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
### containerregistry task show

show a containerregistry task.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--task-name**|string|The name of the container registry task.|task_name|
### containerregistry task update

update a containerregistry task.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--task-name**|string|The name of the container registry task.|task_name|
|**--tags**|dictionary|The ARM resource tags.|tags|
|**--status**|choice|The current status of task.|status|
|**--platform**|object|The platform properties against which the run has to happen.|platform|
|**--agent-configuration**|object|The machine configuration of the run agent.|agent_configuration|
|**--agent-pool-name**|string|The dedicated agent pool for the task.|agent_pool_name|
|**--timeout**|integer|Run timeout in seconds.|timeout|
|**--docker-build-step-update-parameters**|object|The properties for updating a docker build step.|docker_build_step_update_parameters|
|**--file-task-step-update-parameters**|object|The properties of updating a task step.|file_task_step_update_parameters|
|**--encoded-task-step-update-parameters**|object|The properties for updating encoded task step.|encoded_task_step_update_parameters|
|**--trigger**|object|The properties for updating trigger properties.|trigger|
|**--credentials**|object|The parameters that describes a set of credentials that will be used when this run is invoked.|credentials|
|**--identity-principal-id**|string|The principal ID of resource identity.|principal_id|
|**--identity-tenant-id**|string|The tenant ID of resource.|tenant_id|
|**--identity-type**|sealed-choice|The identity type.|type_identity_type|
|**--identity-user-assigned-identities**|dictionary|The list of user identities associated with the resource. The user identity 
dictionary key references will be ARM resource ids in the form: 
'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/
    providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|
### containerregistry task-run create

create a containerregistry task-run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--task-run-name**|string|The name of task run.|task_run_name|
|**--location**|string|The location of the resource. This cannot be changed after the resource is created.|location|
|**--tags**|dictionary|The tags of the resource.|tags|
|**--run-request**|object|The request (parameters) for the run|run_request|
|**--force-update-tag**|string|How the run should be forced to rerun even if the run request configuration has not changed|force_update_tag|
|**--identity-principal-id**|string|The principal ID of resource identity.|principal_id|
|**--identity-tenant-id**|string|The tenant ID of resource.|tenant_id|
|**--identity-type**|sealed-choice|The identity type.|type_identity_type|
|**--identity-user-assigned-identities**|dictionary|The list of user identities associated with the resource. The user identity 
dictionary key references will be ARM resource ids in the form: 
'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/
    providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|
### containerregistry task-run delete

delete a containerregistry task-run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--task-run-name**|string|The task run name.|task_run_name|
### containerregistry task-run get-detail

get-detail a containerregistry task-run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--task-run-name**|string|The run request name.|task_run_name|
### containerregistry task-run list

list a containerregistry task-run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
### containerregistry task-run show

show a containerregistry task-run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--task-run-name**|string|The run request name.|task_run_name|
### containerregistry task-run update

update a containerregistry task-run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--task-run-name**|string|The task run name.|task_run_name|
|**--tags**|dictionary|The ARM resource tags.|tags|
|**--run-request**|object|The request (parameters) for the new run|run_request|
|**--force-update-tag**|string|How the run should be forced to rerun even if the run request configuration has not changed|force_update_tag|
|**--identity-principal-id**|string|The principal ID of resource identity.|principal_id|
|**--identity-tenant-id**|string|The tenant ID of resource.|tenant_id|
|**--identity-type**|sealed-choice|The identity type.|type_identity_type|
|**--identity-user-assigned-identities**|dictionary|The list of user identities associated with the resource. The user identity 
dictionary key references will be ARM resource ids in the form: 
'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/
    providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.|user_assigned_identities|
### containerregistry token create

create a containerregistry token.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--token-name**|string|The name of the token.|token_name|
|**--scope-map-id**|string|The resource ID of the scope map to which the token will be associated with.|scope_map_id|
|**--status**|choice|The status of the token example enabled or disabled.|status|
|**--credentials-active-directory-object**|object|The Active Directory Object that will be used for authenticating the token of a container registry.|active_directory_object|
|**--credentials-certificates**|array||certificates|
|**--credentials-passwords**|array||passwords|
### containerregistry token delete

delete a containerregistry token.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--token-name**|string|The name of the token.|token_name|
### containerregistry token list

list a containerregistry token.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
### containerregistry token show

show a containerregistry token.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--token-name**|string|The name of the token.|token_name|
### containerregistry token update

update a containerregistry token.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--token-name**|string|The name of the token.|token_name|
|**--scope-map-id**|string|The resource ID of the scope map to which the token will be associated with.|scope_map_id|
|**--status**|choice|The status of the token example enabled or disabled.|status|
|**--credentials-active-directory-object**|object|The Active Directory Object that will be used for authenticating the token of a container registry.|active_directory_object|
|**--credentials-certificates**|array||certificates|
|**--credentials-passwords**|array||passwords|
### containerregistry webhook create

create a containerregistry webhook.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--webhook-name**|string|The name of the webhook.|webhook_name|
|**--location**|string|The location of the webhook. This cannot be changed after the resource is created.|location|
|**--tags**|dictionary|The tags for the webhook.|tags|
|**--service-uri**|string|The service URI for the webhook to post notifications.|service_uri|
|**--custom-headers**|dictionary|Custom headers that will be added to the webhook notifications.|custom_headers|
|**--status**|choice|The status of the webhook at the time the operation was called.|status|
|**--scope**|string|The scope of repositories where the event can be triggered. For example, 'foo:*' means events for all tags under repository 'foo'. 'foo:bar' means events for 'foo:bar' only. 'foo' is equivalent to 'foo:latest'. Empty means all events.|scope|
|**--actions**|array|The list of actions that trigger the webhook to post notifications.|actions|
### containerregistry webhook delete

delete a containerregistry webhook.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--webhook-name**|string|The name of the webhook.|webhook_name|
### containerregistry webhook get-callback-config

get-callback-config a containerregistry webhook.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--webhook-name**|string|The name of the webhook.|webhook_name|
### containerregistry webhook list

list a containerregistry webhook.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
### containerregistry webhook list-event

list-event a containerregistry webhook.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--webhook-name**|string|The name of the webhook.|webhook_name|
### containerregistry webhook ping

ping a containerregistry webhook.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--webhook-name**|string|The name of the webhook.|webhook_name|
### containerregistry webhook show

show a containerregistry webhook.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--webhook-name**|string|The name of the webhook.|webhook_name|
### containerregistry webhook update

update a containerregistry webhook.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group to which the container registry belongs.|resource_group_name|
|**--registry-name**|string|The name of the container registry.|registry_name|
|**--webhook-name**|string|The name of the webhook.|webhook_name|
|**--tags**|dictionary|The tags for the webhook.|tags|
|**--service-uri**|string|The service URI for the webhook to post notifications.|service_uri|
|**--custom-headers**|dictionary|Custom headers that will be added to the webhook notifications.|custom_headers|
|**--status**|choice|The status of the webhook at the time the operation was called.|status|
|**--scope**|string|The scope of repositories where the event can be triggered. For example, 'foo:*' means events for all tags under repository 'foo'. 'foo:bar' means events for 'foo:bar' only. 'foo' is equivalent to 'foo:latest'. Empty means all events.|scope|
|**--actions**|array|The list of actions that trigger the webhook to post notifications.|actions|