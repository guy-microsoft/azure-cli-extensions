# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az datacollaboration|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az datacollaboration` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az datacollaboration consumer-invitation|ConsumerInvitations|[commands](#CommandsInConsumerInvitations)|
|az datacollaboration workspace|Workspaces|[commands](#CommandsInWorkspaces)|
|az datacollaboration constrained-resource|ConstrainedResources|[commands](#CommandsInConstrainedResources)|
|az datacollaboration data-asset|DataAssets|[commands](#CommandsInDataAssets)|
|az datacollaboration data-set|DataSets|[commands](#CommandsInDataSets)|
|az datacollaboration pipeline-run|PipelineRuns|[commands](#CommandsInPipelineRuns)|
|az datacollaboration pipeline-step-run|PipelineStepRuns|[commands](#CommandsInPipelineStepRuns)|
|az datacollaboration pipeline|Pipelines|[commands](#CommandsInPipelines)|
|az datacollaboration pipeline-step|PipelineSteps|[commands](#CommandsInPipelineSteps)|
|az datacollaboration proposal|Proposals|[commands](#CommandsInProposals)|
|az datacollaboration data-asset-reference|DataAssetReferences|[commands](#CommandsInDataAssetReferences)|
|az datacollaboration entitlement|Entitlements|[commands](#CommandsInEntitlements)|
|az datacollaboration constraint|Constraints|[commands](#CommandsInConstraints)|
|az datacollaboration policy|Policies|[commands](#CommandsInPolicies)|
|az datacollaboration invitation|Invitations|[commands](#CommandsInInvitations)|
|az datacollaboration participant|Participants|[commands](#CommandsInParticipants)|
|az datacollaboration script-reference|ScriptReferences|[commands](#CommandsInScriptReferences)|
|az datacollaboration resource-reference|ResourceReferences|[commands](#CommandsInResourceReferences)|
|az datacollaboration script|Scripts|[commands](#CommandsInScripts)|
|az datacollaboration script-revision|ScriptRevisions|[commands](#CommandsInScriptRevisions)|

## COMMANDS
### <a name="CommandsInConstrainedResources">Commands in `az datacollaboration constrained-resource` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az datacollaboration constrained-resource list](#ConstrainedResourcesListByWorkspace)|ListByWorkspace|[Parameters](#ParametersConstrainedResourcesListByWorkspace)|[Example](#ExamplesConstrainedResourcesListByWorkspace)|
|[az datacollaboration constrained-resource show](#ConstrainedResourcesGet)|Get|[Parameters](#ParametersConstrainedResourcesGet)|[Example](#ExamplesConstrainedResourcesGet)|
|[az datacollaboration constrained-resource create](#ConstrainedResourcesCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersConstrainedResourcesCreateOrUpdate#Create)|[Example](#ExamplesConstrainedResourcesCreateOrUpdate#Create)|
|[az datacollaboration constrained-resource update](#ConstrainedResourcesCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersConstrainedResourcesCreateOrUpdate#Update)|Not Found|
|[az datacollaboration constrained-resource delete](#ConstrainedResourcesDelete)|Delete|[Parameters](#ParametersConstrainedResourcesDelete)|[Example](#ExamplesConstrainedResourcesDelete)|

### <a name="CommandsInConstraints">Commands in `az datacollaboration constraint` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az datacollaboration constraint list](#ConstraintsListByEntitlement)|ListByEntitlement|[Parameters](#ParametersConstraintsListByEntitlement)|[Example](#ExamplesConstraintsListByEntitlement)|
|[az datacollaboration constraint show](#ConstraintsGet)|Get|[Parameters](#ParametersConstraintsGet)|[Example](#ExamplesConstraintsGet)|
|[az datacollaboration constraint create](#ConstraintsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersConstraintsCreateOrUpdate#Create)|[Example](#ExamplesConstraintsCreateOrUpdate#Create)|
|[az datacollaboration constraint update](#ConstraintsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersConstraintsCreateOrUpdate#Update)|Not Found|
|[az datacollaboration constraint delete](#ConstraintsDelete)|Delete|[Parameters](#ParametersConstraintsDelete)|[Example](#ExamplesConstraintsDelete)|

### <a name="CommandsInConsumerInvitations">Commands in `az datacollaboration consumer-invitation` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az datacollaboration consumer-invitation show](#ConsumerInvitationsGet)|Get|[Parameters](#ParametersConsumerInvitationsGet)|[Example](#ExamplesConsumerInvitationsGet)|
|[az datacollaboration consumer-invitation list-invitation](#ConsumerInvitationsListInvitations)|ListInvitations|[Parameters](#ParametersConsumerInvitationsListInvitations)|[Example](#ExamplesConsumerInvitationsListInvitations)|
|[az datacollaboration consumer-invitation reject-invitation](#ConsumerInvitationsRejectInvitation)|RejectInvitation|[Parameters](#ParametersConsumerInvitationsRejectInvitation)|[Example](#ExamplesConsumerInvitationsRejectInvitation)|

### <a name="CommandsInDataAssets">Commands in `az datacollaboration data-asset` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az datacollaboration data-asset list](#DataAssetsListByWorkspace)|ListByWorkspace|[Parameters](#ParametersDataAssetsListByWorkspace)|[Example](#ExamplesDataAssetsListByWorkspace)|
|[az datacollaboration data-asset show](#DataAssetsGet)|Get|[Parameters](#ParametersDataAssetsGet)|[Example](#ExamplesDataAssetsGet)|
|[az datacollaboration data-asset create](#DataAssetsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersDataAssetsCreateOrUpdate#Create)|[Example](#ExamplesDataAssetsCreateOrUpdate#Create)|
|[az datacollaboration data-asset update](#DataAssetsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersDataAssetsCreateOrUpdate#Update)|Not Found|
|[az datacollaboration data-asset delete](#DataAssetsDelete)|Delete|[Parameters](#ParametersDataAssetsDelete)|[Example](#ExamplesDataAssetsDelete)|

### <a name="CommandsInDataAssetReferences">Commands in `az datacollaboration data-asset-reference` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az datacollaboration data-asset-reference list](#DataAssetReferencesListByProposal)|ListByProposal|[Parameters](#ParametersDataAssetReferencesListByProposal)|[Example](#ExamplesDataAssetReferencesListByProposal)|
|[az datacollaboration data-asset-reference show](#DataAssetReferencesGet)|Get|[Parameters](#ParametersDataAssetReferencesGet)|[Example](#ExamplesDataAssetReferencesGet)|
|[az datacollaboration data-asset-reference create](#DataAssetReferencesCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersDataAssetReferencesCreateOrUpdate#Create)|[Example](#ExamplesDataAssetReferencesCreateOrUpdate#Create)|
|[az datacollaboration data-asset-reference update](#DataAssetReferencesCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersDataAssetReferencesCreateOrUpdate#Update)|Not Found|
|[az datacollaboration data-asset-reference delete](#DataAssetReferencesDelete)|Delete|[Parameters](#ParametersDataAssetReferencesDelete)|[Example](#ExamplesDataAssetReferencesDelete)|
|[az datacollaboration data-asset-reference resolve](#DataAssetReferencesResolve)|Resolve|[Parameters](#ParametersDataAssetReferencesResolve)|[Example](#ExamplesDataAssetReferencesResolve)|

### <a name="CommandsInDataSets">Commands in `az datacollaboration data-set` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az datacollaboration data-set list](#DataSetsListByDataAsset)|ListByDataAsset|[Parameters](#ParametersDataSetsListByDataAsset)|[Example](#ExamplesDataSetsListByDataAsset)|
|[az datacollaboration data-set show](#DataSetsGet)|Get|[Parameters](#ParametersDataSetsGet)|[Example](#ExamplesDataSetsGet)|
|[az datacollaboration data-set create](#DataSetsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersDataSetsCreateOrUpdate#Create)|[Example](#ExamplesDataSetsCreateOrUpdate#Create)|
|[az datacollaboration data-set update](#DataSetsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersDataSetsCreateOrUpdate#Update)|Not Found|
|[az datacollaboration data-set delete](#DataSetsDelete)|Delete|[Parameters](#ParametersDataSetsDelete)|[Example](#ExamplesDataSetsDelete)|

### <a name="CommandsInEntitlements">Commands in `az datacollaboration entitlement` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az datacollaboration entitlement list](#EntitlementsListByProposal)|ListByProposal|[Parameters](#ParametersEntitlementsListByProposal)|[Example](#ExamplesEntitlementsListByProposal)|
|[az datacollaboration entitlement show](#EntitlementsGet)|Get|[Parameters](#ParametersEntitlementsGet)|[Example](#ExamplesEntitlementsGet)|
|[az datacollaboration entitlement create](#EntitlementsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersEntitlementsCreateOrUpdate#Create)|[Example](#ExamplesEntitlementsCreateOrUpdate#Create)|
|[az datacollaboration entitlement update](#EntitlementsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersEntitlementsCreateOrUpdate#Update)|Not Found|
|[az datacollaboration entitlement delete](#EntitlementsDelete)|Delete|[Parameters](#ParametersEntitlementsDelete)|[Example](#ExamplesEntitlementsDelete)|

### <a name="CommandsInInvitations">Commands in `az datacollaboration invitation` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az datacollaboration invitation list](#InvitationsListByProposal)|ListByProposal|[Parameters](#ParametersInvitationsListByProposal)|[Example](#ExamplesInvitationsListByProposal)|
|[az datacollaboration invitation show](#InvitationsGet)|Get|[Parameters](#ParametersInvitationsGet)|[Example](#ExamplesInvitationsGet)|
|[az datacollaboration invitation create](#InvitationsCreate)|Create|[Parameters](#ParametersInvitationsCreate)|[Example](#ExamplesInvitationsCreate)|
|[az datacollaboration invitation delete](#InvitationsDelete)|Delete|[Parameters](#ParametersInvitationsDelete)|[Example](#ExamplesInvitationsDelete)|

### <a name="CommandsInParticipants">Commands in `az datacollaboration participant` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az datacollaboration participant list](#ParticipantsListByProposal)|ListByProposal|[Parameters](#ParametersParticipantsListByProposal)|[Example](#ExamplesParticipantsListByProposal)|
|[az datacollaboration participant show](#ParticipantsGet)|Get|[Parameters](#ParametersParticipantsGet)|[Example](#ExamplesParticipantsGet)|

### <a name="CommandsInPipelines">Commands in `az datacollaboration pipeline` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az datacollaboration pipeline list](#PipelinesListByWorkspace)|ListByWorkspace|[Parameters](#ParametersPipelinesListByWorkspace)|[Example](#ExamplesPipelinesListByWorkspace)|
|[az datacollaboration pipeline show](#PipelinesGet)|Get|[Parameters](#ParametersPipelinesGet)|[Example](#ExamplesPipelinesGet)|
|[az datacollaboration pipeline create](#PipelinesCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersPipelinesCreateOrUpdate#Create)|[Example](#ExamplesPipelinesCreateOrUpdate#Create)|
|[az datacollaboration pipeline update](#PipelinesCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersPipelinesCreateOrUpdate#Update)|Not Found|
|[az datacollaboration pipeline delete](#PipelinesDelete)|Delete|[Parameters](#ParametersPipelinesDelete)|[Example](#ExamplesPipelinesDelete)|
|[az datacollaboration pipeline run](#PipelinesRun)|Run|[Parameters](#ParametersPipelinesRun)|[Example](#ExamplesPipelinesRun)|

### <a name="CommandsInPipelineRuns">Commands in `az datacollaboration pipeline-run` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az datacollaboration pipeline-run list](#PipelineRunsListByWorkspace)|ListByWorkspace|[Parameters](#ParametersPipelineRunsListByWorkspace)|[Example](#ExamplesPipelineRunsListByWorkspace)|
|[az datacollaboration pipeline-run show](#PipelineRunsGet)|Get|[Parameters](#ParametersPipelineRunsGet)|[Example](#ExamplesPipelineRunsGet)|
|[az datacollaboration pipeline-run cancel](#PipelineRunsCancel)|Cancel|[Parameters](#ParametersPipelineRunsCancel)|[Example](#ExamplesPipelineRunsCancel)|

### <a name="CommandsInPipelineSteps">Commands in `az datacollaboration pipeline-step` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az datacollaboration pipeline-step list](#PipelineStepsListByPipeline)|ListByPipeline|[Parameters](#ParametersPipelineStepsListByPipeline)|[Example](#ExamplesPipelineStepsListByPipeline)|
|[az datacollaboration pipeline-step show](#PipelineStepsGet)|Get|[Parameters](#ParametersPipelineStepsGet)|[Example](#ExamplesPipelineStepsGet)|
|[az datacollaboration pipeline-step create](#PipelineStepsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersPipelineStepsCreateOrUpdate#Create)|[Example](#ExamplesPipelineStepsCreateOrUpdate#Create)|
|[az datacollaboration pipeline-step update](#PipelineStepsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersPipelineStepsCreateOrUpdate#Update)|Not Found|
|[az datacollaboration pipeline-step delete](#PipelineStepsDelete)|Delete|[Parameters](#ParametersPipelineStepsDelete)|[Example](#ExamplesPipelineStepsDelete)|

### <a name="CommandsInPipelineStepRuns">Commands in `az datacollaboration pipeline-step-run` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az datacollaboration pipeline-step-run list](#PipelineStepRunsListByPipelineRun)|ListByPipelineRun|[Parameters](#ParametersPipelineStepRunsListByPipelineRun)|[Example](#ExamplesPipelineStepRunsListByPipelineRun)|
|[az datacollaboration pipeline-step-run show](#PipelineStepRunsGet)|Get|[Parameters](#ParametersPipelineStepRunsGet)|[Example](#ExamplesPipelineStepRunsGet)|

### <a name="CommandsInPolicies">Commands in `az datacollaboration policy` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az datacollaboration policy list](#PoliciesListByEntitlement)|ListByEntitlement|[Parameters](#ParametersPoliciesListByEntitlement)|[Example](#ExamplesPoliciesListByEntitlement)|
|[az datacollaboration policy show](#PoliciesGet)|Get|[Parameters](#ParametersPoliciesGet)|[Example](#ExamplesPoliciesGet)|
|[az datacollaboration policy create](#PoliciesCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersPoliciesCreateOrUpdate#Create)|[Example](#ExamplesPoliciesCreateOrUpdate#Create)|
|[az datacollaboration policy update](#PoliciesCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersPoliciesCreateOrUpdate#Update)|Not Found|
|[az datacollaboration policy delete](#PoliciesDelete)|Delete|[Parameters](#ParametersPoliciesDelete)|[Example](#ExamplesPoliciesDelete)|

### <a name="CommandsInProposals">Commands in `az datacollaboration proposal` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az datacollaboration proposal list](#ProposalsListByWorkspace)|ListByWorkspace|[Parameters](#ParametersProposalsListByWorkspace)|[Example](#ExamplesProposalsListByWorkspace)|
|[az datacollaboration proposal show](#ProposalsGet)|Get|[Parameters](#ParametersProposalsGet)|[Example](#ExamplesProposalsGet)|
|[az datacollaboration proposal create](#ProposalsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersProposalsCreateOrUpdate#Create)|[Example](#ExamplesProposalsCreateOrUpdate#Create)|
|[az datacollaboration proposal update](#ProposalsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersProposalsCreateOrUpdate#Update)|Not Found|
|[az datacollaboration proposal delete](#ProposalsDelete)|Delete|[Parameters](#ParametersProposalsDelete)|[Example](#ExamplesProposalsDelete)|
|[az datacollaboration proposal revoke](#ProposalsRevoke)|Revoke|[Parameters](#ParametersProposalsRevoke)|[Example](#ExamplesProposalsRevoke)|
|[az datacollaboration proposal sign](#ProposalsSign)|Sign|[Parameters](#ParametersProposalsSign)|[Example](#ExamplesProposalsSign)|

### <a name="CommandsInResourceReferences">Commands in `az datacollaboration resource-reference` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az datacollaboration resource-reference list](#ResourceReferencesListByWorkspace)|ListByWorkspace|[Parameters](#ParametersResourceReferencesListByWorkspace)|[Example](#ExamplesResourceReferencesListByWorkspace)|

### <a name="CommandsInScripts">Commands in `az datacollaboration script` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az datacollaboration script list](#ScriptsListByWorkspace)|ListByWorkspace|[Parameters](#ParametersScriptsListByWorkspace)|[Example](#ExamplesScriptsListByWorkspace)|
|[az datacollaboration script show](#ScriptsGet)|Get|[Parameters](#ParametersScriptsGet)|[Example](#ExamplesScriptsGet)|
|[az datacollaboration script create](#ScriptsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersScriptsCreateOrUpdate#Create)|[Example](#ExamplesScriptsCreateOrUpdate#Create)|
|[az datacollaboration script update](#ScriptsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersScriptsCreateOrUpdate#Update)|Not Found|
|[az datacollaboration script delete](#ScriptsDelete)|Delete|[Parameters](#ParametersScriptsDelete)|[Example](#ExamplesScriptsDelete)|

### <a name="CommandsInScriptReferences">Commands in `az datacollaboration script-reference` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az datacollaboration script-reference list](#ScriptReferencesListByProposal)|ListByProposal|[Parameters](#ParametersScriptReferencesListByProposal)|[Example](#ExamplesScriptReferencesListByProposal)|
|[az datacollaboration script-reference show](#ScriptReferencesGet)|Get|[Parameters](#ParametersScriptReferencesGet)|[Example](#ExamplesScriptReferencesGet)|
|[az datacollaboration script-reference create](#ScriptReferencesCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersScriptReferencesCreateOrUpdate#Create)|[Example](#ExamplesScriptReferencesCreateOrUpdate#Create)|
|[az datacollaboration script-reference update](#ScriptReferencesCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersScriptReferencesCreateOrUpdate#Update)|Not Found|
|[az datacollaboration script-reference delete](#ScriptReferencesDelete)|Delete|[Parameters](#ParametersScriptReferencesDelete)|[Example](#ExamplesScriptReferencesDelete)|
|[az datacollaboration script-reference resolve](#ScriptReferencesResolve)|Resolve|[Parameters](#ParametersScriptReferencesResolve)|[Example](#ExamplesScriptReferencesResolve)|

### <a name="CommandsInScriptRevisions">Commands in `az datacollaboration script-revision` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az datacollaboration script-revision list](#ScriptRevisionsListByScript)|ListByScript|[Parameters](#ParametersScriptRevisionsListByScript)|[Example](#ExamplesScriptRevisionsListByScript)|
|[az datacollaboration script-revision show](#ScriptRevisionsGet)|Get|[Parameters](#ParametersScriptRevisionsGet)|[Example](#ExamplesScriptRevisionsGet)|

### <a name="CommandsInWorkspaces">Commands in `az datacollaboration workspace` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az datacollaboration workspace list](#WorkspacesListByResourceGroup)|ListByResourceGroup|[Parameters](#ParametersWorkspacesListByResourceGroup)|[Example](#ExamplesWorkspacesListByResourceGroup)|
|[az datacollaboration workspace list](#WorkspacesListBySubscription)|ListBySubscription|[Parameters](#ParametersWorkspacesListBySubscription)|[Example](#ExamplesWorkspacesListBySubscription)|
|[az datacollaboration workspace show](#WorkspacesGet)|Get|[Parameters](#ParametersWorkspacesGet)|[Example](#ExamplesWorkspacesGet)|
|[az datacollaboration workspace create](#WorkspacesCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersWorkspacesCreateOrUpdate#Create)|[Example](#ExamplesWorkspacesCreateOrUpdate#Create)|
|[az datacollaboration workspace update](#WorkspacesUpdate)|Update|[Parameters](#ParametersWorkspacesUpdate)|[Example](#ExamplesWorkspacesUpdate)|
|[az datacollaboration workspace delete](#WorkspacesDelete)|Delete|[Parameters](#ParametersWorkspacesDelete)|[Example](#ExamplesWorkspacesDelete)|


## COMMAND DETAILS

### group `az datacollaboration constrained-resource`
#### <a name="ConstrainedResourcesListByWorkspace">Command `az datacollaboration constrained-resource list`</a>

##### <a name="ExamplesConstrainedResourcesListByWorkspace">Example</a>
```
az datacollaboration constrained-resource list --resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersConstrainedResourcesListByWorkspace">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|
|**--filter**|string|Filters the results using OData syntax.|filter|$filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|$orderby|

#### <a name="ConstrainedResourcesGet">Command `az datacollaboration constrained-resource show`</a>

##### <a name="ExamplesConstrainedResourcesGet">Example</a>
```
az datacollaboration constrained-resource show --name "SynapseSparkPool1" --resource-group "SampleResourceGroup" \
--workspace-name "Workspace1"
```
##### <a name="ParametersConstrainedResourcesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--constrained-resource-name**|string|The name of the constrained resource.|constrained_resource_name|constrainedResourceName|

#### <a name="ConstrainedResourcesCreateOrUpdate#Create">Command `az datacollaboration constrained-resource create`</a>

##### <a name="ExamplesConstrainedResourcesCreateOrUpdate#Create">Example</a>
```
az datacollaboration constrained-resource create --constrained-resource "{\\"kind\\":\\"SynapseSparkPool\\",\\"properti\
es\\":{\\"autoPause\\":{\\"delayInMinutes\\":15,\\"enabled\\":true},\\"autoScale\\":{\\"enabled\\":true,\\"maxNodeCount\
\\":50,\\"minNodeCount\\":3},\\"nodeCount\\":4,\\"nodeSize\\":\\"Medium\\",\\"nodeSizeFamily\\":\\"MemoryOptimized\\",\
\\"sparkVersion\\":\\"2.4\\"}}" --name "SynapseSparkPool1" --resource-group "SampleResourceGroup" --workspace-name \
"Workspace1"
```
##### <a name="ExamplesConstrainedResourcesCreateOrUpdate#Create">Example</a>
```
az datacollaboration constrained-resource create --constrained-resource "{\\"kind\\":\\"SynapseSparkPool\\",\\"properti\
es\\":{\\"autoPause\\":{\\"delayInMinutes\\":15,\\"enabled\\":true},\\"autoScale\\":{\\"enabled\\":true,\\"maxNodeCount\
\\":50,\\"minNodeCount\\":3},\\"nodeCount\\":4,\\"nodeSize\\":\\"Medium\\",\\"nodeSizeFamily\\":\\"MemoryOptimized\\",\
\\"sparkVersion\\":\\"2.4\\"}}" --name "SynapseSparkPool1" --resource-group "SampleResourceGroup" --workspace-name \
"Workspace1"
```
##### <a name="ParametersConstrainedResourcesCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--constrained-resource-name**|string|The name of the constrained resource.|constrained_resource_name|constrainedResourceName|
|**--constrained-resource**|object|The new constrained resource information.|constrained_resource|constrainedResource|

#### <a name="ConstrainedResourcesCreateOrUpdate#Update">Command `az datacollaboration constrained-resource update`</a>

##### <a name="ParametersConstrainedResourcesCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--constrained-resource-name**|string|The name of the constrained resource.|constrained_resource_name|constrainedResourceName|
|**--constrained-resource**|object|The new constrained resource information.|constrained_resource|constrainedResource|

#### <a name="ConstrainedResourcesDelete">Command `az datacollaboration constrained-resource delete`</a>

##### <a name="ExamplesConstrainedResourcesDelete">Example</a>
```
az datacollaboration constrained-resource delete --name "SynapseSparkPool1" --resource-group "SampleResourceGroup" \
--workspace-name "Workspace1"
```
##### <a name="ParametersConstrainedResourcesDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--constrained-resource-name**|string|The name of the constrained resource.|constrained_resource_name|constrainedResourceName|

### group `az datacollaboration constraint`
#### <a name="ConstraintsListByEntitlement">Command `az datacollaboration constraint list`</a>

##### <a name="ExamplesConstraintsListByEntitlement">Example</a>
```
az datacollaboration constraint list --entitlement-name "Entitlement1" --proposal-name "Proposal1" --resource-group \
"SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersConstraintsListByEntitlement">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|
|**--filter**|string|Filters the results using OData syntax.|filter|$filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|$orderby|

#### <a name="ConstraintsGet">Command `az datacollaboration constraint show`</a>

##### <a name="ExamplesConstraintsGet">Example</a>
```
az datacollaboration constraint show --name "Constraint1" --entitlement-name "Entitlement1" --proposal-name \
"Proposal1" --resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersConstraintsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|
|**--constraint-name**|string|The name of the constraint.|constraint_name|constraintName|

#### <a name="ConstraintsCreateOrUpdate#Create">Command `az datacollaboration constraint create`</a>

##### <a name="ExamplesConstraintsCreateOrUpdate#Create">Example</a>
```
az datacollaboration constraint create --script-constraint description="Constraint description" \
script-reference-id="6fa17733-0c87-4671-bc4c-a6d9f1228948" --name "Constraint1" --entitlement-name "Entitlement1" \
--proposal-name "Proposal1" --resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersConstraintsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|
|**--constraint-name**|string|The name of the constraint.|constraint_name|constraintName|
|**--location-constraint**|object|Constraint used to only allow access if the resource is used within the specified Azure location.|location_constraint|LocationConstraint|
|**--script-constraint**|object|Constraint used to only allow access if the resource is used with a specific script.|script_constraint|ScriptConstraint|

#### <a name="ConstraintsCreateOrUpdate#Update">Command `az datacollaboration constraint update`</a>

##### <a name="ParametersConstraintsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|
|**--constraint-name**|string|The name of the constraint.|constraint_name|constraintName|
|**--location-constraint**|object|Constraint used to only allow access if the resource is used within the specified Azure location.|location_constraint|LocationConstraint|
|**--script-constraint**|object|Constraint used to only allow access if the resource is used with a specific script.|script_constraint|ScriptConstraint|

#### <a name="ConstraintsDelete">Command `az datacollaboration constraint delete`</a>

##### <a name="ExamplesConstraintsDelete">Example</a>
```
az datacollaboration constraint delete --name "Constraint1" --entitlement-name "Entitlement1" --proposal-name \
"Proposal1" --resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersConstraintsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|
|**--constraint-name**|string|The name of the constraint.|constraint_name|constraintName|

### group `az datacollaboration consumer-invitation`
#### <a name="ConsumerInvitationsGet">Command `az datacollaboration consumer-invitation show`</a>

##### <a name="ExamplesConsumerInvitationsGet">Example</a>
```
az datacollaboration consumer-invitation show --invitation-id "dfbbc788-19eb-4607-a5a1-c74181bfff03" --location "East \
US 2"
```
##### <a name="ParametersConsumerInvitationsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|Location of the invitation|location|location|
|**--invitation-id**|string|An invitation id|invitation_id|invitationId|

#### <a name="ConsumerInvitationsListInvitations">Command `az datacollaboration consumer-invitation list-invitation`</a>

##### <a name="ExamplesConsumerInvitationsListInvitations">Example</a>
```
az datacollaboration consumer-invitation list-invitation
```
##### <a name="ParametersConsumerInvitationsListInvitations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--skip-token**|string|The continuation token|skip_token|$skipToken|

#### <a name="ConsumerInvitationsRejectInvitation">Command `az datacollaboration consumer-invitation reject-invitation`</a>

##### <a name="ExamplesConsumerInvitationsRejectInvitation">Example</a>
```
az datacollaboration consumer-invitation reject-invitation --invitation-id "dfbbc788-19eb-4607-a5a1-c74181bfff03" \
--location "East US 2"
```
##### <a name="ParametersConsumerInvitationsRejectInvitation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|Location of the invitation|location|location|
|**--invitation-id**|string|An invitation id|invitation_id|invitationId|

### group `az datacollaboration data-asset`
#### <a name="DataAssetsListByWorkspace">Command `az datacollaboration data-asset list`</a>

##### <a name="ExamplesDataAssetsListByWorkspace">Example</a>
```
az datacollaboration data-asset list --resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersDataAssetsListByWorkspace">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--skip-token**|string|Continuation Token|skip_token|$skipToken|
|**--filter**|string|Filters the results using OData syntax.|filter|$filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|$orderby|

#### <a name="DataAssetsGet">Command `az datacollaboration data-asset show`</a>

##### <a name="ExamplesDataAssetsGet">Example</a>
```
az datacollaboration data-asset show --name "DataAsset1" --resource-group "SampleResourceGroup" --workspace-name \
"Workspace1"
```
##### <a name="ParametersDataAssetsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--data-asset-name**|string|The name of the dataAssetName|data_asset_name|dataAssetName|

#### <a name="DataAssetsCreateOrUpdate#Create">Command `az datacollaboration data-asset create`</a>

##### <a name="ExamplesDataAssetsCreateOrUpdate#Create">Example</a>
```
az datacollaboration data-asset create --description "Data of DataSet1" --data-processing-strategy "CopyBased" --name \
"DataAsset1" --resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersDataAssetsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--data-asset-name**|string|The name of the DataAsset|data_asset_name|dataAssetName|
|**--data-processing-strategy**|choice|Data processing strategy to use for the the child DataSets|data_processing_strategy|dataProcessingStrategy|
|**--description**|string|General Description of the DataSet content|description|description|

#### <a name="DataAssetsCreateOrUpdate#Update">Command `az datacollaboration data-asset update`</a>

##### <a name="ParametersDataAssetsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--data-asset-name**|string|The name of the DataAsset|data_asset_name|dataAssetName|
|**--data-processing-strategy**|choice|Data processing strategy to use for the the child DataSets|data_processing_strategy|dataProcessingStrategy|
|**--description**|string|General Description of the DataSet content|description|description|

#### <a name="DataAssetsDelete">Command `az datacollaboration data-asset delete`</a>

##### <a name="ExamplesDataAssetsDelete">Example</a>
```
az datacollaboration data-asset delete --name "DataAsset1" --resource-group "SampleResourceGroup" --workspace-name \
"Workspace1"
```
##### <a name="ParametersDataAssetsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--data-asset-name**|string|The name of the DataAsset|data_asset_name|dataAssetName|

### group `az datacollaboration data-asset-reference`
#### <a name="DataAssetReferencesListByProposal">Command `az datacollaboration data-asset-reference list`</a>

##### <a name="ExamplesDataAssetReferencesListByProposal">Example</a>
```
az datacollaboration data-asset-reference list --proposal-name "Proposal1" --resource-group "SampleResourceGroup" \
--workspace-name "Workspace1"
```
##### <a name="ParametersDataAssetReferencesListByProposal">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|

#### <a name="DataAssetReferencesGet">Command `az datacollaboration data-asset-reference show`</a>

##### <a name="ExamplesDataAssetReferencesGet">Example</a>
```
az datacollaboration data-asset-reference show --proposal-name "Proposal1" --reference-name "DataAssetReference1" \
--resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersDataAssetReferencesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--reference-name**|string|The name of the reference.|reference_name|referenceName|

#### <a name="DataAssetReferencesCreateOrUpdate#Create">Command `az datacollaboration data-asset-reference create`</a>

##### <a name="ExamplesDataAssetReferencesCreateOrUpdate#Create">Example</a>
```
az datacollaboration data-asset-reference create --description "Reference to DataAsset1" --data-asset-id \
"d164252e-2909-4718-a91e-315195c54b09" --proposal-name "Proposal1" --reference-name "DataAssetReference1" \
--resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersDataAssetReferencesCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--reference-name**|string|The name of the reference.|reference_name|referenceName|
|**--data-asset-id**|string|The unique identifier of the referenced data asset|data_asset_id|dataAssetId|
|**--description**|string|General Description of the data asset reference|description|description|

#### <a name="DataAssetReferencesCreateOrUpdate#Update">Command `az datacollaboration data-asset-reference update`</a>

##### <a name="ParametersDataAssetReferencesCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--reference-name**|string|The name of the reference.|reference_name|referenceName|
|**--data-asset-id**|string|The unique identifier of the referenced data asset|data_asset_id|dataAssetId|
|**--description**|string|General Description of the data asset reference|description|description|

#### <a name="DataAssetReferencesDelete">Command `az datacollaboration data-asset-reference delete`</a>

##### <a name="ExamplesDataAssetReferencesDelete">Example</a>
```
az datacollaboration data-asset-reference delete --proposal-name "Proposal1" --reference-name "DataAssetReference1" \
--resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersDataAssetReferencesDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--reference-name**|string|The name of the reference.|reference_name|referenceName|

#### <a name="DataAssetReferencesResolve">Command `az datacollaboration data-asset-reference resolve`</a>

##### <a name="ExamplesDataAssetReferencesResolve">Example</a>
```
az datacollaboration data-asset-reference resolve --proposal-name "Proposal1" --reference-name "DataAssetReference1" \
--resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersDataAssetReferencesResolve">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--reference-name**|string|The name of the reference.|reference_name|referenceName|

### group `az datacollaboration data-set`
#### <a name="DataSetsListByDataAsset">Command `az datacollaboration data-set list`</a>

##### <a name="ExamplesDataSetsListByDataAsset">Example</a>
```
az datacollaboration data-set list --data-asset-name "DataAsset1" --resource-group "SampleResourceGroup" \
--workspace-name "Workspace1"
```
##### <a name="ParametersDataSetsListByDataAsset">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--data-asset-name**|string|The name of the DataAsset|data_asset_name|dataAssetName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|

#### <a name="DataSetsGet">Command `az datacollaboration data-set show`</a>

##### <a name="ExamplesDataSetsGet">Example</a>
```
az datacollaboration data-set show --data-asset-name "DataAsset1" --data-set-category "Production" --resource-group \
"SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersDataSetsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--data-asset-name**|string|The name of the DataAsset|data_asset_name|dataAssetName|
|**--data-set-category**|choice|The usage category name of the DataSet|data_set_category|dataSetCategory|

#### <a name="DataSetsCreateOrUpdate#Create">Command `az datacollaboration data-set create`</a>

##### <a name="ExamplesDataSetsCreateOrUpdate#Create">Example</a>
```
az datacollaboration data-set create --data-asset-name "DataAsset1" --blob-data-set container-name="C1" \
file-path="file21" storage-account-id="subscriptions/12345678-1234-1234-1234-567890abcdef/resourceGroups/SampleResource\
Group/providers/Microsoft.Storage/storageAccounts/storage2" --data-set-category "Production" --resource-group \
"SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersDataSetsCreateOrUpdate#Create">Parameters</a> 
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

#### <a name="DataSetsCreateOrUpdate#Update">Command `az datacollaboration data-set update`</a>

##### <a name="ParametersDataSetsCreateOrUpdate#Update">Parameters</a> 
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

#### <a name="DataSetsDelete">Command `az datacollaboration data-set delete`</a>

##### <a name="ExamplesDataSetsDelete">Example</a>
```
az datacollaboration data-set delete --data-asset-name "DataAsset1" --data-set-category "Production" --resource-group \
"SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersDataSetsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--data-asset-name**|string|The name of the DataAsset|data_asset_name|dataAssetName|
|**--data-set-category**|choice|The usage category name of the DataSet|data_set_category|dataSetCategory|

### group `az datacollaboration entitlement`
#### <a name="EntitlementsListByProposal">Command `az datacollaboration entitlement list`</a>

##### <a name="ExamplesEntitlementsListByProposal">Example</a>
```
az datacollaboration entitlement list --proposal-name "Proposal1" --resource-group "SampleResourceGroup" \
--workspace-name "Workspace1"
```
##### <a name="ParametersEntitlementsListByProposal">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|
|**--filter**|string|Filters the results using OData syntax.|filter|$filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|$orderby|

#### <a name="EntitlementsGet">Command `az datacollaboration entitlement show`</a>

##### <a name="ExamplesEntitlementsGet">Example</a>
```
az datacollaboration entitlement show --name "Entitlement1" --proposal-name "Proposal1" --resource-group \
"SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersEntitlementsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|

#### <a name="EntitlementsCreateOrUpdate#Create">Command `az datacollaboration entitlement create`</a>

##### <a name="ExamplesEntitlementsCreateOrUpdate#Create">Example</a>
```
az datacollaboration entitlement create --description "Entitlement description" --resource-id \
"6fa17733-0c87-4671-bc4c-a6d9f1228948" --resource-type "DataAssetReference" --subject-id \
"a415f518-e721-4852-84de-8b139f92b933" --name "Entitlement1" --proposal-name "Proposal1" --resource-group \
"SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersEntitlementsCreateOrUpdate#Create">Parameters</a> 
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

#### <a name="EntitlementsCreateOrUpdate#Update">Command `az datacollaboration entitlement update`</a>

##### <a name="ParametersEntitlementsCreateOrUpdate#Update">Parameters</a> 
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

#### <a name="EntitlementsDelete">Command `az datacollaboration entitlement delete`</a>

##### <a name="ExamplesEntitlementsDelete">Example</a>
```
az datacollaboration entitlement delete --name "Entitlement1" --proposal-name "Proposal1" --resource-group \
"SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersEntitlementsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|

### group `az datacollaboration invitation`
#### <a name="InvitationsListByProposal">Command `az datacollaboration invitation list`</a>

##### <a name="ExamplesInvitationsListByProposal">Example</a>
```
az datacollaboration invitation list --proposal-name "Proposal1" --resource-group "SampleResourceGroup" \
--workspace-name "Workspace1"
```
##### <a name="ParametersInvitationsListByProposal">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--skip-token**|string|The continuation token|skip_token|$skipToken|

#### <a name="InvitationsGet">Command `az datacollaboration invitation show`</a>

##### <a name="ExamplesInvitationsGet">Example</a>
```
az datacollaboration invitation show --name "Invitation1" --proposal-name "Proposal1" --resource-group \
"SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersInvitationsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--invitation-name**|string|The name of the invitation.|invitation_name|invitationName|

#### <a name="InvitationsCreate">Command `az datacollaboration invitation create`</a>

##### <a name="ExamplesInvitationsCreate">Example</a>
```
az datacollaboration invitation create --target-email "receiver@microsoft.com" --name "Invitation1" --proposal-name \
"Proposal1" --resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersInvitationsCreate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal to send the invitation for.|proposal_name|proposalName|
|**--invitation-name**|string|The name of the invitation.|invitation_name|invitationName|
|**--target-active-directory-id**|string|The target Azure AD Id. Can't be combined with email.|target_active_directory_id|targetActiveDirectoryId|
|**--target-email**|string|The email the invitation is directed to.|target_email|targetEmail|
|**--target-object-id**|string|The target user or application Id that invitation is being sent to. Must be specified along TargetActiveDirectoryId. This enables sending invitations to specific users or applications in an AD tenant.|target_object_id|targetObjectId|

#### <a name="InvitationsDelete">Command `az datacollaboration invitation delete`</a>

##### <a name="ExamplesInvitationsDelete">Example</a>
```
az datacollaboration invitation delete --name "Invitation1" --proposal-name "Proposal1" --resource-group \
"SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersInvitationsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--invitation-name**|string|The name of the invitation.|invitation_name|invitationName|

### group `az datacollaboration participant`
#### <a name="ParticipantsListByProposal">Command `az datacollaboration participant list`</a>

##### <a name="ExamplesParticipantsListByProposal">Example</a>
```
az datacollaboration participant list --proposal-name "Proposal1" --resource-group "SampleResourceGroup" \
--workspace-name "Workspace1"
```
##### <a name="ParametersParticipantsListByProposal">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|

#### <a name="ParticipantsGet">Command `az datacollaboration participant show`</a>

##### <a name="ExamplesParticipantsGet">Example</a>
```
az datacollaboration participant show --name "Participant1" --proposal-name "Proposal1" --resource-group \
"SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersParticipantsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--participant-name**|string|The name of the participant.|participant_name|participantName|

### group `az datacollaboration pipeline`
#### <a name="PipelinesListByWorkspace">Command `az datacollaboration pipeline list`</a>

##### <a name="ExamplesPipelinesListByWorkspace">Example</a>
```
az datacollaboration pipeline list --resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersPipelinesListByWorkspace">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|
|**--filter**|string|Filters the results using OData syntax.|filter|$filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|$orderby|

#### <a name="PipelinesGet">Command `az datacollaboration pipeline show`</a>

##### <a name="ExamplesPipelinesGet">Example</a>
```
az datacollaboration pipeline show --name "Pipeline1" --resource-group "SampleResourceGroup" --workspace-name \
"Workspace1"
```
##### <a name="ParametersPipelinesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|pipelineName|

#### <a name="PipelinesCreateOrUpdate#Create">Command `az datacollaboration pipeline create`</a>

##### <a name="ExamplesPipelinesCreateOrUpdate#Create">Example</a>
```
az datacollaboration pipeline create --description "A pipeline" --name "Pipeline1" --resource-group \
"SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersPipelinesCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|pipelineName|
|**--description**|string|General Description of the pipeline content|description|description|

#### <a name="PipelinesCreateOrUpdate#Update">Command `az datacollaboration pipeline update`</a>

##### <a name="ParametersPipelinesCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|pipelineName|
|**--description**|string|General Description of the pipeline content|description|description|

#### <a name="PipelinesDelete">Command `az datacollaboration pipeline delete`</a>

##### <a name="ExamplesPipelinesDelete">Example</a>
```
az datacollaboration pipeline delete --name "Pipeline1" --resource-group "SampleResourceGroup" --workspace-name \
"Workspace1"
```
##### <a name="ParametersPipelinesDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|pipelineName|

#### <a name="PipelinesRun">Command `az datacollaboration pipeline run`</a>

##### <a name="ExamplesPipelinesRun">Example</a>
```
az datacollaboration pipeline run --name "Pipeline1" --pipeline-run-mode "Test" --resource-group "SampleResourceGroup" \
--workspace-name "Workspace1"
```
##### <a name="ParametersPipelinesRun">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|pipelineName|
|**--pipeline-run-mode**|choice|Mode of pipeline run used.|pipeline_run_mode|pipelineRunMode|

### group `az datacollaboration pipeline-run`
#### <a name="PipelineRunsListByWorkspace">Command `az datacollaboration pipeline-run list`</a>

##### <a name="ExamplesPipelineRunsListByWorkspace">Example</a>
```
az datacollaboration pipeline-run list --resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersPipelineRunsListByWorkspace">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--skip-token**|string|Continuation token|skip_token|$skipToken|
|**--filter**|string|Filters the results using OData syntax.|filter|$filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|$orderby|

#### <a name="PipelineRunsGet">Command `az datacollaboration pipeline-run show`</a>

##### <a name="ExamplesPipelineRunsGet">Example</a>
```
az datacollaboration pipeline-run show --name "a4cdba19-a513-46ca-9d48-47806e396d13" --resource-group \
"SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersPipelineRunsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-run-name**|string|The name of the pipeline run.|pipeline_run_name|pipelineRunName|

#### <a name="PipelineRunsCancel">Command `az datacollaboration pipeline-run cancel`</a>

##### <a name="ExamplesPipelineRunsCancel">Example</a>
```
az datacollaboration pipeline-run cancel --name "a4cdba19-a513-46ca-9d48-47806e396d13" --resource-group \
"SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersPipelineRunsCancel">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-run-name**|string|The name of the pipeline run.|pipeline_run_name|pipelineRunName|

### group `az datacollaboration pipeline-step`
#### <a name="PipelineStepsListByPipeline">Command `az datacollaboration pipeline-step list`</a>

##### <a name="ExamplesPipelineStepsListByPipeline">Example</a>
```
az datacollaboration pipeline-step list --pipeline-name "Pipeline1" --resource-group "SampleResourceGroup" \
--workspace-name "Workspace1"
```
##### <a name="ParametersPipelineStepsListByPipeline">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|pipelineName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|

#### <a name="PipelineStepsGet">Command `az datacollaboration pipeline-step show`</a>

##### <a name="ExamplesPipelineStepsGet">Example</a>
```
az datacollaboration pipeline-step show --pipeline-name "Pipeline1" --name "PipelineStep1" --resource-group \
"SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersPipelineStepsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|pipelineName|
|**--pipeline-step-name**|string|The name of the pipeline step.|pipeline_step_name|pipelineStepName|

#### <a name="PipelineStepsCreateOrUpdate#Create">Command `az datacollaboration pipeline-step create`</a>

##### <a name="ExamplesPipelineStepsCreateOrUpdate#Create">Example</a>
```
az datacollaboration pipeline-step create --pipeline-name "Pipeline1" --synapse-spark-pipeline-step \
dependencies="PipelineStep0" executor-node-size="Medium" executors-count=4 script-id="284878c1-deb7-440a-9f87-28b6e5824\
2a3" script-revision=1 script-sink-bindings={"dataAssetId":"2f5a9076-3372-4282-b52d-a382382930ee","key":"sink1"} \
script-sink-bindings={"dataAssetId":"30ba4508-b74f-46b0-bc30-1d891cd19ba1","key":"sink2"} \
script-source-bindings={"dataAssetId":"093a76ba-a0f2-4a03-80b1-bec1d3368711","key":"source1"} \
script-source-bindings={"dataAssetId":"2aa367d4-839c-468c-95b9-f3e63c628111","key":"source2"} \
synapse-spark-pool-id="08206bdd-a08d-4005-9bdf-1a2ca08a399b" --name "PipelineStep1" --resource-group \
"SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ExamplesPipelineStepsCreateOrUpdate#Create">Example</a>
```
az datacollaboration pipeline-step create --pipeline-name "Pipeline1" --synapse-spark-pipeline-step \
dependencies="PipelineStep0" executor-node-size="Medium" executors-count=4 script-id="284878c1-deb7-440a-9f87-28b6e5824\
2a3" script-revision=1 script-sink-bindings={"dataAssetId":"2f5a9076-3372-4282-b52d-a382382930ee","key":"sink1"} \
script-sink-bindings={"dataAssetId":"30ba4508-b74f-46b0-bc30-1d891cd19ba1","key":"sink2"} \
script-source-bindings={"dataAssetId":"093a76ba-a0f2-4a03-80b1-bec1d3368711","key":"source1"} \
script-source-bindings={"dataAssetId":"2aa367d4-839c-468c-95b9-f3e63c628111","key":"source2"} \
synapse-spark-pool-id="08206bdd-a08d-4005-9bdf-1a2ca08a399b" --name "PipelineStep1" --resource-group \
"SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersPipelineStepsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|pipelineName|
|**--pipeline-step-name**|string|The name of the pipeline step.|pipeline_step_name|pipelineStepName|
|**--synapse-spark-pipeline-step**|object|A Synapse Spark based pipeline step.|synapse_spark_pipeline_step|SynapseSparkPipelineStep|

#### <a name="PipelineStepsCreateOrUpdate#Update">Command `az datacollaboration pipeline-step update`</a>

##### <a name="ParametersPipelineStepsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|pipelineName|
|**--pipeline-step-name**|string|The name of the pipeline step.|pipeline_step_name|pipelineStepName|
|**--synapse-spark-pipeline-step**|object|A Synapse Spark based pipeline step.|synapse_spark_pipeline_step|SynapseSparkPipelineStep|

#### <a name="PipelineStepsDelete">Command `az datacollaboration pipeline-step delete`</a>

##### <a name="ExamplesPipelineStepsDelete">Example</a>
```
az datacollaboration pipeline-step delete --pipeline-name "Pipeline1" --name "PipelineStep1" --resource-group \
"SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersPipelineStepsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-name**|string|The name of the pipeline.|pipeline_name|pipelineName|
|**--pipeline-step-name**|string|The name of the pipeline step.|pipeline_step_name|pipelineStepName|

### group `az datacollaboration pipeline-step-run`
#### <a name="PipelineStepRunsListByPipelineRun">Command `az datacollaboration pipeline-step-run list`</a>

##### <a name="ExamplesPipelineStepRunsListByPipelineRun">Example</a>
```
az datacollaboration pipeline-step-run list --pipeline-run-name "a4cdba19-a513-46ca-9d48-47806e396d13" \
--resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersPipelineStepRunsListByPipelineRun">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-run-name**|string|The name of the pipeline run.|pipeline_run_name|pipelineRunName|
|**--skip-token**|string|Continuation token|skip_token|$skipToken|

#### <a name="PipelineStepRunsGet">Command `az datacollaboration pipeline-step-run show`</a>

##### <a name="ExamplesPipelineStepRunsGet">Example</a>
```
az datacollaboration pipeline-step-run show --pipeline-run-name "a4cdba19-a513-46ca-9d48-47806e396d13" --name \
"5ec0dd18-ea32-4d27-b3a5-2920c5f26325" --resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersPipelineStepRunsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--pipeline-run-name**|string|The name of the pipeline run.|pipeline_run_name|pipelineRunName|
|**--pipeline-step-run-name**|string|The name of the pipeline step run.|pipeline_step_run_name|pipelineStepRunName|

### group `az datacollaboration policy`
#### <a name="PoliciesListByEntitlement">Command `az datacollaboration policy list`</a>

##### <a name="ExamplesPoliciesListByEntitlement">Example</a>
```
az datacollaboration policy list --entitlement-name "Entitlement1" --proposal-name "Proposal1" --resource-group \
"SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersPoliciesListByEntitlement">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|
|**--filter**|string|Filters the results using OData syntax.|filter|$filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|$orderby|

#### <a name="PoliciesGet">Command `az datacollaboration policy show`</a>

##### <a name="ExamplesPoliciesGet">Example</a>
```
az datacollaboration policy show --entitlement-name "Entitlement1" --name "Policy1" --proposal-name "Proposal1" \
--resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersPoliciesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|
|**--policy-name**|string|The name of the policy.|policy_name|policyName|

#### <a name="PoliciesCreateOrUpdate#Create">Command `az datacollaboration policy create`</a>

##### <a name="ExamplesPoliciesCreateOrUpdate#Create">Example</a>
```
az datacollaboration policy create --entitlement-name "Entitlement1" --diagnostic-policy description="Policy \
description" log-level="Information" --name "Policy1" --proposal-name "Proposal1" --resource-group \
"SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersPoliciesCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|
|**--policy-name**|string|The name of the policy.|policy_name|policyName|
|**--diagnostic-policy**|object|A diagnostic policy.|diagnostic_policy|DiagnosticPolicy|

#### <a name="PoliciesCreateOrUpdate#Update">Command `az datacollaboration policy update`</a>

##### <a name="ParametersPoliciesCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|
|**--policy-name**|string|The name of the policy.|policy_name|policyName|
|**--diagnostic-policy**|object|A diagnostic policy.|diagnostic_policy|DiagnosticPolicy|

#### <a name="PoliciesDelete">Command `az datacollaboration policy delete`</a>

##### <a name="ExamplesPoliciesDelete">Example</a>
```
az datacollaboration policy delete --entitlement-name "Entitlement1" --name "Policy1" --proposal-name "Proposal1" \
--resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersPoliciesDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--entitlement-name**|string|The name of the entitlement.|entitlement_name|entitlementName|
|**--policy-name**|string|The name of the policy.|policy_name|policyName|

### group `az datacollaboration proposal`
#### <a name="ProposalsListByWorkspace">Command `az datacollaboration proposal list`</a>

##### <a name="ExamplesProposalsListByWorkspace">Example</a>
```
az datacollaboration proposal list --resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersProposalsListByWorkspace">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|
|**--filter**|string|Filters the results using OData syntax.|filter|$filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|$orderby|

#### <a name="ProposalsGet">Command `az datacollaboration proposal show`</a>

##### <a name="ExamplesProposalsGet">Example</a>
```
az datacollaboration proposal show --name "Proposal1" --resource-group "SampleResourceGroup" --workspace-name \
"Workspace1"
```
##### <a name="ParametersProposalsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|

#### <a name="ProposalsCreateOrUpdate#Create">Command `az datacollaboration proposal create`</a>

##### <a name="ExamplesProposalsCreateOrUpdate#Create">Example</a>
```
az datacollaboration proposal create --description "Proposal description" --terms "Proposal terms" --name "Proposal1" \
--resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersProposalsCreateOrUpdate#Create">Parameters</a> 
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

#### <a name="ProposalsCreateOrUpdate#Update">Command `az datacollaboration proposal update`</a>

##### <a name="ParametersProposalsCreateOrUpdate#Update">Parameters</a> 
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

#### <a name="ProposalsDelete">Command `az datacollaboration proposal delete`</a>

##### <a name="ExamplesProposalsDelete">Example</a>
```
az datacollaboration proposal delete --name "Proposal1" --resource-group "SampleResourceGroup" --workspace-name \
"Workspace1"
```
##### <a name="ParametersProposalsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|

#### <a name="ProposalsRevoke">Command `az datacollaboration proposal revoke`</a>

##### <a name="ExamplesProposalsRevoke">Example</a>
```
az datacollaboration proposal revoke --name "Proposal1" --resource-group "SampleResourceGroup" --workspace-name \
"Workspace1"
```
##### <a name="ParametersProposalsRevoke">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|

#### <a name="ProposalsSign">Command `az datacollaboration proposal sign`</a>

##### <a name="ExamplesProposalsSign">Example</a>
```
az datacollaboration proposal sign --name "Proposal1" --proposal-version "ae660cb9-0c0c-4ff5-a68f-dc5584a63c79" \
--resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersProposalsSign">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--proposal-version**|string|Proposal version to be signed|proposal_version|proposalVersion|

### group `az datacollaboration resource-reference`
#### <a name="ResourceReferencesListByWorkspace">Command `az datacollaboration resource-reference list`</a>

##### <a name="ExamplesResourceReferencesListByWorkspace">Example</a>
```
az datacollaboration resource-reference list --resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersResourceReferencesListByWorkspace">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|
|**--filter**|string|Filters the results using OData syntax.|filter|$filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|$orderby|

### group `az datacollaboration script`
#### <a name="ScriptsListByWorkspace">Command `az datacollaboration script list`</a>

##### <a name="ExamplesScriptsListByWorkspace">Example</a>
```
az datacollaboration script list --resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersScriptsListByWorkspace">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|
|**--filter**|string|Filters the results using OData syntax.|filter|$filter|
|**--orderby**|string|Sorts the results using OData syntax.|orderby|$orderby|

#### <a name="ScriptsGet">Command `az datacollaboration script show`</a>

##### <a name="ExamplesScriptsGet">Example</a>
```
az datacollaboration script show --resource-group "SampleResourceGroup" --name "Script1" --workspace-name "Workspace1"
```
##### <a name="ParametersScriptsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--script-name**|string|The name of the script.|script_name|scriptName|

#### <a name="ScriptsCreateOrUpdate#Create">Command `az datacollaboration script create`</a>

##### <a name="ExamplesScriptsCreateOrUpdate#Create">Example</a>
```
az datacollaboration script create --resource-group "SampleResourceGroup" --synapse-spark-script content="Hello \
Python!" language="Python" sinks="bar" sources="foo" visibility="ShowAll" --name "Script1" --workspace-name \
"Workspace1"
```
##### <a name="ExamplesScriptsCreateOrUpdate#Create">Example</a>
```
az datacollaboration script create --resource-group "SampleResourceGroup" --synapse-spark-script content="Hello \
Python!" language="Python" sinks="bar" sources="foo" visibility="ShowAll" --name "Script1" --workspace-name \
"Workspace1"
```
##### <a name="ParametersScriptsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--script-name**|string|The name of the script.|script_name|scriptName|
|**--synapse-spark-script**|object|A type of script based on the compute engine|synapse_spark_script|SynapseSparkScript|

#### <a name="ScriptsCreateOrUpdate#Update">Command `az datacollaboration script update`</a>

##### <a name="ParametersScriptsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--script-name**|string|The name of the script.|script_name|scriptName|
|**--synapse-spark-script**|object|A type of script based on the compute engine|synapse_spark_script|SynapseSparkScript|

#### <a name="ScriptsDelete">Command `az datacollaboration script delete`</a>

##### <a name="ExamplesScriptsDelete">Example</a>
```
az datacollaboration script delete --resource-group "SampleResourceGroup" --name "Script1" --workspace-name \
"Workspace1"
```
##### <a name="ParametersScriptsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--script-name**|string|The name of the script.|script_name|scriptName|

### group `az datacollaboration script-reference`
#### <a name="ScriptReferencesListByProposal">Command `az datacollaboration script-reference list`</a>

##### <a name="ExamplesScriptReferencesListByProposal">Example</a>
```
az datacollaboration script-reference list --proposal-name "Proposal1" --resource-group "SampleResourceGroup" \
--workspace-name "Workspace1"
```
##### <a name="ParametersScriptReferencesListByProposal">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|

#### <a name="ScriptReferencesGet">Command `az datacollaboration script-reference show`</a>

##### <a name="ExamplesScriptReferencesGet">Example</a>
```
az datacollaboration script-reference show --proposal-name "Proposal1" --reference-name "ScriptReference1" \
--resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersScriptReferencesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--reference-name**|string|The name of the reference.|reference_name|referenceName|

#### <a name="ScriptReferencesCreateOrUpdate#Create">Command `az datacollaboration script-reference create`</a>

##### <a name="ExamplesScriptReferencesCreateOrUpdate#Create">Example</a>
```
az datacollaboration script-reference create --proposal-name "Proposal1" --reference-name "ScriptReference1" \
--resource-group "SampleResourceGroup" --revision 1 --script-id "d164252e-2909-4718-a91e-315195c54b09" \
--workspace-name "Workspace1"
```
##### <a name="ParametersScriptReferencesCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--reference-name**|string|The name of the reference.|reference_name|referenceName|
|**--revision**|integer|The revision number of the script being referenced. If omitted, the script latest version will be referenced.|revision|revision|
|**--script-id**|string|The unique identifier of the referenced script|script_id|scriptId|

#### <a name="ScriptReferencesCreateOrUpdate#Update">Command `az datacollaboration script-reference update`</a>

##### <a name="ParametersScriptReferencesCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--reference-name**|string|The name of the reference.|reference_name|referenceName|
|**--revision**|integer|The revision number of the script being referenced. If omitted, the script latest version will be referenced.|revision|revision|
|**--script-id**|string|The unique identifier of the referenced script|script_id|scriptId|

#### <a name="ScriptReferencesDelete">Command `az datacollaboration script-reference delete`</a>

##### <a name="ExamplesScriptReferencesDelete">Example</a>
```
az datacollaboration script-reference delete --proposal-name "Proposal1" --reference-name "ScriptReference1" \
--resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersScriptReferencesDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--reference-name**|string|The name of the reference.|reference_name|referenceName|

#### <a name="ScriptReferencesResolve">Command `az datacollaboration script-reference resolve`</a>

##### <a name="ExamplesScriptReferencesResolve">Example</a>
```
az datacollaboration script-reference resolve --proposal-name "Proposal1" --reference-name "ScriptReference1" \
--resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### <a name="ParametersScriptReferencesResolve">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--proposal-name**|string|The name of the proposal.|proposal_name|proposalName|
|**--reference-name**|string|The name of the reference.|reference_name|referenceName|

### group `az datacollaboration script-revision`
#### <a name="ScriptRevisionsListByScript">Command `az datacollaboration script-revision list`</a>

##### <a name="ExamplesScriptRevisionsListByScript">Example</a>
```
az datacollaboration script-revision list --resource-group "SampleResourceGroup" --script-name "Script1" \
--workspace-name "Workspace1"
```
##### <a name="ParametersScriptRevisionsListByScript">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--script-name**|string|The name of the script.|script_name|scriptName|
|**--skip-token**|string|continuation token|skip_token|$skipToken|

#### <a name="ScriptRevisionsGet">Command `az datacollaboration script-revision show`</a>

##### <a name="ExamplesScriptRevisionsGet">Example</a>
```
az datacollaboration script-revision show --resource-group "SampleResourceGroup" --revision 1 --script-name "Script1" \
--workspace-name "Workspace1"
```
##### <a name="ParametersScriptRevisionsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--script-name**|string|The name of the script.|script_name|scriptName|
|**--revision**|integer|The revision of the script.|revision|revision|

### group `az datacollaboration workspace`
#### <a name="WorkspacesListByResourceGroup">Command `az datacollaboration workspace list`</a>

##### <a name="ExamplesWorkspacesListByResourceGroup">Example</a>
```
az datacollaboration workspace list --resource-group "SampleResourceGroup"
```
##### <a name="ParametersWorkspacesListByResourceGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--skip-token**|string|Continuation token|skip_token|$skipToken|

#### <a name="WorkspacesListBySubscription">Command `az datacollaboration workspace list`</a>

##### <a name="ExamplesWorkspacesListBySubscription">Example</a>
```
az datacollaboration workspace list
```
##### <a name="ParametersWorkspacesListBySubscription">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="WorkspacesGet">Command `az datacollaboration workspace show`</a>

##### <a name="ExamplesWorkspacesGet">Example</a>
```
az datacollaboration workspace show --resource-group "SampleResourceGroup" --name "Workspace1"
```
##### <a name="ParametersWorkspacesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|

#### <a name="WorkspacesCreateOrUpdate#Create">Command `az datacollaboration workspace create`</a>

##### <a name="ExamplesWorkspacesCreateOrUpdate#Create">Example</a>
```
az datacollaboration workspace create --resource-group "SampleResourceGroup" --location "West US 2" --tags tag1="Red" \
tag2="White" --name "Workspace1"
```
##### <a name="ParametersWorkspacesCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--location**|string|Location of the azure resource.|location|location|
|**--tags**|dictionary|Tags on the azure resource.|tags|tags|

#### <a name="WorkspacesUpdate">Command `az datacollaboration workspace update`</a>

##### <a name="ExamplesWorkspacesUpdate">Example</a>
```
az datacollaboration workspace update --resource-group "SampleResourceGroup" --name "Workspace1" --tags tag1="Red" \
tag2="White"
```
##### <a name="ParametersWorkspacesUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--tags**|dictionary|Tags on the azure resource.|tags|tags|

#### <a name="WorkspacesDelete">Command `az datacollaboration workspace delete`</a>

##### <a name="ExamplesWorkspacesDelete">Example</a>
```
az datacollaboration workspace delete --resource-group "SampleResourceGroup" --name "Workspace1"
```
##### <a name="ParametersWorkspacesDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The resource group name.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
