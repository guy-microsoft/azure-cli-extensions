# Azure CLI machinelearningservices Extension #
This is the extension for machinelearningservices

### How to use ###
Install this extension using the below CLI command
```
az extension add --name machinelearningservices
```

### Included Features ###
#### machinelearningservices workspace ####
##### Create #####
```
az machinelearningservices workspace create --type "SystemAssigned" --location "eastus2euap" \
    --description "test description" \
    --application-insights "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/workspace-1234/providers/microsoft.insights/components/testinsights" \
    --container-registry "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/workspace-1234/providers/Microsoft.ContainerRegistry/registries/testRegistry" \
    --key-vault-properties identity-client-id="" key-identifier="https://testkv.vault.azure.net/keys/testkey/aabbccddee112233445566778899aabb" key-vault-arm-id="/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/workspace-1234/providers/Microsoft.KeyVault/vaults/testkv" \
    --status "Enabled" --friendly-name "HelloName" --hbi-workspace false \
    --key-vault "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/workspace-1234/providers/Microsoft.KeyVault/vaults/testkv" \
    --shared-private-link-resources name="testdbresource" private-link-resource-id="/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/workspace-1234/providers/Microsoft.DocumentDB/databaseAccounts/testdbresource/privateLinkResources/Sql" group-id="Sql" request-message="Please approve" status="Approved" \
    --storage-account "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/accountcrud-1234/providers/Microsoft.Storage/storageAccounts/testStorageAccount" \
    --sku name="Basic" tier="Basic" --resource-group "workspace-1234" --name "testworkspace" 

az machinelearningservices workspace wait --created --resource-group "{rg}" --name "{myWorkspace}"
```
##### Show #####
```
az machinelearningservices workspace show --resource-group "workspace-1234" --name "testworkspace"
```
##### List #####
```
az machinelearningservices workspace list --resource-group "workspace-1234"
```
##### Update #####
```
az machinelearningservices workspace update --description "new description" --friendly-name "New friendly name" \
    --sku name="Enterprise" tier="Enterprise" --resource-group "workspace-1234" --name "testworkspace" 
```
##### List-key #####
```
az machinelearningservices workspace list-key --resource-group "testrg123" --name "workspaces123"
```
##### Resync-key #####
```
az machinelearningservices workspace resync-key --resource-group "testrg123" --name "workspaces123"
```
##### Delete #####
```
az machinelearningservices workspace delete --resource-group "workspace-1234" --name "testworkspace"
```
#### machinelearningservices workspace-feature ####
##### List #####
```
az machinelearningservices workspace-feature list --resource-group "myResourceGroup" --workspace-name "testworkspace"
```
#### machinelearningservices usage ####
##### List #####
```
az machinelearningservices usage list --location "eastus"
```
#### machinelearningservices virtual-machine-size ####
##### List #####
```
az machinelearningservices virtual-machine-size list --location "eastus"
```
#### machinelearningservices quota ####
##### List #####
```
az machinelearningservices quota list --location "eastus"
```
##### Update #####
```
az machinelearningservices quota update --location "eastus" \
    --value type="Microsoft.MachineLearningServices/workspaces/quotas" id="/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg/providers/Microsoft.MachineLearningServices/workspaces/demo_workspace1/quotas/Standard_DSv2_Family_Cluster_Dedicated_vCPUs" limit=100 unit="Count" \
    --value type="Microsoft.MachineLearningServices/workspaces/quotas" id="/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg/providers/Microsoft.MachineLearningServices/workspaces/demo_workspace2/quotas/Standard_DSv2_Family_Cluster_Dedicated_vCPUs" limit=200 unit="Count" 
```
#### machinelearningservices machine-learning-compute ####
##### Aks create #####
```
az machinelearningservices machine-learning-compute aks create --compute-name "compute123" --location "eastus" \
    --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Aks create #####
```
az machinelearningservices machine-learning-compute aks create --compute-name "compute123" --location "eastus" \
    --ak-s-properties "{\\"enableNodePublicIp\\":true,\\"isolatedNetwork\\":false,\\"osType\\":\\"Windows\\",\\"remoteLoginPortPublicAccess\\":\\"NotSpecified\\",\\"scaleSettings\\":{\\"maxNodeCount\\":1,\\"minNodeCount\\":0,\\"nodeIdleTimeBeforeScaleDown\\":\\"PT5M\\"},\\"virtualMachineImage\\":{\\"id\\":\\"/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResourceGroup/providers/Microsoft.Compute/galleries/myImageGallery/images/myImageDefinition/versions/0.0.1\\"},\\"vmPriority\\":\\"Dedicated\\",\\"vmSize\\":\\"STANDARD_NC6\\"}" \
    --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Aks create #####
