# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az machinelearningservices|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az machinelearningservices` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az machinelearningservices workspace|Workspaces|[commands](#CommandsInWorkspaces)|
|az machinelearningservices workspace-feature|WorkspaceFeatures|[commands](#CommandsInWorkspaceFeatures)|
|az machinelearningservices usage|Usages|[commands](#CommandsInUsages)|
|az machinelearningservices virtual-machine-size|VirtualMachineSizes|[commands](#CommandsInVirtualMachineSizes)|
|az machinelearningservices quota|Quotas|[commands](#CommandsInQuotas)|
|az machinelearningservices machine-learning-compute|MachineLearningCompute|[commands](#CommandsInMachineLearningCompute)|
|az machinelearningservices||[commands](#CommandsIn)|
|az machinelearningservices private-endpoint-connection|PrivateEndpointConnections|[commands](#CommandsInPrivateEndpointConnections)|
|az machinelearningservices private-link-resource|PrivateLinkResources|[commands](#CommandsInPrivateLinkResources)|
|az machinelearningservices linked-service|LinkedServices|[commands](#CommandsInLinkedServices)|
|az machinelearningservices machine-learning-service|MachineLearningService|[commands](#CommandsInMachineLearningService)|
|az machinelearningservices notebook|Notebooks|[commands](#CommandsInNotebooks)|
|az machinelearningservices workspace-connection|WorkspaceConnections|[commands](#CommandsInWorkspaceConnections)|
|az machinelearningservices code-container|CodeContainers|[commands](#CommandsInCodeContainers)|
|az machinelearningservices code-version|CodeVersions|[commands](#CommandsInCodeVersions)|
|az machinelearningservices data-container|DataContainers|[commands](#CommandsInDataContainers)|
|az machinelearningservices datastore|Datastores|[commands](#CommandsInDatastores)|
|az machinelearningservices data-version|DataVersions|[commands](#CommandsInDataVersions)|
|az machinelearningservices environment-container|EnvironmentContainers|[commands](#CommandsInEnvironmentContainers)|
|az machinelearningservices environment-specification-version|EnvironmentSpecificationVersions|[commands](#CommandsInEnvironmentSpecificationVersions)|
|az machinelearningservices job|Jobs|[commands](#CommandsInJobs)|
|az machinelearningservices labeling-job|LabelingJobs|[commands](#CommandsInLabelingJobs)|
|az machinelearningservices model-container|ModelContainers|[commands](#CommandsInModelContainers)|
|az machinelearningservices model-version|ModelVersions|[commands](#CommandsInModelVersions)|

## COMMANDS
### <a name="CommandsIn">Commands in `az machinelearningservices` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices list-sku](#ListSkus)|ListSkus|[Parameters](#ParametersListSkus)|[Example](#ExamplesListSkus)|

### <a name="CommandsInCodeContainers">Commands in `az machinelearningservices code-container` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices code-container list](#CodeContainersList)|List|[Parameters](#ParametersCodeContainersList)|[Example](#ExamplesCodeContainersList)|
|[az machinelearningservices code-container show](#CodeContainersGet)|Get|[Parameters](#ParametersCodeContainersGet)|[Example](#ExamplesCodeContainersGet)|
|[az machinelearningservices code-container create](#CodeContainersCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersCodeContainersCreateOrUpdate#Create)|[Example](#ExamplesCodeContainersCreateOrUpdate#Create)|
|[az machinelearningservices code-container update](#CodeContainersCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersCodeContainersCreateOrUpdate#Update)|Not Found|
|[az machinelearningservices code-container delete](#CodeContainersDelete)|Delete|[Parameters](#ParametersCodeContainersDelete)|[Example](#ExamplesCodeContainersDelete)|

### <a name="CommandsInCodeVersions">Commands in `az machinelearningservices code-version` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices code-version list](#CodeVersionsList)|List|[Parameters](#ParametersCodeVersionsList)|[Example](#ExamplesCodeVersionsList)|
|[az machinelearningservices code-version show](#CodeVersionsGet)|Get|[Parameters](#ParametersCodeVersionsGet)|[Example](#ExamplesCodeVersionsGet)|
|[az machinelearningservices code-version create](#CodeVersionsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersCodeVersionsCreateOrUpdate#Create)|[Example](#ExamplesCodeVersionsCreateOrUpdate#Create)|
|[az machinelearningservices code-version update](#CodeVersionsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersCodeVersionsCreateOrUpdate#Update)|Not Found|
|[az machinelearningservices code-version delete](#CodeVersionsDelete)|Delete|[Parameters](#ParametersCodeVersionsDelete)|[Example](#ExamplesCodeVersionsDelete)|

### <a name="CommandsInDataContainers">Commands in `az machinelearningservices data-container` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices data-container list](#DataContainersList)|List|[Parameters](#ParametersDataContainersList)|[Example](#ExamplesDataContainersList)|
|[az machinelearningservices data-container show](#DataContainersGet)|Get|[Parameters](#ParametersDataContainersGet)|[Example](#ExamplesDataContainersGet)|
|[az machinelearningservices data-container create](#DataContainersCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersDataContainersCreateOrUpdate#Create)|[Example](#ExamplesDataContainersCreateOrUpdate#Create)|
|[az machinelearningservices data-container update](#DataContainersCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersDataContainersCreateOrUpdate#Update)|Not Found|
|[az machinelearningservices data-container delete](#DataContainersDelete)|Delete|[Parameters](#ParametersDataContainersDelete)|[Example](#ExamplesDataContainersDelete)|

### <a name="CommandsInDataVersions">Commands in `az machinelearningservices data-version` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices data-version list](#DataVersionsList)|List|[Parameters](#ParametersDataVersionsList)|[Example](#ExamplesDataVersionsList)|
|[az machinelearningservices data-version show](#DataVersionsGet)|Get|[Parameters](#ParametersDataVersionsGet)|[Example](#ExamplesDataVersionsGet)|
|[az machinelearningservices data-version create](#DataVersionsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersDataVersionsCreateOrUpdate#Create)|[Example](#ExamplesDataVersionsCreateOrUpdate#Create)|
|[az machinelearningservices data-version update](#DataVersionsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersDataVersionsCreateOrUpdate#Update)|Not Found|
|[az machinelearningservices data-version delete](#DataVersionsDelete)|Delete|[Parameters](#ParametersDataVersionsDelete)|[Example](#ExamplesDataVersionsDelete)|

### <a name="CommandsInDatastores">Commands in `az machinelearningservices datastore` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices datastore list](#DatastoresList)|List|[Parameters](#ParametersDatastoresList)|[Example](#ExamplesDatastoresList)|
|[az machinelearningservices datastore show](#DatastoresGet)|Get|[Parameters](#ParametersDatastoresGet)|[Example](#ExamplesDatastoresGet)|
|[az machinelearningservices datastore create](#DatastoresCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersDatastoresCreateOrUpdate#Create)|[Example](#ExamplesDatastoresCreateOrUpdate#Create)|
|[az machinelearningservices datastore update](#DatastoresCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersDatastoresCreateOrUpdate#Update)|Not Found|
|[az machinelearningservices datastore delete](#DatastoresDelete)|Delete|[Parameters](#ParametersDatastoresDelete)|[Example](#ExamplesDatastoresDelete)|
|[az machinelearningservices datastore list-secret](#DatastoresListSecrets)|ListSecrets|[Parameters](#ParametersDatastoresListSecrets)|[Example](#ExamplesDatastoresListSecrets)|

### <a name="CommandsInEnvironmentContainers">Commands in `az machinelearningservices environment-container` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices environment-container list](#EnvironmentContainersList)|List|[Parameters](#ParametersEnvironmentContainersList)|[Example](#ExamplesEnvironmentContainersList)|
|[az machinelearningservices environment-container show](#EnvironmentContainersGet)|Get|[Parameters](#ParametersEnvironmentContainersGet)|[Example](#ExamplesEnvironmentContainersGet)|
|[az machinelearningservices environment-container create](#EnvironmentContainersCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersEnvironmentContainersCreateOrUpdate#Create)|[Example](#ExamplesEnvironmentContainersCreateOrUpdate#Create)|
|[az machinelearningservices environment-container update](#EnvironmentContainersCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersEnvironmentContainersCreateOrUpdate#Update)|Not Found|
|[az machinelearningservices environment-container delete](#EnvironmentContainersDelete)|Delete|[Parameters](#ParametersEnvironmentContainersDelete)|[Example](#ExamplesEnvironmentContainersDelete)|

### <a name="CommandsInEnvironmentSpecificationVersions">Commands in `az machinelearningservices environment-specification-version` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices environment-specification-version list](#EnvironmentSpecificationVersionsList)|List|[Parameters](#ParametersEnvironmentSpecificationVersionsList)|[Example](#ExamplesEnvironmentSpecificationVersionsList)|
|[az machinelearningservices environment-specification-version show](#EnvironmentSpecificationVersionsGet)|Get|[Parameters](#ParametersEnvironmentSpecificationVersionsGet)|[Example](#ExamplesEnvironmentSpecificationVersionsGet)|
|[az machinelearningservices environment-specification-version create](#EnvironmentSpecificationVersionsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersEnvironmentSpecificationVersionsCreateOrUpdate#Create)|[Example](#ExamplesEnvironmentSpecificationVersionsCreateOrUpdate#Create)|
|[az machinelearningservices environment-specification-version update](#EnvironmentSpecificationVersionsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersEnvironmentSpecificationVersionsCreateOrUpdate#Update)|Not Found|
|[az machinelearningservices environment-specification-version delete](#EnvironmentSpecificationVersionsDelete)|Delete|[Parameters](#ParametersEnvironmentSpecificationVersionsDelete)|[Example](#ExamplesEnvironmentSpecificationVersionsDelete)|

### <a name="CommandsInJobs">Commands in `az machinelearningservices job` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices job list](#JobsList)|List|[Parameters](#ParametersJobsList)|[Example](#ExamplesJobsList)|
|[az machinelearningservices job show](#JobsGet)|Get|[Parameters](#ParametersJobsGet)|[Example](#ExamplesJobsGet)|
|[az machinelearningservices job create](#JobsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersJobsCreateOrUpdate#Create)|[Example](#ExamplesJobsCreateOrUpdate#Create)|
|[az machinelearningservices job update](#JobsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersJobsCreateOrUpdate#Update)|Not Found|
|[az machinelearningservices job delete](#JobsDelete)|Delete|[Parameters](#ParametersJobsDelete)|[Example](#ExamplesJobsDelete)|
|[az machinelearningservices job cancel](#JobsCancel)|Cancel|[Parameters](#ParametersJobsCancel)|[Example](#ExamplesJobsCancel)|
|[az machinelearningservices job poll](#JobsPoll)|Poll|[Parameters](#ParametersJobsPoll)|[Example](#ExamplesJobsPoll)|

### <a name="CommandsInLabelingJobs">Commands in `az machinelearningservices labeling-job` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices labeling-job list](#LabelingJobsList)|List|[Parameters](#ParametersLabelingJobsList)|[Example](#ExamplesLabelingJobsList)|
|[az machinelearningservices labeling-job show](#LabelingJobsGet)|Get|[Parameters](#ParametersLabelingJobsGet)|[Example](#ExamplesLabelingJobsGet)|
|[az machinelearningservices labeling-job create](#LabelingJobsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersLabelingJobsCreateOrUpdate#Create)|[Example](#ExamplesLabelingJobsCreateOrUpdate#Create)|
|[az machinelearningservices labeling-job update](#LabelingJobsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersLabelingJobsCreateOrUpdate#Update)|Not Found|
|[az machinelearningservices labeling-job delete](#LabelingJobsDelete)|Delete|[Parameters](#ParametersLabelingJobsDelete)|[Example](#ExamplesLabelingJobsDelete)|
|[az machinelearningservices labeling-job export-label](#LabelingJobsExportLabels)|ExportLabels|[Parameters](#ParametersLabelingJobsExportLabels)|[Example](#ExamplesLabelingJobsExportLabels)|
|[az machinelearningservices labeling-job pause](#LabelingJobsPause)|Pause|[Parameters](#ParametersLabelingJobsPause)|[Example](#ExamplesLabelingJobsPause)|
|[az machinelearningservices labeling-job resume](#LabelingJobsResume)|Resume|[Parameters](#ParametersLabelingJobsResume)|[Example](#ExamplesLabelingJobsResume)|
|[az machinelearningservices labeling-job show-export-summary](#LabelingJobsGetExportSummary)|GetExportSummary|[Parameters](#ParametersLabelingJobsGetExportSummary)|[Example](#ExamplesLabelingJobsGetExportSummary)|

### <a name="CommandsInLinkedServices">Commands in `az machinelearningservices linked-service` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices linked-service list](#LinkedServicesList)|List|[Parameters](#ParametersLinkedServicesList)|[Example](#ExamplesLinkedServicesList)|
|[az machinelearningservices linked-service show](#LinkedServicesGet)|Get|[Parameters](#ParametersLinkedServicesGet)|[Example](#ExamplesLinkedServicesGet)|
|[az machinelearningservices linked-service create](#LinkedServicesCreate)|Create|[Parameters](#ParametersLinkedServicesCreate)|[Example](#ExamplesLinkedServicesCreate)|
|[az machinelearningservices linked-service delete](#LinkedServicesDelete)|Delete|[Parameters](#ParametersLinkedServicesDelete)|[Example](#ExamplesLinkedServicesDelete)|

### <a name="CommandsInMachineLearningCompute">Commands in `az machinelearningservices machine-learning-compute` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices machine-learning-compute list](#MachineLearningComputeListByWorkspace)|ListByWorkspace|[Parameters](#ParametersMachineLearningComputeListByWorkspace)|[Example](#ExamplesMachineLearningComputeListByWorkspace)|
|[az machinelearningservices machine-learning-compute show](#MachineLearningComputeGet)|Get|[Parameters](#ParametersMachineLearningComputeGet)|[Example](#ExamplesMachineLearningComputeGet)|
|[az machinelearningservices machine-learning-compute aks create](#MachineLearningComputeCreateOrUpdate#Create#AKS)|CreateOrUpdate#Create#AKS|[Parameters](#ParametersMachineLearningComputeCreateOrUpdate#Create#AKS)|[Example](#ExamplesMachineLearningComputeCreateOrUpdate#Create#AKS)|
|[az machinelearningservices machine-learning-compute aml-compute create](#MachineLearningComputeCreateOrUpdate#Create#AmlCompute)|CreateOrUpdate#Create#AmlCompute|[Parameters](#ParametersMachineLearningComputeCreateOrUpdate#Create#AmlCompute)|[Example](#ExamplesMachineLearningComputeCreateOrUpdate#Create#AmlCompute)|
|[az machinelearningservices machine-learning-compute compute-instance create](#MachineLearningComputeCreateOrUpdate#Create#ComputeInstance)|CreateOrUpdate#Create#ComputeInstance|[Parameters](#ParametersMachineLearningComputeCreateOrUpdate#Create#ComputeInstance)|[Example](#ExamplesMachineLearningComputeCreateOrUpdate#Create#ComputeInstance)|
|[az machinelearningservices machine-learning-compute data-factory create](#MachineLearningComputeCreateOrUpdate#Create#DataFactory)|CreateOrUpdate#Create#DataFactory|[Parameters](#ParametersMachineLearningComputeCreateOrUpdate#Create#DataFactory)|[Example](#ExamplesMachineLearningComputeCreateOrUpdate#Create#DataFactory)|
|[az machinelearningservices machine-learning-compute data-lake-analytics create](#MachineLearningComputeCreateOrUpdate#Create#DataLakeAnalytics)|CreateOrUpdate#Create#DataLakeAnalytics|[Parameters](#ParametersMachineLearningComputeCreateOrUpdate#Create#DataLakeAnalytics)|[Example](#ExamplesMachineLearningComputeCreateOrUpdate#Create#DataLakeAnalytics)|
|[az machinelearningservices machine-learning-compute databricks create](#MachineLearningComputeCreateOrUpdate#Create#Databricks)|CreateOrUpdate#Create#Databricks|[Parameters](#ParametersMachineLearningComputeCreateOrUpdate#Create#Databricks)|[Example](#ExamplesMachineLearningComputeCreateOrUpdate#Create#Databricks)|
|[az machinelearningservices machine-learning-compute hd-insight create](#MachineLearningComputeCreateOrUpdate#Create#HDInsight)|CreateOrUpdate#Create#HDInsight|[Parameters](#ParametersMachineLearningComputeCreateOrUpdate#Create#HDInsight)|[Example](#ExamplesMachineLearningComputeCreateOrUpdate#Create#HDInsight)|
|[az machinelearningservices machine-learning-compute virtual-machine create](#MachineLearningComputeCreateOrUpdate#Create#VirtualMachine)|CreateOrUpdate#Create#VirtualMachine|[Parameters](#ParametersMachineLearningComputeCreateOrUpdate#Create#VirtualMachine)|[Example](#ExamplesMachineLearningComputeCreateOrUpdate#Create#VirtualMachine)|
|[az machinelearningservices machine-learning-compute update](#MachineLearningComputeUpdate)|Update|[Parameters](#ParametersMachineLearningComputeUpdate)|[Example](#ExamplesMachineLearningComputeUpdate)|
|[az machinelearningservices machine-learning-compute delete](#MachineLearningComputeDelete)|Delete|[Parameters](#ParametersMachineLearningComputeDelete)|[Example](#ExamplesMachineLearningComputeDelete)|
|[az machinelearningservices machine-learning-compute list-key](#MachineLearningComputeListKeys)|ListKeys|[Parameters](#ParametersMachineLearningComputeListKeys)|[Example](#ExamplesMachineLearningComputeListKeys)|
|[az machinelearningservices machine-learning-compute list-node](#MachineLearningComputeListNodes)|ListNodes|[Parameters](#ParametersMachineLearningComputeListNodes)|[Example](#ExamplesMachineLearningComputeListNodes)|
|[az machinelearningservices machine-learning-compute restart](#MachineLearningComputeRestart)|Restart|[Parameters](#ParametersMachineLearningComputeRestart)|[Example](#ExamplesMachineLearningComputeRestart)|
|[az machinelearningservices machine-learning-compute start](#MachineLearningComputeStart)|Start|[Parameters](#ParametersMachineLearningComputeStart)|[Example](#ExamplesMachineLearningComputeStart)|
|[az machinelearningservices machine-learning-compute stop](#MachineLearningComputeStop)|Stop|[Parameters](#ParametersMachineLearningComputeStop)|[Example](#ExamplesMachineLearningComputeStop)|

### <a name="CommandsInMachineLearningService">Commands in `az machinelearningservices machine-learning-service` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices machine-learning-service list](#MachineLearningServiceListByWorkspace)|ListByWorkspace|[Parameters](#ParametersMachineLearningServiceListByWorkspace)|[Example](#ExamplesMachineLearningServiceListByWorkspace)|
|[az machinelearningservices machine-learning-service show](#MachineLearningServiceGet)|Get|[Parameters](#ParametersMachineLearningServiceGet)|[Example](#ExamplesMachineLearningServiceGet)|
|[az machinelearningservices machine-learning-service create](#MachineLearningServiceCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersMachineLearningServiceCreateOrUpdate#Create)|[Example](#ExamplesMachineLearningServiceCreateOrUpdate#Create)|
|[az machinelearningservices machine-learning-service update](#MachineLearningServiceCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersMachineLearningServiceCreateOrUpdate#Update)|Not Found|
|[az machinelearningservices machine-learning-service delete](#MachineLearningServiceDelete)|Delete|[Parameters](#ParametersMachineLearningServiceDelete)|[Example](#ExamplesMachineLearningServiceDelete)|

### <a name="CommandsInModelContainers">Commands in `az machinelearningservices model-container` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices model-container list](#ModelContainersList)|List|[Parameters](#ParametersModelContainersList)|[Example](#ExamplesModelContainersList)|
|[az machinelearningservices model-container show](#ModelContainersGet)|Get|[Parameters](#ParametersModelContainersGet)|[Example](#ExamplesModelContainersGet)|
|[az machinelearningservices model-container create](#ModelContainersCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersModelContainersCreateOrUpdate#Create)|[Example](#ExamplesModelContainersCreateOrUpdate#Create)|
|[az machinelearningservices model-container update](#ModelContainersCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersModelContainersCreateOrUpdate#Update)|Not Found|
|[az machinelearningservices model-container delete](#ModelContainersDelete)|Delete|[Parameters](#ParametersModelContainersDelete)|[Example](#ExamplesModelContainersDelete)|

### <a name="CommandsInModelVersions">Commands in `az machinelearningservices model-version` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices model-version list](#ModelVersionsList)|List|[Parameters](#ParametersModelVersionsList)|[Example](#ExamplesModelVersionsList)|
|[az machinelearningservices model-version show](#ModelVersionsGet)|Get|[Parameters](#ParametersModelVersionsGet)|[Example](#ExamplesModelVersionsGet)|
|[az machinelearningservices model-version create](#ModelVersionsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersModelVersionsCreateOrUpdate#Create)|[Example](#ExamplesModelVersionsCreateOrUpdate#Create)|
|[az machinelearningservices model-version update](#ModelVersionsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersModelVersionsCreateOrUpdate#Update)|Not Found|
|[az machinelearningservices model-version delete](#ModelVersionsDelete)|Delete|[Parameters](#ParametersModelVersionsDelete)|[Example](#ExamplesModelVersionsDelete)|

### <a name="CommandsInNotebooks">Commands in `az machinelearningservices notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices notebook list-key](#NotebooksListKeys)|ListKeys|[Parameters](#ParametersNotebooksListKeys)|[Example](#ExamplesNotebooksListKeys)|
|[az machinelearningservices notebook prepare](#NotebooksPrepare)|Prepare|[Parameters](#ParametersNotebooksPrepare)|[Example](#ExamplesNotebooksPrepare)|

### <a name="CommandsInPrivateEndpointConnections">Commands in `az machinelearningservices private-endpoint-connection` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices private-endpoint-connection show](#PrivateEndpointConnectionsGet)|Get|[Parameters](#ParametersPrivateEndpointConnectionsGet)|[Example](#ExamplesPrivateEndpointConnectionsGet)|
|[az machinelearningservices private-endpoint-connection delete](#PrivateEndpointConnectionsDelete)|Delete|[Parameters](#ParametersPrivateEndpointConnectionsDelete)|[Example](#ExamplesPrivateEndpointConnectionsDelete)|
|[az machinelearningservices private-endpoint-connection put](#PrivateEndpointConnectionsPut)|Put|[Parameters](#ParametersPrivateEndpointConnectionsPut)|[Example](#ExamplesPrivateEndpointConnectionsPut)|

### <a name="CommandsInPrivateLinkResources">Commands in `az machinelearningservices private-link-resource` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices private-link-resource list](#PrivateLinkResourcesListByWorkspace)|ListByWorkspace|[Parameters](#ParametersPrivateLinkResourcesListByWorkspace)|[Example](#ExamplesPrivateLinkResourcesListByWorkspace)|

### <a name="CommandsInQuotas">Commands in `az machinelearningservices quota` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices quota list](#QuotasList)|List|[Parameters](#ParametersQuotasList)|[Example](#ExamplesQuotasList)|
|[az machinelearningservices quota update](#QuotasUpdate)|Update|[Parameters](#ParametersQuotasUpdate)|[Example](#ExamplesQuotasUpdate)|

### <a name="CommandsInUsages">Commands in `az machinelearningservices usage` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices usage list](#UsagesList)|List|[Parameters](#ParametersUsagesList)|[Example](#ExamplesUsagesList)|

### <a name="CommandsInVirtualMachineSizes">Commands in `az machinelearningservices virtual-machine-size` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices virtual-machine-size list](#VirtualMachineSizesList)|List|[Parameters](#ParametersVirtualMachineSizesList)|[Example](#ExamplesVirtualMachineSizesList)|

### <a name="CommandsInWorkspaces">Commands in `az machinelearningservices workspace` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices workspace list](#WorkspacesListByResourceGroup)|ListByResourceGroup|[Parameters](#ParametersWorkspacesListByResourceGroup)|[Example](#ExamplesWorkspacesListByResourceGroup)|
|[az machinelearningservices workspace list](#WorkspacesListBySubscription)|ListBySubscription|[Parameters](#ParametersWorkspacesListBySubscription)|[Example](#ExamplesWorkspacesListBySubscription)|
|[az machinelearningservices workspace show](#WorkspacesGet)|Get|[Parameters](#ParametersWorkspacesGet)|[Example](#ExamplesWorkspacesGet)|
|[az machinelearningservices workspace create](#WorkspacesCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersWorkspacesCreateOrUpdate#Create)|[Example](#ExamplesWorkspacesCreateOrUpdate#Create)|
|[az machinelearningservices workspace update](#WorkspacesUpdate)|Update|[Parameters](#ParametersWorkspacesUpdate)|[Example](#ExamplesWorkspacesUpdate)|
|[az machinelearningservices workspace delete](#WorkspacesDelete)|Delete|[Parameters](#ParametersWorkspacesDelete)|[Example](#ExamplesWorkspacesDelete)|
|[az machinelearningservices workspace list-key](#WorkspacesListKeys)|ListKeys|[Parameters](#ParametersWorkspacesListKeys)|[Example](#ExamplesWorkspacesListKeys)|
|[az machinelearningservices workspace resync-key](#WorkspacesResyncKeys)|ResyncKeys|[Parameters](#ParametersWorkspacesResyncKeys)|[Example](#ExamplesWorkspacesResyncKeys)|

### <a name="CommandsInWorkspaceConnections">Commands in `az machinelearningservices workspace-connection` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices workspace-connection list](#WorkspaceConnectionsList)|List|[Parameters](#ParametersWorkspaceConnectionsList)|[Example](#ExamplesWorkspaceConnectionsList)|
|[az machinelearningservices workspace-connection show](#WorkspaceConnectionsGet)|Get|[Parameters](#ParametersWorkspaceConnectionsGet)|[Example](#ExamplesWorkspaceConnectionsGet)|
|[az machinelearningservices workspace-connection create](#WorkspaceConnectionsCreate)|Create|[Parameters](#ParametersWorkspaceConnectionsCreate)|[Example](#ExamplesWorkspaceConnectionsCreate)|
|[az machinelearningservices workspace-connection delete](#WorkspaceConnectionsDelete)|Delete|[Parameters](#ParametersWorkspaceConnectionsDelete)|[Example](#ExamplesWorkspaceConnectionsDelete)|

### <a name="CommandsInWorkspaceFeatures">Commands in `az machinelearningservices workspace-feature` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az machinelearningservices workspace-feature list](#WorkspaceFeaturesList)|List|[Parameters](#ParametersWorkspaceFeaturesList)|[Example](#ExamplesWorkspaceFeaturesList)|


## COMMAND DETAILS

### group `az machinelearningservices`
#### <a name="ListSkus">Command `az machinelearningservices list-sku`</a>

##### <a name="ExamplesListSkus">Example</a>
```
az machinelearningservices list-sku
```
##### <a name="ParametersListSkus">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
### group `az machinelearningservices code-container`
#### <a name="CodeContainersList">Command `az machinelearningservices code-container list`</a>

##### <a name="ExamplesCodeContainersList">Example</a>
```
az machinelearningservices code-container list --skiptoken "skiptoken" --resource-group "testrg123" --workspace-name \
"testworkspace"
```
##### <a name="ParametersCodeContainersList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--skiptoken**|string|Continuation token for pagination.|skiptoken|$skiptoken|

#### <a name="CodeContainersGet">Command `az machinelearningservices code-container show`</a>

##### <a name="ExamplesCodeContainersGet">Example</a>
```
az machinelearningservices code-container show --name "testContainer" --resource-group "testrg123" --workspace-name \
"testworkspace"
```
##### <a name="ParametersCodeContainersGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="CodeContainersCreateOrUpdate#Create">Command `az machinelearningservices code-container create`</a>

##### <a name="ExamplesCodeContainersCreateOrUpdate#Create">Example</a>
```
az machinelearningservices code-container create --name "testContainer" --properties description="string" \
tags={"tag1":"value1","tag2":"value2"} --resource-group "testrg123" --workspace-name "testworkspace"
```
##### <a name="ParametersCodeContainersCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--properties**|dictionary|Dictionary of <string>|properties|properties|
|**--tags**|dictionary|Dictionary of <string>|tags|tags|
|**--description**|string||description|description|

#### <a name="CodeContainersCreateOrUpdate#Update">Command `az machinelearningservices code-container update`</a>

##### <a name="ParametersCodeContainersCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--properties**|dictionary|Dictionary of <string>|properties|properties|
|**--tags**|dictionary|Dictionary of <string>|tags|tags|
|**--description**|string||description|description|

#### <a name="CodeContainersDelete">Command `az machinelearningservices code-container delete`</a>

##### <a name="ExamplesCodeContainersDelete">Example</a>
```
az machinelearningservices code-container delete --name "testContainer" --resource-group "testrg123" --workspace-name \
"testworkspace"
```
##### <a name="ParametersCodeContainersDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

### group `az machinelearningservices code-version`
#### <a name="CodeVersionsList">Command `az machinelearningservices code-version list`</a>

##### <a name="ExamplesCodeVersionsList">Example</a>
```
az machinelearningservices code-version list --name "testContainer" --skiptoken "skiptoken" --resource-group \
"testrg123" --workspace-name "testworkspace"
```
##### <a name="ParametersCodeVersionsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--skiptoken**|string|Continuation token for pagination.|skiptoken|$skiptoken|

#### <a name="CodeVersionsGet">Command `az machinelearningservices code-version show`</a>

##### <a name="ExamplesCodeVersionsGet">Example</a>
```
az machinelearningservices code-version show --name "testContainer" --resource-group "testrg123" --version "1" \
--workspace-name "testworkspace"
```
##### <a name="ParametersCodeVersionsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--version**|string|Version identifier.|version|version|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="CodeVersionsCreateOrUpdate#Create">Command `az machinelearningservices code-version create`</a>

##### <a name="ExamplesCodeVersionsCreateOrUpdate#Create">Example</a>
```
az machinelearningservices code-version create --name "testContainer" --properties description="string" \
assetPath={"path":"string","isDirectory":true} datastoreId="string" properties={"prop1":"value1","prop2":"value2"} \
tags={"tag1":"value1","tag2":"value2"} --resource-group "testrg123" --version "1" --workspace-name "testworkspace"
```
##### <a name="ParametersCodeVersionsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--version**|string|Version identifier.|version|version|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--datastore-id**|string|The asset datastoreId|datastore_id|datastoreId|
|**--asset-path**|object|Details of an AssetUri.|asset_path|assetPath|
|**--description**|string|The asset description text.|description|description|
|**--tags**|dictionary|Tag dictionary. Tags can be added, removed, and updated.|tags|tags|
|**--properties**|dictionary|The asset property dictionary.|properties|properties|

#### <a name="CodeVersionsCreateOrUpdate#Update">Command `az machinelearningservices code-version update`</a>

##### <a name="ParametersCodeVersionsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--version**|string|Version identifier.|version|version|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--datastore-id**|string|The asset datastoreId|datastore_id|datastoreId|
|**--asset-path**|object|Details of an AssetUri.|asset_path|assetPath|
|**--description**|string|The asset description text.|description|description|
|**--tags**|dictionary|Tag dictionary. Tags can be added, removed, and updated.|tags|tags|
|**--properties**|dictionary|The asset property dictionary.|properties|properties|

#### <a name="CodeVersionsDelete">Command `az machinelearningservices code-version delete`</a>

##### <a name="ExamplesCodeVersionsDelete">Example</a>
```
az machinelearningservices code-version delete --name "testContainer" --resource-group "testrg123" --version "1" \
--workspace-name "testworkspace"
```
##### <a name="ParametersCodeVersionsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--version**|string|Version identifier.|version|version|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

### group `az machinelearningservices data-container`
#### <a name="DataContainersList">Command `az machinelearningservices data-container list`</a>

##### <a name="ExamplesDataContainersList">Example</a>
```
az machinelearningservices data-container list --resource-group "testrg123" --workspace-name "workspace123"
```
##### <a name="ParametersDataContainersList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--skiptoken**|string|Continuation token for pagination.|skiptoken|$skiptoken|

#### <a name="DataContainersGet">Command `az machinelearningservices data-container show`</a>

##### <a name="ExamplesDataContainersGet">Example</a>
```
az machinelearningservices data-container show --name "datacontainer123" --resource-group "testrg123" --workspace-name \
"workspace123"
```
##### <a name="ParametersDataContainersGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="DataContainersCreateOrUpdate#Create">Command `az machinelearningservices data-container create`</a>

##### <a name="ExamplesDataContainersCreateOrUpdate#Create">Example</a>
```
az machinelearningservices data-container create --name "datacontainer123" --properties description="string" \
properties={"properties1":"value1","properties2":"value2"} tags={"tag1":"value1","tag2":"value2"} --resource-group \
"testrg123" --workspace-name "workspace123"
```
##### <a name="ParametersDataContainersCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--properties**|dictionary|Dictionary of <string>|properties|properties|
|**--tags**|dictionary|Dictionary of <string>|tags|tags|
|**--description**|string||description|description|

#### <a name="DataContainersCreateOrUpdate#Update">Command `az machinelearningservices data-container update`</a>

##### <a name="ParametersDataContainersCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--properties**|dictionary|Dictionary of <string>|properties|properties|
|**--tags**|dictionary|Dictionary of <string>|tags|tags|
|**--description**|string||description|description|

#### <a name="DataContainersDelete">Command `az machinelearningservices data-container delete`</a>

##### <a name="ExamplesDataContainersDelete">Example</a>
```
az machinelearningservices data-container delete --name "datacontainer123" --resource-group "testrg123" \
--workspace-name "workspace123"
```
##### <a name="ParametersDataContainersDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

### group `az machinelearningservices data-version`
#### <a name="DataVersionsList">Command `az machinelearningservices data-version list`</a>

##### <a name="ExamplesDataVersionsList">Example</a>
```
az machinelearningservices data-version list --name "dataset123" --resource-group "testrg123" --workspace-name \
"workspace123"
```
##### <a name="ParametersDataVersionsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--skiptoken**|string|Continuation token for pagination.|skiptoken|$skiptoken|

#### <a name="DataVersionsGet">Command `az machinelearningservices data-version show`</a>

##### <a name="ExamplesDataVersionsGet">Example</a>
```
az machinelearningservices data-version show --name "dataset123" --resource-group "testrg123" --version "456" \
--workspace-name "workspace123"
```
##### <a name="ParametersDataVersionsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--version**|string|Version identifier.|version|version|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="DataVersionsCreateOrUpdate#Create">Command `az machinelearningservices data-version create`</a>

##### <a name="ExamplesDataVersionsCreateOrUpdate#Create">Example</a>
```
az machinelearningservices data-version create --name "dataset123" --properties description="string" \
assetPath={"path":"string","isDirectory":false} datasetType="Simple" datastoreId="string" \
properties={"properties1":"value1","properties2":"value2"} tags={"tag1":"value1","tag2":"value2"} --resource-group \
"testrg123" --version "456" --workspace-name "workspace123"
```
##### <a name="ParametersDataVersionsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--version**|string|Version identifier.|version|version|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--dataset-type**|choice|The Format of dataset.|dataset_type|datasetType|
|**--datastore-id**|string|The asset datastoreId|datastore_id|datastoreId|
|**--asset-path**|object|Details of an AssetUri.|asset_path|assetPath|
|**--description**|string|The asset description text.|description|description|
|**--tags**|dictionary|Tag dictionary. Tags can be added, removed, and updated.|tags|tags|
|**--properties**|dictionary|The asset property dictionary.|properties|properties|

#### <a name="DataVersionsCreateOrUpdate#Update">Command `az machinelearningservices data-version update`</a>

##### <a name="ParametersDataVersionsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--version**|string|Version identifier.|version|version|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--dataset-type**|choice|The Format of dataset.|dataset_type|datasetType|
|**--datastore-id**|string|The asset datastoreId|datastore_id|datastoreId|
|**--asset-path**|object|Details of an AssetUri.|asset_path|assetPath|
|**--description**|string|The asset description text.|description|description|
|**--tags**|dictionary|Tag dictionary. Tags can be added, removed, and updated.|tags|tags|
|**--properties**|dictionary|The asset property dictionary.|properties|properties|

#### <a name="DataVersionsDelete">Command `az machinelearningservices data-version delete`</a>

##### <a name="ExamplesDataVersionsDelete">Example</a>
```
az machinelearningservices data-version delete --name "dataset123" --resource-group "testrg123" --version "456" \
--workspace-name "workspace123"
```
##### <a name="ParametersDataVersionsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--version**|string|Version identifier.|version|version|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

### group `az machinelearningservices datastore`
#### <a name="DatastoresList">Command `az machinelearningservices datastore list`</a>

##### <a name="ExamplesDatastoresList">Example</a>
```
az machinelearningservices datastore list --resource-group "testrg123" --workspace-name "testworkspace"
```
##### <a name="ParametersDatastoresList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--skiptoken**|string|Continuation token for pagination.|skiptoken|$skiptoken|
|**--count**|integer|Maximum number of results to return.|count|count|
|**--is-default**|boolean|Filter down to the workspace default datastore.|is_default|isDefault|
|**--names**|array|Names of datastores to return.|names|names|
|**--search-text**|string|Text to search for in the datastore names.|search_text|searchText|
|**--order-by**|string|Order by property (createdtime | modifiedtime | name).|order_by|orderBy|
|**--order-by-asc**|boolean|Order by property in ascending order.|order_by_asc|orderByAsc|

#### <a name="DatastoresGet">Command `az machinelearningservices datastore show`</a>

##### <a name="ExamplesDatastoresGet">Example</a>
```
az machinelearningservices datastore show --name "testDatastore" --resource-group "testrg123" --workspace-name \
"testworkspace"
```
##### <a name="ParametersDatastoresGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Datastore name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="DatastoresCreateOrUpdate#Create">Command `az machinelearningservices datastore create`</a>

##### <a name="ExamplesDatastoresCreateOrUpdate#Create">Example</a>
```
az machinelearningservices datastore create --name "testDatastore" --properties description="string" \
contents={"type":"AzureBlob","azureDataLake":{"credentials":{"type":"AccountKey","accountKey":{"key":"string"},"certifi\
cate":{"authorityUrl":"string","certificate":"string","clientId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","resourceUri":"\
string","tenantId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","thumbprint":"string"},"sas":{"sasToken":"string"},"servicePr\
incipal":{"authorityUrl":"string","clientId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","clientSecret":"string","resourceUr\
i":"string","tenantId":"3fa85f64-5717-4562-b3fc-2c963f66afa6"},"sqlAdmin":{"password":"string","userId":"string"}},"sto\
reName":"string"},"azureMySql":{"credentials":{"type":"AccountKey","accountKey":{"key":"string"},"certificate":{"author\
ityUrl":"string","certificate":"string","clientId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","resourceUri":"string","tenan\
tId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","thumbprint":"string"},"sas":{"sasToken":"string"},"servicePrincipal":{"aut\
horityUrl":"string","clientId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","clientSecret":"string","resourceUri":"string","t\
enantId":"3fa85f64-5717-4562-b3fc-2c963f66afa6"},"sqlAdmin":{"password":"string","userId":"string"}},"databaseName":"st\
ring","endpoint":"database.windows.net","portNumber":0,"serverName":"string"},"azurePostgreSql":{"credentials":{"type":\
"AccountKey","accountKey":{"key":"string"},"certificate":{"authorityUrl":"string","certificate":"string","clientId":"3f\
a85f64-5717-4562-b3fc-2c963f66afa6","resourceUri":"string","tenantId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","thumbprin\
t":"string"},"sas":{"sasToken":"string"},"servicePrincipal":{"authorityUrl":"string","clientId":"3fa85f64-5717-4562-b3f\
c-2c963f66afa6","clientSecret":"string","resourceUri":"string","tenantId":"3fa85f64-5717-4562-b3fc-2c963f66afa6"},"sqlA\
dmin":{"password":"string","userId":"string"}},"databaseName":"string","enableSSL":true,"endpoint":"database.windows.ne\
t","portNumber":0,"serverName":"string"},"azureSqlDatabase":{"credentials":{"type":"AccountKey","accountKey":{"key":"st\
ring"},"certificate":{"authorityUrl":"string","certificate":"string","clientId":"3fa85f64-5717-4562-b3fc-2c963f66afa6",\
"resourceUri":"string","tenantId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","thumbprint":"string"},"sas":{"sasToken":"stri\
ng"},"servicePrincipal":{"authorityUrl":"string","clientId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","clientSecret":"stri\
ng","resourceUri":"string","tenantId":"3fa85f64-5717-4562-b3fc-2c963f66afa6"},"sqlAdmin":{"password":"string","userId":\
"string"}},"databaseName":"string","endpoint":"database.windows.net","portNumber":0,"serverName":"string"},"azureStorag\
e":{"accountName":"string","blobCacheTimeout":0,"containerName":"string","credentials":{"type":"AccountKey","accountKey\
":{"key":"string"},"certificate":{"authorityUrl":"string","certificate":"string","clientId":"3fa85f64-5717-4562-b3fc-2c\
963f66afa6","resourceUri":"string","tenantId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","thumbprint":"string"},"sas":{"sas\
Token":"string"},"servicePrincipal":{"authorityUrl":"string","clientId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","clientS\
ecret":"string","resourceUri":"string","tenantId":"3fa85f64-5717-4562-b3fc-2c963f66afa6"},"sqlAdmin":{"password":"strin\
g","userId":"string"}},"endpoint":"core.windows.net","protocol":"https"},"glusterFs":{"serverAddress":"string","volumeN\
ame":"string"}} isDefault=true linkedInfo={"linkedId":"string","linkedResourceName":"string","origin":"Synapse"} \
properties={"additionalProp1":"string","additionalProp2":"string","additionalProp3":"string"} \
tags={"additionalProp1":"string","additionalProp2":"string","additionalProp3":"string"} --resource-group "testrg123" \
--workspace-name "testworkspace"
```
##### <a name="ParametersDatastoresCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Datastore name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--type**|choice|Storage type backing the datastore.|type|type|
|**--is-default**|boolean|Whether this datastore is the default for the workspace.|is_default|isDefault|
|**--linked-info**|object||linked_info|linkedInfo|
|**--properties**|dictionary|Dictionary of <string>|properties|properties|
|**--description**|string|The asset description text.|description|description|
|**--tags**|dictionary|Tag dictionary. Tags can be added, removed, and updated.|tags|tags|
|**--azure-data-lake**|object||azure_data_lake|azureDataLake|
|**--azure-my-sql**|object||azure_my_sql|azureMySql|
|**--azure-postgre-sql**|object||azure_postgre_sql|azurePostgreSql|
|**--azure-sql-database**|object||azure_sql_database|azureSqlDatabase|
|**--azure-storage**|object||azure_storage|azureStorage|
|**--gluster-fs**|object||gluster_fs|glusterFs|

#### <a name="DatastoresCreateOrUpdate#Update">Command `az machinelearningservices datastore update`</a>

##### <a name="ParametersDatastoresCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Datastore name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--type**|choice|Storage type backing the datastore.|type|type|
|**--is-default**|boolean|Whether this datastore is the default for the workspace.|is_default|isDefault|
|**--linked-info**|object||linked_info|linkedInfo|
|**--properties**|dictionary|Dictionary of <string>|properties|properties|
|**--description**|string|The asset description text.|description|description|
|**--tags**|dictionary|Tag dictionary. Tags can be added, removed, and updated.|tags|tags|
|**--azure-data-lake**|object||azure_data_lake|azureDataLake|
|**--azure-my-sql**|object||azure_my_sql|azureMySql|
|**--azure-postgre-sql**|object||azure_postgre_sql|azurePostgreSql|
|**--azure-sql-database**|object||azure_sql_database|azureSqlDatabase|
|**--azure-storage**|object||azure_storage|azureStorage|
|**--gluster-fs**|object||gluster_fs|glusterFs|

#### <a name="DatastoresDelete">Command `az machinelearningservices datastore delete`</a>

##### <a name="ExamplesDatastoresDelete">Example</a>
```
az machinelearningservices datastore delete --name "testDatastore" --resource-group "testrg123" --workspace-name \
"testworkspace"
```
##### <a name="ParametersDatastoresDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Datastore name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="DatastoresListSecrets">Command `az machinelearningservices datastore list-secret`</a>

##### <a name="ExamplesDatastoresListSecrets">Example</a>
```
az machinelearningservices datastore list-secret --name "testDatastore" --resource-group "testrg123" --workspace-name \
"testworkspace"
```
##### <a name="ParametersDatastoresListSecrets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Datastore name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

### group `az machinelearningservices environment-container`
#### <a name="EnvironmentContainersList">Command `az machinelearningservices environment-container list`</a>

##### <a name="ExamplesEnvironmentContainersList">Example</a>
```
az machinelearningservices environment-container list --skiptoken "skiptoken" --resource-group "testrg123" \
--workspace-name "testworkspace"
```
##### <a name="ParametersEnvironmentContainersList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--skiptoken**|string|Continuation token for pagination.|skiptoken|$skiptoken|

#### <a name="EnvironmentContainersGet">Command `az machinelearningservices environment-container show`</a>

##### <a name="ExamplesEnvironmentContainersGet">Example</a>
```
az machinelearningservices environment-container show --name "testContainer" --resource-group "testrg123" \
--workspace-name "testworkspace"
```
##### <a name="ParametersEnvironmentContainersGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="EnvironmentContainersCreateOrUpdate#Create">Command `az machinelearningservices environment-container create`</a>

##### <a name="ExamplesEnvironmentContainersCreateOrUpdate#Create">Example</a>
```
az machinelearningservices environment-container create --name "testContainer" --properties description="string" \
properties={"additionalProp1":"string","additionalProp2":"string","additionalProp3":"string"} \
tags={"additionalProp1":"string","additionalProp2":"string","additionalProp3":"string"} --resource-group "testrg123" \
--workspace-name "testworkspace"
```
##### <a name="ParametersEnvironmentContainersCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--properties**|dictionary|Dictionary of <string>|properties|properties|
|**--tags**|dictionary|Dictionary of <string>|tags|tags|
|**--description**|string||description|description|

#### <a name="EnvironmentContainersCreateOrUpdate#Update">Command `az machinelearningservices environment-container update`</a>

##### <a name="ParametersEnvironmentContainersCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--properties**|dictionary|Dictionary of <string>|properties|properties|
|**--tags**|dictionary|Dictionary of <string>|tags|tags|
|**--description**|string||description|description|

#### <a name="EnvironmentContainersDelete">Command `az machinelearningservices environment-container delete`</a>

##### <a name="ExamplesEnvironmentContainersDelete">Example</a>
```
az machinelearningservices environment-container delete --name "testContainer" --resource-group "testrg123" \
--workspace-name "testworkspace"
```
##### <a name="ParametersEnvironmentContainersDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

### group `az machinelearningservices environment-specification-version`
#### <a name="EnvironmentSpecificationVersionsList">Command `az machinelearningservices environment-specification-version list`</a>

##### <a name="ExamplesEnvironmentSpecificationVersionsList">Example</a>
```
az machinelearningservices environment-specification-version list --name "testContainer" --skiptoken "skiptoken" \
--resource-group "testrg123" --workspace-name "testworkspace"
```
##### <a name="ParametersEnvironmentSpecificationVersionsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string||name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--orderby**|string||orderby|$orderby|
|**--top**|string||top|$top|
|**--skiptoken**|string|Continuation token for pagination.|skiptoken|$skiptoken|

#### <a name="EnvironmentSpecificationVersionsGet">Command `az machinelearningservices environment-specification-version show`</a>

##### <a name="ExamplesEnvironmentSpecificationVersionsGet">Example</a>
```
az machinelearningservices environment-specification-version show --name "testContainer" --resource-group "testrg123" \
--version "1" --workspace-name "testworkspace"
```
##### <a name="ParametersEnvironmentSpecificationVersionsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--version**|string|Version identifier.|version|version|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="EnvironmentSpecificationVersionsCreateOrUpdate#Create">Command `az machinelearningservices environment-specification-version create`</a>

##### <a name="ExamplesEnvironmentSpecificationVersionsCreateOrUpdate#Create">Example</a>
```
az machinelearningservices environment-specification-version create --name "testContainer" --properties \
description="string" assetPath={"path":"string","isDirectory":true} condaFile="string" datastoreId="string" \
docker={"type":"Build"} properties={"additionalProp1":"string","additionalProp2":"string","additionalProp3":"string"} \
tags={"additionalProp1":"string","additionalProp2":"string","additionalProp3":"string"} --resource-group "testrg123" \
--version "1" --workspace-name "testworkspace"
```
##### <a name="ParametersEnvironmentSpecificationVersionsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string||name|name|
|**--version**|string||version|version|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--docker**|object|Class to represent configuration settings for Docker|docker|docker|
|**--conda-file**|string|Standard configuration file used by conda that lets you install any kind of package, including Python, R, and C/C++ packages <see href="https://repo2docker.readthedocs.io/en/latest/config_files.html#environment-yml-install-a-conda-environment" />|conda_file|condaFile|
|**--datastore-id**|string|The asset datastoreId|datastore_id|datastoreId|
|**--asset-path**|object|Details of an AssetUri.|asset_path|assetPath|
|**--description**|string|The asset description text.|description|description|
|**--tags**|dictionary|Tag dictionary. Tags can be added, removed, and updated.|tags|tags|
|**--properties**|dictionary|The asset property dictionary.|properties|properties|

#### <a name="EnvironmentSpecificationVersionsCreateOrUpdate#Update">Command `az machinelearningservices environment-specification-version update`</a>

##### <a name="ParametersEnvironmentSpecificationVersionsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string||name|name|
|**--version**|string||version|version|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--docker**|object|Class to represent configuration settings for Docker|docker|docker|
|**--conda-file**|string|Standard configuration file used by conda that lets you install any kind of package, including Python, R, and C/C++ packages <see href="https://repo2docker.readthedocs.io/en/latest/config_files.html#environment-yml-install-a-conda-environment" />|conda_file|condaFile|
|**--datastore-id**|string|The asset datastoreId|datastore_id|datastoreId|
|**--asset-path**|object|Details of an AssetUri.|asset_path|assetPath|
|**--description**|string|The asset description text.|description|description|
|**--tags**|dictionary|Tag dictionary. Tags can be added, removed, and updated.|tags|tags|
|**--properties**|dictionary|The asset property dictionary.|properties|properties|

#### <a name="EnvironmentSpecificationVersionsDelete">Command `az machinelearningservices environment-specification-version delete`</a>

##### <a name="ExamplesEnvironmentSpecificationVersionsDelete">Example</a>
```
az machinelearningservices environment-specification-version delete --name "testContainer" --resource-group \
"testrg123" --version "1" --workspace-name "testworkspace"
```
##### <a name="ParametersEnvironmentSpecificationVersionsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--version**|string|Version identifier.|version|version|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

### group `az machinelearningservices job`
#### <a name="JobsList">Command `az machinelearningservices job list`</a>

##### <a name="ExamplesJobsList">Example</a>
```
az machinelearningservices job list --skiptoken "skiptoken" --resource-group "testrg123" --workspace-name \
"testworkspace"
```
##### <a name="ExamplesJobsList">Example</a>
```
az machinelearningservices job list --skiptoken "skiptoken" --resource-group "testrg123" --workspace-name \
"testworkspace"
```
##### <a name="ParametersJobsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--skiptoken**|string|Continuation token for pagination.|skiptoken|$skiptoken|

#### <a name="JobsGet">Command `az machinelearningservices job show`</a>

##### <a name="ExamplesJobsGet">Example</a>
```
az machinelearningservices job show --id "testContainer" --resource-group "testrg123" --workspace-name "testworkspace"
```
##### <a name="ExamplesJobsGet">Example</a>
```
az machinelearningservices job show --id "testContainer" --resource-group "testrg123" --workspace-name "testworkspace"
```
##### <a name="ParametersJobsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|The name and identifier for the Job.|id|id|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="JobsCreateOrUpdate#Create">Command `az machinelearningservices job create`</a>

##### <a name="ExamplesJobsCreateOrUpdate#Create">Example</a>
```
az machinelearningservices job create --properties "{\\"description\\":\\"string\\",\\"properties\\":{\\"additionalProp\
1\\":\\"string\\",\\"additionalProp2\\":\\"string\\",\\"additionalProp3\\":\\"string\\"},\\"tags\\":{\\"additionalProp1\
\\":\\"string\\",\\"additionalProp2\\":\\"string\\",\\"additionalProp3\\":\\"string\\"}}" --id "testContainer" \
--resource-group "testrg123" --workspace-name "testworkspace"
```
##### <a name="ExamplesJobsCreateOrUpdate#Create">Example</a>
```
az machinelearningservices job create --properties "{\\"description\\":\\"string\\",\\"properties\\":{\\"additionalProp\
1\\":\\"string\\",\\"additionalProp2\\":\\"string\\",\\"additionalProp3\\":\\"string\\"},\\"tags\\":{\\"additionalProp1\
\\":\\"string\\",\\"additionalProp2\\":\\"string\\",\\"additionalProp3\\":\\"string\\"}}" --id "testContainer" \
--resource-group "testrg123" --workspace-name "testworkspace"
```
##### <a name="ParametersJobsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|The name and identifier for the Job.|id|id|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--properties**|object|Job base definition|properties|properties|

#### <a name="JobsCreateOrUpdate#Update">Command `az machinelearningservices job update`</a>

##### <a name="ParametersJobsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|The name and identifier for the Job.|id|id|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--properties**|object|Job base definition|properties|properties|

#### <a name="JobsDelete">Command `az machinelearningservices job delete`</a>

##### <a name="ExamplesJobsDelete">Example</a>
```
az machinelearningservices job delete --id "testContainer" --resource-group "testrg123" --workspace-name \
"testworkspace"
```
##### <a name="ExamplesJobsDelete">Example</a>
```
az machinelearningservices job delete --id "testContainer" --resource-group "testrg123" --workspace-name \
"testworkspace"
```
##### <a name="ParametersJobsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|The name and identifier for the Job.|id|id|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="JobsCancel">Command `az machinelearningservices job cancel`</a>

##### <a name="ExamplesJobsCancel">Example</a>
```
az machinelearningservices job cancel --id "testContainer" --resource-group "testrg123" --workspace-name \
"testworkspace"
```
##### <a name="ExamplesJobsCancel">Example</a>
```
az machinelearningservices job cancel --id "testContainer" --resource-group "testrg123" --workspace-name \
"testworkspace"
```
##### <a name="ParametersJobsCancel">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|The name and identifier for the Job.|id|id|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="JobsPoll">Command `az machinelearningservices job poll`</a>

##### <a name="ExamplesJobsPoll">Example</a>
```
az machinelearningservices job poll --operation-id "1" --id "testContainer" --resource-group "testrg123" \
--workspace-name "testworkspace"
```
##### <a name="ExamplesJobsPoll">Example</a>
```
az machinelearningservices job poll --operation-id "1" --id "testContainer" --resource-group "testrg123" \
--workspace-name "testworkspace"
```
##### <a name="ParametersJobsPoll">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|The name and identifier for the Job.|id|id|
|**--operation-id**|string|The operation ID of the async operation to be polled|operation_id|operationId|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

### group `az machinelearningservices labeling-job`
#### <a name="LabelingJobsList">Command `az machinelearningservices labeling-job list`</a>

##### <a name="ExamplesLabelingJobsList">Example</a>
```
az machinelearningservices labeling-job list --skiptoken "skiptoken" --count "10" --resource-group "workspace-1234" \
--workspace-name "testworkspace"
```
##### <a name="ParametersLabelingJobsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--skiptoken**|string|Continuation token for pagination.|skiptoken|$skiptoken|
|**--count**|integer|Number of labeling jobs to return.|count|count|

#### <a name="LabelingJobsGet">Command `az machinelearningservices labeling-job show`</a>

##### <a name="ExamplesLabelingJobsGet">Example</a>
```
az machinelearningservices labeling-job show --id "testLabelingJob" --include-job-instructions true \
--include-label-categories true --resource-group "workspace-1234" --workspace-name "testworkspace"
```
##### <a name="ParametersLabelingJobsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|The name and identifier for the LabelingJob.|id|id|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--include-job-instructions**|boolean|Boolean value to indicate whether to include JobInstructions in response.|include_job_instructions|includeJobInstructions|
|**--include-label-categories**|boolean|Boolean value to indicate Whether to include LabelCategories in response.|include_label_categories|includeLabelCategories|

#### <a name="LabelingJobsCreateOrUpdate#Create">Command `az machinelearningservices labeling-job create`</a>

##### <a name="ExamplesLabelingJobsCreateOrUpdate#Create">Example</a>
```
az machinelearningservices labeling-job create --properties description="string" createdTimeUtc="2020-12-08T01:23:37.11\
8Z" datasetConfiguration={"assetName":"string","datasetVersion":"string","incrementalDatasetRefreshEnabled":true} \
jobInstructions={"uri":"string"} jobType="Labeling" labelCategories={"additionalProp1":{"allowMultiSelect":true,"classe\
s":{"additionalProp1":{"displayName":"string","subclasses":{}},"additionalProp2":{"displayName":"string","subclasses":{\
}},"additionalProp3":{"displayName":"string","subclasses":{}}},"displayName":"string"},"additionalProp2":{"allowMultiSe\
lect":true,"classes":{"additionalProp1":{"displayName":"string","subclasses":{}},"additionalProp2":{"displayName":"stri\
ng","subclasses":{}},"additionalProp3":{"displayName":"string","subclasses":{}}},"displayName":"string"},"additionalPro\
p3":{"allowMultiSelect":true,"classes":{"additionalProp1":{"displayName":"string","subclasses":{}},"additionalProp2":{"\
displayName":"string","subclasses":{}},"additionalProp3":{"displayName":"string","subclasses":{}}},"displayName":"strin\
g"}} labelingJobMediaProperties={"mediaType":"Image"} mlAssistConfiguration={"inferencingComputeBinding":{"computeId":"\
string","nodeCount":0},"mlAssistEnabled":true,"trainingComputeBinding":{"computeId":"string","nodeCount":0}} \
progressMetrics={} projectId="3fa85f64-5717-4562-b3fc-2c963f66afa6" properties={"additionalProp1":"string","additionalP\
rop2":"string","additionalProp3":"string"} status="NotStarted" statusMessages={} tags={"additionalProp1":"string","addi\
tionalProp2":"string","additionalProp3":"string"} --id "testLabelingJob" --resource-group "workspace-1234" \
--workspace-name "testworkspace"
```
##### <a name="ParametersLabelingJobsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|The name and identifier for the LabelingJob.|id|id|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--description**|string|The asset description text.|description|description|
|**--tags**|dictionary|Tag dictionary. Tags can be added, removed, and updated.|tags|tags|
|**--properties**|dictionary|The asset property dictionary.|properties|properties|
|**--label-categories**|dictionary|Label categories of the job.|label_categories|labelCategories|
|**--dataset-configuration**|object|Labeling dataset configuration definition|dataset_configuration|datasetConfiguration|
|**--labeling-job-media-properties**|object|Properties of a labeling job|labeling_job_media_properties|labelingJobMediaProperties|
|**--project-id**|uuid|Internal id of the job(Previously called project).|project_id|projectId|
|**--status**|choice|Status of the job.|status|status|
|**--created-time-utc**|date-time|Created time of the job in UTC timezone.|created_time_utc|createdTimeUtc|
|**--inferencing-compute-binding**|object|Compute binding definition.|inferencing_compute_binding|inferencingComputeBinding|
|**--training-compute-binding**|object|Compute binding definition.|training_compute_binding|trainingComputeBinding|
|**--ml-assist-enabled**|boolean|Indicates whether MLAssist feature is enabled.|ml_assist_enabled|mlAssistEnabled|
|**--uri**|string|The link to a page with detailed labeling instructions for labelers.|uri|uri|

#### <a name="LabelingJobsCreateOrUpdate#Update">Command `az machinelearningservices labeling-job update`</a>

##### <a name="ParametersLabelingJobsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|The name and identifier for the LabelingJob.|id|id|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--description**|string|The asset description text.|description|description|
|**--tags**|dictionary|Tag dictionary. Tags can be added, removed, and updated.|tags|tags|
|**--properties**|dictionary|The asset property dictionary.|properties|properties|
|**--label-categories**|dictionary|Label categories of the job.|label_categories|labelCategories|
|**--dataset-configuration**|object|Labeling dataset configuration definition|dataset_configuration|datasetConfiguration|
|**--labeling-job-media-properties**|object|Properties of a labeling job|labeling_job_media_properties|labelingJobMediaProperties|
|**--project-id**|uuid|Internal id of the job(Previously called project).|project_id|projectId|
|**--status**|choice|Status of the job.|status|status|
|**--created-time-utc**|date-time|Created time of the job in UTC timezone.|created_time_utc|createdTimeUtc|
|**--inferencing-compute-binding**|object|Compute binding definition.|inferencing_compute_binding|inferencingComputeBinding|
|**--training-compute-binding**|object|Compute binding definition.|training_compute_binding|trainingComputeBinding|
|**--ml-assist-enabled**|boolean|Indicates whether MLAssist feature is enabled.|ml_assist_enabled|mlAssistEnabled|
|**--uri**|string|The link to a page with detailed labeling instructions for labelers.|uri|uri|

#### <a name="LabelingJobsDelete">Command `az machinelearningservices labeling-job delete`</a>

##### <a name="ExamplesLabelingJobsDelete">Example</a>
```
az machinelearningservices labeling-job delete --id "testLabelingJob" --resource-group "workspace-1234" \
--workspace-name "testworkspace"
```
##### <a name="ParametersLabelingJobsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|The name and identifier for the LabelingJob.|id|id|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="LabelingJobsExportLabels">Command `az machinelearningservices labeling-job export-label`</a>

##### <a name="ExamplesLabelingJobsExportLabels">Example</a>
```
az machinelearningservices labeling-job export-label --body "CSV" --id "testLabelingJob" --resource-group \
"workspace-1234" --workspace-name "testworkspace"
```
##### <a name="ParametersLabelingJobsExportLabels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|The name and identifier for the LabelingJob.|id|id|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--body**|choice|The desired format of export operation.|body|body|

#### <a name="LabelingJobsPause">Command `az machinelearningservices labeling-job pause`</a>

##### <a name="ExamplesLabelingJobsPause">Example</a>
```
az machinelearningservices labeling-job pause --id "testLabelingJob" --resource-group "workspace-1234" \
--workspace-name "testworkspace"
```
##### <a name="ParametersLabelingJobsPause">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|The name and identifier for the LabelingJob.|id|id|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="LabelingJobsResume">Command `az machinelearningservices labeling-job resume`</a>

##### <a name="ExamplesLabelingJobsResume">Example</a>
```
az machinelearningservices labeling-job resume --id "testLabelingJob" --resource-group "workspace-1234" \
--workspace-name "testworkspace"
```
##### <a name="ParametersLabelingJobsResume">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|The name and identifier for the LabelingJob.|id|id|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="LabelingJobsGetExportSummary">Command `az machinelearningservices labeling-job show-export-summary`</a>

##### <a name="ExamplesLabelingJobsGetExportSummary">Example</a>
```
az machinelearningservices labeling-job show-export-summary --export-id "3fa85f64-5717-4562-b3fc-2c963f66afa6" --id \
"testLabelingJob" --resource-group "workspace-1234" --workspace-name "testworkspace"
```
##### <a name="ParametersLabelingJobsGetExportSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|The name and identifier for the LabelingJob.|id|id|
|**--export-id**|uuid|The unique identifier of Export Labels operation.|export_id|exportId|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

### group `az machinelearningservices linked-service`
#### <a name="LinkedServicesList">Command `az machinelearningservices linked-service list`</a>

##### <a name="ExamplesLinkedServicesList">Example</a>
```
az machinelearningservices linked-service list --resource-group "resourceGroup-1" --workspace-name "workspace-1"
```
##### <a name="ParametersLinkedServicesList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="LinkedServicesGet">Command `az machinelearningservices linked-service show`</a>

##### <a name="ExamplesLinkedServicesGet">Example</a>
```
az machinelearningservices linked-service show --link-name "link-1" --resource-group "resourceGroup-1" \
--workspace-name "workspace-1"
```
##### <a name="ParametersLinkedServicesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--link-name**|string|Friendly name of the linked workspace|link_name|linkName|

#### <a name="LinkedServicesCreate">Command `az machinelearningservices linked-service create`</a>

##### <a name="ExamplesLinkedServicesCreate">Example</a>
```
az machinelearningservices linked-service create --link-name "link-1" --name "link-1" --type "SystemAssigned" \
--location "westus" --properties linked-service-resource-id="/subscriptions/00000000-1111-2222-3333-444444444444/resour\
ceGroups/resourceGroup-1/providers/Microsoft.Synapse/workspaces/Syn-1" --resource-group "resourceGroup-1" \
--workspace-name "workspace-1"
```
##### <a name="ParametersLinkedServicesCreate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--link-name**|string|Friendly name of the linked workspace|link_name|linkName|
|**--name**|string|Friendly name of the linked service|name|name|
|**--location**|string|location of the linked service.|location|location|
|**--properties**|object|LinkedService specific properties.|properties|properties|
|**--type**|sealed-choice|The identity type.|type|type|
|**--user-assigned-identities**|dictionary|The user assigned identities associated with the resource.|user_assigned_identities|userAssignedIdentities|

#### <a name="LinkedServicesDelete">Command `az machinelearningservices linked-service delete`</a>

##### <a name="ExamplesLinkedServicesDelete">Example</a>
```
az machinelearningservices linked-service delete --link-name "link-1" --resource-group "resourceGroup-1" \
--workspace-name "workspace-1"
```
##### <a name="ParametersLinkedServicesDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--link-name**|string|Friendly name of the linked workspace|link_name|linkName|

### group `az machinelearningservices machine-learning-compute`
#### <a name="MachineLearningComputeListByWorkspace">Command `az machinelearningservices machine-learning-compute list`</a>

##### <a name="ExamplesMachineLearningComputeListByWorkspace">Example</a>
```
az machinelearningservices machine-learning-compute list --resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ParametersMachineLearningComputeListByWorkspace">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--skiptoken**|string|Continuation token for pagination.|skiptoken|$skiptoken|

#### <a name="MachineLearningComputeGet">Command `az machinelearningservices machine-learning-compute show`</a>

##### <a name="ExamplesMachineLearningComputeGet">Example</a>
```
az machinelearningservices machine-learning-compute show --compute-name "compute123" --resource-group "testrg123" \
--workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeGet">Example</a>
```
az machinelearningservices machine-learning-compute show --compute-name "compute123" --resource-group "testrg123" \
--workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeGet">Example</a>
```
az machinelearningservices machine-learning-compute show --compute-name "compute123" --resource-group "testrg123" \
--workspace-name "workspaces123"
```
##### <a name="ParametersMachineLearningComputeGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|

#### <a name="MachineLearningComputeCreateOrUpdate#Create#AKS">Command `az machinelearningservices machine-learning-compute aks create`</a>

##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#AKS">Example</a>
```
az machinelearningservices machine-learning-compute aks create --compute-name "compute123" --location "eastus" \
--resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#AKS">Example</a>
```
az machinelearningservices machine-learning-compute aks create --compute-name "compute123" --location "eastus" \
--ak-s-properties "{\\"enableNodePublicIp\\":true,\\"isolatedNetwork\\":false,\\"osType\\":\\"Windows\\",\\"remoteLogin\
PortPublicAccess\\":\\"NotSpecified\\",\\"scaleSettings\\":{\\"maxNodeCount\\":1,\\"minNodeCount\\":0,\\"nodeIdleTimeBe\
foreScaleDown\\":\\"PT5M\\"},\\"virtualMachineImage\\":{\\"id\\":\\"/subscriptions/00000000-0000-0000-0000-000000000000\
/resourceGroups/myResourceGroup/providers/Microsoft.Compute/galleries/myImageGallery/images/myImageDefinition/versions/\
0.0.1\\"},\\"vmPriority\\":\\"Dedicated\\",\\"vmSize\\":\\"STANDARD_NC6\\"}" --resource-group "testrg123" \
--workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#AKS">Example</a>
```
az machinelearningservices machine-learning-compute aks create --compute-name "compute123" --location "eastus" \
--resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#AKS">Example</a>
```
az machinelearningservices machine-learning-compute aks create --compute-name "compute123" --location "eastus" \
--ak-s-properties "{\\"applicationSharingPolicy\\":\\"Personal\\",\\"computeInstanceAuthorizationType\\":\\"personal\\"\
,\\"personalComputeInstanceSettings\\":{\\"assignedUser\\":{\\"objectId\\":\\"00000000-0000-0000-0000-000000000000\\",\
\\"tenantId\\":\\"00000000-0000-0000-0000-000000000000\\"}},\\"sshSettings\\":{\\"sshPublicAccess\\":\\"Disabled\\"},\\\
"subnet\\":\\"test-subnet-resource-id\\",\\"vmSize\\":\\"STANDARD_NC6\\"}" --resource-group "testrg123" \
--workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#AKS">Example</a>
```
az machinelearningservices machine-learning-compute aks create --compute-name "compute123" --location "eastus" \
--ak-s-properties "{\\"vmSize\\":\\"STANDARD_NC6\\"}" --resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ParametersMachineLearningComputeCreateOrUpdate#Create#AKS">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|
|**--location**|string|Specifies the location of the resource.|location|location|
|**--tags**|dictionary|Contains resource tags defined as key/value pairs.|tags|tags|
|**--sku**|object|The sku of the workspace.|sku|sku|
|**--type**|sealed-choice|The identity type.|type|type|
|**--user-assigned-identities**|dictionary|The user assigned identities associated with the resource.|user_assigned_identities|userAssignedIdentities|
|**--ak-s-compute-location**|string|Location for the underlying compute|ak_s_compute_location|computeLocation|
|**--ak-s-description**|string|The description of the Machine Learning compute.|ak_s_description|description|
|**--ak-s-resource-id**|string|ARM resource id of the underlying compute|ak_s_resource_id|resourceId|
|**--ak-s-properties**|object|AKS properties|ak_s_properties|properties|

#### <a name="MachineLearningComputeCreateOrUpdate#Create#AmlCompute">Command `az machinelearningservices machine-learning-compute aml-compute create`</a>

##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#AmlCompute">Example</a>
```
az machinelearningservices machine-learning-compute aml-compute create --compute-name "compute123" --location "eastus" \
--resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#AmlCompute">Example</a>
```
az machinelearningservices machine-learning-compute aml-compute create --compute-name "compute123" --location "eastus" \
--aml-compute-properties "{\\"enableNodePublicIp\\":true,\\"isolatedNetwork\\":false,\\"osType\\":\\"Windows\\",\\"remo\
teLoginPortPublicAccess\\":\\"NotSpecified\\",\\"scaleSettings\\":{\\"maxNodeCount\\":1,\\"minNodeCount\\":0,\\"nodeIdl\
eTimeBeforeScaleDown\\":\\"PT5M\\"},\\"virtualMachineImage\\":{\\"id\\":\\"/subscriptions/00000000-0000-0000-0000-00000\
0000000/resourceGroups/myResourceGroup/providers/Microsoft.Compute/galleries/myImageGallery/images/myImageDefinition/ve\
rsions/0.0.1\\"},\\"vmPriority\\":\\"Dedicated\\",\\"vmSize\\":\\"STANDARD_NC6\\"}" --resource-group "testrg123" \
--workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#AmlCompute">Example</a>
```
az machinelearningservices machine-learning-compute aml-compute create --compute-name "compute123" --location "eastus" \
--resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#AmlCompute">Example</a>
```
az machinelearningservices machine-learning-compute aml-compute create --compute-name "compute123" --location "eastus" \
--aml-compute-properties "{\\"applicationSharingPolicy\\":\\"Personal\\",\\"computeInstanceAuthorizationType\\":\\"pers\
onal\\",\\"personalComputeInstanceSettings\\":{\\"assignedUser\\":{\\"objectId\\":\\"00000000-0000-0000-0000-0000000000\
00\\",\\"tenantId\\":\\"00000000-0000-0000-0000-000000000000\\"}},\\"sshSettings\\":{\\"sshPublicAccess\\":\\"Disabled\
\\"},\\"subnet\\":\\"test-subnet-resource-id\\",\\"vmSize\\":\\"STANDARD_NC6\\"}" --resource-group "testrg123" \
--workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#AmlCompute">Example</a>
```
az machinelearningservices machine-learning-compute aml-compute create --compute-name "compute123" --location "eastus" \
--aml-compute-properties "{\\"vmSize\\":\\"STANDARD_NC6\\"}" --resource-group "testrg123" --workspace-name \
"workspaces123"
```
##### <a name="ParametersMachineLearningComputeCreateOrUpdate#Create#AmlCompute">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|
|**--location**|string|Specifies the location of the resource.|location|location|
|**--tags**|dictionary|Contains resource tags defined as key/value pairs.|tags|tags|
|**--sku**|object|The sku of the workspace.|sku|sku|
|**--type**|sealed-choice|The identity type.|type|type|
|**--user-assigned-identities**|dictionary|The user assigned identities associated with the resource.|user_assigned_identities|userAssignedIdentities|
|**--compute-location**|string|Location for the underlying compute|aml_compute_compute_location|computeLocation|
|**--description**|string|The description of the Machine Learning compute.|aml_compute_description|description|
|**--resource-id**|string|ARM resource id of the underlying compute|aml_compute_resource_id|resourceId|
|**--aml-compute-properties**|object|AML Compute properties|aml_compute_properties|properties|

#### <a name="MachineLearningComputeCreateOrUpdate#Create#ComputeInstance">Command `az machinelearningservices machine-learning-compute compute-instance create`</a>

##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#ComputeInstance">Example</a>
```
az machinelearningservices machine-learning-compute compute-instance create --compute-name "compute123" --location \
"eastus" --resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#ComputeInstance">Example</a>
```
az machinelearningservices machine-learning-compute compute-instance create --compute-name "compute123" --location \
"eastus" --compute-instance-properties "{\\"enableNodePublicIp\\":true,\\"isolatedNetwork\\":false,\\"osType\\":\\"Wind\
ows\\",\\"remoteLoginPortPublicAccess\\":\\"NotSpecified\\",\\"scaleSettings\\":{\\"maxNodeCount\\":1,\\"minNodeCount\\\
":0,\\"nodeIdleTimeBeforeScaleDown\\":\\"PT5M\\"},\\"virtualMachineImage\\":{\\"id\\":\\"/subscriptions/00000000-0000-0\
000-0000-000000000000/resourceGroups/myResourceGroup/providers/Microsoft.Compute/galleries/myImageGallery/images/myImag\
eDefinition/versions/0.0.1\\"},\\"vmPriority\\":\\"Dedicated\\",\\"vmSize\\":\\"STANDARD_NC6\\"}" --resource-group \
"testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#ComputeInstance">Example</a>
```
az machinelearningservices machine-learning-compute compute-instance create --compute-name "compute123" --location \
"eastus" --resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#ComputeInstance">Example</a>
```
az machinelearningservices machine-learning-compute compute-instance create --compute-name "compute123" --location \
"eastus" --compute-instance-properties "{\\"applicationSharingPolicy\\":\\"Personal\\",\\"computeInstanceAuthorizationT\
ype\\":\\"personal\\",\\"personalComputeInstanceSettings\\":{\\"assignedUser\\":{\\"objectId\\":\\"00000000-0000-0000-0\
000-000000000000\\",\\"tenantId\\":\\"00000000-0000-0000-0000-000000000000\\"}},\\"sshSettings\\":{\\"sshPublicAccess\\\
":\\"Disabled\\"},\\"subnet\\":\\"test-subnet-resource-id\\",\\"vmSize\\":\\"STANDARD_NC6\\"}" --resource-group \
"testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#ComputeInstance">Example</a>
```
az machinelearningservices machine-learning-compute compute-instance create --compute-name "compute123" --location \
"eastus" --compute-instance-properties "{\\"vmSize\\":\\"STANDARD_NC6\\"}" --resource-group "testrg123" \
--workspace-name "workspaces123"
```
##### <a name="ParametersMachineLearningComputeCreateOrUpdate#Create#ComputeInstance">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|
|**--location**|string|Specifies the location of the resource.|location|location|
|**--tags**|dictionary|Contains resource tags defined as key/value pairs.|tags|tags|
|**--sku**|object|The sku of the workspace.|sku|sku|
|**--type**|sealed-choice|The identity type.|type|type|
|**--user-assigned-identities**|dictionary|The user assigned identities associated with the resource.|user_assigned_identities|userAssignedIdentities|
|**--compute-location**|string|Location for the underlying compute|compute_instance_compute_location|computeLocation|
|**--description**|string|The description of the Machine Learning compute.|compute_instance_description|description|
|**--resource-id**|string|ARM resource id of the underlying compute|compute_instance_resource_id|resourceId|
|**--compute-instance-properties**|object|Compute Instance properties|compute_instance_properties|properties|

#### <a name="MachineLearningComputeCreateOrUpdate#Create#DataFactory">Command `az machinelearningservices machine-learning-compute data-factory create`</a>

##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#DataFactory">Example</a>
```
az machinelearningservices machine-learning-compute data-factory create --compute-name "compute123" --location \
"eastus" --resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#DataFactory">Example</a>
```
az machinelearningservices machine-learning-compute data-factory create --compute-name "compute123" --location \
"eastus" --resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#DataFactory">Example</a>
```
az machinelearningservices machine-learning-compute data-factory create --compute-name "compute123" --location \
"eastus" --resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#DataFactory">Example</a>
```
az machinelearningservices machine-learning-compute data-factory create --compute-name "compute123" --location \
"eastus" --resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#DataFactory">Example</a>
```
az machinelearningservices machine-learning-compute data-factory create --compute-name "compute123" --location \
"eastus" --resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ParametersMachineLearningComputeCreateOrUpdate#Create#DataFactory">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|
|**--location**|string|Specifies the location of the resource.|location|location|
|**--tags**|dictionary|Contains resource tags defined as key/value pairs.|tags|tags|
|**--sku**|object|The sku of the workspace.|sku|sku|
|**--type**|sealed-choice|The identity type.|type|type|
|**--user-assigned-identities**|dictionary|The user assigned identities associated with the resource.|user_assigned_identities|userAssignedIdentities|
|**--compute-location**|string|Location for the underlying compute|data_factory_compute_location|computeLocation|
|**--description**|string|The description of the Machine Learning compute.|data_factory_description|description|
|**--resource-id**|string|ARM resource id of the underlying compute|data_factory_resource_id|resourceId|

#### <a name="MachineLearningComputeCreateOrUpdate#Create#DataLakeAnalytics">Command `az machinelearningservices machine-learning-compute data-lake-analytics create`</a>

##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#DataLakeAnalytics">Example</a>
```
az machinelearningservices machine-learning-compute data-lake-analytics create --compute-name "compute123" --location \
"eastus" --resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#DataLakeAnalytics">Example</a>
```
az machinelearningservices machine-learning-compute data-lake-analytics create --compute-name "compute123" --location \
"eastus" --resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#DataLakeAnalytics">Example</a>
```
az machinelearningservices machine-learning-compute data-lake-analytics create --compute-name "compute123" --location \
"eastus" --resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#DataLakeAnalytics">Example</a>
```
az machinelearningservices machine-learning-compute data-lake-analytics create --compute-name "compute123" --location \
"eastus" --resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#DataLakeAnalytics">Example</a>
```
az machinelearningservices machine-learning-compute data-lake-analytics create --compute-name "compute123" --location \
"eastus" --resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ParametersMachineLearningComputeCreateOrUpdate#Create#DataLakeAnalytics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|
|**--location**|string|Specifies the location of the resource.|location|location|
|**--tags**|dictionary|Contains resource tags defined as key/value pairs.|tags|tags|
|**--sku**|object|The sku of the workspace.|sku|sku|
|**--type**|sealed-choice|The identity type.|type|type|
|**--user-assigned-identities**|dictionary|The user assigned identities associated with the resource.|user_assigned_identities|userAssignedIdentities|
|**--compute-location**|string|Location for the underlying compute|data_lake_analytics_compute_location|computeLocation|
|**--description**|string|The description of the Machine Learning compute.|data_lake_analytics_description|description|
|**--resource-id**|string|ARM resource id of the underlying compute|data_lake_analytics_resource_id|resourceId|
|**--data-lake-store-account-name**|string|DataLake Store Account Name|data_lake_analytics_data_lake_store_account_name|dataLakeStoreAccountName|

#### <a name="MachineLearningComputeCreateOrUpdate#Create#Databricks">Command `az machinelearningservices machine-learning-compute databricks create`</a>

##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#Databricks">Example</a>
```
az machinelearningservices machine-learning-compute databricks create --compute-name "compute123" --location "eastus" \
--resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#Databricks">Example</a>
```
az machinelearningservices machine-learning-compute databricks create --compute-name "compute123" --location "eastus" \
--resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#Databricks">Example</a>
```
az machinelearningservices machine-learning-compute databricks create --compute-name "compute123" --location "eastus" \
--resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#Databricks">Example</a>
```
az machinelearningservices machine-learning-compute databricks create --compute-name "compute123" --location "eastus" \
--resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#Databricks">Example</a>
```
az machinelearningservices machine-learning-compute databricks create --compute-name "compute123" --location "eastus" \
--resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ParametersMachineLearningComputeCreateOrUpdate#Create#Databricks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|
|**--location**|string|Specifies the location of the resource.|location|location|
|**--tags**|dictionary|Contains resource tags defined as key/value pairs.|tags|tags|
|**--sku**|object|The sku of the workspace.|sku|sku|
|**--type**|sealed-choice|The identity type.|type|type|
|**--user-assigned-identities**|dictionary|The user assigned identities associated with the resource.|user_assigned_identities|userAssignedIdentities|
|**--compute-location**|string|Location for the underlying compute|databricks_compute_location|computeLocation|
|**--description**|string|The description of the Machine Learning compute.|databricks_description|description|
|**--resource-id**|string|ARM resource id of the underlying compute|databricks_resource_id|resourceId|
|**--databricks-access-token**|string|Databricks access token|databricks_databricks_access_token|databricksAccessToken|

#### <a name="MachineLearningComputeCreateOrUpdate#Create#HDInsight">Command `az machinelearningservices machine-learning-compute hd-insight create`</a>

##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#HDInsight">Example</a>
```
az machinelearningservices machine-learning-compute hd-insight create --compute-name "compute123" --location "eastus" \
--resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#HDInsight">Example</a>
```
az machinelearningservices machine-learning-compute hd-insight create --compute-name "compute123" --location "eastus" \
--resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#HDInsight">Example</a>
```
az machinelearningservices machine-learning-compute hd-insight create --compute-name "compute123" --location "eastus" \
--resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#HDInsight">Example</a>
```
az machinelearningservices machine-learning-compute hd-insight create --compute-name "compute123" --location "eastus" \
--resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#HDInsight">Example</a>
```
az machinelearningservices machine-learning-compute hd-insight create --compute-name "compute123" --location "eastus" \
--resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ParametersMachineLearningComputeCreateOrUpdate#Create#HDInsight">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|
|**--location**|string|Specifies the location of the resource.|location|location|
|**--tags**|dictionary|Contains resource tags defined as key/value pairs.|tags|tags|
|**--sku**|object|The sku of the workspace.|sku|sku|
|**--type**|sealed-choice|The identity type.|type|type|
|**--user-assigned-identities**|dictionary|The user assigned identities associated with the resource.|user_assigned_identities|userAssignedIdentities|
|**--compute-location**|string|Location for the underlying compute|hd_insight_compute_location|computeLocation|
|**--description**|string|The description of the Machine Learning compute.|hd_insight_description|description|
|**--resource-id**|string|ARM resource id of the underlying compute|hd_insight_resource_id|resourceId|
|**--ssh-port**|integer|Port open for ssh connections on the master node of the cluster.|hd_insight_ssh_port|sshPort|
|**--address**|string|Public IP address of the master node of the cluster.|hd_insight_address|address|
|**--administrator-account**|object|Admin credentials for master node of the cluster|hd_insight_administrator_account|administratorAccount|

#### <a name="MachineLearningComputeCreateOrUpdate#Create#VirtualMachine">Command `az machinelearningservices machine-learning-compute virtual-machine create`</a>

##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#VirtualMachine">Example</a>
```
az machinelearningservices machine-learning-compute virtual-machine create --compute-name "compute123" --location \
"eastus" --resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#VirtualMachine">Example</a>
```
az machinelearningservices machine-learning-compute virtual-machine create --compute-name "compute123" --location \
"eastus" --resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#VirtualMachine">Example</a>
```
az machinelearningservices machine-learning-compute virtual-machine create --compute-name "compute123" --location \
"eastus" --resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#VirtualMachine">Example</a>
```
az machinelearningservices machine-learning-compute virtual-machine create --compute-name "compute123" --location \
"eastus" --resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ExamplesMachineLearningComputeCreateOrUpdate#Create#VirtualMachine">Example</a>
```
az machinelearningservices machine-learning-compute virtual-machine create --compute-name "compute123" --location \
"eastus" --resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ParametersMachineLearningComputeCreateOrUpdate#Create#VirtualMachine">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|
|**--location**|string|Specifies the location of the resource.|location|location|
|**--tags**|dictionary|Contains resource tags defined as key/value pairs.|tags|tags|
|**--sku**|object|The sku of the workspace.|sku|sku|
|**--type**|sealed-choice|The identity type.|type|type|
|**--user-assigned-identities**|dictionary|The user assigned identities associated with the resource.|user_assigned_identities|userAssignedIdentities|
|**--compute-location**|string|Location for the underlying compute|virtual_machine_compute_location|computeLocation|
|**--description**|string|The description of the Machine Learning compute.|virtual_machine_description|description|
|**--resource-id**|string|ARM resource id of the underlying compute|virtual_machine_resource_id|resourceId|
|**--virtual-machine-size**|string|Virtual Machine size|virtual_machine_virtual_machine_size|virtualMachineSize|
|**--ssh-port**|integer|Port open for ssh connections.|virtual_machine_ssh_port|sshPort|
|**--address**|string|Public IP address of the virtual machine.|virtual_machine_address|address|
|**--administrator-account**|object|Admin credentials for virtual machine|virtual_machine_administrator_account|administratorAccount|

#### <a name="MachineLearningComputeUpdate">Command `az machinelearningservices machine-learning-compute update`</a>

##### <a name="ExamplesMachineLearningComputeUpdate">Example</a>
```
az machinelearningservices machine-learning-compute update --compute-name "compute123" --scale-settings \
max-node-count=4 min-node-count=4 node-idle-time-before-scale-down="PT5M" --resource-group "testrg123" \
--workspace-name "workspaces123"
```
##### <a name="ParametersMachineLearningComputeUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|
|**--scale-settings**|object|Desired scale settings for the amlCompute.|scale_settings|scaleSettings|

#### <a name="MachineLearningComputeDelete">Command `az machinelearningservices machine-learning-compute delete`</a>

##### <a name="ExamplesMachineLearningComputeDelete">Example</a>
```
az machinelearningservices machine-learning-compute delete --compute-name "compute123" --resource-group "testrg123" \
--underlying-resource-action "Delete" --workspace-name "workspaces123"
```
##### <a name="ParametersMachineLearningComputeDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|
|**--underlying-resource-action**|choice|Delete the underlying compute if 'Delete', or detach the underlying compute from workspace if 'Detach'.|underlying_resource_action|underlyingResourceAction|

#### <a name="MachineLearningComputeListKeys">Command `az machinelearningservices machine-learning-compute list-key`</a>

##### <a name="ExamplesMachineLearningComputeListKeys">Example</a>
```
az machinelearningservices machine-learning-compute list-key --compute-name "compute123" --resource-group "testrg123" \
--workspace-name "workspaces123"
```
##### <a name="ParametersMachineLearningComputeListKeys">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|

#### <a name="MachineLearningComputeListNodes">Command `az machinelearningservices machine-learning-compute list-node`</a>

##### <a name="ExamplesMachineLearningComputeListNodes">Example</a>
```
az machinelearningservices machine-learning-compute list-node --compute-name "compute123" --resource-group "testrg123" \
--workspace-name "workspaces123"
```
##### <a name="ParametersMachineLearningComputeListNodes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|

#### <a name="MachineLearningComputeRestart">Command `az machinelearningservices machine-learning-compute restart`</a>

##### <a name="ExamplesMachineLearningComputeRestart">Example</a>
```
az machinelearningservices machine-learning-compute restart --compute-name "compute123" --resource-group "testrg123" \
--workspace-name "workspaces123"
```
##### <a name="ParametersMachineLearningComputeRestart">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|

#### <a name="MachineLearningComputeStart">Command `az machinelearningservices machine-learning-compute start`</a>

##### <a name="ExamplesMachineLearningComputeStart">Example</a>
```
az machinelearningservices machine-learning-compute start --compute-name "compute123" --resource-group "testrg123" \
--workspace-name "workspaces123"
```
##### <a name="ParametersMachineLearningComputeStart">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|

#### <a name="MachineLearningComputeStop">Command `az machinelearningservices machine-learning-compute stop`</a>

##### <a name="ExamplesMachineLearningComputeStop">Example</a>
```
az machinelearningservices machine-learning-compute stop --compute-name "compute123" --resource-group "testrg123" \
--workspace-name "workspaces123"
```
##### <a name="ParametersMachineLearningComputeStop">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|

### group `az machinelearningservices machine-learning-service`
#### <a name="MachineLearningServiceListByWorkspace">Command `az machinelearningservices machine-learning-service list`</a>

##### <a name="ExamplesMachineLearningServiceListByWorkspace">Example</a>
```
az machinelearningservices machine-learning-service list --resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ParametersMachineLearningServiceListByWorkspace">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--skiptoken**|string|Continuation token for pagination.|skiptoken|$skiptoken|
|**--model-id**|string|The Model Id.|model_id|modelId|
|**--model-name**|string|The Model name.|model_name|modelName|
|**--tag**|string|The object tag.|tag|tag|
|**--tags**|string|A set of tags with which to filter the returned services. It is a comma separated string of tags key or tags key=value Example: tagKey1,tagKey2,tagKey3=value3 .|tags|tags|
|**--properties**|string|A set of properties with which to filter the returned services. It is a comma separated string of properties key and/or properties key=value Example: propKey1,propKey2,propKey3=value3 .|properties|properties|
|**--run-id**|string|runId for model associated with service.|run_id|runId|
|**--expand**|boolean|Set to True to include Model details.|expand|expand|
|**--orderby**|choice|The option to order the response.|orderby|orderby|

#### <a name="MachineLearningServiceGet">Command `az machinelearningservices machine-learning-service show`</a>

##### <a name="ExamplesMachineLearningServiceGet">Example</a>
```
az machinelearningservices machine-learning-service show --resource-group "testrg123" --service-name "service123" \
--workspace-name "workspaces123"
```
##### <a name="ParametersMachineLearningServiceGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--service-name**|string|Name of the Azure Machine Learning service.|service_name|serviceName|
|**--expand**|boolean|Set to True to include Model details.|expand|expand|

#### <a name="MachineLearningServiceCreateOrUpdate#Create">Command `az machinelearningservices machine-learning-service create`</a>

##### <a name="ExamplesMachineLearningServiceCreateOrUpdate#Create">Example</a>
```
az machinelearningservices machine-learning-service create --properties "{\\"appInsightsEnabled\\":true,\\"authEnabled\
\\":true,\\"computeType\\":\\"ACI\\",\\"containerResourceRequirements\\":{\\"cpu\\":1,\\"memoryInGB\\":1},\\"environmen\
tImageRequest\\":{\\"assets\\":[{\\"id\\":null,\\"mimeType\\":\\"application/x-python\\",\\"unpack\\":false,\\"url\\":\
\\"aml://storage/azureml/score.py\\"}],\\"driverProgram\\":\\"score.py\\",\\"environment\\":{\\"name\\":\\"AzureML-Scik\
it-learn-0.20.3\\",\\"docker\\":{\\"baseDockerfile\\":null,\\"baseImage\\":\\"mcr.microsoft.com/azureml/base:openmpi3.1\
.2-ubuntu16.04\\",\\"baseImageRegistry\\":{\\"address\\":null,\\"password\\":null,\\"username\\":null}},\\"environmentV\
ariables\\":{\\"EXAMPLE_ENV_VAR\\":\\"EXAMPLE_VALUE\\"},\\"inferencingStackVersion\\":null,\\"python\\":{\\"baseCondaEn\
vironment\\":null,\\"condaDependencies\\":{\\"name\\":\\"azureml_ae1acbe6e1e6aabbad900b53c491a17c\\",\\"channels\\":[\\\
"conda-forge\\"],\\"dependencies\\":[\\"python=3.6.2\\",{\\"pip\\":[\\"azureml-core==1.0.69\\",\\"azureml-defaults==1.0\
.69\\",\\"azureml-telemetry==1.0.69\\",\\"azureml-train-restclients-hyperdrive==1.0.69\\",\\"azureml-train-core==1.0.69\
\\",\\"scikit-learn==0.20.3\\",\\"scipy==1.2.1\\",\\"numpy==1.16.2\\",\\"joblib==0.13.2\\"]}]},\\"interpreterPath\\":\\\
"python\\",\\"userManagedDependencies\\":false},\\"spark\\":{\\"packages\\":[],\\"precachePackages\\":true,\\"repositor\
ies\\":[]},\\"version\\":\\"3\\"},\\"models\\":[{\\"name\\":\\"sklearn_regression_model.pkl\\",\\"mimeType\\":\\"applic\
ation/x-python\\",\\"url\\":\\"aml://storage/azureml/sklearn_regression_model.pkl\\"}]},\\"location\\":\\"eastus2\\"}" \
--resource-group "testrg123" --service-name "service456" --workspace-name "workspaces123"
```
##### <a name="ParametersMachineLearningServiceCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--service-name**|string|Name of the Azure Machine Learning service.|service_name|serviceName|
|**--properties**|object|The payload that is used to create or update the Service.|properties|properties|

#### <a name="MachineLearningServiceCreateOrUpdate#Update">Command `az machinelearningservices machine-learning-service update`</a>

##### <a name="ParametersMachineLearningServiceCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--service-name**|string|Name of the Azure Machine Learning service.|service_name|serviceName|
|**--properties**|object|The payload that is used to create or update the Service.|properties|properties|

#### <a name="MachineLearningServiceDelete">Command `az machinelearningservices machine-learning-service delete`</a>

##### <a name="ExamplesMachineLearningServiceDelete">Example</a>
```
az machinelearningservices machine-learning-service delete --resource-group "testrg123" --service-name "service123" \
--workspace-name "workspaces123"
```
##### <a name="ParametersMachineLearningServiceDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--service-name**|string|Name of the Azure Machine Learning service.|service_name|serviceName|

### group `az machinelearningservices model-container`
#### <a name="ModelContainersList">Command `az machinelearningservices model-container list`</a>

##### <a name="ExamplesModelContainersList">Example</a>
```
az machinelearningservices model-container list --resource-group "testrg123" --workspace-name "workspace123"
```
##### <a name="ParametersModelContainersList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--skiptoken**|string|Continuation token for pagination.|skiptoken|$skiptoken|
|**--count**|integer|Maximum number of results to return.|count|count|

#### <a name="ModelContainersGet">Command `az machinelearningservices model-container show`</a>

##### <a name="ExamplesModelContainersGet">Example</a>
```
az machinelearningservices model-container show --name "testContainer" --resource-group "testrg123" --workspace-name \
"workspace123"
```
##### <a name="ParametersModelContainersGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="ModelContainersCreateOrUpdate#Create">Command `az machinelearningservices model-container create`</a>

##### <a name="ExamplesModelContainersCreateOrUpdate#Create">Example</a>
```
az machinelearningservices model-container create --name "testContainer" --properties description="Model container \
description" tags={"tag1":"value1","tag2":"value2"} --resource-group "testrg123" --workspace-name "workspace123"
```
##### <a name="ParametersModelContainersCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--latest-versions**|array|Latest model versions for each stage.|latest_versions|latestVersions|
|**--description**|string|The asset description text.|description|description|
|**--tags**|dictionary|Tag dictionary. Tags can be added, removed, and updated.|tags|tags|
|**--properties**|dictionary|The asset property dictionary.|properties|properties|

#### <a name="ModelContainersCreateOrUpdate#Update">Command `az machinelearningservices model-container update`</a>

##### <a name="ParametersModelContainersCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--latest-versions**|array|Latest model versions for each stage.|latest_versions|latestVersions|
|**--description**|string|The asset description text.|description|description|
|**--tags**|dictionary|Tag dictionary. Tags can be added, removed, and updated.|tags|tags|
|**--properties**|dictionary|The asset property dictionary.|properties|properties|

#### <a name="ModelContainersDelete">Command `az machinelearningservices model-container delete`</a>

##### <a name="ExamplesModelContainersDelete">Example</a>
```
az machinelearningservices model-container delete --name "testContainer" --resource-group "testrg123" --workspace-name \
"workspace123"
```
##### <a name="ParametersModelContainersDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

### group `az machinelearningservices model-version`
#### <a name="ModelVersionsList">Command `az machinelearningservices model-version list`</a>

##### <a name="ExamplesModelVersionsList">Example</a>
```
az machinelearningservices model-version list --name "testContainer" --resource-group "testrg123" --version "999" \
--workspace-name "workspace123"
```
##### <a name="ParametersModelVersionsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Model name.|name|name|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--skiptoken**|string|Continuation token for pagination.|skiptoken|$skiptoken|
|**--version**|string|Model version.|version|version|
|**--description**|string|Model description.|description|description|
|**--count**|integer|Maximum number of results to return.|count|count|
|**--offset**|integer|Number of initial results to skip.|offset|offset|
|**--tags**|string|Comma-separated list of tag names (and optionally values). Example: tag1,tag2=value2|tags|tags|
|**--properties**|string|Comma-separated list of property names (and optionally values). Example: prop1,prop2=value2|properties|properties|
|**--order-by**|string|Property by which to order the results.|order_by|orderBy|
|**--latest-version-only**|boolean|Only return the most recent version of a model.|latest_version_only|latestVersionOnly|

#### <a name="ModelVersionsGet">Command `az machinelearningservices model-version show`</a>

##### <a name="ExamplesModelVersionsGet">Example</a>
```
az machinelearningservices model-version show --name "testContainer" --resource-group "testrg123" --version "999" \
--workspace-name "workspace123"
```
##### <a name="ParametersModelVersionsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--version**|string|Version identifier.|version|version|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="ModelVersionsCreateOrUpdate#Create">Command `az machinelearningservices model-version create`</a>

##### <a name="ExamplesModelVersionsCreateOrUpdate#Create">Example</a>
```
az machinelearningservices model-version create --name "testContainer" --properties description="Model version \
description" assetPath={"path":"LocalUpload/12345/some/path","isDirectory":true} datastoreId="/subscriptions/00000000-1\
111-2222-3333-444444444444/resourceGroups/testrg123/providers/Microsoft.MachineLearningServices/workspaces/workspace123\
/datastores/datastore123" properties={"prop1":"value1","prop2":"value2"} stage="Production" \
tags={"tag1":"value1","tag2":"value2"} --resource-group "testrg123" --version "999" --workspace-name "workspace123"
```
##### <a name="ParametersModelVersionsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--version**|string|Version identifier.|version|version|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--stage**|string|Model asset stage.|stage|stage|
|**--datastore-id**|string|The asset datastoreId|datastore_id|datastoreId|
|**--asset-path**|object|Details of an AssetUri.|asset_path|assetPath|
|**--description**|string|The asset description text.|description|description|
|**--tags**|dictionary|Tag dictionary. Tags can be added, removed, and updated.|tags|tags|
|**--properties**|dictionary|The asset property dictionary.|properties|properties|

#### <a name="ModelVersionsCreateOrUpdate#Update">Command `az machinelearningservices model-version update`</a>

##### <a name="ParametersModelVersionsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--version**|string|Version identifier.|version|version|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--stage**|string|Model asset stage.|stage|stage|
|**--datastore-id**|string|The asset datastoreId|datastore_id|datastoreId|
|**--asset-path**|object|Details of an AssetUri.|asset_path|assetPath|
|**--description**|string|The asset description text.|description|description|
|**--tags**|dictionary|Tag dictionary. Tags can be added, removed, and updated.|tags|tags|
|**--properties**|dictionary|The asset property dictionary.|properties|properties|

#### <a name="ModelVersionsDelete">Command `az machinelearningservices model-version delete`</a>

##### <a name="ExamplesModelVersionsDelete">Example</a>
```
az machinelearningservices model-version delete --name "testContainer" --resource-group "testrg123" --version "999" \
--workspace-name "workspace123"
```
##### <a name="ParametersModelVersionsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Container name.|name|name|
|**--version**|string|Version identifier.|version|version|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

### group `az machinelearningservices notebook`
#### <a name="NotebooksListKeys">Command `az machinelearningservices notebook list-key`</a>

##### <a name="ExamplesNotebooksListKeys">Example</a>
```
az machinelearningservices notebook list-key --resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ParametersNotebooksListKeys">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="NotebooksPrepare">Command `az machinelearningservices notebook prepare`</a>

##### <a name="ExamplesNotebooksPrepare">Example</a>
```
az machinelearningservices notebook prepare --resource-group "testrg123" --workspace-name "workspaces123"
```
##### <a name="ParametersNotebooksPrepare">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

### group `az machinelearningservices private-endpoint-connection`
#### <a name="PrivateEndpointConnectionsGet">Command `az machinelearningservices private-endpoint-connection show`</a>

##### <a name="ExamplesPrivateEndpointConnectionsGet">Example</a>
```
az machinelearningservices private-endpoint-connection show --name "{privateEndpointConnectionName}" --resource-group \
"rg-1234" --workspace-name "testworkspace"
```
##### <a name="ParametersPrivateEndpointConnectionsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--private-endpoint-connection-name**|string|The name of the private endpoint connection associated with the workspace|private_endpoint_connection_name|privateEndpointConnectionName|

#### <a name="PrivateEndpointConnectionsDelete">Command `az machinelearningservices private-endpoint-connection delete`</a>

##### <a name="ExamplesPrivateEndpointConnectionsDelete">Example</a>
```
az machinelearningservices private-endpoint-connection delete --name "{privateEndpointConnectionName}" \
--resource-group "rg-1234" --workspace-name "testworkspace"
```
##### <a name="ParametersPrivateEndpointConnectionsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--private-endpoint-connection-name**|string|The name of the private endpoint connection associated with the workspace|private_endpoint_connection_name|privateEndpointConnectionName|

#### <a name="PrivateEndpointConnectionsPut">Command `az machinelearningservices private-endpoint-connection put`</a>

##### <a name="ExamplesPrivateEndpointConnectionsPut">Example</a>
```
az machinelearningservices private-endpoint-connection put --name "{privateEndpointConnectionName}" \
--private-link-service-connection-state description="Auto-Approved" status="Approved" --resource-group "rg-1234" \
--workspace-name "testworkspace"
```
##### <a name="ParametersPrivateEndpointConnectionsPut">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--private-endpoint-connection-name**|string|The name of the private endpoint connection associated with the workspace|private_endpoint_connection_name|privateEndpointConnectionName|
|**--location**|string|Specifies the location of the resource.|location|location|
|**--tags**|dictionary|Contains resource tags defined as key/value pairs.|tags|tags|
|**--sku**|object|The sku of the workspace.|sku|sku|
|**--type**|sealed-choice|The identity type.|type|type|
|**--user-assigned-identities**|dictionary|The user assigned identities associated with the resource.|user_assigned_identities|userAssignedIdentities|
|**--private-link-service-connection-state**|object|A collection of information about the state of the connection between service consumer and provider.|private_link_service_connection_state|privateLinkServiceConnectionState|

### group `az machinelearningservices private-link-resource`
#### <a name="PrivateLinkResourcesListByWorkspace">Command `az machinelearningservices private-link-resource list`</a>

##### <a name="ExamplesPrivateLinkResourcesListByWorkspace">Example</a>
```
az machinelearningservices private-link-resource list --resource-group "rg-1234" --workspace-name "testworkspace"
```
##### <a name="ParametersPrivateLinkResourcesListByWorkspace">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

### group `az machinelearningservices quota`
#### <a name="QuotasList">Command `az machinelearningservices quota list`</a>

##### <a name="ExamplesQuotasList">Example</a>
```
az machinelearningservices quota list --location "eastus"
```
##### <a name="ParametersQuotasList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|The location for which resource usage is queried.|location|location|

#### <a name="QuotasUpdate">Command `az machinelearningservices quota update`</a>

##### <a name="ExamplesQuotasUpdate">Example</a>
```
az machinelearningservices quota update --location "eastus" --value type="Microsoft.MachineLearningServices/workspaces/\
quotas" id="/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg/providers/Microsoft.MachineLearningSe\
rvices/workspaces/demo_workspace1/quotas/Standard_DSv2_Family_Cluster_Dedicated_vCPUs" limit=100 unit="Count" --value \
type="Microsoft.MachineLearningServices/workspaces/quotas" id="/subscriptions/00000000-0000-0000-0000-000000000000/reso\
urceGroups/rg/providers/Microsoft.MachineLearningServices/workspaces/demo_workspace2/quotas/Standard_DSv2_Family_Cluste\
r_Dedicated_vCPUs" limit=200 unit="Count"
```
##### <a name="ParametersQuotasUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|The location for update quota is queried.|location|location|
|**--value**|array|The list for update quota.|value|value|
|**--quota-update-parameters-location**|string|Region of workspace quota to be updated.|quota_update_parameters_location|location|

### group `az machinelearningservices usage`
#### <a name="UsagesList">Command `az machinelearningservices usage list`</a>

##### <a name="ExamplesUsagesList">Example</a>
```
az machinelearningservices usage list --location "eastus"
```
##### <a name="ParametersUsagesList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|The location for which resource usage is queried.|location|location|

### group `az machinelearningservices virtual-machine-size`
#### <a name="VirtualMachineSizesList">Command `az machinelearningservices virtual-machine-size list`</a>

##### <a name="ExamplesVirtualMachineSizesList">Example</a>
```
az machinelearningservices virtual-machine-size list --location "eastus"
```
##### <a name="ParametersVirtualMachineSizesList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|The location upon which virtual-machine-sizes is queried.|location|location|

### group `az machinelearningservices workspace`
#### <a name="WorkspacesListByResourceGroup">Command `az machinelearningservices workspace list`</a>

##### <a name="ExamplesWorkspacesListByResourceGroup">Example</a>
```
az machinelearningservices workspace list --resource-group "workspace-1234"
```
##### <a name="ParametersWorkspacesListByResourceGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--skiptoken**|string|Continuation token for pagination.|skiptoken|$skiptoken|

#### <a name="WorkspacesListBySubscription">Command `az machinelearningservices workspace list`</a>

##### <a name="ExamplesWorkspacesListBySubscription">Example</a>
```
az machinelearningservices workspace list
```
##### <a name="ParametersWorkspacesListBySubscription">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="WorkspacesGet">Command `az machinelearningservices workspace show`</a>

##### <a name="ExamplesWorkspacesGet">Example</a>
```
az machinelearningservices workspace show --resource-group "workspace-1234" --name "testworkspace"
```
##### <a name="ParametersWorkspacesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="WorkspacesCreateOrUpdate#Create">Command `az machinelearningservices workspace create`</a>

##### <a name="ExamplesWorkspacesCreateOrUpdate#Create">Example</a>
```
az machinelearningservices workspace create --type "SystemAssigned" --location "eastus2euap" --description "test \
description" --application-insights "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/workspace-1234/\
providers/microsoft.insights/components/testinsights" --container-registry "/subscriptions/00000000-1111-2222-3333-4444\
44444444/resourceGroups/workspace-1234/providers/Microsoft.ContainerRegistry/registries/testRegistry" \
--key-vault-properties identity-client-id="" key-identifier="https://testkv.vault.azure.net/keys/testkey/aabbccddee1122\
33445566778899aabb" key-vault-arm-id="/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/workspace-1234\
/providers/Microsoft.KeyVault/vaults/testkv" --status "Enabled" --friendly-name "HelloName" --hbi-workspace false \
--key-vault "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/workspace-1234/providers/Microsoft.KeyV\
ault/vaults/testkv" --shared-private-link-resources name="testdbresource" private-link-resource-id="/subscriptions/0000\
0000-1111-2222-3333-444444444444/resourceGroups/workspace-1234/providers/Microsoft.DocumentDB/databaseAccounts/testdbre\
source/privateLinkResources/Sql" group-id="Sql" request-message="Please approve" status="Approved" --storage-account \
"/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/accountcrud-1234/providers/Microsoft.Storage/storag\
eAccounts/testStorageAccount" --sku name="Basic" tier="Basic" --resource-group "workspace-1234" --name "testworkspace"
```
##### <a name="ParametersWorkspacesCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--location**|string|Specifies the location of the resource.|location|location|
|**--tags**|dictionary|Contains resource tags defined as key/value pairs.|tags|tags|
|**--sku**|object|The sku of the workspace.|sku|sku|
|**--type**|sealed-choice|The identity type.|type|type|
|**--user-assigned-identities**|dictionary|The user assigned identities associated with the resource.|user_assigned_identities|userAssignedIdentities|
|**--description**|string|The description of this workspace.|description|description|
|**--friendly-name**|string|The friendly name for this workspace. This name in mutable|friendly_name|friendlyName|
|**--key-vault**|string|ARM id of the key vault associated with this workspace. This cannot be changed once the workspace has been created|key_vault|keyVault|
|**--application-insights**|string|ARM id of the application insights associated with this workspace. This cannot be changed once the workspace has been created|application_insights|applicationInsights|
|**--container-registry**|string|ARM id of the container registry associated with this workspace. This cannot be changed once the workspace has been created|container_registry|containerRegistry|
|**--storage-account**|string|ARM id of the storage account associated with this workspace. This cannot be changed once the workspace has been created|storage_account|storageAccount|
|**--discovery-url**|string|Url for the discovery service to identify regional endpoints for machine learning experimentation services|discovery_url|discoveryUrl|
|**--hbi-workspace**|boolean|The flag to signal HBI data in the workspace and reduce diagnostic data collected by the service|hbi_workspace|hbiWorkspace|
|**--image-build-compute**|string|The compute name for image build|image_build_compute|imageBuildCompute|
|**--allow-public-access-when-behind-vnet**|boolean|The flag to indicate whether to allow public access when behind VNet.|allow_public_access_when_behind_vnet|allowPublicAccessWhenBehindVnet|
|**--shared-private-link-resources**|array|The list of shared private link resources in this workspace.|shared_private_link_resources|sharedPrivateLinkResources|
|**--status**|choice|Indicates whether or not the encryption is enabled for the workspace.|status|status|
|**--key-vault-properties**|object|Customer Key vault properties.|key_vault_properties|keyVaultProperties|

#### <a name="WorkspacesUpdate">Command `az machinelearningservices workspace update`</a>

##### <a name="ExamplesWorkspacesUpdate">Example</a>
```
az machinelearningservices workspace update --description "new description" --friendly-name "New friendly name" --sku \
name="Enterprise" tier="Enterprise" --resource-group "workspace-1234" --name "testworkspace"
```
##### <a name="ParametersWorkspacesUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--tags**|dictionary|The resource tags for the machine learning workspace.|tags|tags|
|**--sku**|object|The sku of the workspace.|sku|sku|
|**--description**|string|The description of this workspace.|description|description|
|**--friendly-name**|string|The friendly name for this workspace.|friendly_name|friendlyName|

#### <a name="WorkspacesDelete">Command `az machinelearningservices workspace delete`</a>

##### <a name="ExamplesWorkspacesDelete">Example</a>
```
az machinelearningservices workspace delete --resource-group "workspace-1234" --name "testworkspace"
```
##### <a name="ParametersWorkspacesDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="WorkspacesListKeys">Command `az machinelearningservices workspace list-key`</a>

##### <a name="ExamplesWorkspacesListKeys">Example</a>
```
az machinelearningservices workspace list-key --resource-group "testrg123" --name "workspaces123"
```
##### <a name="ParametersWorkspacesListKeys">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="WorkspacesResyncKeys">Command `az machinelearningservices workspace resync-key`</a>

##### <a name="ExamplesWorkspacesResyncKeys">Example</a>
```
az machinelearningservices workspace resync-key --resource-group "testrg123" --name "workspaces123"
```
##### <a name="ParametersWorkspacesResyncKeys">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

### group `az machinelearningservices workspace-connection`
#### <a name="WorkspaceConnectionsList">Command `az machinelearningservices workspace-connection list`</a>

##### <a name="ExamplesWorkspaceConnectionsList">Example</a>
```
az machinelearningservices workspace-connection list --category "ACR" --resource-group "resourceGroup-1" --target \
"www.facebook.com" --workspace-name "workspace-1"
```
##### <a name="ParametersWorkspaceConnectionsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--target**|string|Target of the workspace connection.|target|target|
|**--category**|string|Category of the workspace connection.|category|category|

#### <a name="WorkspaceConnectionsGet">Command `az machinelearningservices workspace-connection show`</a>

##### <a name="ExamplesWorkspaceConnectionsGet">Example</a>
```
az machinelearningservices workspace-connection show --connection-name "connection-1" --resource-group \
"resourceGroup-1" --workspace-name "workspace-1"
```
##### <a name="ParametersWorkspaceConnectionsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--connection-name**|string|Friendly name of the workspace connection|connection_name|connectionName|

#### <a name="WorkspaceConnectionsCreate">Command `az machinelearningservices workspace-connection create`</a>

##### <a name="ExamplesWorkspaceConnectionsCreate">Example</a>
```
az machinelearningservices workspace-connection create --connection-name "connection-1" --name "connection-1" \
--auth-type "PAT" --category "ACR" --target "www.facebook.com" --value "secrets" --resource-group "resourceGroup-1" \
--workspace-name "workspace-1"
```
##### <a name="ParametersWorkspaceConnectionsCreate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--connection-name**|string|Friendly name of the workspace connection|connection_name|connectionName|
|**--name**|string|Friendly name of the workspace connection|name|name|
|**--category**|string|Category of the workspace connection.|category|category|
|**--target**|string|Target of the workspace connection.|target|target|
|**--auth-type**|string|Authorization type of the workspace connection.|auth_type|authType|
|**--value**|string|Value details of the workspace connection.|value|value|

#### <a name="WorkspaceConnectionsDelete">Command `az machinelearningservices workspace-connection delete`</a>

##### <a name="ExamplesWorkspaceConnectionsDelete">Example</a>
```
az machinelearningservices workspace-connection delete --connection-name "connection-1" --resource-group \
"resourceGroup-1" --workspace-name "workspace-1"
```
##### <a name="ParametersWorkspaceConnectionsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--connection-name**|string|Friendly name of the workspace connection|connection_name|connectionName|

### group `az machinelearningservices workspace-feature`
#### <a name="WorkspaceFeaturesList">Command `az machinelearningservices workspace-feature list`</a>

##### <a name="ExamplesWorkspaceFeaturesList">Example</a>
```
az machinelearningservices workspace-feature list --resource-group "myResourceGroup" --workspace-name "testworkspace"
```
##### <a name="ParametersWorkspaceFeaturesList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
