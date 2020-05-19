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

from knack.help_files import helps


helps['machinelearningservices workspace'] = """
    type: group
    short-summary: machinelearningservices workspace
"""

helps['machinelearningservices workspace list'] = """
    type: command
    short-summary: Lists all the available machine learning workspaces under the specified subscription.
    examples:
      - name: Get Workspaces by Resource Group
        text: |-
               az machinelearningservices workspace list --resource-group "workspace-1234"
"""

helps['machinelearningservices workspace show'] = """
    type: command
    short-summary: Gets the properties of the specified machine learning workspace.
    examples:
      - name: Get Workspace
        text: |-
               az machinelearningservices workspace show --resource-group "workspace-1234" --workspace-name "testworksp\
ace"
"""

helps['machinelearningservices workspace create'] = """
    type: command
    short-summary: Creates or updates a workspace with the specified parameters.
    examples:
      - name: Create Workspace
        text: |-
               az machinelearningservices workspace create --location "eastus2euap" --description "test description" --\
application-insights "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/workspace-1234/providers/micro\
soft.insights/components/testinsights" --container-registry "/subscriptions/00000000-1111-2222-3333-444444444444/resour\
ceGroups/workspace-1234/providers/Microsoft.ContainerRegistry/registries/testRegistry" --encryption-key-vault-propertie\
s identity-client-id="" key-identifier="https://testkv.vault.azure.net/keys/testkey/aabbccddee112233445566778899aabb" k\
ey-vault-arm-id="/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/workspace-1234/providers/Microsoft.\
KeyVault/vaults/testkv" --encryption-status "Enabled" --friendly-name "HelloName" --hbi-workspace false --key-vault "/s\
ubscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/workspace-1234/providers/Microsoft.KeyVault/vaults/tes\
tkv" --shared-private-link-resources name="testdbresource" private-link-resource-id="/subscriptions/00000000-1111-2222-\
3333-444444444444/resourceGroups/workspace-1234/providers/Microsoft.DocumentDB/databaseAccounts/testdbresource/privateL\
inkResources/Sql" group-id="Sql" request-message="Please approve" status="Approved" --storage-account "/subscriptions/0\
0000000-1111-2222-3333-444444444444/resourceGroups/accountcrud-1234/providers/Microsoft.Storage/storageAccounts/testSto\
rageAccount" --sku name="Basic" tier="Basic" --resource-group "workspace-1234" --workspace-name "testworkspace"
"""

helps['machinelearningservices workspace update'] = """
    type: command
    short-summary: Updates a machine learning workspace with the specified parameters.
    examples:
      - name: Update Workspace
        text: |-
               az machinelearningservices workspace update --description "new description" --friendly-name "New friendl\
y name" --sku name="Enterprise" tier="Enterprise" --resource-group "workspace-1234" --workspace-name "testworkspace"
"""

helps['machinelearningservices workspace delete'] = """
    type: command
    short-summary: Deletes a machine learning workspace.
    examples:
      - name: Delete Workspace
        text: |-
               az machinelearningservices workspace delete --resource-group "workspace-1234" --workspace-name "testwork\
space"
"""

helps['machinelearningservices workspace list-key'] = """
    type: command
    short-summary: Lists all the keys associated with this workspace. This includes keys for the storage account, app i\
nsights and password for container registry
    examples:
      - name: List Workspace Keys
        text: |-
               az machinelearningservices workspace list-key --resource-group "testrg123" --workspace-name "workspaces1\
23"
"""

helps['machinelearningservices workspace resync-key'] = """
    type: command
    short-summary: Resync all the keys associated with this workspace. This includes keys for the storage account, app \
insights and password for container registry
    examples:
      - name: Resync Workspace Keys
        text: |-
               az machinelearningservices workspace resync-key --resource-group "testrg123" --workspace-name "workspace\
s123"
"""

helps['machinelearningservices workspace-feature'] = """
    type: group
    short-summary: machinelearningservices workspace-feature
"""