```
az machinelearningservices machine-learning-compute aks create --compute-name "compute123" --location "eastus" \
    --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Aks create #####
```
az machinelearningservices machine-learning-compute aks create --compute-name "compute123" --location "eastus" \
    --ak-s-properties "{\\"applicationSharingPolicy\\":\\"Personal\\",\\"computeInstanceAuthorizationType\\":\\"personal\\",\\"personalComputeInstanceSettings\\":{\\"assignedUser\\":{\\"objectId\\":\\"00000000-0000-0000-0000-000000000000\\",\\"tenantId\\":\\"00000000-0000-0000-0000-000000000000\\"}},\\"sshSettings\\":{\\"sshPublicAccess\\":\\"Disabled\\"},\\"subnet\\":\\"test-subnet-resource-id\\",\\"vmSize\\":\\"STANDARD_NC6\\"}" \
    --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Aks create #####
```
az machinelearningservices machine-learning-compute aks create --compute-name "compute123" --location "eastus" \
    --ak-s-properties "{\\"vmSize\\":\\"STANDARD_NC6\\"}" --resource-group "testrg123" \
    --workspace-name "workspaces123" 
```
##### Aml-compute create #####
```
az machinelearningservices machine-learning-compute aml-compute create --compute-name "compute123" --location "eastus" \
    --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Aml-compute create #####
```
az machinelearningservices machine-learning-compute aml-compute create --compute-name "compute123" --location "eastus" \
    --aml-compute-properties "{\\"enableNodePublicIp\\":true,\\"isolatedNetwork\\":false,\\"osType\\":\\"Windows\\",\\"remoteLoginPortPublicAccess\\":\\"NotSpecified\\",\\"scaleSettings\\":{\\"maxNodeCount\\":1,\\"minNodeCount\\":0,\\"nodeIdleTimeBeforeScaleDown\\":\\"PT5M\\"},\\"virtualMachineImage\\":{\\"id\\":\\"/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResourceGroup/providers/Microsoft.Compute/galleries/myImageGallery/images/myImageDefinition/versions/0.0.1\\"},\\"vmPriority\\":\\"Dedicated\\",\\"vmSize\\":\\"STANDARD_NC6\\"}" \
    --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Aml-compute create #####
```
az machinelearningservices machine-learning-compute aml-compute create --compute-name "compute123" --location "eastus" \
    --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Aml-compute create #####
```
az machinelearningservices machine-learning-compute aml-compute create --compute-name "compute123" --location "eastus" \
    --aml-compute-properties "{\\"applicationSharingPolicy\\":\\"Personal\\",\\"computeInstanceAuthorizationType\\":\\"personal\\",\\"personalComputeInstanceSettings\\":{\\"assignedUser\\":{\\"objectId\\":\\"00000000-0000-0000-0000-000000000000\\",\\"tenantId\\":\\"00000000-0000-0000-0000-000000000000\\"}},\\"sshSettings\\":{\\"sshPublicAccess\\":\\"Disabled\\"},\\"subnet\\":\\"test-subnet-resource-id\\",\\"vmSize\\":\\"STANDARD_NC6\\"}" \
    --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Aml-compute create #####
```
az machinelearningservices machine-learning-compute aml-compute create --compute-name "compute123" --location "eastus" \
    --aml-compute-properties "{\\"vmSize\\":\\"STANDARD_NC6\\"}" --resource-group "testrg123" \
    --workspace-name "workspaces123" 
```
##### Compute-instance create #####
```
az machinelearningservices machine-learning-compute compute-instance create --compute-name "compute123" \
    --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Compute-instance create #####
```
az machinelearningservices machine-learning-compute compute-instance create --compute-name "compute123" \
    --location "eastus" \
    --compute-instance-properties "{\\"enableNodePublicIp\\":true,\\"isolatedNetwork\\":false,\\"osType\\":\\"Windows\\",\\"remoteLoginPortPublicAccess\\":\\"NotSpecified\\",\\"scaleSettings\\":{\\"maxNodeCount\\":1,\\"minNodeCount\\":0,\\"nodeIdleTimeBeforeScaleDown\\":\\"PT5M\\"},\\"virtualMachineImage\\":{\\"id\\":\\"/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResourceGroup/providers/Microsoft.Compute/galleries/myImageGallery/images/myImageDefinition/versions/0.0.1\\"},\\"vmPriority\\":\\"Dedicated\\",\\"vmSize\\":\\"STANDARD_NC6\\"}" \
    --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Compute-instance create #####
```
az machinelearningservices machine-learning-compute compute-instance create --compute-name "compute123" \
    --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Compute-instance create #####
```
az machinelearningservices machine-learning-compute compute-instance create --compute-name "compute123" \
    --location "eastus" \
    --compute-instance-properties "{\\"applicationSharingPolicy\\":\\"Personal\\",\\"computeInstanceAuthorizationType\\":\\"personal\\",\\"personalComputeInstanceSettings\\":{\\"assignedUser\\":{\\"objectId\\":\\"00000000-0000-0000-0000-000000000000\\",\\"tenantId\\":\\"00000000-0000-0000-0000-000000000000\\"}},\\"sshSettings\\":{\\"sshPublicAccess\\":\\"Disabled\\"},\\"subnet\\":\\"test-subnet-resource-id\\",\\"vmSize\\":\\"STANDARD_NC6\\"}" \
    --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Compute-instance create #####
