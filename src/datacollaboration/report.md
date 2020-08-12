# Azure CLI Module Creation Report

### datacollaboration constraint create

create a datacollaboration constraint.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|
|**--constraint-name**|string|The name of the constraint.|constraint_name|
|**--location-constraint**|object|Constraint used to only allow access if the resource is used within the specified Azure location.|location_constraint|
|**--script-constraint**|object|Constraint used to only allow access if the resource is used with a specific script.|script_constraint|
### datacollaboration constraint delete

delete a datacollaboration constraint.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|
|**--constraint-name**|string|The name of the constraint.|constraint_name|
### datacollaboration constraint list

list a datacollaboration constraint.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|
|**--skip-token**|string|continuation token|skip_token|
|**--filter**|string|Filters the results using OData syntax.|filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|
### datacollaboration constraint show

show a datacollaboration constraint.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|
|**--constraint-name**|string|The name of the constraint.|constraint_name|
### datacollaboration constraint update

create a datacollaboration constraint.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|
|**--constraint-name**|string|The name of the constraint.|constraint_name|
|**--location-constraint**|object|Constraint used to only allow access if the resource is used within the specified Azure location.|location_constraint|
|**--script-constraint**|object|Constraint used to only allow access if the resource is used with a specific script.|script_constraint|
### datacollaboration consumer-invitation list-invitation

list-invitation a datacollaboration consumer-invitation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--skip-token**|string|The continuation token|skip_token|
### datacollaboration consumer-invitation reject-invitation

reject-invitation a datacollaboration consumer-invitation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--location**|string|Location of the invitation|location|
|**--invitation-id**|string|An invitation id|invitation_id|
### datacollaboration consumer-invitation show

show a datacollaboration consumer-invitation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--location**|string|Location of the invitation|location|
|**--invitation-id**|string|An invitation id|invitation_id|
### datacollaboration data-asset create

create a datacollaboration data-asset.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--data-asset-name**|string|The name of the DataAsset|data_asset_name|
|**--data-processing-strategy**|choice|Data processing strategy to use for the the child DataSets|data_processing_strategy|
|**--description**|string|General Description of the DataSet content|description|
### datacollaboration data-asset delete

delete a datacollaboration data-asset.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--data-asset-name**|string|The name of the DataAsset|data_asset_name|
### datacollaboration data-asset list

list a datacollaboration data-asset.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--skip-token**|string|Continuation Token|skip_token|
|**--filter**|string|Filters the results using OData syntax.|filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|
### datacollaboration data-asset show

show a datacollaboration data-asset.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--data-asset-name**|string|The name of the dataAssetName|data_asset_name|
### datacollaboration data-asset update

create a datacollaboration data-asset.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--data-asset-name**|string|The name of the DataAsset|data_asset_name|
|**--data-processing-strategy**|choice|Data processing strategy to use for the the child DataSets|data_processing_strategy|
|**--description**|string|General Description of the DataSet content|description|
### datacollaboration data-asset-reference create

create a datacollaboration data-asset-reference.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--reference-name**|string|The name of the reference.|reference_name|
|**--data-asset-id**|string|The unique identifier of the referenced data asset|data_asset_id|
|**--description**|string|General Description of the data asset reference|description|
### datacollaboration data-asset-reference delete

delete a datacollaboration data-asset-reference.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--reference-name**|string|The name of the reference.|reference_name|
### datacollaboration data-asset-reference list

list a datacollaboration data-asset-reference.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--skip-token**|string|continuation token|skip_token|
### datacollaboration data-asset-reference resolve

resolve a datacollaboration data-asset-reference.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--reference-name**|string|The name of the reference.|reference_name|
### datacollaboration data-asset-reference show

show a datacollaboration data-asset-reference.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--reference-name**|string|The name of the reference.|reference_name|
### datacollaboration data-asset-reference update

create a datacollaboration data-asset-reference.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--reference-name**|string|The name of the reference.|reference_name|
|**--data-asset-id**|string|The unique identifier of the referenced data asset|data_asset_id|
|**--description**|string|General Description of the data asset reference|description|
### datacollaboration data-set create