helps['machinelearningservices workspace-feature list'] = """
    type: command
    short-summary: Lists all enabled features for a workspace
    examples:
      - name: List Workspace features
        text: |-
               az machinelearningservices workspace-feature list --resource-group "myResourceGroup" --workspace-name "t\
estworkspace"
"""

helps['machinelearningservices usage'] = """
    type: group
    short-summary: machinelearningservices usage
"""

helps['machinelearningservices usage list'] = """
    type: command
    short-summary: Gets the current usage information as well as limits for AML resources for given subscription and lo\
cation.
    examples:
      - name: List Usages
        text: |-
               az machinelearningservices usage list --location "eastus"
"""

helps['machinelearningservices virtual-machine-size'] = """
    type: group
    short-summary: machinelearningservices virtual-machine-size
"""

helps['machinelearningservices virtual-machine-size list'] = """
    type: command
    short-summary: Returns supported VM Sizes in a location
    examples:
      - name: List VM Sizes
        text: |-
               az machinelearningservices virtual-machine-size list --location "eastus"
"""

helps['machinelearningservices quota'] = """
    type: group
    short-summary: machinelearningservices quota
"""

helps['machinelearningservices quota list'] = """
    type: command
    short-summary: Gets the currently assigned Workspace Quotas based on VMFamily.
    examples:
      - name: List workspace quotas by VMFamily
        text: |-
               az machinelearningservices quota list --location "eastus"
"""

helps['machinelearningservices quota update'] = """
    type: command
    short-summary: Update quota for each VM family in workspace.
    examples:
      - name: update quotas
        text: |-
               az machinelearningservices quota update --location "eastus" --value type="Microsoft.MachineLearningServi\
ces/workspaces/dedicatedCores/quotas" id="/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg/provide\
rs/Microsoft.MachineLearningServices/workspaces/demo_workspace1/quotas/StandardDSv2Family" limit=100 unit="Count" --val\
ue type="Microsoft.MachineLearningServices/workspaces/dedicatedCores/quotas" id="/subscriptions/00000000-0000-0000-0000\
-000000000000/resourceGroups/rg/providers/Microsoft.MachineLearningServices/workspaces/demo_workspace2/quotas/StandardD\
Sv2Family" limit=200 unit="Count"
"""

helps['machinelearningservices machine-learning-compute'] = """
    type: group
    short-summary: machinelearningservices machine-learning-compute
"""

helps['machinelearningservices machine-learning-compute list'] = """
    type: command
    short-summary: Gets computes in specified workspace.
    examples:
      - name: Get Computes
        text: |-
               az machinelearningservices machine-learning-compute list --resource-group "testrg123" --workspace-name "\
workspaces123"
"""

helps['machinelearningservices machine-learning-compute show'] = """
    type: command
    short-summary: Gets compute definition by its name. Any secrets (storage keys, service credentials, etc) are not re\
turned - use 'keys' nested resource to get them.
    examples:
      - name: Get a AKS Compute
        text: |-
               az machinelearningservices machine-learning-compute show --compute-name "compute123" --resource-group "t\
estrg123" --workspace-name "workspaces123"
      - name: Get a AML Compute
        text: |-
               az machinelearningservices machine-learning-compute show --compute-name "compute123" --resource-group "t\
estrg123" --workspace-name "workspaces123"
"""

helps['machinelearningservices machine-learning-compute aks'] = """
    type: group
    short-summary: machinelearningservices machine-learning-compute sub group aks
"""

