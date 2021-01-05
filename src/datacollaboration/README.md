# Azure CLI datacollaboration Extension #
This is the extension for datacollaboration

### How to use ###
Install this extension using the below CLI command
```
az extension add --name datacollaboration
```

### Included Features ###
#### datacollaboration consumer-invitation ####
##### Show #####
```
az datacollaboration consumer-invitation show --invitation-id "dfbbc788-19eb-4607-a5a1-c74181bfff03" \
    --location "East US 2" 
```
##### List-invitation #####
```
az datacollaboration consumer-invitation list-invitation
```
##### Reject-invitation #####
```
az datacollaboration consumer-invitation reject-invitation --invitation-id "dfbbc788-19eb-4607-a5a1-c74181bfff03" \
    --location "East US 2" 
```
#### datacollaboration workspace ####
##### Create #####
```
az datacollaboration workspace create --resource-group "SampleResourceGroup" --location "West US 2" \
    --tags tag1="Red" tag2="White" --name "Workspace1" 

az datacollaboration workspace wait --created --resource-group "{rg}" --name "{myWorkspace}"
```
##### Show #####
```
az datacollaboration workspace show --resource-group "SampleResourceGroup" --name "Workspace1"
```
##### List #####
```
az datacollaboration workspace list --resource-group "SampleResourceGroup"
```
##### Update #####
```
az datacollaboration workspace update --resource-group "SampleResourceGroup" --name "Workspace1" \
    --tags tag1="Red" tag2="White" 
```
##### Delete #####
```
az datacollaboration workspace delete --resource-group "SampleResourceGroup" --name "Workspace1"
```
#### datacollaboration constrained-resource ####
##### Create #####
```
az datacollaboration constrained-resource create \
    --constrained-resource "{\\"kind\\":\\"SynapseSparkPool\\",\\"properties\\":{\\"autoPause\\":{\\"delayInMinutes\\":15,\\"enabled\\":true},\\"autoScale\\":{\\"enabled\\":true,\\"maxNodeCount\\":50,\\"minNodeCount\\":3},\\"nodeCount\\":4,\\"nodeSize\\":\\"Medium\\",\\"nodeSizeFamily\\":\\"MemoryOptimized\\",\\"sparkVersion\\":\\"2.4\\"}}" \
    --name "SynapseSparkPool1" --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### Create #####
```
az datacollaboration constrained-resource create \
    --constrained-resource "{\\"kind\\":\\"SynapseSparkPool\\",\\"properties\\":{\\"autoPause\\":{\\"delayInMinutes\\":15,\\"enabled\\":true},\\"autoScale\\":{\\"enabled\\":true,\\"maxNodeCount\\":50,\\"minNodeCount\\":3},\\"nodeCount\\":4,\\"nodeSize\\":\\"Medium\\",\\"nodeSizeFamily\\":\\"MemoryOptimized\\",\\"sparkVersion\\":\\"2.4\\"}}" \
    --name "SynapseSparkPool1" --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### List #####
```
az datacollaboration constrained-resource list --resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### Show #####
```
az datacollaboration constrained-resource show --name "SynapseSparkPool1" --resource-group "SampleResourceGroup" \
    --workspace-name "Workspace1" 
```
##### Delete #####
```
az datacollaboration constrained-resource delete --name "SynapseSparkPool1" --resource-group "SampleResourceGroup" \
    --workspace-name "Workspace1" 
```
#### datacollaboration data-asset ####
##### Create #####
```
az datacollaboration data-asset create --description "Data of DataSet1" --data-processing-strategy "CopyBased" \
    --name "DataAsset1" --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### Show #####
```
az datacollaboration data-asset show --name "DataAsset1" --resource-group "SampleResourceGroup" \
    --workspace-name "Workspace1" 
```
##### List #####
```
az datacollaboration data-asset list --resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### Delete #####
```
az datacollaboration data-asset delete --name "DataAsset1" --resource-group "SampleResourceGroup" \
    --workspace-name "Workspace1" 