create a datacollaboration data-set.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--data-asset-name**|string|The name of the DataAsset|data_asset_name|
|**--data-set-category**|choice|The usage category name of the DataSet|data_set_category|
|**--a-d-l-s-gen2-file-data-set**|object|An ADLS Gen 2 file data set.|a_d_l_s_gen2_file_data_set|
|**--a-d-l-s-gen2-file-system-data-set**|object|An ADLS Gen 2 file system data set.|a_d_l_s_gen2_file_system_data_set|
|**--a-d-l-s-gen2-folder-data-set**|object|An ADLS Gen 2 folder data set.|a_d_l_s_gen2_folder_data_set|
|**--blob-container-data-set**|object|An Azure storage blob container data set.|blob_container_data_set|
|**--blob-data-set**|object|An Azure storage blob data set.|blob_data_set|
|**--blob-folder-data-set**|object|An Azure storage blob folder data set.|blob_folder_data_set|
### datacollaboration data-set delete

delete a datacollaboration data-set.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--data-asset-name**|string|The name of the DataAsset|data_asset_name|
|**--data-set-category**|choice|The usage category name of the DataSet|data_set_category|
### datacollaboration data-set list

list a datacollaboration data-set.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--data-asset-name**|string|The name of the DataAsset|data_asset_name|
|**--skip-token**|string|continuation token|skip_token|
### datacollaboration data-set show

show a datacollaboration data-set.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--data-asset-name**|string|The name of the DataAsset|data_asset_name|
|**--data-set-category**|choice|The usage category name of the DataSet|data_set_category|
### datacollaboration data-set update

create a datacollaboration data-set.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--data-asset-name**|string|The name of the DataAsset|data_asset_name|
|**--data-set-category**|choice|The usage category name of the DataSet|data_set_category|
|**--a-d-l-s-gen2-file-data-set**|object|An ADLS Gen 2 file data set.|a_d_l_s_gen2_file_data_set|
|**--a-d-l-s-gen2-file-system-data-set**|object|An ADLS Gen 2 file system data set.|a_d_l_s_gen2_file_system_data_set|
|**--a-d-l-s-gen2-folder-data-set**|object|An ADLS Gen 2 folder data set.|a_d_l_s_gen2_folder_data_set|
|**--blob-container-data-set**|object|An Azure storage blob container data set.|blob_container_data_set|
|**--blob-data-set**|object|An Azure storage blob data set.|blob_data_set|
|**--blob-folder-data-set**|object|An Azure storage blob folder data set.|blob_folder_data_set|
### datacollaboration entitlement create

create a datacollaboration entitlement.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|
|**--resource-id**|string|The unique identifier of the resource of the entitlement.
Must be a reference resource from the same proposal.|resource_id|
|**--resource-type**|choice|The type of resourced used by the entitlement.|resource_type|
|**--subject-id**|string|The unique identifier of the subject of the entitlement.
The subject must be a participant in the same proposal.|subject_id|
|**--description**|string|Textual description of the entitlement|description|
### datacollaboration entitlement delete

delete a datacollaboration entitlement.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|
### datacollaboration entitlement list

list a datacollaboration entitlement.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--skip-token**|string|continuation token|skip_token|
|**--filter**|string|Filters the results using OData syntax.|filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|
### datacollaboration entitlement show

show a datacollaboration entitlement.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|
### datacollaboration entitlement update

create a datacollaboration entitlement.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|
|**--resource-id**|string|The unique identifier of the resource of the entitlement.
Must be a reference resource from the same proposal.|resource_id|
|**--resource-type**|choice|The type of resourced used by the entitlement.|resource_type|
|**--subject-id**|string|The unique identifier of the subject of the entitlement.
The subject must be a participant in the same proposal.|subject_id|
|**--description**|string|Textual description of the entitlement|description|
### datacollaboration invitation create

create a datacollaboration invitation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal to send the invitation for.|proposal_name|
|**--invitation-name**|string|The name of the invitation.|invitation_name|
|**--target-active-directory-id**|string|The target Azure AD Id. Can't be combined with email.|target_active_directory_id|
|**--target-email**|string|The email the invitation is directed to.|target_email|
|**--target-object-id**|string|The target user or application Id that invitation is being sent to.
Must be specified along TargetActiveDirectoryId. This enables sending
invitations to specific users or applications in an AD tenant.|target_object_id|
### datacollaboration invitation delete

