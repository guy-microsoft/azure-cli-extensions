# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
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
               az machinelearningservices workspace show --resource-group "workspace-1234"
               --workspace-name "testworkspace"
"""

helps['machinelearningservices workspace create'] = """
    type: command
    short-summary: Creates or updates a workspace with the specified parameters.
    examples:
      - name: Create Workspace
        text: |-
               az machinelearningservices workspace create --location "eastus2euap"
               --properties-description "test description" --properties-application-insights "/subscripti
               ons/00000000-1111-2222-3333-444444444444/resourceGroups/workspace-1234/providers/microsoft
               .insights/components/testinsights" --properties-container-registry "/subscriptions/0000000
               0-1111-2222-3333-444444444444/resourceGroups/workspace-1234/providers/Microsoft.ContainerR
               egistry/registries/testRegistry" --properties-encryption "{\\"keyVaultProperties\\":{\\"ident
               ityClientId\\":\\"\\",\\"keyIdentifier\\":\\"https://testkv.vault.azure.net/keys/testkey/aabbccd
               dee112233445566778899aabb\\",\\"keyVaultArmId\\":\\"/subscriptions/00000000-1111-2222-3333-444
               444444444/resourceGroups/workspace-1234/providers/Microsoft.KeyVault/vaults/testkv\\"},\\"st
               atus\\":\\"Enabled\\"}" --properties-friendly-name "HelloName" --properties-hbi-workspace
               false --properties-key-vault "/subscriptions/00000000-1111-2222-3333-444444444444/resource
               Groups/workspace-1234/providers/Microsoft.KeyVault/vaults/testkv"
               --properties-shared-private-link-resources name=testdbresource properties=[object Object]
               --properties-storage-account "/subscriptions/00000000-1111-2222-3333-444444444444/resource
               Groups/accountcrud-1234/providers/Microsoft.Storage/storageAccounts/testStorageAccount"
               --sku name=Basic tier=Basic --resource-group "workspace-1234" --workspace-name
               "testworkspace"
"""

helps['machinelearningservices workspace update'] = """
    type: command
    short-summary: Updates a machine learning workspace with the specified parameters.
    examples:
      - name: Update Workspace
        text: |-
               az machinelearningservices workspace update --properties-description "new description"
               --properties-friendly-name "New friendly name" --sku name=Enterprise tier=Enterprise
               --resource-group "workspace-1234" --workspace-name "testworkspace"
"""

helps['machinelearningservices workspace delete'] = """
    type: command
    short-summary: Deletes a machine learning workspace.
    examples:
      - name: Delete Workspace
        text: |-
               az machinelearningservices workspace delete --resource-group "workspace-1234"
               --workspace-name "testworkspace"
"""

helps['machinelearningservices workspace list-key'] = """
    type: command
    short-summary: Lists all the keys associated with this workspace. This includes keys for the storage account, app insights and password for container registry
    examples:
      - name: List Workspace Keys
        text: |-
               az machinelearningservices workspace list-key --resource-group "testrg123"
               --workspace-name "workspaces123"
"""

helps['machinelearningservices workspace resync-key'] = """
    type: command
    short-summary: Resync all the keys associated with this workspace. This includes keys for the storage account, app insights and password for container registry
    examples:
      - name: Resync Workspace Keys
        text: |-
               az machinelearningservices workspace resync-key --resource-group "testrg123"
               --workspace-name "workspaces123"
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
               az machinelearningservices workspace-feature list --resource-group "myResourceGroup"
               --workspace-name "testworkspace"
"""

helps['machinelearningservices usage'] = """
    type: group
    short-summary: machinelearningservices usage
"""

helps['machinelearningservices usage list'] = """
    type: command
    short-summary: Gets the current usage information as well as limits for AML resources for given subscription and location.
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
               az machinelearningservices quota update --location "eastus" --value type=Microsoft.Machine\\
               LearningServices/workspaces/quotas id=/subscriptions/00000000-0000-0000-0000-000000000000/\\
               resourceGroups/rg/providers/Microsoft.MachineLearningServices/workspaces/demo_workspace1/q\\
               uotas/Standard_DSv2_Family_Cluster_Dedicated_vCPUs limit=100 unit=Count --value type=Micro\\
               soft.MachineLearningServices/workspaces/quotas id=/subscriptions/00000000-0000-0000-0000-0\\
               00000000000/resourceGroups/rg/providers/Microsoft.MachineLearningServices/workspaces/demo_\\
               workspace2/quotas/Standard_DSv2_Family_Cluster_Dedicated_vCPUs limit=200 unit=Count
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
               az machinelearningservices machine-learning-compute list --resource-group "testrg123"
               --workspace-name "workspaces123"
"""

helps['machinelearningservices machine-learning-compute show'] = """
    type: command
    short-summary: Gets compute definition by its name. Any secrets (storage keys, service credentials, etc) are not returned - use 'keys' nested resource to get them.
    examples:
      - name: Get a AKS Compute
        text: |-
               az machinelearningservices machine-learning-compute show --compute-name "compute123"
               --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Get a AML Compute
        text: |-
               az machinelearningservices machine-learning-compute show --compute-name "compute123"
               --resource-group "testrg123" --workspace-name "workspaces123"
"""

helps['machinelearningservices machine-learning-compute create'] = """
    type: command
    short-summary: Creates or updates compute. This call will overwrite a compute if it exists. This is a nonrecoverable operation. If your intent is to create a new compute, do a GET first to verify that it does not exist yet.
    examples:
      - name: Create AKS Compute
        text: |-
               az machinelearningservices machine-learning-compute create --compute-name "compute123"
               --location "eastus" --properties "{\\"computeType\\":\\"AKS\\"}" --resource-group "testrg123"
               --workspace-name "workspaces123"
      - name: Create a AML Compute
        text: |-
               az machinelearningservices machine-learning-compute create --compute-name "compute123"
               --location "eastus" --properties "{\\"computeType\\":\\"AmlCompute\\",\\"properties\\":{\\"remote
               LoginPortPublicAccess\\":\\"NotSpecified\\",\\"scaleSettings\\":{\\"maxNodeCount\\":1,\\"minNodeCo
               unt\\":0,\\"nodeIdleTimeBeforeScaleDown\\":\\"PT5M\\"},\\"vmPriority\\":\\"Dedicated\\",\\"vmSize\\":
               \\"STANDARD_NC6\\"}}" --resource-group "testrg123" --workspace-name "workspaces123"
      - name: Create a DataFactory Compute
        text: |-
               az machinelearningservices machine-learning-compute create --compute-name "compute123"
               --location "eastus" --properties "{\\"computeType\\":\\"DataFactory\\"}" --resource-group
               "testrg123" --workspace-name "workspaces123"
      - name: Update a AKS Compute
        text: |-
               az machinelearningservices machine-learning-compute create --compute-name "compute123"
               --location "eastus" --properties "{\\"description\\":\\"some compute\\",\\"computeType\\":\\"AKS\\
               ",\\"properties\\":{\\"agentCount\\":4},\\"resourceId\\":\\"/subscriptions/34adfa4f-cedf-4dc0-ba2
               9-b6d1a69ab345/resourcegroups/testrg123/providers/Microsoft.ContainerService/managedCluste
               rs/compute123-56826-c9b00420020b2\\"}" --resource-group "testrg123" --workspace-name
               "workspaces123"
      - name: Update a AML Compute
        text: |-
               az machinelearningservices machine-learning-compute create --compute-name "compute123"
               --location "eastus" --properties "{\\"computeType\\":\\"AmlCompute\\",\\"properties\\":{\\"descri
               ption\\":\\"some compute\\",\\"computeType\\":\\"AmlCompute\\",\\"properties\\":{\\"scaleSettings\\":
               {\\"maxNodeCount\\":4,\\"minNodeCount\\":4,\\"nodeIdleTimeBeforeScaleDown\\":\\"PT5M\\"}}}}"
               --resource-group "testrg123" --workspace-name "workspaces123"