helps['machinelearningservices machine-learning-compute aks create'] = """
    type: command
    short-summary: Creates or updates compute. This call will overwrite a compute if it exists. This is a nonrecoverabl\
e operation. If your intent is to create a new compute, do a GET first to verify that it does not exist yet.
    examples:
      - name: Create AKS Compute
        text: |-
               az machinelearningservices machine-learning-compute aks create --compute-name "compute123" --location "e\
astus" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Create a AML Compute
        text: |-
               az machinelearningservices machine-learning-compute aks create --compute-name "compute123" --identity-ty\
pe "SystemAssigned, UserAssigned" --identity-user-assigned-identities "{\\"/subscriptions/00000000-0000-0000-0000-00000\
0000000/resourceGroups/myResourceGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/identity-name\\":{}}"\
 --location "eastus" --aks-properties "{\\"osType\\":\\"Windows\\",\\"remoteLoginPortPublicAccess\\":\\"NotSpecified\\"\
,\\"scaleSettings\\":{\\"maxNodeCount\\":1,\\"minNodeCount\\":0,\\"nodeIdleTimeBeforeScaleDown\\":\\"PT5M\\"},\\"virtua\
lMachineImage\\":{\\"id\\":\\"/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResourceGroup/provid\
ers/Microsoft.Compute/galleries/myImageGallery/images/myImageDefinition/versions/0.0.1\\"},\\"vmPriority\\":\\"Dedicate\
d\\",\\"vmSize\\":\\"STANDARD_NC6\\"}" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Create a DataFactory Compute
        text: |-
               az machinelearningservices machine-learning-compute aks create --compute-name "compute123" --location "e\
astus" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Update a AKS Compute
        text: |-
               az machinelearningservices machine-learning-compute aks create --compute-name "compute123" --location "e\
astus" --description "some compute" --aks-properties "{\\"agentCount\\":4}" --resource-id "/subscriptions/34adfa4f-cedf\
-4dc0-ba29-b6d1a69ab345/resourcegroups/testrg123/providers/Microsoft.ContainerService/managedClusters/compute123-56826-\
c9b00420020b2" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Update a AML Compute
        text: |-
               az machinelearningservices machine-learning-compute aks create --compute-name "compute123" --identity-ty\
pe "SystemAssigned, UserAssigned" --identity-user-assigned-identities "{\\"/subscriptions/00000000-0000-0000-0000-00000\
0000000/resourceGroups/myResourceGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/identity-name\\":{}}"\
 --location "eastus" --aks-properties "{\\"scaleSettings\\":{\\"maxNodeCount\\":1,\\"minNodeCount\\":0,\\"nodeIdleTimeB\
eforeScaleDown\\":\\"PT5M\\"}}" --resource-group "testrg123" --workspace-name "workspaces123"
"""

helps['machinelearningservices machine-learning-compute aml-compute'] = """
    type: group
    short-summary: machinelearningservices machine-learning-compute sub group aml-compute
"""

helps['machinelearningservices machine-learning-compute aml-compute create'] = """
    type: command
    short-summary: Creates or updates compute. This call will overwrite a compute if it exists. This is a nonrecoverabl\
e operation. If your intent is to create a new compute, do a GET first to verify that it does not exist yet.
    examples:
      - name: Create AKS Compute
        text: |-
               az machinelearningservices machine-learning-compute aml-compute create --compute-name "compute123" --loc\
ation "eastus" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Create a AML Compute
        text: |-
               az machinelearningservices machine-learning-compute aml-compute create --compute-name "compute123" --ide\
ntity-type "SystemAssigned, UserAssigned" --identity-user-assigned-identities "{\\"/subscriptions/00000000-0000-0000-00\
00-000000000000/resourceGroups/myResourceGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/identity-name\
\\":{}}" --location "eastus" --aml-compute-properties "{\\"osType\\":\\"Windows\\",\\"remoteLoginPortPublicAccess\\":\\\
"NotSpecified\\",\\"scaleSettings\\":{\\"maxNodeCount\\":1,\\"minNodeCount\\":0,\\"nodeIdleTimeBeforeScaleDown\\":\\"PT\
5M\\"},\\"virtualMachineImage\\":{\\"id\\":\\"/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myReso\
urceGroup/providers/Microsoft.Compute/galleries/myImageGallery/images/myImageDefinition/versions/0.0.1\\"},\\"vmPriorit\
y\\":\\"Dedicated\\",\\"vmSize\\":\\"STANDARD_NC6\\"}" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Create a DataFactory Compute
        text: |-
               az machinelearningservices machine-learning-compute aml-compute create --compute-name "compute123" --loc\
ation "eastus" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Update a AKS Compute
        text: |-
               az machinelearningservices machine-learning-compute aml-compute create --compute-name "compute123" --loc\
ation "eastus" --description "some compute" --aml-compute-properties "{\\"agentCount\\":4}" --resource-id "/subscriptio\
ns/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourcegroups/testrg123/providers/Microsoft.ContainerService/managedClusters/c\
ompute123-56826-c9b00420020b2" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Update a AML Compute
        text: |-
               az machinelearningservices machine-learning-compute aml-compute create --compute-name "compute123" --ide\
ntity-type "SystemAssigned, UserAssigned" --identity-user-assigned-identities "{\\"/subscriptions/00000000-0000-0000-00\
00-000000000000/resourceGroups/myResourceGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/identity-name\
\\":{}}" --location "eastus" --aml-compute-properties "{\\"scaleSettings\\":{\\"maxNodeCount\\":1,\\"minNodeCount\\":0,\
\\"nodeIdleTimeBeforeScaleDown\\":\\"PT5M\\"}}" --resource-group "testrg123" --workspace-name "workspaces123"
"""