```
#### datacollaboration data-set ####
##### Create #####
```
az datacollaboration data-set create --data-asset-name "DataAsset1" \
    --blob-data-set container-name="C1" file-path="file21" storage-account-id="subscriptions/12345678-1234-1234-1234-567890abcdef/resourceGroups/SampleResourceGroup/providers/Microsoft.Storage/storageAccounts/storage2" \
    --data-set-category "Production" --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### Show #####
```
az datacollaboration data-set show --data-asset-name "DataAsset1" --data-set-category "Production" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### List #####
```
az datacollaboration data-set list --data-asset-name "DataAsset1" --resource-group "SampleResourceGroup" \
    --workspace-name "Workspace1" 
```
##### Delete #####
```
az datacollaboration data-set delete --data-asset-name "DataAsset1" --data-set-category "Production" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
#### datacollaboration pipeline-run ####
##### List #####
```
az datacollaboration pipeline-run list --resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### Show #####
```
az datacollaboration pipeline-run show --name "a4cdba19-a513-46ca-9d48-47806e396d13" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### Cancel #####
```
az datacollaboration pipeline-run cancel --name "a4cdba19-a513-46ca-9d48-47806e396d13" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
#### datacollaboration pipeline-step-run ####
##### List #####
```
az datacollaboration pipeline-step-run list --pipeline-run-name "a4cdba19-a513-46ca-9d48-47806e396d13" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### Show #####
```
az datacollaboration pipeline-step-run show --pipeline-run-name "a4cdba19-a513-46ca-9d48-47806e396d13" \
    --name "5ec0dd18-ea32-4d27-b3a5-2920c5f26325" --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
#### datacollaboration pipeline ####
##### Create #####
```
az datacollaboration pipeline create --description "A pipeline" --name "Pipeline1" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### Show #####
```
az datacollaboration pipeline show --name "Pipeline1" --resource-group "SampleResourceGroup" \
    --workspace-name "Workspace1" 
```
##### List #####
```
az datacollaboration pipeline list --resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### Run #####
```
az datacollaboration pipeline run --name "Pipeline1" --pipeline-run-mode "Test" --resource-group "SampleResourceGroup" \
    --workspace-name "Workspace1" 
```
##### Delete #####
```
az datacollaboration pipeline delete --name "Pipeline1" --resource-group "SampleResourceGroup" \
    --workspace-name "Workspace1" 
```
#### datacollaboration pipeline-step ####
##### Create #####
```
az datacollaboration pipeline-step create --pipeline-name "Pipeline1" \
    --synapse-spark-pipeline-step dependencies="PipelineStep0" executor-node-size="Medium" executors-count=4 script-id="284878c1-deb7-440a-9f87-28b6e58242a3" script-revision=1 script-sink-bindings={"dataAssetId":"2f5a9076-3372-4282-b52d-a382382930ee","key":"sink1"} script-sink-bindings={"dataAssetId":"30ba4508-b74f-46b0-bc30-1d891cd19ba1","key":"sink2"} script-source-bindings={"dataAssetId":"093a76ba-a0f2-4a03-80b1-bec1d3368711","key":"source1"} script-source-bindings={"dataAssetId":"2aa367d4-839c-468c-95b9-f3e63c628111","key":"source2"} synapse-spark-pool-id="08206bdd-a08d-4005-9bdf-1a2ca08a399b" \
    --name "PipelineStep1" --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### Create #####
```
az datacollaboration pipeline-step create --pipeline-name "Pipeline1" \
    --synapse-spark-pipeline-step dependencies="PipelineStep0" executor-node-size="Medium" executors-count=4 script-id="284878c1-deb7-440a-9f87-28b6e58242a3" script-revision=1 script-sink-bindings={"dataAssetId":"2f5a9076-3372-4282-b52d-a382382930ee","key":"sink1"} script-sink-bindings={"dataAssetId":"30ba4508-b74f-46b0-bc30-1d891cd19ba1","key":"sink2"} script-source-bindings={"dataAssetId":"093a76ba-a0f2-4a03-80b1-bec1d3368711","key":"source1"} script-source-bindings={"dataAssetId":"2aa367d4-839c-468c-95b9-f3e63c628111","key":"source2"} synapse-spark-pool-id="08206bdd-a08d-4005-9bdf-1a2ca08a399b" \
    --name "PipelineStep1" --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### List #####
```
az datacollaboration pipeline-step list --pipeline-name "Pipeline1" --resource-group "SampleResourceGroup" \
    --workspace-name "Workspace1" 
