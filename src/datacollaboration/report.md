# Azure CLI Module Creation Report

### datacollaboration constraint create

create a datacollaboration constraint.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration constraint|Constraints|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|CreateOrUpdate#Create|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|
|**--constraint-name**|string|The name of the constraint.|constraint_name|constraintName|
|**--location-constraint**|object|Constraint used to only allow access if the resource is used within the specified Azure location.|location_constraint|LocationConstraint|
|**--script-constraint**|object|Constraint used to only allow access if the resource is used with a specific script.|script_constraint|ScriptConstraint|

### datacollaboration constraint delete

delete a datacollaboration constraint.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration constraint|Constraints|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|Delete|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|
|**--constraint-name**|string|The name of the constraint.|constraint_name|constraintName|

### datacollaboration constraint list

list a datacollaboration constraint.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration constraint|Constraints|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListByEntitlement|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|
|**--filter**|string|Filters the results using OData syntax.|filter|$filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|$orderby|

### datacollaboration constraint show

show a datacollaboration constraint.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration constraint|Constraints|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|show|Get|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|
|**--constraint-name**|string|The name of the constraint.|constraint_name|constraintName|

### datacollaboration constraint update

update a datacollaboration constraint.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration constraint|Constraints|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|CreateOrUpdate#Update|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|
|**--constraint-name**|string|The name of the constraint.|constraint_name|constraintName|
|**--location-constraint**|object|Constraint used to only allow access if the resource is used within the specified Azure location.|location_constraint|LocationConstraint|
|**--script-constraint**|object|Constraint used to only allow access if the resource is used with a specific script.|script_constraint|ScriptConstraint|

### datacollaboration consumer-invitation list-invitation

list-invitation a datacollaboration consumer-invitation.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration consumer-invitation|ConsumerInvitations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-invitation|ListInvitations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--skip-token**|string|The continuation token|skip_token|$skipToken|

### datacollaboration consumer-invitation reject-invitation

reject-invitation a datacollaboration consumer-invitation.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration consumer-invitation|ConsumerInvitations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reject-invitation|RejectInvitation|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|Location of the invitation|location|location|
|**--invitation-id**|string|An invitation id|invitation_id|invitationId|

### datacollaboration consumer-invitation show

show a datacollaboration consumer-invitation.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration consumer-invitation|ConsumerInvitations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|show|Get|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|Location of the invitation|location|location|
|**--invitation-id**|string|An invitation id|invitation_id|invitationId|

### datacollaboration data-asset create

create a datacollaboration data-asset.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration data-asset|DataAssets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|CreateOrUpdate#Create|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--data-asset-name**|string|The name of the DataAsset|data_asset_name|dataAssetName|
|**--data-processing-strategy**|choice|Data processing strategy to use for the the child DataSets|data_processing_strategy|dataProcessingStrategy|
|**--description**|string|General Description of the DataSet content|description|description|

### datacollaboration data-asset delete

delete a datacollaboration data-asset.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration data-asset|DataAssets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|Delete|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--data-asset-name**|string|The name of the DataAsset|data_asset_name|dataAssetName|

### datacollaboration data-asset list

list a datacollaboration data-asset.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration data-asset|DataAssets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListByWorkspace|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--skip-token**|string|Continuation Token|skip_token|$skipToken|
|**--filter**|string|Filters the results using OData syntax.|filter|$filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|$orderby|

### datacollaboration data-asset show

show a datacollaboration data-asset.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration data-asset|DataAssets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|show|Get|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--data-asset-name**|string|The name of the dataAssetName|data_asset_name|dataAssetName|

### datacollaboration data-asset update

update a datacollaboration data-asset.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration data-asset|DataAssets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|CreateOrUpdate#Update|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--data-asset-name**|string|The name of the DataAsset|data_asset_name|dataAssetName|
|**--data-processing-strategy**|choice|Data processing strategy to use for the the child DataSets|data_processing_strategy|dataProcessingStrategy|
|**--description**|string|General Description of the DataSet content|description|description|

