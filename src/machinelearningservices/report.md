# Azure CLI Module Creation Report

### machinelearningservices  list

list a machinelearningservices .

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
### machinelearningservices linked-workspace create

create a machinelearningservices linked-workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|
|**--link_name**|string|Friendly name of the linked workspace|link_name|link_name|
|**--resource_id**|string|ResourceId of the linked workspace|resource_id|resource_id|
|**--user_assigned_identity_resource_id**|string|ResourceId of the user assigned identity for the linked workspace|user_assigned_identity_resource_id|user_assigned_identity_resource_id|
### machinelearningservices linked-workspace delete

delete a machinelearningservices linked-workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|
|**--link_name**|string|Friendly name of the linked workspace|link_name|link_name|
### machinelearningservices linked-workspace list

list a machinelearningservices linked-workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|
|**--link_subscription_id**|string|The subscriptionid of the linked workspace.|link_subscription_id|link_subscription_id|
|**--link_resource_group**|string|The resource group name of the linked workspace.|link_resource_group|link_resource_group|
|**--link_resource_name**|string|The resource name of the linked workspace.|link_resource_name|link_resource_name|
|**--link_resource_id**|string|The resourceId of the linked workspace.|link_resource_id|link_resource_id|
|**--uai_resource_id**|string|The resourceId of the user assigned identity for the linked workspace.|uai_resource_id|uai_resource_id|
### machinelearningservices linked-workspace show

show a machinelearningservices linked-workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|
|**--link_name**|string|Friendly name of the linked workspace|link_name|link_name|
### machinelearningservices linked-workspace update

update a machinelearningservices linked-workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|
|**--link_name**|string|Friendly name of the linked workspace|link_name|link_name|
|**--user_assigned_identity_resource_id**|string|ResourceId of the user assigned identity for the linked workspace|user_assigned_identity_resource_id|user_assigned_identity_resource_id|
### machinelearningservices machine-learning-compute create

create a machinelearningservices machine-learning-compute.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|
|**--compute_name**|string|Name of the Azure Machine Learning compute.|compute_name|compute_name|
|**--identity**|object|Identity for the resource.|identity|identity|
|**--location**|string|Specifies the location of the resource.|location|location|
|**--tags**|dictionary|Contains resource tags defined as key/value pairs.|tags|tags|
|**--sku**|object|Sku of the resource|sku|sku|
|**--properties**|object|Machine Learning compute object.|properties|properties|
### machinelearningservices machine-learning-compute delete

delete a machinelearningservices machine-learning-compute.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|
|**--compute_name**|string|Name of the Azure Machine Learning compute.|compute_name|compute_name|
|**--underlying_resource_action**|choice|Delete the underlying compute if 'Delete', or detach the underlying compute from workspace if 'Detach'.|underlying_resource_action|underlying_resource_action|
### machinelearningservices machine-learning-compute list

list a machinelearningservices machine-learning-compute.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|
|**--skiptoken**|string|Continuation token for pagination.|skiptoken|skiptoken|
### machinelearningservices machine-learning-compute list-key

list-key a machinelearningservices machine-learning-compute.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|
|**--compute_name**|string|Name of the Azure Machine Learning compute.|compute_name|compute_name|
### machinelearningservices machine-learning-compute list-node

list-node a machinelearningservices machine-learning-compute.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|
|**--compute_name**|string|Name of the Azure Machine Learning compute.|compute_name|compute_name|
### machinelearningservices machine-learning-compute show

show a machinelearningservices machine-learning-compute.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|
|**--compute_name**|string|Name of the Azure Machine Learning compute.|compute_name|compute_name|
### machinelearningservices machine-learning-compute update

update a machinelearningservices machine-learning-compute.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|
|**--compute_name**|string|Name of the Azure Machine Learning compute.|compute_name|compute_name|
|**--scale_settings**|object|scale settings for AML Compute|scale_settings|properties_scale_settings|
### machinelearningservices private-endpoint-connection delete

delete a machinelearningservices private-endpoint-connection.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|
|**--private_endpoint_connection_name**|string|The name of the private endpoint connection associated with the workspace|private_endpoint_connection_name|private_endpoint_connection_name|
### machinelearningservices private-endpoint-connection put

