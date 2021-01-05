# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


from .. import try_manual


# EXAMPLE: /Workspaces/put/Workspaces_CreateOrUpdate
@try_manual
def step_workspace_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration workspace create '
             '--resource-group "{rg}" '
             '--location "West US 2" '
             '--tags tag1="Red" tag2="White" '
             '--name "{myWorkspace}"',
             checks=[])
    test.cmd('az datacollaboration workspace wait --created '
             '--resource-group "{rg}" '
             '--name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Workspaces/get/Workspaces_Get
@try_manual
def step_workspace_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration workspace show '
             '--resource-group "{rg}" '
             '--name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Workspaces/get/Workspaces_ListByResourceGroup
@try_manual
def step_workspace_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration workspace list '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Workspaces/get/Workspaces_ListBySubscription
@try_manual
def step_workspace_list2(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration workspace list '
             '-g ""',
             checks=checks)


# EXAMPLE: /Workspaces/patch/Workspaces_Update
@try_manual
def step_workspace_update(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration workspace update '
             '--resource-group "{rg}" '
             '--name "{myWorkspace}" '
             '--tags tag1="Red" tag2="White"',
             checks=checks)


# EXAMPLE: /ConstrainedResources/put/ConstrainedResources_CreateOrUpdate
@try_manual
def step_constrained_resource_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration constrained-resource create '
             '--constrained-resource "{{\\"kind\\":\\"SynapseSparkPool\\",\\"properties\\":{{\\"autoPause\\":{{\\"delay'
             'InMinutes\\":15,\\"enabled\\":true}},\\"autoScale\\":{{\\"enabled\\":true,\\"maxNodeCount\\":50,\\"minNod'
             'eCount\\":3}},\\"nodeCount\\":4,\\"nodeSize\\":\\"Medium\\",\\"nodeSizeFamily\\":\\"MemoryOptimized\\",\\'
             '"sparkVersion\\":\\"2.4\\"}}}}" '
             '--name "{myConstrainedResource}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /ConstrainedResources/put/ConstrainedResources_SynapseSparkPool_CreateOrUpdate
@try_manual
def step_constrained_resource_create2(test, rg, checks=None):
    return step_constrained_resource_create(test, rg, checks)


# EXAMPLE: /ConstrainedResources/get/ConstrainedResources_Get
@try_manual
def step_constrained_resource_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration constrained-resource show '
             '--name "{myConstrainedResource}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /ConstrainedResources/get/ConstrainedResources_ListByWorkspace
@try_manual
def step_constrained_resource_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration constrained-resource list '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /ConstrainedResources/delete/ConstrainedResources_Delete
@try_manual
def step_constrained_resource_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration constrained-resource delete -y '
             '--name "{myConstrainedResource}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Proposals/put/Proposals_CreateOrUpdate
@try_manual
def step_proposal_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration proposal create '
             '--description "Proposal description" '
             '--terms "Proposal terms" '
             '--name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[])
    test.cmd('az datacollaboration proposal wait --created '
             '--name "{myProposal}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Proposals/post/Proposals_Revoke
@try_manual
def step_proposal_revoke(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration proposal revoke '
             '--name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Proposals/post/Proposals_Sign
@try_manual
def step_proposal_sign(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration proposal sign '
             '--name "{myProposal}" '
             '--proposal-version "ae660cb9-0c0c-4ff5-a68f-dc5584a63c79" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Constraints/put/Constraints_CreateOrUpdate
@try_manual
def step_constraint_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration constraint create '
             '--script-constraint description="Constraint description" script-reference-id="6fa17733-0c87-4671-bc4c-a6d'
             '9f1228948" '
             '--name "{myConstraint}" '
             '--entitlement-name "{myEntitlement}" '
             '--proposal-name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Constraints/get/Constraints_Get
@try_manual
def step_constraint_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration constraint show '
             '--name "{myConstraint}" '
             '--entitlement-name "{myEntitlement}" '
             '--proposal-name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Constraints/get/Constraints_ListByEntitlement
@try_manual
def step_constraint_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration constraint list '
             '--entitlement-name "{myEntitlement}" '
             '--proposal-name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Constraints/delete/Constraints_Delete
@try_manual
def step_constraint_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration constraint delete -y '
             '--name "{myConstraint}" '
             '--entitlement-name "{myEntitlement}" '
             '--proposal-name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /ConsumerInvitations/get/ConsumerInvitations_Get
@try_manual
def step_consumer_invitation_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration consumer-invitation show '
             '--invitation-id "dfbbc788-19eb-4607-a5a1-c74181bfff03" '
             '--location "East US 2"',
             checks=checks)


# EXAMPLE: /ConsumerInvitations/get/ConsumerInvitations_ListInvitations
@try_manual
def step_consumer_invitation_list_invitation(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration consumer-invitation list-invitation',
             checks=checks)


# EXAMPLE: /ConsumerInvitations/post/ConsumerInvitations_RejectInvitation
@try_manual
def step_consumer_invitation_reject_invitation(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration consumer-invitation reject-invitation '
             '--invitation-id "dfbbc788-19eb-4607-a5a1-c74181bfff03" '
             '--location "East US 2"',
             checks=checks)


# EXAMPLE: /DataAssetReferences/put/DataAssetReferences_CreateOrUpdate
@try_manual
def step_data_asset_reference_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration data-asset-reference create '
             '--description "Reference to DataAsset1" '
             '--data-asset-id "d164252e-2909-4718-a91e-315195c54b09" '
             '--proposal-name "{myProposal}" '
             '--reference-name "DataAssetReference1" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /DataAssetReferences/get/DataAssetReferences_Get
@try_manual
def step_data_asset_reference_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration data-asset-reference show '
             '--proposal-name "{myProposal}" '
             '--reference-name "DataAssetReference1" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /DataAssetReferences/get/DataAssetReferences_ListByProposal
@try_manual
def step_data_asset_reference_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration data-asset-reference list '
             '--proposal-name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /DataAssetReferences/post/DataAssetReferences_Resolve
@try_manual
def step_data_asset_reference_resolve(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration data-asset-reference resolve '
             '--proposal-name "{myProposal}" '
             '--reference-name "DataAssetReference1" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /DataAssetReferences/delete/DataAssetReferences_Delete
@try_manual
def step_data_asset_reference_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration data-asset-reference delete -y '
             '--proposal-name "{myProposal}" '
             '--reference-name "DataAssetReference1" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /DataAssets/put/DataAssets_CreateOrUpdate
@try_manual
def step_data_asset_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration data-asset create '
             '--description "Data of DataSet1" '
             '--data-processing-strategy "CopyBased" '
             '--name "{myDataAsset}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /DataAssets/get/DataAssets_Get
@try_manual
def step_data_asset_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration data-asset show '
             '--name "{myDataAsset}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /DataAssets/get/DataAssets_ListByWorkspace
@try_manual
def step_data_asset_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration data-asset list '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /DataSets/put/DataSets_CreateOrUpdate
@try_manual
def step_data_set_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration data-set create '
             '--data-asset-name "{myDataAsset}" '
             '--blob-data-set container-name="C1" file-path="file21" storage-account-id="subscriptions/12345678-1234-12'
             '34-1234-567890abcdef/resourceGroups/SampleResourceGroup/providers/Microsoft.Storage/storageAccounts/stora'
             'ge2" '
             '--data-set-category "Production" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /DataSets/get/DataSets_Get
@try_manual
def step_data_set_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration data-set show '
             '--data-asset-name "{myDataAsset}" '
             '--data-set-category "Production" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /DataSets/get/DataSets_ListByDataAsset
@try_manual
def step_data_set_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration data-set list '
             '--data-asset-name "{myDataAsset}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /DataSets/delete/DataSets_Delete
@try_manual
def step_data_set_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration data-set delete -y '
             '--data-asset-name "{myDataAsset}" '
             '--data-set-category "Production" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /DataAssets/delete/DataAssets_Delete
@try_manual
def step_data_asset_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration data-asset delete -y '
             '--name "{myDataAsset}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Entitlements/put/Entitlements_CreateOrUpdate
@try_manual
def step_entitlement_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration entitlement create '
             '--description "Entitlement description" '
             '--resource-id "6fa17733-0c87-4671-bc4c-a6d9f1228948" '
             '--resource-type "DataAssetReference" '
             '--subject-id "a415f518-e721-4852-84de-8b139f92b933" '
             '--name "{myEntitlement}" '
             '--proposal-name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Entitlements/get/Entitlements_Get
@try_manual
def step_entitlement_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration entitlement show '
             '--name "{myEntitlement}" '
             '--proposal-name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Entitlements/get/Entitlements_ListByProposal
@try_manual
def step_entitlement_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration entitlement list '
             '--proposal-name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Entitlements/delete/Entitlements_Delete
@try_manual
def step_entitlement_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration entitlement delete -y '
             '--name "{myEntitlement}" '
             '--proposal-name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Invitations/put/Invitations_Create
@try_manual
def step_invitation_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration invitation create '
             '--target-email "receiver@microsoft.com" '
             '--name "{myInvitation}" '
             '--proposal-name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Invitations/get/Invitations_Get
@try_manual
def step_invitation_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration invitation show '
             '--name "{myInvitation}" '
             '--proposal-name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Invitations/get/Invitations_ListByProposal
@try_manual
def step_invitation_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration invitation list '
             '--proposal-name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Invitations/delete/Invitations_Delete
@try_manual
def step_invitation_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration invitation delete -y '
             '--name "{myInvitation}" '
             '--proposal-name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Participants/get/Participants_Get
@try_manual
def step_participant_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration participant show '
             '--name "{myParticipant}" '
             '--proposal-name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Participants/get/Participants_ListByProposal
@try_manual
def step_participant_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration participant list '
             '--proposal-name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /PipelineRuns/get/PipelineRuns_Get
@try_manual
def step_pipeline_run_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration pipeline-run show '
             '--name "{myPipelineRun}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /PipelineRuns/get/PipelineRuns_ListByWorkspace
@try_manual
def step_pipeline_run_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration pipeline-run list '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /PipelineRuns/post/PipelineRuns_Cancel
@try_manual
def step_pipeline_run_cancel(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration pipeline-run cancel '
             '--name "{myPipelineRun}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Pipelines/put/Pipelines_CreateOrUpdate
@try_manual
def step_pipeline_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration pipeline create '
             '--description "A pipeline" '
             '--name "{myPipeline}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Pipelines/get/Pipelines_Get
@try_manual
def step_pipeline_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration pipeline show '
             '--name "{myPipeline}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Pipelines/get/Pipelines_ListByWorkspace
@try_manual
def step_pipeline_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration pipeline list '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Pipelines/post/Pipelines_Run
@try_manual
def step_pipeline_run(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration pipeline run '
             '--name "{myPipeline}" '
             '--pipeline-run-mode "Test" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Pipelines/delete/Pipelines_Delete
@try_manual
def step_pipeline_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration pipeline delete -y '
             '--name "{myPipeline}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /PipelineStepRuns/get/PipelineStepRuns_Get
@try_manual
def step_pipeline_step_run_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration pipeline-step-run show '
             '--pipeline-run-name "{myPipelineRun}" '
             '--name "{myPipelineStepRun}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /PipelineStepRuns/get/PipelineStepRuns_ListByPipelineRun
@try_manual
def step_pipeline_step_run_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration pipeline-step-run list '
             '--pipeline-run-name "{myPipelineRun}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /PipelineSteps/put/PipelineSteps_CreateOrUpdate
@try_manual
def step_pipeline_step_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration pipeline-step create '
             '--pipeline-name "{myPipeline}" '
             '--synapse-spark-pipeline-step dependencies="PipelineStep0" executor-node-size="Medium" executors-count=4 '
             'script-id="284878c1-deb7-440a-9f87-28b6e58242a3" script-revision=1 script-sink-bindings={{"dataAssetId":"'
             '2f5a9076-3372-4282-b52d-a382382930ee","key":"sink1"}} script-sink-bindings={{"dataAssetId":"30ba4508-b74f'
             '-46b0-bc30-1d891cd19ba1","key":"sink2"}} script-source-bindings={{"dataAssetId":"093a76ba-a0f2-4a03-80b1-'
             'bec1d3368711","key":"source1"}} script-source-bindings={{"dataAssetId":"2aa367d4-839c-468c-95b9-f3e63c628'
             '111","key":"source2"}} synapse-spark-pool-id="08206bdd-a08d-4005-9bdf-1a2ca08a399b" '
             '--name "{myPipelineStep}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /PipelineSteps/put/PipelineSteps_SynapseSpark_CreateOrUpdate
@try_manual
def step_pipeline_step_create2(test, rg, checks=None):
    return step_pipeline_step_create(test, rg, checks)


# EXAMPLE: /PipelineSteps/get/PipelineSteps_Get
@try_manual
def step_pipeline_step_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration pipeline-step show '
             '--pipeline-name "{myPipeline}" '
             '--name "{myPipelineStep}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /PipelineSteps/get/PipelineSteps_ListByPipeline
@try_manual
def step_pipeline_step_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration pipeline-step list '
             '--pipeline-name "{myPipeline}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /PipelineSteps/delete/PipelineSteps_Delete
@try_manual
def step_pipeline_step_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration pipeline-step delete -y '
             '--pipeline-name "{myPipeline}" '
             '--name "{myPipelineStep}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Proposals/get/Proposals_Get
@try_manual
def step_proposal_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration proposal show '
             '--name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Proposals/get/Proposals_ListByWorkspace
@try_manual
def step_proposal_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration proposal list '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Policies/put/Policies_CreateOrUpdate
@try_manual
def step_policy_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration policy create '
             '--entitlement-name "{myEntitlement}" '
             '--diagnostic-policy description="Policy description" log-level="Information" '
             '--name "{myPolicy}" '
             '--proposal-name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Policies/get/Policies_Get
@try_manual
def step_policy_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration policy show '
             '--entitlement-name "{myEntitlement}" '
             '--name "{myPolicy}" '
             '--proposal-name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Policies/get/Policies_ListByEntitlement
@try_manual
def step_policy_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration policy list '
             '--entitlement-name "{myEntitlement}" '
             '--proposal-name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Policies/delete/Policies_Delete
@try_manual
def step_policy_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration policy delete -y '
             '--entitlement-name "{myEntitlement}" '
             '--name "{myPolicy}" '
             '--proposal-name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Proposals/delete/Proposals_Delete
@try_manual
def step_proposal_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration proposal delete -y '
             '--name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /ResourceReferences/get/ResourceReferences_ListByWorkspace
@try_manual
def step_resource_reference_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration resource-reference list '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /ScriptReferences/put/ScriptReferences_CreateOrUpdate
@try_manual
def step_script_reference_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration script-reference create '
             '--proposal-name "{myProposal}" '
             '--reference-name "ScriptReference1" '
             '--resource-group "{rg}" '
             '--revision 1 '
             '--script-id "d164252e-2909-4718-a91e-315195c54b09" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /ScriptReferences/get/ScriptReferences_Get
@try_manual
def step_script_reference_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration script-reference show '
             '--proposal-name "{myProposal}" '
             '--reference-name "ScriptReference1" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /ScriptReferences/get/ScriptReferences_ListByProposal
@try_manual
def step_script_reference_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration script-reference list '
             '--proposal-name "{myProposal}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /ScriptReferences/post/ScriptReferences_Resolve
@try_manual
def step_script_reference_resolve(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration script-reference resolve '
             '--proposal-name "{myProposal}" '
             '--reference-name "ScriptReference1" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /ScriptReferences/delete/ScriptReferences_Delete
@try_manual
def step_script_reference_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration script-reference delete -y '
             '--proposal-name "{myProposal}" '
             '--reference-name "ScriptReference1" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Scripts/put/Scripts_CreateOrUpdate
@try_manual
def step_script_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration script create '
             '--resource-group "{rg}" '
             '--synapse-spark-script content="Hello Python!" language="Python" sinks="bar" sources="foo" '
             'visibility="ShowAll" '
             '--name "{myScript}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Scripts/put/Scripts_SynapseSpark_CreateOrUpdate
@try_manual
def step_script_create2(test, rg, checks=None):
    return step_script_create(test, rg, checks)


# EXAMPLE: /Scripts/get/Scripts_Get
@try_manual
def step_script_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration script show '
             '--resource-group "{rg}" '
             '--name "{myScript}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Scripts/get/Scripts_ListByWorkspace
@try_manual
def step_script_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration script list '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /ScriptRevisions/get/ScriptRevisions_Get
@try_manual
def step_script_revision_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration script-revision show '
             '--resource-group "{rg}" '
             '--revision 1 '
             '--script-name "{myScript}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /ScriptRevisions/get/ScriptRevisions_ListByScript
@try_manual
def step_script_revision_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration script-revision list '
             '--resource-group "{rg}" '
             '--script-name "{myScript}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Scripts/delete/Scripts_Delete
@try_manual
def step_script_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration script delete -y '
             '--resource-group "{rg}" '
             '--name "{myScript}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Workspaces/delete/Workspaces_Delete
@try_manual
def step_workspace_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datacollaboration workspace delete -y '
             '--resource-group "{rg}" '
             '--name "{myWorkspace}"',
             checks=checks)