### datacollaboration data-asset-reference create

create a datacollaboration data-asset-reference.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration data-asset-reference|DataAssetReferences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|CreateOrUpdate#Create|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--reference-name**|string|The name of the reference.|reference_name|referenceName|
|**--data-asset-id**|string|The unique identifier of the referenced data asset|data_asset_id|dataAssetId|
|**--description**|string|General Description of the data asset reference|description|description|

### datacollaboration data-asset-reference delete

delete a datacollaboration data-asset-reference.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration data-asset-reference|DataAssetReferences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|Delete|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--reference-name**|string|The name of the reference.|reference_name|referenceName|

### datacollaboration data-asset-reference list

list a datacollaboration data-asset-reference.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration data-asset-reference|DataAssetReferences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListByProposal|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|

### datacollaboration data-asset-reference resolve

resolve a datacollaboration data-asset-reference.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration data-asset-reference|DataAssetReferences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|resolve|Resolve|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--reference-name**|string|The name of the reference.|reference_name|referenceName|

### datacollaboration data-asset-reference show

show a datacollaboration data-asset-reference.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration data-asset-reference|DataAssetReferences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|show|Get|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--reference-name**|string|The name of the reference.|reference_name|referenceName|

### datacollaboration data-asset-reference update

update a datacollaboration data-asset-reference.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration data-asset-reference|DataAssetReferences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|CreateOrUpdate#Update|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--reference-name**|string|The name of the reference.|reference_name|referenceName|
|**--data-asset-id**|string|The unique identifier of the referenced data asset|data_asset_id|dataAssetId|
|**--description**|string|General Description of the data asset reference|description|description|

### datacollaboration data-set create

create a datacollaboration data-set.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration data-set|DataSets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|CreateOrUpdate#Create|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--data-asset-name**|string|The name of the DataAsset|data_asset_name|dataAssetName|
|**--data-set-category**|choice|The usage category name of the DataSet|data_set_category|dataSetCategory|
|**--adls-gen2-file-data-set**|object|An ADLS Gen 2 file data set.|adls_gen2_file_data_set|ADLSGen2FileDataSet|
|**--adls-gen2-file-system-data-set**|object|An ADLS Gen 2 file system data set.|adls_gen2_file_system_data_set|ADLSGen2FileSystemDataSet|
|**--adls-gen2-folder-data-set**|object|An ADLS Gen 2 folder data set.|adls_gen2_folder_data_set|ADLSGen2FolderDataSet|
|**--blob-container-data-set**|object|An Azure storage blob container data set.|blob_container_data_set|BlobContainerDataSet|
|**--blob-data-set**|object|An Azure storage blob data set.|blob_data_set|BlobDataSet|
|**--blob-folder-data-set**|object|An Azure storage blob folder data set.|blob_folder_data_set|BlobFolderDataSet|

### datacollaboration data-set delete

delete a datacollaboration data-set.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration data-set|DataSets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|Delete|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--data-asset-name**|string|The name of the DataAsset|data_asset_name|dataAssetName|
|**--data-set-category**|choice|The usage category name of the DataSet|data_set_category|dataSetCategory|

### datacollaboration data-set list

list a datacollaboration data-set.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration data-set|DataSets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListByDataAsset|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--data-asset-name**|string|The name of the DataAsset|data_asset_name|dataAssetName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|

### datacollaboration data-set show

show a datacollaboration data-set.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration data-set|DataSets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|show|Get|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--data-asset-name**|string|The name of the DataAsset|data_asset_name|dataAssetName|
|**--data-set-category**|choice|The usage category name of the DataSet|data_set_category|dataSetCategory|

### datacollaboration data-set update