put a machinelearningservices private-endpoint-connection.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|
|**--private_endpoint_connection_name**|string|The name of the private endpoint connection associated with the workspace|private_endpoint_connection_name|private_endpoint_connection_name|
|**--identity**|object|Identity for the resource.|identity|identity|
|**--location**|string|Specifies the location of the resource.|location|location|
|**--tags**|dictionary|Contains resource tags defined as key/value pairs.|tags|tags|
|**--sku**|object|Sku of the resource|sku|sku|
|**--private_endpoint**|object|The Private Endpoint resource.|private_endpoint|properties_private_endpoint|
|**--private_link_service_connection_state**|object|A collection of information about the state of the connection between service consumer and provider.|private_link_service_connection_state|properties_private_link_service_connection_state|
|**--provisioning_state**|choice|The current provisioning state.|provisioning_state|properties_provisioning_state|
### machinelearningservices private-endpoint-connection show

show a machinelearningservices private-endpoint-connection.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|
|**--private_endpoint_connection_name**|string|The name of the private endpoint connection associated with the workspace|private_endpoint_connection_name|private_endpoint_connection_name|
### machinelearningservices private-link-resource list

list a machinelearningservices private-link-resource.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|
### machinelearningservices quota list

list a machinelearningservices quota.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--location**|string|The location for which resource usage is queried.|location|location|
### machinelearningservices quota update

update a machinelearningservices quota.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--location**|string|The location for which resource usage is queried.|location|location|
|**--value**|array|The list for update quota.|value|value|
### machinelearningservices usage list

list a machinelearningservices usage.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--location**|string|The location for which resource usage is queried.|location|location|
### machinelearningservices virtual-machine-size list

list a machinelearningservices virtual-machine-size.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--location**|string|The location for which resource usage is queried.|location|location|
### machinelearningservices workspace create

create a machinelearningservices workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|
|**--identity**|object|Identity for the resource.|identity|identity|
|**--location**|string|Specifies the location of the resource.|location|location|
|**--tags**|dictionary|Contains resource tags defined as key/value pairs.|tags|tags|
|**--sku**|object|Sku of the resource|sku|sku|
|**--description**|string|The description of this workspace.|description|properties_description|
|**--friendly_name**|string|The friendly name for this workspace. This name in mutable|friendly_name|properties_friendly_name|
|**--key_vault**|string|ARM id of the key vault associated with this workspace. This cannot be changed once the workspace has been created|key_vault|properties_key_vault|
|**--application_insights**|string|ARM id of the application insights associated with this workspace. This cannot be changed once the workspace has been created|application_insights|properties_application_insights|
|**--container_registry**|string|ARM id of the container registry associated with this workspace. This cannot be changed once the workspace has been created|container_registry|properties_container_registry|
|**--storage_account**|string|ARM id of the storage account associated with this workspace. This cannot be changed once the workspace has been created|storage_account|properties_storage_account|
|**--discovery_url**|string|Url for the discovery service to identify regional endpoints for machine learning experimentation services|discovery_url|properties_discovery_url|
|**--encryption**|object||encryption|properties_encryption|
|**--hbi_workspace**|boolean|The flag to signal HBI data in the workspace and reduce diagnostic data collected by the service|hbi_workspace|properties_hbi_workspace|
|**--image_build_compute**|string|The compute name for image build|image_build_compute|properties_image_build_compute|
|**--allow_public_access_when_behind_vnet**|boolean|The flag to indicate whether to allow public access when behind VNet.|allow_public_access_when_behind_vnet|properties_allow_public_access_when_behind_vnet|
|**--shared_private_link_resources**|array|The list of shared private link resources in this workspace.|shared_private_link_resources|properties_shared_private_link_resources|
|**--linked_workspaces**|dictionary|Dictionary that contains all linked workspaces in the AML workspace, with resourceId of the linked workspace as key.|linked_workspaces|properties_linked_workspaces|
### machinelearningservices workspace delete

delete a machinelearningservices workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|
### machinelearningservices workspace list

list a machinelearningservices workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--skiptoken**|string|Continuation token for pagination.|skiptoken|skiptoken|
### machinelearningservices workspace list-key

list-key a machinelearningservices workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|
### machinelearningservices workspace resync-key

resync-key a machinelearningservices workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|
### machinelearningservices workspace show

show a machinelearningservices workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|
### machinelearningservices workspace update

update a machinelearningservices workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|
|**--tags**|dictionary|The resource tags for the machine learning workspace.|tags|tags|
|**--sku**|object|Sku of the resource|sku|sku|
|**--description**|string|The description of this workspace.|description|properties_description|
|**--friendly_name**|string|The friendly name for this workspace.|friendly_name|properties_friendly_name|
### machinelearningservices workspace-feature list

list a machinelearningservices workspace-feature.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Name of the resource group in which workspace is located.|resource_group_name|resource_group_name|
|**--workspace_name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspace_name|