"""

helps['machinelearningservices machine-learning-compute update'] = """
    type: command
    short-summary: Updates properties of a compute. This call will overwrite a compute if it exists. This is a nonrecoverable operation.
    examples:
      - name: Update a AmlCompute Compute
        text: |-
               az machinelearningservices machine-learning-compute update --compute-name "compute123"
               --properties-scale-settings
               max-node-count=4 min-node-count=4 node-idle-time-before-scale-down=PT5M --resource-group
               "testrg123" --workspace-name "workspaces123"
"""

helps['machinelearningservices machine-learning-compute delete'] = """
    type: command
    short-summary: Deletes specified Machine Learning compute.
    examples:
      - name: Delete Compute
        text: |-
               az machinelearningservices machine-learning-compute delete --compute-name "compute123"
               --resource-group "testrg123" --underlying-resource-action "Delete" --workspace-name
               "workspaces123"
"""

helps['machinelearningservices machine-learning-compute list-node'] = """
    type: command
    short-summary: Get the details (e.g IP address, port etc) of all the compute nodes in the compute.
    examples:
      - name: Get compute nodes information for a compute
        text: |-
               az machinelearningservices machine-learning-compute list-node --compute-name "compute123"
               --resource-group "testrg123" --workspace-name "workspaces123"
"""

helps['machinelearningservices machine-learning-compute list-key'] = """
    type: command
    short-summary: Gets secrets related to Machine Learning compute (storage keys, service credentials, etc).
    examples:
      - name: List AKS Compute Keys
        text: |-
               az machinelearningservices machine-learning-compute list-key --compute-name "compute123"
               --resource-group "testrg123" --workspace-name "workspaces123"
