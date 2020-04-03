# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class AzureMachineLearningWorkspacesScenarioTest(ScenarioTest):

    def current_subscription(self):
        subs = self.cmd('az account show').get_output_in_json()
        return subs['id']

    @ResourceGroupPreparer(name_prefix='cli_test_machinelearningservices_workspace-1234'[:9], key='rg')
    @ResourceGroupPreparer(name_prefix='cli_test_machinelearningservices_accountcrud-1234'[:9], key='rg_2')
    @ResourceGroupPreparer(name_prefix='cli_test_machinelearningservices_testrg123'[:9], key='rg_3')
    @ResourceGroupPreparer(name_prefix='cli_test_machinelearningservices_resourceGroup-4321'[:9], key='rg_4')
    @ResourceGroupPreparer(name_prefix='cli_test_machinelearningservices_rg'[:9], key='rg_8')
    @ResourceGroupPreparer(name_prefix='cli_test_machinelearningservices_resourceGroup-1234'[:9], key='rg_5')
    @ResourceGroupPreparer(name_prefix='cli_test_machinelearningservices_rg-1234'[:9], key='rg_6')
    @ResourceGroupPreparer(name_prefix='cli_test_machinelearningservices_myResourceGroup'[:9], key='rg_7')
    def test_machinelearningservices(self, resource_group):

        self.kwargs.update({
            'subscription_id': self.current_subscription()
        })

        self.kwargs.update({
            'linkedWorkspace-1234': self.create_random_name(prefix='cli_test_workspaces'[:9], length=24),
            'Workspaces_5': self.create_random_name(prefix='cli_test_workspaces'[:9], length=24),
            'Workspaces_6': self.create_random_name(prefix='cli_test_workspaces'[:9], length=24),
            'Workspaces_2': self.create_random_name(prefix='cli_test_workspaces'[:9], length=24),
            'Workspaces_3': self.create_random_name(prefix='cli_test_workspaces'[:9], length=24),
            'Workspaces_4': self.create_random_name(prefix='cli_test_workspaces'[:9], length=24),
        })

        self.cmd('az machinelearningservices workspace create '
                 '--location "eastus2euap" '
                 '--properties-description "test description" '
                 '--properties-application-insights "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/microsoft.insights/components/testinsights" '
                 '--properties-container-registry "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.ContainerRegistry/registries/testRegistry" '
                 '--properties-encryption "{{\\"keyVaultProperties\\":{{\\"identityClientId\\":\\"\\",\\"keyIdentifier\\":\\"https://testkv.vault.azure.net/keys/testkey/aabbccddee112233445566778899aabb\\",\\"keyVaultArmId\\":\\"/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.KeyVault/vaults/testkv\\"}},\\"status\\":\\"Enabled\\"}}" '
                 '--properties-friendly-name "HelloName" '
                 '--properties-hbi-workspace false '
                 '--properties-key-vault "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.KeyVault/vaults/testkv" '
                 '--properties-shared-private-link-resources name=testdbresource properties=[object Object]=undefined '
                 '--properties-storage-account "/subscriptions/{subscription_id}/resourceGroups/{rg_2}/providers/Microsoft.Storage/storageAccounts/testStorageAccount" '
                 '--sku name=Basic tier=Basic '
                 '--resource-group "{rg}" '
                 '--workspace-name "{Workspaces_2}"',
                 checks=[])

        self.cmd('az machinelearningservices linked-workspace create '
                 '--link-name "link-12" '
                 '--resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg_4}/providers/Microsoft.Synapse/workspaces/{linkedWorkspace-1234}" '
                 '--user-assigned-identity-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg_4}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/uai123" '
                 '--resource-group "{rg_5}" '
                 '--workspace-name "{Workspaces_3}"',
                 checks=[])

        self.cmd('az machinelearningservices machine-learning-compute create '
                 '--compute-name "compute123" '
                 '--location "eastus" '
                 '--properties "{{\\"computeType\\":\\"AmlCompute\\",\\"properties\\":{{\\"description\\":\\"some compute\\",\\"computeType\\":\\"AmlCompute\\",\\"properties\\":{{\\"scaleSettings\\":{{\\"maxNodeCount\\":4,\\"minNodeCount\\":4,\\"nodeIdleTimeBeforeScaleDown\\":\\"PT5M\\"}}}}}}}}" '
                 '--resource-group "{rg_3}" '
                 '--workspace-name "{Workspaces_4}"',
                 checks=[])

        self.cmd('az machinelearningservices machine-learning-compute create '
                 '--compute-name "compute123" '
                 '--location "eastus" '
                 '--properties "{{\\"description\\":\\"some compute\\",\\"computeType\\":\\"AKS\\",\\"properties\\":{{\\"agentCount\\":4}},\\"resourceId\\":\\"/subscriptions/{subscription_id}/resourcegroups/{rg_3}/providers/Microsoft.ContainerService/managedClusters/compute123-56826-c9b00420020b2\\"}}" '
                 '--resource-group "{rg_3}" '
                 '--workspace-name "{Workspaces_4}"',
                 checks=[])

        self.cmd('az machinelearningservices machine-learning-compute create '
                 '--compute-name "compute123" '
                 '--location "eastus" '
                 '--properties "{{\\"computeType\\":\\"DataFactory\\"}}" '
                 '--resource-group "{rg_3}" '
                 '--workspace-name "{Workspaces_4}"',
                 checks=[])

        self.cmd('az machinelearningservices machine-learning-compute create '
                 '--compute-name "compute123" '
                 '--location "eastus" '
                 '--properties "{{\\"computeType\\":\\"AmlCompute\\",\\"properties\\":{{\\"remoteLoginPortPublicAccess\\":\\"NotSpecified\\",\\"scaleSettings\\":{{\\"maxNodeCount\\":1,\\"minNodeCount\\":0,\\"nodeIdleTimeBeforeScaleDown\\":\\"PT5M\\"}},\\"vmPriority\\":\\"Dedicated\\",\\"vmSize\\":\\"STANDARD_NC6\\"}}}}" '
                 '--resource-group "{rg_3}" '
                 '--workspace-name "{Workspaces_4}"',
                 checks=[])

        self.cmd('az machinelearningservices machine-learning-compute create '
                 '--compute-name "compute123" '
                 '--location "eastus" '
                 '--properties "{{\\"computeType\\":\\"AKS\\"}}" '
                 '--resource-group "{rg_3}" '
                 '--workspace-name "{Workspaces_4}"',
                 checks=[])

        self.cmd('az machinelearningservices private-endpoint-connection show '
                 '--private-endpoint-connection-name "{{privateEndpointConnectionName}}" '
                 '--resource-group "{rg_6}" '
                 '--workspace-name "{Workspaces_2}"',
                 checks=[])

        self.cmd('az machinelearningservices machine-learning-compute show '
                 '--compute-name "compute123" '
                 '--resource-group "{rg_3}" '
                 '--workspace-name "{Workspaces_4}"',
                 checks=[])

        self.cmd('az machinelearningservices machine-learning-compute show '
                 '--compute-name "compute123" '
                 '--resource-group "{rg_3}" '
                 '--workspace-name "{Workspaces_4}"',
                 checks=[])

        self.cmd('az machinelearningservices linked-workspace show '
                 '--link-name "link-12" '
                 '--resource-group "{rg_5}" '
                 '--workspace-name "{Workspaces_3}"',
                 checks=[])

        self.cmd('az machinelearningservices workspace show '
                 '--resource-group "{rg}" '
                 '--workspace-name "{Workspaces_2}"',
                 checks=[])

        self.cmd('az machinelearningservices private-link-resource list '
                 '--resource-group "{rg_6}" '
                 '--workspace-name "{Workspaces_2}"',
                 checks=[])

        self.cmd('az machinelearningservices workspace-feature list '
                 '--resource-group "{rg_7}" '
                 '--workspace-name "{Workspaces_2}"',
                 checks=[])

        self.cmd('az machinelearningservices machine-learning-compute list '
                 '--resource-group "{rg_3}" '
                 '--workspace-name "{Workspaces_4}"',
                 checks=[])

        self.cmd('az machinelearningservices linked-workspace list '
                 '--resource-group "{rg_5}" '
                 '--workspace-name "{Workspaces_3}"',
                 checks=[])

        self.cmd('az machinelearningservices workspace list '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az machinelearningservices virtual-machine-size list '
                 '--location "eastus"',
                 checks=[])

        self.cmd('az machinelearningservices usage list '
                 '--location "eastus"',
                 checks=[])

        self.cmd('az machinelearningservices quota list '
                 '--location "eastus"',
                 checks=[])

        self.cmd('az machinelearningservices  list',
                 checks=[])

        self.cmd('az machinelearningservices workspace list',
                 checks=[])

        self.cmd('az machinelearningservices private-endpoint-connection put '
                 '--private-endpoint-connection-name "{{privateEndpointConnectionName}}" '
                 '--properties-private-link-service-connection-state description=Auto-Approved status=Approved '
                 '--resource-group "{rg_6}" '
                 '--workspace-name "{Workspaces_2}"',
                 checks=[])

        self.cmd('az machinelearningservices machine-learning-compute list-node '
                 '--compute-name "compute123" '
                 '--resource-group "{rg_3}" '
                 '--workspace-name "{Workspaces_4}"',
                 checks=[])

        self.cmd('az machinelearningservices machine-learning-compute list-key '
                 '--compute-name "compute123" '
                 '--resource-group "{rg_3}" '
                 '--workspace-name "{Workspaces_4}"',
                 checks=[])

        self.cmd('az machinelearningservices machine-learning-compute update '
                 '--compute-name "compute123" '
                 '--properties-scale-settings max-node-count=4 min-node-count=4 node-idle-time-before-scale-down=PT5M '
                 '--resource-group "{rg_3}" '
                 '--workspace-name "{Workspaces_4}"',
                 checks=[])

        self.cmd('az machinelearningservices linked-workspace update '
                 '--link-name "link-12" '
                 '--user-assigned-identity-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg_4}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/uai124" '
                 '--resource-group "{rg_5}" '
                 '--workspace-name "{Workspaces_3}"',
                 checks=[])

        self.cmd('az machinelearningservices workspace resync-key '
                 '--resource-group "{rg_3}" '
                 '--workspace-name "{Workspaces_4}"',
                 checks=[])

        self.cmd('az machinelearningservices workspace list-key '
                 '--resource-group "{rg_3}" '
                 '--workspace-name "{Workspaces_4}"',
                 checks=[])

        self.cmd('az machinelearningservices workspace update '
                 '--properties-description "new description" '
                 '--properties-friendly-name "New friendly name" '
                 '--sku name=Enterprise tier=Enterprise '
                 '--resource-group "{rg}" '
                 '--workspace-name "{Workspaces_2}"',
                 checks=[])

        self.cmd('az machinelearningservices quota update '
                 '--location "eastus" '
                 '--value type=Microsoft.MachineLearningServices/workspaces/quotas id=/subscriptions/{subscription_id}/resourceGroups/{rg_8}/providers/Microsoft.MachineLearningServices/workspaces/{Workspaces_5}/quotas/{Standard_DSv2_Family_Cluster_Dedicated_vCPUs} limit=100 unit=Count '
                 '--value type=Microsoft.MachineLearningServices/workspaces/quotas id=/subscriptions/{subscription_id}/resourceGroups/{rg_8}/providers/Microsoft.MachineLearningServices/workspaces/{Workspaces_6}/quotas/{Standard_DSv2_Family_Cluster_Dedicated_vCPUs} limit=200 unit=Count',
                 checks=[])

        self.cmd('az machinelearningservices private-endpoint-connection delete '
                 '--private-endpoint-connection-name "{{privateEndpointConnectionName}}" '
                 '--resource-group "{rg_6}" '
                 '--workspace-name "{Workspaces_2}"',
                 checks=[])

        self.cmd('az machinelearningservices machine-learning-compute delete '
                 '--compute-name "compute123" '
                 '--resource-group "{rg_3}" '
                 '--underlying-resource-action "Delete" '
                 '--workspace-name "{Workspaces_4}"',
                 checks=[])

        self.cmd('az machinelearningservices linked-workspace delete '
                 '--link-name "link-12" '
                 '--resource-group "{rg_5}" '
                 '--workspace-name "{Workspaces_3}"',
                 checks=[])

        self.cmd('az machinelearningservices workspace delete '
                 '--resource-group "{rg}" '
                 '--workspace-name "{Workspaces_2}"',
                 checks=[])