delete a datacollaboration invitation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--invitation-name**|string|The name of the invitation.|invitation_name|
### datacollaboration invitation list

list a datacollaboration invitation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--skip-token**|string|The continuation token|skip_token|
### datacollaboration invitation show

show a datacollaboration invitation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--invitation-name**|string|The name of the invitation.|invitation_name|
### datacollaboration participant list

list a datacollaboration participant.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--skip-token**|string|continuation token|skip_token|
### datacollaboration participant show

show a datacollaboration participant.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--participant-name**|string|The name of the participant.|participant_name|
### datacollaboration pipeline create

create a datacollaboration pipeline.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|
|**--description**|string|General Description of the pipeline content|description|
### datacollaboration pipeline delete

delete a datacollaboration pipeline.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|
### datacollaboration pipeline list

list a datacollaboration pipeline.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--skip-token**|string|continuation token|skip_token|
|**--filter**|string|Filters the results using OData syntax.|filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|
### datacollaboration pipeline run

run a datacollaboration pipeline.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|
### datacollaboration pipeline show

show a datacollaboration pipeline.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|
### datacollaboration pipeline update

create a datacollaboration pipeline.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|
|**--description**|string|General Description of the pipeline content|description|
### datacollaboration pipeline-run cancel

cancel a datacollaboration pipeline-run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|
|**--pipeline-run-name**|string|The name of the pipeline run.|pipeline_run_name|
### datacollaboration pipeline-run list

list a datacollaboration pipeline-run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|
|**--skip-token**|string|Continuation token|skip_token|
### datacollaboration pipeline-run show

show a datacollaboration pipeline-run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|
|**--pipeline-run-name**|string|The name of the pipeline run.|pipeline_run_name|
### datacollaboration pipeline-step create

create a datacollaboration pipeline-step.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|
|**--pipeline-step-name**|string|The name of the pipeline step.|pipeline_step_name|
|**--synapse-spark-pipeline-step**|object|A Synapse Spark based pipeline step.|synapse_spark_pipeline_step|
### datacollaboration pipeline-step delete

delete a datacollaboration pipeline-step.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|
|**--pipeline-step-name**|string|The name of the pipeline step.|pipeline_step_name|
### datacollaboration pipeline-step list

list a datacollaboration pipeline-step.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|
|**--skip-token**|string|continuation token|skip_token|
### datacollaboration pipeline-step show

show a datacollaboration pipeline-step.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|
|**--pipeline-step-name**|string|The name of the pipeline step.|pipeline_step_name|
### datacollaboration pipeline-step update

create a datacollaboration pipeline-step.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|
|**--pipeline-step-name**|string|The name of the pipeline step.|pipeline_step_name|
|**--synapse-spark-pipeline-step**|object|A Synapse Spark based pipeline step.|synapse_spark_pipeline_step|
### datacollaboration pipeline-step-run list

list a datacollaboration pipeline-step-run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|
|**--pipeline-run-name**|string|The name of the pipeline run.|pipeline_run_name|
|**--skip-token**|string|Continuation token|skip_token|
### datacollaboration pipeline-step-run show

show a datacollaboration pipeline-step-run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|
|**--pipeline-run-name**|string|The name of the pipeline run.|pipeline_run_name|
|**--pipeline-step-run-id**|string|The id of the pipeline step run.|pipeline_step_run_id|
### datacollaboration policy create

create a datacollaboration policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|
|**--policy-name**|string|The name of the policy.|policy_name|
|**--diagnostic-policy**|object|A diagnostic policy.|diagnostic_policy|
### datacollaboration policy delete

delete a datacollaboration policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|
|**--policy-name**|string|The name of the policy.|policy_name|
### datacollaboration policy list

list a datacollaboration policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|
|**--skip-token**|string|continuation token|skip_token|
|**--filter**|string|Filters the results using OData syntax.|filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|
### datacollaboration policy show

show a datacollaboration policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|
|**--policy-name**|string|The name of the policy.|policy_name|
### datacollaboration policy update

create a datacollaboration policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|
|**--policy-name**|string|The name of the policy.|policy_name|
|**--diagnostic-policy**|object|A diagnostic policy.|diagnostic_policy|
### datacollaboration proposal create