update a datacollaboration data-set.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration data-set|DataSets|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|CreateOrUpdate#Update|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--data-asset-name**|string|The name of the DataAsset|data_asset_name|dataAssetName|
|**--data-set-category**|choice|The usage category name of the DataSet|data_set_category|dataSetCategory|
|**--adls-gen2-file-data-set**|object|An ADLS Gen 2 file data set.|adls_gen2_file_data_set|ADLSGen2FileDataSet|
|**--adls-gen2-file-system-data-set**|object|An ADLS Gen 2 file system data set.|adls_gen2_file_system_data_set|ADLSGen2FileSystemDataSet|
|**--adls-gen2-folder-data-set**|object|An ADLS Gen 2 folder data set.|adls_gen2_folder_data_set|ADLSGen2FolderDataSet|
|**--blob-container-data-set**|object|An Azure storage blob container data set.|blob_container_data_set|BlobContainerDataSet|
|**--blob-data-set**|object|An Azure storage blob data set.|blob_data_set|BlobDataSet|
|**--blob-folder-data-set**|object|An Azure storage blob folder data set.|blob_folder_data_set|BlobFolderDataSet|

### datacollaboration entitlement create

create a datacollaboration entitlement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration entitlement|Entitlements|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|CreateOrUpdate#Create|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|
|**--resource-id**|string|The unique identifier of the resource of the entitlement. Must be a reference resource from the same proposal.|resource_id|resourceId|
|**--resource-type**|choice|The type of resourced used by the entitlement.|resource_type|resourceType|
|**--subject-id**|string|The unique identifier of the subject of the entitlement. The subject must be a participant in the same proposal.|subject_id|subjectId|
|**--description**|string|Textual description of the entitlement|description|description|

### datacollaboration entitlement delete

delete a datacollaboration entitlement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration entitlement|Entitlements|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|Delete|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|

### datacollaboration entitlement list

list a datacollaboration entitlement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration entitlement|Entitlements|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListByProposal|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|
|**--filter**|string|Filters the results using OData syntax.|filter|$filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|$orderby|

### datacollaboration entitlement show

show a datacollaboration entitlement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration entitlement|Entitlements|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|show|Get|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|

### datacollaboration entitlement update

update a datacollaboration entitlement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration entitlement|Entitlements|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|CreateOrUpdate#Update|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|
|**--resource-id**|string|The unique identifier of the resource of the entitlement. Must be a reference resource from the same proposal.|resource_id|resourceId|
|**--resource-type**|choice|The type of resourced used by the entitlement.|resource_type|resourceType|
|**--subject-id**|string|The unique identifier of the subject of the entitlement. The subject must be a participant in the same proposal.|subject_id|subjectId|
|**--description**|string|Textual description of the entitlement|description|description|

### datacollaboration invitation create

create a datacollaboration invitation.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration invitation|Invitations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|Create|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal to send the invitation for.|proposal_name|proposalName|
|**--invitation-name**|string|The name of the invitation.|invitation_name|invitationName|
|**--target-active-directory-id**|string|The target Azure AD Id. Can't be combined with email.|target_active_directory_id|targetActiveDirectoryId|
|**--target-email**|string|The email the invitation is directed to.|target_email|targetEmail|
|**--target-object-id**|string|The target user or application Id that invitation is being sent to. Must be specified along TargetActiveDirectoryId. This enables sending invitations to specific users or applications in an AD tenant.|target_object_id|targetObjectId|

### datacollaboration invitation delete

delete a datacollaboration invitation.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration invitation|Invitations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|Delete|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--invitation-name**|string|The name of the invitation.|invitation_name|invitationName|

### datacollaboration invitation list

list a datacollaboration invitation.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration invitation|Invitations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListByProposal|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--skip-token**|string|The continuation token|skip_token|$skipToken|

### datacollaboration invitation show

show a datacollaboration invitation.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration invitation|Invitations|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|show|Get|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--invitation-name**|string|The name of the invitation.|invitation_name|invitationName|

### datacollaboration participant list