```
##### Show #####
```
az datacollaboration pipeline-step show --pipeline-name "Pipeline1" --name "PipelineStep1" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### Delete #####
```
az datacollaboration pipeline-step delete --pipeline-name "Pipeline1" --name "PipelineStep1" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
#### datacollaboration proposal ####
##### Create #####
```
az datacollaboration proposal create --description "Proposal description" --terms "Proposal terms" --name "Proposal1" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 

az datacollaboration proposal wait --created --name "{myProposal}" --resource-group "{rg}"
```
##### Show #####
```
az datacollaboration proposal show --name "Proposal1" --resource-group "SampleResourceGroup" \
    --workspace-name "Workspace1" 
```
##### List #####
```
az datacollaboration proposal list --resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### Revoke #####
```
az datacollaboration proposal revoke --name "Proposal1" --resource-group "SampleResourceGroup" \
    --workspace-name "Workspace1" 
```
##### Sign #####
```
az datacollaboration proposal sign --name "Proposal1" --proposal-version "ae660cb9-0c0c-4ff5-a68f-dc5584a63c79" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### Delete #####
```
az datacollaboration proposal delete --name "Proposal1" --resource-group "SampleResourceGroup" \
    --workspace-name "Workspace1" 
```
#### datacollaboration data-asset-reference ####
##### Create #####
```
az datacollaboration data-asset-reference create --description "Reference to DataAsset1" \
    --data-asset-id "d164252e-2909-4718-a91e-315195c54b09" --proposal-name "Proposal1" \
    --reference-name "DataAssetReference1" --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### Show #####
```
az datacollaboration data-asset-reference show --proposal-name "Proposal1" --reference-name "DataAssetReference1" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### List #####
```
az datacollaboration data-asset-reference list --proposal-name "Proposal1" --resource-group "SampleResourceGroup" \
    --workspace-name "Workspace1" 
```
##### Resolve #####
```
az datacollaboration data-asset-reference resolve --proposal-name "Proposal1" --reference-name "DataAssetReference1" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### Delete #####
```
az datacollaboration data-asset-reference delete --proposal-name "Proposal1" --reference-name "DataAssetReference1" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
#### datacollaboration entitlement ####
##### Create #####
```
az datacollaboration entitlement create --description "Entitlement description" \
    --resource-id "6fa17733-0c87-4671-bc4c-a6d9f1228948" --resource-type "DataAssetReference" \
    --subject-id "a415f518-e721-4852-84de-8b139f92b933" --name "Entitlement1" --proposal-name "Proposal1" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### Show #####
```
az datacollaboration entitlement show --name "Entitlement1" --proposal-name "Proposal1" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### List #####
```
az datacollaboration entitlement list --proposal-name "Proposal1" --resource-group "SampleResourceGroup" \
    --workspace-name "Workspace1" 
```
##### Delete #####
```
az datacollaboration entitlement delete --name "Entitlement1" --proposal-name "Proposal1" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
#### datacollaboration constraint ####
##### Create #####
```
az datacollaboration constraint create \
    --script-constraint description="Constraint description" script-reference-id="6fa17733-0c87-4671-bc4c-a6d9f1228948" \
    --name "Constraint1" --entitlement-name "Entitlement1" --proposal-name "Proposal1" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### Show #####
```
az datacollaboration constraint show --name "Constraint1" --entitlement-name "Entitlement1" \
    --proposal-name "Proposal1" --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### List #####
```
az datacollaboration constraint list --entitlement-name "Entitlement1" --proposal-name "Proposal1" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### Delete #####
```
az datacollaboration constraint delete --name "Constraint1" --entitlement-name "Entitlement1" \
    --proposal-name "Proposal1" --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