helps['machinelearningservices machine-learning-compute data-factory'] = """
    type: group
    short-summary: machinelearningservices machine-learning-compute sub group data-factory
"""

helps['machinelearningservices machine-learning-compute data-factory create'] = """
    type: command
    short-summary: Creates or updates compute. This call will overwrite a compute if it exists. This is a nonrecoverabl\
e operation. If your intent is to create a new compute, do a GET first to verify that it does not exist yet.
    examples:
      - name: Create AKS Compute
        text: |-
               az machinelearningservices machine-learning-compute data-factory create --compute-name "compute123" --lo\
cation "eastus" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Create a AML Compute
        text: |-
               az machinelearningservices machine-learning-compute data-factory create --compute-name "compute123" --id\
entity-type "SystemAssigned, UserAssigned" --identity-user-assigned-identities "{\\"/subscriptions/00000000-0000-0000-0\
000-000000000000/resourceGroups/myResourceGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/identity-nam\
e\\":{}}" --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Create a DataFactory Compute
        text: |-
               az machinelearningservices machine-learning-compute data-factory create --compute-name "compute123" --lo\
cation "eastus" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Update a AKS Compute
        text: |-
               az machinelearningservices machine-learning-compute data-factory create --compute-name "compute123" --lo\
cation "eastus" --description "some compute" --resource-id "/subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourc\
egroups/testrg123/providers/Microsoft.ContainerService/managedClusters/compute123-56826-c9b00420020b2" --resource-group\
 "testrg123" --workspace-name "workspaces123"
      - name: Update a AML Compute
        text: |-
               az machinelearningservices machine-learning-compute data-factory create --compute-name "compute123" --id\
entity-type "SystemAssigned, UserAssigned" --identity-user-assigned-identities "{\\"/subscriptions/00000000-0000-0000-0\
000-000000000000/resourceGroups/myResourceGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/identity-nam\
e\\":{}}" --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123"
"""

helps['machinelearningservices machine-learning-compute data-lake-analytics'] = """
    type: group
    short-summary: machinelearningservices machine-learning-compute sub group data-lake-analytics
"""