list a datacollaboration participant.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration participant|Participants|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListByProposal|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|

### datacollaboration participant show

show a datacollaboration participant.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration participant|Participants|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|show|Get|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--participant-name**|string|The name of the participant.|participant_name|participantName|

### datacollaboration pipeline create

create a datacollaboration pipeline.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration pipeline|Pipelines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|CreateOrUpdate#Create|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|pipelineName|
|**--description**|string|General Description of the pipeline content|description|description|

### datacollaboration pipeline delete

delete a datacollaboration pipeline.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration pipeline|Pipelines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|Delete|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|pipelineName|

### datacollaboration pipeline list

list a datacollaboration pipeline.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration pipeline|Pipelines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListByWorkspace|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|
|**--filter**|string|Filters the results using OData syntax.|filter|$filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|$orderby|

### datacollaboration pipeline run

run a datacollaboration pipeline.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration pipeline|Pipelines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|run|Run|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|pipelineName|
|**--pipeline-run-mode**|choice|Mode of pipeline run used.|pipeline_run_mode|pipelineRunMode|

### datacollaboration pipeline show

show a datacollaboration pipeline.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration pipeline|Pipelines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|show|Get|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|pipelineName|

### datacollaboration pipeline update

update a datacollaboration pipeline.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration pipeline|Pipelines|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|CreateOrUpdate#Update|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|pipelineName|
|**--description**|string|General Description of the pipeline content|description|description|

### datacollaboration pipeline-run cancel

cancel a datacollaboration pipeline-run.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration pipeline-run|PipelineRuns|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|Cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-run-name**|string|The name of the pipeline run.|pipeline_run_name|pipelineRunName|

### datacollaboration pipeline-run list

list a datacollaboration pipeline-run.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration pipeline-run|PipelineRuns|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListByWorkspace|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--skip-token**|string|Continuation token|skip_token|$skipToken|
|**--filter**|string|Filters the results using OData syntax.|filter|$filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|$orderby|

### datacollaboration pipeline-run show

show a datacollaboration pipeline-run.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration pipeline-run|PipelineRuns|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|show|Get|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-run-name**|string|The name of the pipeline run.|pipeline_run_name|pipelineRunName|

### datacollaboration pipeline-step create

create a datacollaboration pipeline-step.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration pipeline-step|PipelineSteps|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|CreateOrUpdate#Create|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|pipelineName|
|**--pipeline-step-name**|string|The name of the pipeline step.|pipeline_step_name|pipelineStepName|
|**--synapse-spark-pipeline-step**|object|A Synapse Spark based pipeline step.|synapse_spark_pipeline_step|SynapseSparkPipelineStep|

### datacollaboration pipeline-step delete

delete a datacollaboration pipeline-step.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration pipeline-step|PipelineSteps|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|Delete|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|pipelineName|
|**--pipeline-step-name**|string|The name of the pipeline step.|pipeline_step_name|pipelineStepName|

### datacollaboration pipeline-step list

list a datacollaboration pipeline-step.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration pipeline-step|PipelineSteps|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListByPipeline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|pipelineName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|

### datacollaboration pipeline-step show

show a datacollaboration pipeline-step.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration pipeline-step|PipelineSteps|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|show|Get|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|pipelineName|
|**--pipeline-step-name**|string|The name of the pipeline step.|pipeline_step_name|pipelineStepName|

### datacollaboration pipeline-step update

update a datacollaboration pipeline-step.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration pipeline-step|PipelineSteps|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|CreateOrUpdate#Update|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|pipelineName|
|**--pipeline-step-name**|string|The name of the pipeline step.|pipeline_step_name|pipelineStepName|
|**--synapse-spark-pipeline-step**|object|A Synapse Spark based pipeline step.|synapse_spark_pipeline_step|SynapseSparkPipelineStep|

### datacollaboration pipeline-step-run list