"""

helps['machinelearningservices '] = """
    type: group
    short-summary: machinelearningservices 
"""

helps['machinelearningservices  list'] = """
    type: command
    short-summary: Lists all skus with associated features
    examples:
      - name: List Skus
        text: |-
               az machinelearningservices  list
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
               az machinelearningservices private-endpoint-connection show
               --private-endpoint-connection-name "{privateEndpointConnectionName}" --resource-group
               "rg-1234" --workspace-name "testworkspace"
"""

helps['machinelearningservices private-endpoint-connection delete'] = """
    type: command
    short-summary: Deletes the specified private endpoint connection associated with the workspace.
    examples:
      - name: WorkspaceDeletePrivateEndpointConnection
        text: |-
               az machinelearningservices private-endpoint-connection delete
               --private-endpoint-connection-name "{privateEndpointConnectionName}" --resource-group
               "rg-1234" --workspace-name "testworkspace"
"""

helps['machinelearningservices private-endpoint-connection put'] = """
    type: command
    short-summary: Update the state of specified private endpoint connection associated with the workspace.
    examples:
      - name: WorkspacePutPrivateEndpointConnection
        text: |-
               az machinelearningservices private-endpoint-connection put
               --private-endpoint-connection-name "{privateEndpointConnectionName}"
               --properties-private-link-service-connection-state
               description=Auto-Approved status=Approved --resource-group "rg-1234" --workspace-name
               "testworkspace"
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
               az machinelearningservices private-link-resource list --resource-group "rg-1234"
               --workspace-name "testworkspace"
"""

helps['machinelearningservices linked-workspace'] = """
    type: group
    short-summary: machinelearningservices linked-workspace
"""

helps['machinelearningservices linked-workspace list'] = """
    type: command
    short-summary: List linked workspaces under a workspace per some query criteria.
    examples:
      - name: ListLinkedWorkspaces
        text: |-
               az machinelearningservices linked-workspace list --resource-group "resourceGroup-1234"
               --workspace-name "workspace-123"
"""

helps['machinelearningservices linked-workspace show'] = """
    type: command
    short-summary: Get the detail of a linked workspace.
    examples:
      - name: GetLinkedWorkspace
        text: |-
               az machinelearningservices linked-workspace show --link-name "link-12" --resource-group
               "resourceGroup-1234" --workspace-name "workspace-123"
"""

helps['machinelearningservices linked-workspace create'] = """
    type: command
    short-summary: Add a new linked workspace.
    examples:
      - name: CreateLinkedWorkspace
        text: |-
               az machinelearningservices linked-workspace create --link-name "link-12" --resource-id "/s
               ubscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/resourceGroup-4321/provid
               ers/Microsoft.Synapse/workspaces/linkedWorkspace-1234"
               --user-assigned-identity-resource-id "/subscriptions/00000000-1111-2222-3333-444444444444/
               resourceGroups/resourceGroup-4321/providers/Microsoft.ManagedIdentity/userAssignedIdentiti
               es/uai123" --resource-group "resourceGroup-1234" --workspace-name "workspace-123"
"""

helps['machinelearningservices linked-workspace update'] = """
    type: command
    short-summary: Update the detail of a linked workspace.
    examples:
      - name: UpdateLinkedWorkspace
        text: |-
               az machinelearningservices linked-workspace update --link-name "link-12"
               --user-assigned-identity-resource-id "/subscriptions/00000000-1111-2222-3333-444444444444/
               resourceGroups/resourceGroup-4321/providers/Microsoft.ManagedIdentity/userAssignedIdentiti
               es/uai124" --resource-group "resourceGroup-1234" --workspace-name "workspace-123"
"""

helps['machinelearningservices linked-workspace delete'] = """
    type: command
    short-summary: Delete a linked workspace.
    examples:
      - name: DeleteLinkedWorkspace
        text: |-
               az machinelearningservices linked-workspace delete --link-name "link-12" --resource-group
               "resourceGroup-1234" --workspace-name "workspace-123"
"""