helps['machinelearningservices machine-learning-compute data-lake-analytics create'] = """
    type: command
    short-summary: Creates or updates compute. This call will overwrite a compute if it exists. This is a nonrecoverabl\
e operation. If your intent is to create a new compute, do a GET first to verify that it does not exist yet.
    examples:
      - name: Create AKS Compute
        text: |-
               az machinelearningservices machine-learning-compute data-lake-analytics create --compute-name "compute12\
3" --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Create a AML Compute
        text: |-
               az machinelearningservices machine-learning-compute data-lake-analytics create --compute-name "compute12\
3" --identity-type "SystemAssigned, UserAssigned" --identity-user-assigned-identities "{\\"/subscriptions/00000000-0000\
-0000-0000-000000000000/resourceGroups/myResourceGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/ident\
ity-name\\":{}}" --location "eastus" --data-lake-analytics-properties osType="Windows" remoteLoginPortPublicAccess="Not\
Specified" scaleSettings={"maxNodeCount":1,"minNodeCount":0,"nodeIdleTimeBeforeScaleDown":"PT5M"} virtualMachineImage={\
"id":"/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResourceGroup/providers/Microsoft.Compute/ga\
lleries/myImageGallery/images/myImageDefinition/versions/0.0.1"} vmPriority="Dedicated" vmSize="STANDARD_NC6" --resourc\
e-group "testrg123" --workspace-name "workspaces123"
      - name: Create a DataFactory Compute
        text: |-
               az machinelearningservices machine-learning-compute data-lake-analytics create --compute-name "compute12\
3" --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Update a AKS Compute
        text: |-
               az machinelearningservices machine-learning-compute data-lake-analytics create --compute-name "compute12\
3" --location "eastus" --description "some compute" --data-lake-analytics-properties agentCount=4 --resource-id "/subsc\
riptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourcegroups/testrg123/providers/Microsoft.ContainerService/managedClus\
ters/compute123-56826-c9b00420020b2" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Update a AML Compute
        text: |-
               az machinelearningservices machine-learning-compute data-lake-analytics create --compute-name "compute12\
3" --identity-type "SystemAssigned, UserAssigned" --identity-user-assigned-identities "{\\"/subscriptions/00000000-0000\
-0000-0000-000000000000/resourceGroups/myResourceGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/ident\
ity-name\\":{}}" --location "eastus" --data-lake-analytics-properties scaleSettings={"maxNodeCount":1,"minNodeCount":0,\
"nodeIdleTimeBeforeScaleDown":"PT5M"} --resource-group "testrg123" --workspace-name "workspaces123"
"""

helps['machinelearningservices machine-learning-compute databricks'] = """
    type: group
    short-summary: machinelearningservices machine-learning-compute sub group databricks
"""

helps['machinelearningservices machine-learning-compute databricks create'] = """
    type: command
    short-summary: Creates or updates compute. This call will overwrite a compute if it exists. This is a nonrecoverabl\
e operation. If your intent is to create a new compute, do a GET first to verify that it does not exist yet.
    examples:
      - name: Create AKS Compute
        text: |-
               az machinelearningservices machine-learning-compute databricks create --compute-name "compute123" --loca\
tion "eastus" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Create a AML Compute
        text: |-
               az machinelearningservices machine-learning-compute databricks create --compute-name "compute123" --iden\
tity-type "SystemAssigned, UserAssigned" --identity-user-assigned-identities "{\\"/subscriptions/00000000-0000-0000-000\
0-000000000000/resourceGroups/myResourceGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/identity-name\
\\":{}}" --location "eastus" --databricks-properties osType="Windows" remoteLoginPortPublicAccess="NotSpecified" scaleS\
ettings={"maxNodeCount":1,"minNodeCount":0,"nodeIdleTimeBeforeScaleDown":"PT5M"} virtualMachineImage={"id":"/subscripti\
ons/00000000-0000-0000-0000-000000000000/resourceGroups/myResourceGroup/providers/Microsoft.Compute/galleries/myImageGa\
llery/images/myImageDefinition/versions/0.0.1"} vmPriority="Dedicated" vmSize="STANDARD_NC6" --resource-group "testrg12\
3" --workspace-name "workspaces123"
      - name: Create a DataFactory Compute
        text: |-
               az machinelearningservices machine-learning-compute databricks create --compute-name "compute123" --loca\
tion "eastus" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Update a AKS Compute
        text: |-
               az machinelearningservices machine-learning-compute databricks create --compute-name "compute123" --loca\
tion "eastus" --description "some compute" --databricks-properties agentCount=4 --resource-id "/subscriptions/34adfa4f-\
cedf-4dc0-ba29-b6d1a69ab345/resourcegroups/testrg123/providers/Microsoft.ContainerService/managedClusters/compute123-56\
826-c9b00420020b2" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Update a AML Compute
        text: |-
               az machinelearningservices machine-learning-compute databricks create --compute-name "compute123" --iden\
tity-type "SystemAssigned, UserAssigned" --identity-user-assigned-identities "{\\"/subscriptions/00000000-0000-0000-000\
0-000000000000/resourceGroups/myResourceGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/identity-name\
\\":{}}" --location "eastus" --databricks-properties scaleSettings={"maxNodeCount":1,"minNodeCount":0,"nodeIdleTimeBefo\
reScaleDown":"PT5M"} --resource-group "testrg123" --workspace-name "workspaces123"
"""