list a datacollaboration pipeline-step-run.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration pipeline-step-run|PipelineStepRuns|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListByPipelineRun|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-run-name**|string|The name of the pipeline run.|pipeline_run_name|pipelineRunName|
|**--skip-token**|string|Continuation token|skip_token|$skipToken|

### datacollaboration pipeline-step-run show

show a datacollaboration pipeline-step-run.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration pipeline-step-run|PipelineStepRuns|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|show|Get|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-run-name**|string|The name of the pipeline run.|pipeline_run_name|pipelineRunName|
|**--pipeline-step-run-name**|string|The name of the pipeline step run.|pipeline_step_run_name|pipelineStepRunName|

### datacollaboration policy create

create a datacollaboration policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration policy|Policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|CreateOrUpdate#Create|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|
|**--policy-name**|string|The name of the policy.|policy_name|policyName|
|**--diagnostic-policy**|object|A diagnostic policy.|diagnostic_policy|DiagnosticPolicy|

### datacollaboration policy delete

delete a datacollaboration policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration policy|Policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|Delete|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|
|**--policy-name**|string|The name of the policy.|policy_name|policyName|

### datacollaboration policy list

list a datacollaboration policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration policy|Policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListByEntitlement|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|
|**--filter**|string|Filters the results using OData syntax.|filter|$filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|$orderby|

### datacollaboration policy show

show a datacollaboration policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration policy|Policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|show|Get|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|
|**--policy-name**|string|The name of the policy.|policy_name|policyName|

### datacollaboration policy update

update a datacollaboration policy.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration policy|Policies|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|CreateOrUpdate#Update|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|
|**--policy-name**|string|The name of the policy.|policy_name|policyName|
|**--diagnostic-policy**|object|A diagnostic policy.|diagnostic_policy|DiagnosticPolicy|

### datacollaboration proposal create

create a datacollaboration proposal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration proposal|Proposals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|CreateOrUpdate#Create|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--description**|string|Textual description of the proposal|description|description|
|**--display-name**|string|Display name of the proposal|display_name|displayName|
|**--invitation-id**|string|The invitation id for joining a proposal|invitation_id|invitationId|
|**--invitation-location**|string|The invitation id for joining a proposal|invitation_location|invitationLocation|
|**--terms**|string|Terms of the proposal|terms|terms|

### datacollaboration proposal delete

delete a datacollaboration proposal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration proposal|Proposals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|Delete|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|

### datacollaboration proposal list

list a datacollaboration proposal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration proposal|Proposals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListByWorkspace|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|
|**--filter**|string|Filters the results using OData syntax.|filter|$filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|$orderby|

### datacollaboration proposal revoke

revoke a datacollaboration proposal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration proposal|Proposals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|revoke|Revoke|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|

### datacollaboration proposal show

show a datacollaboration proposal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration proposal|Proposals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|show|Get|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|

### datacollaboration proposal sign

sign a datacollaboration proposal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration proposal|Proposals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|sign|Sign|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--proposal-version**|string|Proposal version to be signed|proposal_version|proposalVersion|

### datacollaboration proposal update

update a datacollaboration proposal.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration proposal|Proposals|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|CreateOrUpdate#Update|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--description**|string|Textual description of the proposal|description|description|
|**--display-name**|string|Display name of the proposal|display_name|displayName|
|**--invitation-id**|string|The invitation id for joining a proposal|invitation_id|invitationId|
|**--invitation-location**|string|The invitation id for joining a proposal|invitation_location|invitationLocation|
|**--terms**|string|Terms of the proposal|terms|terms|

### datacollaboration resource-reference list

list a datacollaboration resource-reference.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration resource-reference|ResourceReferences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListByWorkspace|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|
|**--filter**|string|Filters the results using OData syntax.|filter|$filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|$orderby|

### datacollaboration script create