#### datacollaboration policy ####
##### Create #####
```
az datacollaboration policy create --entitlement-name "Entitlement1" \
    --diagnostic-policy description="Policy description" log-level="Information" --name "Policy1" \
    --proposal-name "Proposal1" --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### Show #####
```
az datacollaboration policy show --entitlement-name "Entitlement1" --name "Policy1" --proposal-name "Proposal1" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### List #####
```
az datacollaboration policy list --entitlement-name "Entitlement1" --proposal-name "Proposal1" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### Delete #####
```
az datacollaboration policy delete --entitlement-name "Entitlement1" --name "Policy1" --proposal-name "Proposal1" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
#### datacollaboration invitation ####
##### Create #####
```
az datacollaboration invitation create --target-email "receiver@microsoft.com" --name "Invitation1" \
    --proposal-name "Proposal1" --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### Show #####
```
az datacollaboration invitation show --name "Invitation1" --proposal-name "Proposal1" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### List #####
```
az datacollaboration invitation list --proposal-name "Proposal1" --resource-group "SampleResourceGroup" \
    --workspace-name "Workspace1" 
```
##### Delete #####
```
az datacollaboration invitation delete --name "Invitation1" --proposal-name "Proposal1" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
#### datacollaboration participant ####
##### List #####
```
az datacollaboration participant list --proposal-name "Proposal1" --resource-group "SampleResourceGroup" \
    --workspace-name "Workspace1" 
```
##### Show #####
```
az datacollaboration participant show --name "Participant1" --proposal-name "Proposal1" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
#### datacollaboration script-reference ####
##### Create #####
```
az datacollaboration script-reference create --proposal-name "Proposal1" --reference-name "ScriptReference1" \
    --resource-group "SampleResourceGroup" --revision 1 --script-id "d164252e-2909-4718-a91e-315195c54b09" \
    --workspace-name "Workspace1" 
```
##### Show #####
```
az datacollaboration script-reference show --proposal-name "Proposal1" --reference-name "ScriptReference1" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### List #####
```
az datacollaboration script-reference list --proposal-name "Proposal1" --resource-group "SampleResourceGroup" \
    --workspace-name "Workspace1" 
```
##### Resolve #####
```
az datacollaboration script-reference resolve --proposal-name "Proposal1" --reference-name "ScriptReference1" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
##### Delete #####
```
az datacollaboration script-reference delete --proposal-name "Proposal1" --reference-name "ScriptReference1" \
    --resource-group "SampleResourceGroup" --workspace-name "Workspace1" 
```
#### datacollaboration resource-reference ####
##### List #####
```
az datacollaboration resource-reference list --resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
#### datacollaboration script ####
##### Create #####
```
az datacollaboration script create --resource-group "SampleResourceGroup" \
    --synapse-spark-script content="Hello Python!" language="Python" sinks="bar" sources="foo" visibility="ShowAll" \
    --name "Script1" --workspace-name "Workspace1" 
```
##### Create #####
```
az datacollaboration script create --resource-group "SampleResourceGroup" \
    --synapse-spark-script content="Hello Python!" language="Python" sinks="bar" sources="foo" visibility="ShowAll" \
    --name "Script1" --workspace-name "Workspace1" 
```
##### List #####
```
az datacollaboration script list --resource-group "SampleResourceGroup" --workspace-name "Workspace1"
```
##### Show #####
```
az datacollaboration script show --resource-group "SampleResourceGroup" --name "Script1" --workspace-name "Workspace1"
```
##### Delete #####
```
az datacollaboration script delete --resource-group "SampleResourceGroup" --name "Script1" \
    --workspace-name "Workspace1" 
```
#### datacollaboration script-revision ####
##### List #####
```
az datacollaboration script-revision list --resource-group "SampleResourceGroup" --script-name "Script1" \
    --workspace-name "Workspace1" 
```
##### Show #####
```
az datacollaboration script-revision show --resource-group "SampleResourceGroup" --revision 1 --script-name "Script1" \
    --workspace-name "Workspace1" 
```