```
az machinelearningservices machine-learning-compute compute-instance create --compute-name "compute123" \
    --location "eastus" --compute-instance-properties "{\\"vmSize\\":\\"STANDARD_NC6\\"}" --resource-group "testrg123" \
    --workspace-name "workspaces123" 
```
##### Data-factory create #####
```
az machinelearningservices machine-learning-compute data-factory create --compute-name "compute123" \
    --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Data-factory create #####
```
az machinelearningservices machine-learning-compute data-factory create --compute-name "compute123" \
    --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Data-factory create #####
```
az machinelearningservices machine-learning-compute data-factory create --compute-name "compute123" \
    --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Data-factory create #####
```
az machinelearningservices machine-learning-compute data-factory create --compute-name "compute123" \
    --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Data-factory create #####
```
az machinelearningservices machine-learning-compute data-factory create --compute-name "compute123" \
    --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Data-lake-analytics create #####
```
az machinelearningservices machine-learning-compute data-lake-analytics create --compute-name "compute123" \
    --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Data-lake-analytics create #####
```
az machinelearningservices machine-learning-compute data-lake-analytics create --compute-name "compute123" \
    --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Data-lake-analytics create #####
```
az machinelearningservices machine-learning-compute data-lake-analytics create --compute-name "compute123" \
    --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Data-lake-analytics create #####
```
az machinelearningservices machine-learning-compute data-lake-analytics create --compute-name "compute123" \
    --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Data-lake-analytics create #####
```
az machinelearningservices machine-learning-compute data-lake-analytics create --compute-name "compute123" \
    --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Databricks create #####
```
az machinelearningservices machine-learning-compute databricks create --compute-name "compute123" --location "eastus" \
    --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Databricks create #####
```
az machinelearningservices machine-learning-compute databricks create --compute-name "compute123" --location "eastus" \
    --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Databricks create #####
```
az machinelearningservices machine-learning-compute databricks create --compute-name "compute123" --location "eastus" \
    --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Databricks create #####
```
az machinelearningservices machine-learning-compute databricks create --compute-name "compute123" --location "eastus" \
    --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Databricks create #####
```
az machinelearningservices machine-learning-compute databricks create --compute-name "compute123" --location "eastus" \
    --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Hd-insight create #####
```
az machinelearningservices machine-learning-compute hd-insight create --compute-name "compute123" --location "eastus" \
    --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Hd-insight create #####
```
az machinelearningservices machine-learning-compute hd-insight create --compute-name "compute123" --location "eastus" \
    --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Hd-insight create #####
```
az machinelearningservices machine-learning-compute hd-insight create --compute-name "compute123" --location "eastus" \
    --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Hd-insight create #####
```
az machinelearningservices machine-learning-compute hd-insight create --compute-name "compute123" --location "eastus" \
    --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Hd-insight create #####
```
az machinelearningservices machine-learning-compute hd-insight create --compute-name "compute123" --location "eastus" \
    --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Virtual-machine create #####
```
az machinelearningservices machine-learning-compute virtual-machine create --compute-name "compute123" \
    --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Virtual-machine create #####
```
az machinelearningservices machine-learning-compute virtual-machine create --compute-name "compute123" \
    --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Virtual-machine create #####
```
az machinelearningservices machine-learning-compute virtual-machine create --compute-name "compute123" \
    --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Virtual-machine create #####
```
az machinelearningservices machine-learning-compute virtual-machine create --compute-name "compute123" \
    --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### Virtual-machine create #####
```
az machinelearningservices machine-learning-compute virtual-machine create --compute-name "compute123" \
    --location "eastus" --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### List #####
```
az machinelearningservices machine-learning-compute list --resource-group "testrg123" --workspace-name "workspaces123"
```
##### Show #####
```
az machinelearningservices machine-learning-compute show --compute-name "compute123" --resource-group "testrg123" \
    --workspace-name "workspaces123" 
```
##### Show #####
```
az machinelearningservices machine-learning-compute show --compute-name "compute123" --resource-group "testrg123" \
    --workspace-name "workspaces123" 
```
##### Show #####
```
az machinelearningservices machine-learning-compute show --compute-name "compute123" --resource-group "testrg123" \
    --workspace-name "workspaces123" 
```
##### Update #####
```
az machinelearningservices machine-learning-compute update --compute-name "compute123" \
    --scale-settings max-node-count=4 min-node-count=4 node-idle-time-before-scale-down="PT5M" \
    --resource-group "testrg123" --workspace-name "workspaces123" 