create a datacollaboration script.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration script|Scripts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|CreateOrUpdate#Create|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--script-name**|string|The name of the script.|script_name|scriptName|
|**--synapse-spark-script**|object|A type of script based on the compute engine|synapse_spark_script|SynapseSparkScript|

### datacollaboration script delete

delete a datacollaboration script.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration script|Scripts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|Delete|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--script-name**|string|The name of the script.|script_name|scriptName|

### datacollaboration script list

list a datacollaboration script.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration script|Scripts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListByWorkspace|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|
|**--filter**|string|Filters the results using OData syntax.|filter|$filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|$orderby|

### datacollaboration script show

show a datacollaboration script.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration script|Scripts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|show|Get|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--script-name**|string|The name of the script.|script_name|scriptName|

### datacollaboration script update

update a datacollaboration script.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration script|Scripts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|CreateOrUpdate#Update|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--script-name**|string|The name of the script.|script_name|scriptName|
|**--synapse-spark-script**|object|A type of script based on the compute engine|synapse_spark_script|SynapseSparkScript|

### datacollaboration script-reference create

create a datacollaboration script-reference.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration script-reference|ScriptReferences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|CreateOrUpdate#Create|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--reference-name**|string|The name of the reference.|reference_name|referenceName|
|**--revision**|integer|The revision number of the script being referenced. If omitted, the script latest version will be referenced.|revision|revision|
|**--script-id**|string|The unique identifier of the referenced script|script_id|scriptId|

### datacollaboration script-reference delete

delete a datacollaboration script-reference.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration script-reference|ScriptReferences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|Delete|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--reference-name**|string|The name of the reference.|reference_name|referenceName|

### datacollaboration script-reference list

list a datacollaboration script-reference.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration script-reference|ScriptReferences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListByProposal|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|

### datacollaboration script-reference resolve

resolve a datacollaboration script-reference.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration script-reference|ScriptReferences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|resolve|Resolve|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--reference-name**|string|The name of the reference.|reference_name|referenceName|

### datacollaboration script-reference show

show a datacollaboration script-reference.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration script-reference|ScriptReferences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|show|Get|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--reference-name**|string|The name of the reference.|reference_name|referenceName|

### datacollaboration script-reference update

update a datacollaboration script-reference.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration script-reference|ScriptReferences|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|CreateOrUpdate#Update|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--reference-name**|string|The name of the reference.|reference_name|referenceName|
|**--revision**|integer|The revision number of the script being referenced. If omitted, the script latest version will be referenced.|revision|revision|
|**--script-id**|string|The unique identifier of the referenced script|script_id|scriptId|

### datacollaboration script-revision list

list a datacollaboration script-revision.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration script-revision|ScriptRevisions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListByScript|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--script-name**|string|The name of the script.|script_name|scriptName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|

### datacollaboration script-revision show

show a datacollaboration script-revision.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration script-revision|ScriptRevisions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|show|Get|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--script-name**|string|The name of the script.|script_name|scriptName|
|**--revision**|integer|The revision of the script.|revision|revision|

### datacollaboration workspace create

create a datacollaboration workspace.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration workspace|Workspaces|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|CreateOrUpdate#Create|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--location**|string|Location of the azure resource.|location|location|
|**--tags**|dictionary|Tags on the azure resource.|tags|tags|

### datacollaboration workspace delete

delete a datacollaboration workspace.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration workspace|Workspaces|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|Delete|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|

### datacollaboration workspace list

list a datacollaboration workspace.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration workspace|Workspaces|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListByResourceGroup|
|list|ListBySubscription|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--skip-token**|string|Continuation token|skip_token|$skipToken|

### datacollaboration workspace show

show a datacollaboration workspace.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration workspace|Workspaces|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|show|Get|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|

### datacollaboration workspace update

update a datacollaboration workspace.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|datacollaboration workspace|Workspaces|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|Update|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--tags**|dictionary|Tags on the azure resource.|tags|tags|