helps['machinelearningservices machine-learning-compute hd-insight'] = """
    type: group
    short-summary: machinelearningservices machine-learning-compute sub group hd-insight
"""

helps['machinelearningservices machine-learning-compute hd-insight create'] = """
    type: command
    short-summary: Creates or updates compute. This call will overwrite a compute if it exists. This is a nonrecoverabl\
e operation. If your intent is to create a new compute, do a GET first to verify that it does not exist yet.
    examples:
      - name: Create AKS Compute
        text: |-
               az machinelearningservices machine-learning-compute hd-insight create --compute-name "compute123" --loca\
tion "eastus" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Create a AML Compute
        text: |-
               az machinelearningservices machine-learning-compute hd-insight create --compute-name "compute123" --iden\
tity-type "SystemAssigned, UserAssigned" --identity-user-assigned-identities "{\\"/subscriptions/00000000-0000-0000-000\
0-000000000000/resourceGroups/myResourceGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/identity-name\
\\":{}}" --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Create a DataFactory Compute
        text: |-
               az machinelearningservices machine-learning-compute hd-insight create --compute-name "compute123" --loca\
tion "eastus" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Update a AKS Compute
        text: |-
               az machinelearningservices machine-learning-compute hd-insight create --compute-name "compute123" --loca\
tion "eastus" --description "some compute" --resource-id "/subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourceg\
roups/testrg123/providers/Microsoft.ContainerService/managedClusters/compute123-56826-c9b00420020b2" --resource-group "\
testrg123" --workspace-name "workspaces123"
      - name: Update a AML Compute
        text: |-
               az machinelearningservices machine-learning-compute hd-insight create --compute-name "compute123" --iden\
tity-type "SystemAssigned, UserAssigned" --identity-user-assigned-identities "{\\"/subscriptions/00000000-0000-0000-000\
0-000000000000/resourceGroups/myResourceGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/identity-name\
\\":{}}" --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123"
"""

helps['machinelearningservices machine-learning-compute virtual-machine'] = """
    type: group
    short-summary: machinelearningservices machine-learning-compute sub group virtual-machine
"""

helps['machinelearningservices machine-learning-compute virtual-machine create'] = """
    type: command
    short-summary: Creates or updates compute. This call will overwrite a compute if it exists. This is a nonrecoverabl\
e operation. If your intent is to create a new compute, do a GET first to verify that it does not exist yet.
    examples:
      - name: Create AKS Compute
        text: |-
               az machinelearningservices machine-learning-compute virtual-machine create --compute-name "compute123" -\
-location "eastus" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Create a AML Compute
        text: |-
               az machinelearningservices machine-learning-compute virtual-machine create --compute-name "compute123" -\
-identity-type "SystemAssigned, UserAssigned" --identity-user-assigned-identities "{\\"/subscriptions/00000000-0000-000\
0-0000-000000000000/resourceGroups/myResourceGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/identity-\
name\\":{}}" --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Create a DataFactory Compute
        text: |-
               az machinelearningservices machine-learning-compute virtual-machine create --compute-name "compute123" -\
-location "eastus" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Update a AKS Compute
        text: |-
               az machinelearningservices machine-learning-compute virtual-machine create --compute-name "compute123" -\
-location "eastus" --description "some compute" --resource-id "/subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/reso\
urcegroups/testrg123/providers/Microsoft.ContainerService/managedClusters/compute123-56826-c9b00420020b2" --resource-gr\
oup "testrg123" --workspace-name "workspaces123"
      - name: Update a AML Compute
        text: |-
               az machinelearningservices machine-learning-compute virtual-machine create --compute-name "compute123" -\
-identity-type "SystemAssigned, UserAssigned" --identity-user-assigned-identities "{\\"/subscriptions/00000000-0000-000\
0-0000-000000000000/resourceGroups/myResourceGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/identity-\
name\\":{}}" --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123"
"""