```
##### List-key #####
```
az machinelearningservices machine-learning-compute list-key --compute-name "compute123" --resource-group "testrg123" \
    --workspace-name "workspaces123" 
```
##### List-node #####
```
az machinelearningservices machine-learning-compute list-node --compute-name "compute123" --resource-group "testrg123" \
    --workspace-name "workspaces123" 
```
##### Restart #####
```
az machinelearningservices machine-learning-compute restart --compute-name "compute123" --resource-group "testrg123" \
    --workspace-name "workspaces123" 
```
##### Start #####
```
az machinelearningservices machine-learning-compute start --compute-name "compute123" --resource-group "testrg123" \
    --workspace-name "workspaces123" 
```
##### Stop #####
```
az machinelearningservices machine-learning-compute stop --compute-name "compute123" --resource-group "testrg123" \
    --workspace-name "workspaces123" 
```
##### Delete #####
```
az machinelearningservices machine-learning-compute delete --compute-name "compute123" --resource-group "testrg123" \
    --underlying-resource-action "Delete" --workspace-name "workspaces123" 
```
#### machinelearningservices ####
##### List-sku #####
```
az machinelearningservices list-sku
```
#### machinelearningservices private-endpoint-connection ####
##### Put #####
```
az machinelearningservices private-endpoint-connection put --name "{privateEndpointConnectionName}" \
    --private-link-service-connection-state description="Auto-Approved" status="Approved" --resource-group "rg-1234" \
    --workspace-name "testworkspace" 
```
##### Show #####
```
az machinelearningservices private-endpoint-connection show --name "{privateEndpointConnectionName}" \
    --resource-group "rg-1234" --workspace-name "testworkspace" 
```
##### Delete #####
```
az machinelearningservices private-endpoint-connection delete --name "{privateEndpointConnectionName}" \
    --resource-group "rg-1234" --workspace-name "testworkspace" 
```
#### machinelearningservices private-link-resource ####
##### List #####
```
az machinelearningservices private-link-resource list --resource-group "rg-1234" --workspace-name "testworkspace"
```
#### machinelearningservices linked-service ####
##### Create #####
```
az machinelearningservices linked-service create --link-name "link-1" --name "link-1" --type "SystemAssigned" \
    --location "westus" \
    --properties linked-service-resource-id="/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/resourceGroup-1/providers/Microsoft.Synapse/workspaces/Syn-1" \
    --resource-group "resourceGroup-1" --workspace-name "workspace-1" 
```
##### Show #####
```
az machinelearningservices linked-service show --link-name "link-1" --resource-group "resourceGroup-1" \
    --workspace-name "workspace-1" 
```
##### List #####
```
az machinelearningservices linked-service list --resource-group "resourceGroup-1" --workspace-name "workspace-1"
```
##### Delete #####
```
az machinelearningservices linked-service delete --link-name "link-1" --resource-group "resourceGroup-1" \
    --workspace-name "workspace-1" 
```
#### machinelearningservices machine-learning-service ####
##### Create #####
```
az machinelearningservices machine-learning-service create \
    --properties "{\\"appInsightsEnabled\\":true,\\"authEnabled\\":true,\\"computeType\\":\\"ACI\\",\\"containerResourceRequirements\\":{\\"cpu\\":1,\\"memoryInGB\\":1},\\"environmentImageRequest\\":{\\"assets\\":[{\\"id\\":null,\\"mimeType\\":\\"application/x-python\\",\\"unpack\\":false,\\"url\\":\\"aml://storage/azureml/score.py\\"}],\\"driverProgram\\":\\"score.py\\",\\"environment\\":{\\"name\\":\\"AzureML-Scikit-learn-0.20.3\\",\\"docker\\":{\\"baseDockerfile\\":null,\\"baseImage\\":\\"mcr.microsoft.com/azureml/base:openmpi3.1.2-ubuntu16.04\\",\\"baseImageRegistry\\":{\\"address\\":null,\\"password\\":null,\\"username\\":null}},\\"environmentVariables\\":{\\"EXAMPLE_ENV_VAR\\":\\"EXAMPLE_VALUE\\"},\\"inferencingStackVersion\\":null,\\"python\\":{\\"baseCondaEnvironment\\":null,\\"condaDependencies\\":{\\"name\\":\\"azureml_ae1acbe6e1e6aabbad900b53c491a17c\\",\\"channels\\":[\\"conda-forge\\"],\\"dependencies\\":[\\"python=3.6.2\\",{\\"pip\\":[\\"azureml-core==1.0.69\\",\\"azureml-defaults==1.0.69\\",\\"azureml-telemetry==1.0.69\\",\\"azureml-train-restclients-hyperdrive==1.0.69\\",\\"azureml-train-core==1.0.69\\",\\"scikit-learn==0.20.3\\",\\"scipy==1.2.1\\",\\"numpy==1.16.2\\",\\"joblib==0.13.2\\"]}]},\\"interpreterPath\\":\\"python\\",\\"userManagedDependencies\\":false},\\"spark\\":{\\"packages\\":[],\\"precachePackages\\":true,\\"repositories\\":[]},\\"version\\":\\"3\\"},\\"models\\":[{\\"name\\":\\"sklearn_regression_model.pkl\\",\\"mimeType\\":\\"application/x-python\\",\\"url\\":\\"aml://storage/azureml/sklearn_regression_model.pkl\\"}]},\\"location\\":\\"eastus2\\"}" \
    --resource-group "testrg123" --service-name "service456" --workspace-name "workspaces123" 