create a datacollaboration proposal.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--description**|string|Textual description of the proposal|description|
|**--display-name**|string|Display name of the proposal|display_name|
|**--invitation-id**|string|The invitation id for joining a proposal|invitation_id|
|**--invitation-location**|string|The invitation id for joining a proposal|invitation_location|
|**--terms**|string|Terms of the proposal|terms|
### datacollaboration proposal delete

delete a datacollaboration proposal.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
### datacollaboration proposal list

list a datacollaboration proposal.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--skip-token**|string|continuation token|skip_token|
|**--filter**|string|Filters the results using OData syntax.|filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|
### datacollaboration proposal revoke

revoke a datacollaboration proposal.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
### datacollaboration proposal show

show a datacollaboration proposal.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
### datacollaboration proposal sign

sign a datacollaboration proposal.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--proposal-version**|string|Proposal version to be signed|proposal_version|
### datacollaboration proposal update

create a datacollaboration proposal.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--description**|string|Textual description of the proposal|description|
|**--display-name**|string|Display name of the proposal|display_name|
|**--invitation-id**|string|The invitation id for joining a proposal|invitation_id|
|**--invitation-location**|string|The invitation id for joining a proposal|invitation_location|
|**--terms**|string|Terms of the proposal|terms|
### datacollaboration script create

create a datacollaboration script.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--script-name**|string|The name of the script.|script_name|
|**--synapse-spark-script**|object|A type of script based on the compute engine|synapse_spark_script|
### datacollaboration script delete

delete a datacollaboration script.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--script-name**|string|The name of the script.|script_name|
### datacollaboration script list

list a datacollaboration script.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--skip-token**|string|continuation token|skip_token|
|**--filter**|string|Filters the results using OData syntax.|filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|
### datacollaboration script show

show a datacollaboration script.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--script-name**|string|The name of the script.|script_name|
### datacollaboration script update

create a datacollaboration script.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--script-name**|string|The name of the script.|script_name|
|**--synapse-spark-script**|object|A type of script based on the compute engine|synapse_spark_script|
### datacollaboration script-reference create

create a datacollaboration script-reference.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--reference-name**|string|The name of the reference.|reference_name|
|**--revision**|integer|The revision number of the script being referenced.
If omitted, the script latest version will be referenced.|revision|
|**--script-id**|string|The unique identifier of the referenced script|script_id|
### datacollaboration script-reference delete

delete a datacollaboration script-reference.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--reference-name**|string|The name of the reference.|reference_name|
### datacollaboration script-reference list

list a datacollaboration script-reference.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--skip-token**|string|continuation token|skip_token|
### datacollaboration script-reference resolve

resolve a datacollaboration script-reference.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--reference-name**|string|The name of the reference.|reference_name|
### datacollaboration script-reference show

show a datacollaboration script-reference.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--reference-name**|string|The name of the reference.|reference_name|
### datacollaboration script-reference update

create a datacollaboration script-reference.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--proposal-name**|string|The name of the proposal.|proposal_name|
|**--reference-name**|string|The name of the reference.|reference_name|
|**--revision**|integer|The revision number of the script being referenced.
If omitted, the script latest version will be referenced.|revision|
|**--script-id**|string|The unique identifier of the referenced script|script_id|
### datacollaboration script-revision list

list a datacollaboration script-revision.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--script-name**|string|The name of the script.|script_name|
|**--skip-token**|string|continuation token|skip_token|
### datacollaboration script-revision show

show a datacollaboration script-revision.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--script-name**|string|The name of the script.|script_name|
|**--revision**|integer|The revision of the script.|revision|
### datacollaboration workspace create

create a datacollaboration workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--location**|string|Location of the azure resource.|location|
|**--tags**|dictionary|Tags on the azure resource.|tags|
### datacollaboration workspace delete

delete a datacollaboration workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
### datacollaboration workspace list

list a datacollaboration workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--skip-token**|string|Continuation token|skip_token|
### datacollaboration workspace show

show a datacollaboration workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
### datacollaboration workspace update

update a datacollaboration workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--tags**|dictionary|Tags on the azure resource.|tags|