helps['machinelearningservices machine-learning-compute update'] = """
    type: command
    short-summary: Updates properties of a compute. This call will overwrite a compute if it exists. This is a nonrecov\
erable operation.
    examples:
      - name: Update a AmlCompute Compute
        text: |-
               az machinelearningservices machine-learning-compute update --compute-name "compute123" --scale-settings \
max-node-count=4 min-node-count=4 node-idle-time-before-scale-down="PT5M" --resource-group "testrg123" --workspace-name\
 "workspaces123"
"""

helps['machinelearningservices machine-learning-compute delete'] = """
    type: command
    short-summary: Deletes specified Machine Learning compute.
    examples:
      - name: Delete Compute
        text: |-
               az machinelearningservices machine-learning-compute delete --compute-name "compute123" --resource-group \
"testrg123" --underlying-resource-action "Delete" --workspace-name "workspaces123"
"""

helps['machinelearningservices machine-learning-compute list-key'] = """
    type: command
    short-summary: Gets secrets related to Machine Learning compute (storage keys, service credentials, etc).
    examples:
      - name: List AKS Compute Keys
        text: |-
               az machinelearningservices machine-learning-compute list-key --compute-name "compute123" --resource-grou\
p "testrg123" --workspace-name "workspaces123"
"""

helps['machinelearningservices machine-learning-compute list-node'] = """
    type: command
    short-summary: Get the details (e.g IP address, port etc) of all the compute nodes in the compute.
    examples:
      - name: Get compute nodes information for a compute
        text: |-
               az machinelearningservices machine-learning-compute list-node --compute-name "compute123" --resource-gro\
up "testrg123" --workspace-name "workspaces123"
"""

helps['machinelearningservices '] = """
    type: group
    short-summary: machinelearningservices 
"""

helps['machinelearningservices  list-sku'] = """
    type: command
    short-summary: Lists all skus with associated features
    examples:
      - name: List Skus
        text: |-
               az machinelearningservices  list-sku
"""

helps['machinelearningservices private-endpoint-connection'] = """
    type: group
    short-summary: machinelearningservices private-endpoint-connection
"""

helps['machinelearningservices private-endpoint-connection show'] = """
    type: command
    short-summary: Gets the specified private endpoint connection associated with the workspace.
    examples:
      - name: WorkspaceGetPrivateEndpointConnection
        text: |-
               az machinelearningservices private-endpoint-connection show --private-endpoint-connection-name "{private\
EndpointConnectionName}" --resource-group "rg-1234" --workspace-name "testworkspace"
"""

helps['machinelearningservices private-endpoint-connection delete'] = """
    type: command
    short-summary: Deletes the specified private endpoint connection associated with the workspace.
    examples:
      - name: WorkspaceDeletePrivateEndpointConnection
        text: |-
               az machinelearningservices private-endpoint-connection delete --private-endpoint-connection-name "{priva\
teEndpointConnectionName}" --resource-group "rg-1234" --workspace-name "testworkspace"
"""

helps['machinelearningservices private-endpoint-connection put'] = """
    type: command
    short-summary: Update the state of specified private endpoint connection associated with the workspace.
    examples:
      - name: WorkspacePutPrivateEndpointConnection
        text: |-
               az machinelearningservices private-endpoint-connection put --private-endpoint-connection-name "{privateE\
ndpointConnectionName}" --private-link-service-connection-state description="Auto-Approved" status="Approved" --resourc\
e-group "rg-1234" --workspace-name "testworkspace"
"""

helps['machinelearningservices private-link-resource'] = """
    type: group
    short-summary: machinelearningservices private-link-resource
"""

helps['machinelearningservices private-link-resource list'] = """
    type: command
    short-summary: Gets the private link resources that need to be created for a workspace.
    examples:
      - name: WorkspaceListPrivateLinkResources
        text: |-
               az machinelearningservices private-link-resource list --resource-group "rg-1234" --workspace-name "testw\
orkspace"
"""