```
##### Show #####
```
az machinelearningservices machine-learning-service show --resource-group "testrg123" --service-name "service123" \
    --workspace-name "workspaces123" 
```
##### List #####
```
az machinelearningservices machine-learning-service list --resource-group "testrg123" --workspace-name "workspaces123"
```
##### Delete #####
```
az machinelearningservices machine-learning-service delete --resource-group "testrg123" --service-name "service123" \
    --workspace-name "workspaces123" 
```
#### machinelearningservices notebook ####
##### List-key #####
```
az machinelearningservices notebook list-key --resource-group "testrg123" --workspace-name "workspaces123"
```
##### Prepare #####
```
az machinelearningservices notebook prepare --resource-group "testrg123" --workspace-name "workspaces123"
```
#### machinelearningservices workspace-connection ####
##### Create #####
```
az machinelearningservices workspace-connection create --connection-name "connection-1" --name "connection-1" \
    --auth-type "PAT" --category "ACR" --target "www.facebook.com" --value "secrets" \
    --resource-group "resourceGroup-1" --workspace-name "workspace-1" 
```
##### Show #####
```
az machinelearningservices workspace-connection show --connection-name "connection-1" \
    --resource-group "resourceGroup-1" --workspace-name "workspace-1" 
```
##### List #####
```
az machinelearningservices workspace-connection list --category "ACR" --resource-group "resourceGroup-1" \
    --target "www.facebook.com" --workspace-name "workspace-1" 
```
##### Delete #####
```
az machinelearningservices workspace-connection delete --connection-name "connection-1" \
    --resource-group "resourceGroup-1" --workspace-name "workspace-1" 
```
#### machinelearningservices code-container ####
##### Create #####
```
az machinelearningservices code-container create --name "testContainer" \
    --properties description="string" tags={"tag1":"value1","tag2":"value2"} --resource-group "testrg123" \
    --workspace-name "testworkspace" 
```
##### Show #####
```
az machinelearningservices code-container show --name "testContainer" --resource-group "testrg123" \
    --workspace-name "testworkspace" 
```
##### List #####
```
az machinelearningservices code-container list --skiptoken "skiptoken" --resource-group "testrg123" \
    --workspace-name "testworkspace" 
```
##### Delete #####
```
az machinelearningservices code-container delete --name "testContainer" --resource-group "testrg123" \
    --workspace-name "testworkspace" 
```
#### machinelearningservices code-version ####
##### Create #####
```
az machinelearningservices code-version create --name "testContainer" \
    --properties description="string" assetPath={"path":"string","isDirectory":true} datastoreId="string" properties={"prop1":"value1","prop2":"value2"} tags={"tag1":"value1","tag2":"value2"} \
    --resource-group "testrg123" --version "1" --workspace-name "testworkspace" 
```
##### Show #####
```
az machinelearningservices code-version show --name "testContainer" --resource-group "testrg123" --version "1" \
    --workspace-name "testworkspace" 
```
##### List #####
```
az machinelearningservices code-version list --name "testContainer" --skiptoken "skiptoken" \
    --resource-group "testrg123" --workspace-name "testworkspace" 
```
##### Delete #####
```
az machinelearningservices code-version delete --name "testContainer" --resource-group "testrg123" --version "1" \
    --workspace-name "testworkspace" 
```
#### machinelearningservices data-container ####
##### Create #####
```
az machinelearningservices data-container create --name "datacontainer123" \
    --properties description="string" properties={"properties1":"value1","properties2":"value2"} tags={"tag1":"value1","tag2":"value2"} \
    --resource-group "testrg123" --workspace-name "workspace123" 
```
##### Show #####
```
az machinelearningservices data-container show --name "datacontainer123" --resource-group "testrg123" \
    --workspace-name "workspace123" 
```
##### List #####
```
az machinelearningservices data-container list --resource-group "testrg123" --workspace-name "workspace123"
```
##### Delete #####
```
az machinelearningservices data-container delete --name "datacontainer123" --resource-group "testrg123" \
    --workspace-name "workspace123" 
```
#### machinelearningservices datastore ####
##### Create #####
```
az machinelearningservices datastore create --name "testDatastore" \
    --properties description="string" contents={"type":"AzureBlob","azureDataLake":{"credentials":{"type":"AccountKey","accountKey":{"key":"string"},"certificate":{"authorityUrl":"string","certificate":"string","clientId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","resourceUri":"string","tenantId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","thumbprint":"string"},"sas":{"sasToken":"string"},"servicePrincipal":{"authorityUrl":"string","clientId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","clientSecret":"string","resourceUri":"string","tenantId":"3fa85f64-5717-4562-b3fc-2c963f66afa6"},"sqlAdmin":{"password":"string","userId":"string"}},"storeName":"string"},"azureMySql":{"credentials":{"type":"AccountKey","accountKey":{"key":"string"},"certificate":{"authorityUrl":"string","certificate":"string","clientId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","resourceUri":"string","tenantId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","thumbprint":"string"},"sas":{"sasToken":"string"},"servicePrincipal":{"authorityUrl":"string","clientId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","clientSecret":"string","resourceUri":"string","tenantId":"3fa85f64-5717-4562-b3fc-2c963f66afa6"},"sqlAdmin":{"password":"string","userId":"string"}},"databaseName":"string","endpoint":"database.windows.net","portNumber":0,"serverName":"string"},"azurePostgreSql":{"credentials":{"type":"AccountKey","accountKey":{"key":"string"},"certificate":{"authorityUrl":"string","certificate":"string","clientId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","resourceUri":"string","tenantId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","thumbprint":"string"},"sas":{"sasToken":"string"},"servicePrincipal":{"authorityUrl":"string","clientId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","clientSecret":"string","resourceUri":"string","tenantId":"3fa85f64-5717-4562-b3fc-2c963f66afa6"},"sqlAdmin":{"password":"string","userId":"string"}},"databaseName":"string","enableSSL":true,"endpoint":"database.windows.net","portNumber":0,"serverName":"string"},"azureSqlDatabase":{"credentials":{"type":"AccountKey","accountKey":{"key":"string"},"certificate":{"authorityUrl":"string","certificate":"string","clientId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","resourceUri":"string","tenantId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","thumbprint":"string"},"sas":{"sasToken":"string"},"servicePrincipal":{"authorityUrl":"string","clientId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","clientSecret":"string","resourceUri":"string","tenantId":"3fa85f64-5717-4562-b3fc-2c963f66afa6"},"sqlAdmin":{"password":"string","userId":"string"}},"databaseName":"string","endpoint":"database.windows.net","portNumber":0,"serverName":"string"},"azureStorage":{"accountName":"string","blobCacheTimeout":0,"containerName":"string","credentials":{"type":"AccountKey","accountKey":{"key":"string"},"certificate":{"authorityUrl":"string","certificate":"string","clientId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","resourceUri":"string","tenantId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","thumbprint":"string"},"sas":{"sasToken":"string"},"servicePrincipal":{"authorityUrl":"string","clientId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","clientSecret":"string","resourceUri":"string","tenantId":"3fa85f64-5717-4562-b3fc-2c963f66afa6"},"sqlAdmin":{"password":"string","userId":"string"}},"endpoint":"core.windows.net","protocol":"https"},"glusterFs":{"serverAddress":"string","volumeName":"string"}} isDefault=true linkedInfo={"linkedId":"string","linkedResourceName":"string","origin":"Synapse"} properties={"additionalProp1":"string","additionalProp2":"string","additionalProp3":"string"} tags={"additionalProp1":"string","additionalProp2":"string","additionalProp3":"string"} \
    --resource-group "testrg123" --workspace-name "testworkspace" 
```
##### Show #####
```
az machinelearningservices datastore show --name "testDatastore" --resource-group "testrg123" \
    --workspace-name "testworkspace" 
```
##### List #####
```
az machinelearningservices datastore list --resource-group "testrg123" --workspace-name "testworkspace"
```
##### List-secret #####
```
az machinelearningservices datastore list-secret --name "testDatastore" --resource-group "testrg123" \
    --workspace-name "testworkspace" 
```
##### Delete #####
```
az machinelearningservices datastore delete --name "testDatastore" --resource-group "testrg123" \
    --workspace-name "testworkspace" 
```
#### machinelearningservices data-version ####
##### Create #####
```
az machinelearningservices data-version create --name "dataset123" \
    --properties description="string" assetPath={"path":"string","isDirectory":false} datasetType="Simple" datastoreId="string" properties={"properties1":"value1","properties2":"value2"} tags={"tag1":"value1","tag2":"value2"} \
    --resource-group "testrg123" --version "456" --workspace-name "workspace123" 
```
##### Show #####
```
az machinelearningservices data-version show --name "dataset123" --resource-group "testrg123" --version "456" \
    --workspace-name "workspace123" 
```
##### List #####
```
az machinelearningservices data-version list --name "dataset123" --resource-group "testrg123" \
    --workspace-name "workspace123" 
```
##### Delete #####
```
az machinelearningservices data-version delete --name "dataset123" --resource-group "testrg123" --version "456" \
    --workspace-name "workspace123" 
```
#### machinelearningservices environment-container ####
##### Create #####
```
az machinelearningservices environment-container create --name "testContainer" \
    --properties description="string" properties={"additionalProp1":"string","additionalProp2":"string","additionalProp3":"string"} tags={"additionalProp1":"string","additionalProp2":"string","additionalProp3":"string"} \
    --resource-group "testrg123" --workspace-name "testworkspace" 
```
##### Show #####
```
az machinelearningservices environment-container show --name "testContainer" --resource-group "testrg123" \
    --workspace-name "testworkspace" 
```
##### List #####
```
az machinelearningservices environment-container list --skiptoken "skiptoken" --resource-group "testrg123" \
    --workspace-name "testworkspace" 
```
##### Delete #####
```
az machinelearningservices environment-container delete --name "testContainer" --resource-group "testrg123" \
    --workspace-name "testworkspace" 
```
#### machinelearningservices environment-specification-version ####
##### Create #####
```
az machinelearningservices environment-specification-version create --name "testContainer" \
    --properties description="string" assetPath={"path":"string","isDirectory":true} condaFile="string" datastoreId="string" docker={"type":"Build"} properties={"additionalProp1":"string","additionalProp2":"string","additionalProp3":"string"} tags={"additionalProp1":"string","additionalProp2":"string","additionalProp3":"string"} \
    --resource-group "testrg123" --version "1" --workspace-name "testworkspace" 
```
##### Show #####
```
az machinelearningservices environment-specification-version show --name "testContainer" --resource-group "testrg123" \
    --version "1" --workspace-name "testworkspace" 
```
##### List #####
```
az machinelearningservices environment-specification-version list --name "testContainer" --skiptoken "skiptoken" \
    --resource-group "testrg123" --workspace-name "testworkspace" 
```
##### Delete #####
```
az machinelearningservices environment-specification-version delete --name "testContainer" \
    --resource-group "testrg123" --version "1" --workspace-name "testworkspace" 
```
#### machinelearningservices job ####
##### Create #####
```
az machinelearningservices job create \
    --properties "{\\"description\\":\\"string\\",\\"properties\\":{\\"additionalProp1\\":\\"string\\",\\"additionalProp2\\":\\"string\\",\\"additionalProp3\\":\\"string\\"},\\"tags\\":{\\"additionalProp1\\":\\"string\\",\\"additionalProp2\\":\\"string\\",\\"additionalProp3\\":\\"string\\"}}" \
    --id "testContainer" --resource-group "testrg123" --workspace-name "testworkspace" 
```
##### Create #####
```
az machinelearningservices job create \
    --properties "{\\"description\\":\\"string\\",\\"properties\\":{\\"additionalProp1\\":\\"string\\",\\"additionalProp2\\":\\"string\\",\\"additionalProp3\\":\\"string\\"},\\"tags\\":{\\"additionalProp1\\":\\"string\\",\\"additionalProp2\\":\\"string\\",\\"additionalProp3\\":\\"string\\"}}" \
    --id "testContainer" --resource-group "testrg123" --workspace-name "testworkspace" 
```
##### Show #####
```
az machinelearningservices job show --id "testContainer" --resource-group "testrg123" --workspace-name "testworkspace"
```
##### Show #####
```
az machinelearningservices job show --id "testContainer" --resource-group "testrg123" --workspace-name "testworkspace"
```
##### List #####
```
az machinelearningservices job list --skiptoken "skiptoken" --resource-group "testrg123" \
    --workspace-name "testworkspace" 
```
##### List #####
```
az machinelearningservices job list --skiptoken "skiptoken" --resource-group "testrg123" \
    --workspace-name "testworkspace" 
```
##### Cancel #####
```
az machinelearningservices job cancel --id "testContainer" --resource-group "testrg123" \
    --workspace-name "testworkspace" 
```
##### Cancel #####
```
az machinelearningservices job cancel --id "testContainer" --resource-group "testrg123" \
    --workspace-name "testworkspace" 
```
##### Poll #####
```
az machinelearningservices job poll --operation-id "1" --id "testContainer" --resource-group "testrg123" \
    --workspace-name "testworkspace" 
```
##### Poll #####
```
az machinelearningservices job poll --operation-id "1" --id "testContainer" --resource-group "testrg123" \
    --workspace-name "testworkspace" 
```
##### Delete #####
```
az machinelearningservices job delete --id "testContainer" --resource-group "testrg123" \
    --workspace-name "testworkspace" 
```
##### Delete #####
```
az machinelearningservices job delete --id "testContainer" --resource-group "testrg123" \
    --workspace-name "testworkspace" 
```
#### machinelearningservices labeling-job ####
##### Create #####
```
az machinelearningservices labeling-job create \
    --properties description="string" createdTimeUtc="2020-12-08T01:23:37.118Z" datasetConfiguration={"assetName":"string","datasetVersion":"string","incrementalDatasetRefreshEnabled":true} jobInstructions={"uri":"string"} jobType="Labeling" labelCategories={"additionalProp1":{"allowMultiSelect":true,"classes":{"additionalProp1":{"displayName":"string","subclasses":{}},"additionalProp2":{"displayName":"string","subclasses":{}},"additionalProp3":{"displayName":"string","subclasses":{}}},"displayName":"string"},"additionalProp2":{"allowMultiSelect":true,"classes":{"additionalProp1":{"displayName":"string","subclasses":{}},"additionalProp2":{"displayName":"string","subclasses":{}},"additionalProp3":{"displayName":"string","subclasses":{}}},"displayName":"string"},"additionalProp3":{"allowMultiSelect":true,"classes":{"additionalProp1":{"displayName":"string","subclasses":{}},"additionalProp2":{"displayName":"string","subclasses":{}},"additionalProp3":{"displayName":"string","subclasses":{}}},"displayName":"string"}} labelingJobMediaProperties={"mediaType":"Image"} mlAssistConfiguration={"inferencingComputeBinding":{"computeId":"string","nodeCount":0},"mlAssistEnabled":true,"trainingComputeBinding":{"computeId":"string","nodeCount":0}} progressMetrics={} projectId="3fa85f64-5717-4562-b3fc-2c963f66afa6" properties={"additionalProp1":"string","additionalProp2":"string","additionalProp3":"string"} status="NotStarted" statusMessages={} tags={"additionalProp1":"string","additionalProp2":"string","additionalProp3":"string"} \
    --id "testLabelingJob" --resource-group "workspace-1234" --workspace-name "testworkspace" 
```
##### Show #####
```
az machinelearningservices labeling-job show --id "testLabelingJob" --include-job-instructions true \
    --include-label-categories true --resource-group "workspace-1234" --workspace-name "testworkspace" 
```
##### List #####
```
az machinelearningservices labeling-job list --skiptoken "skiptoken" --count "10" --resource-group "workspace-1234" \
    --workspace-name "testworkspace" 
```
##### Export-label #####
```
az machinelearningservices labeling-job export-label --body "CSV" --id "testLabelingJob" \
    --resource-group "workspace-1234" --workspace-name "testworkspace" 
```
##### Pause #####
```
az machinelearningservices labeling-job pause --id "testLabelingJob" --resource-group "workspace-1234" \
    --workspace-name "testworkspace" 
```
##### Resume #####
```
az machinelearningservices labeling-job resume --id "testLabelingJob" --resource-group "workspace-1234" \
    --workspace-name "testworkspace" 
```
##### Show-export-summary #####
```
az machinelearningservices labeling-job show-export-summary --export-id "3fa85f64-5717-4562-b3fc-2c963f66afa6" \
    --id "testLabelingJob" --resource-group "workspace-1234" --workspace-name "testworkspace" 
```
##### Delete #####
```
az machinelearningservices labeling-job delete --id "testLabelingJob" --resource-group "workspace-1234" \
    --workspace-name "testworkspace" 
```
#### machinelearningservices model-container ####
##### Create #####
```
az machinelearningservices model-container create --name "testContainer" \
    --properties description="Model container description" tags={"tag1":"value1","tag2":"value2"} \
    --resource-group "testrg123" --workspace-name "workspace123" 
```
##### Show #####
```
az machinelearningservices model-container show --name "testContainer" --resource-group "testrg123" \
    --workspace-name "workspace123" 
```
##### List #####
```
az machinelearningservices model-container list --resource-group "testrg123" --workspace-name "workspace123"
```
##### Delete #####
```
az machinelearningservices model-container delete --name "testContainer" --resource-group "testrg123" \
    --workspace-name "workspace123" 
```
#### machinelearningservices model-version ####
##### Create #####
```
az machinelearningservices model-version create --name "testContainer" \
    --properties description="Model version description" assetPath={"path":"LocalUpload/12345/some/path","isDirectory":true} datastoreId="/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg123/providers/Microsoft.MachineLearningServices/workspaces/workspace123/datastores/datastore123" properties={"prop1":"value1","prop2":"value2"} stage="Production" tags={"tag1":"value1","tag2":"value2"} \
    --resource-group "testrg123" --version "999" --workspace-name "workspace123" 
```
##### Show #####
```
az machinelearningservices model-version show --name "testContainer" --resource-group "testrg123" --version "999" \
    --workspace-name "workspace123" 
```
##### List #####
```
az machinelearningservices model-version list --name "testContainer" --resource-group "testrg123" --version "999" \
    --workspace-name "workspace123" 
```
##### Delete #####
```
az machinelearningservices model-version delete --name "testContainer" --resource-group "testrg123" --version "999" \
    --workspace-name "workspace123" 
```