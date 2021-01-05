# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az devops|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az devops` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az devops pipeline-template-definition|PipelineTemplateDefinitions|[commands](#CommandsInPipelineTemplateDefinitions)|
|az devops pipeline|Pipelines|[commands](#CommandsInPipelines)|

## COMMANDS
### <a name="CommandsInPipelines">Commands in `az devops pipeline` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devops pipeline list](#PipelinesListByResourceGroup)|ListByResourceGroup|[Parameters](#ParametersPipelinesListByResourceGroup)|[Example](#ExamplesPipelinesListByResourceGroup)|
|[az devops pipeline list](#PipelinesListBySubscription)|ListBySubscription|[Parameters](#ParametersPipelinesListBySubscription)|[Example](#ExamplesPipelinesListBySubscription)|
|[az devops pipeline show](#PipelinesGet)|Get|[Parameters](#ParametersPipelinesGet)|[Example](#ExamplesPipelinesGet)|
|[az devops pipeline create](#PipelinesCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersPipelinesCreateOrUpdate#Create)|[Example](#ExamplesPipelinesCreateOrUpdate#Create)|
|[az devops pipeline update](#PipelinesUpdate)|Update|[Parameters](#ParametersPipelinesUpdate)|[Example](#ExamplesPipelinesUpdate)|
|[az devops pipeline delete](#PipelinesDelete)|Delete|[Parameters](#ParametersPipelinesDelete)|[Example](#ExamplesPipelinesDelete)|

### <a name="CommandsInPipelineTemplateDefinitions">Commands in `az devops pipeline-template-definition` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devops pipeline-template-definition list](#PipelineTemplateDefinitionsList)|List|[Parameters](#ParametersPipelineTemplateDefinitionsList)|[Example](#ExamplesPipelineTemplateDefinitionsList)|


## COMMAND DETAILS

### group `az devops pipeline`
#### <a name="PipelinesListByResourceGroup">Command `az devops pipeline list`</a>

##### <a name="ExamplesPipelinesListByResourceGroup">Example</a>
```
az devops pipeline list --resource-group "myAspNetWebAppPipeline-rg"
```
##### <a name="ParametersPipelinesListByResourceGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group within the Azure subscription.|resource_group_name|resourceGroupName|

#### <a name="PipelinesListBySubscription">Command `az devops pipeline list`</a>

##### <a name="ExamplesPipelinesListBySubscription">Example</a>
```
az devops pipeline list
```
##### <a name="ParametersPipelinesListBySubscription">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="PipelinesGet">Command `az devops pipeline show`</a>

##### <a name="ExamplesPipelinesGet">Example</a>
```
az devops pipeline show --name "myAspNetWebAppPipeline" --resource-group "myAspNetWebAppPipeline-rg"
```
##### <a name="ParametersPipelinesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group within the Azure subscription.|resource_group_name|resourceGroupName|
|**--pipeline-name**|string|The name of the Azure Pipeline resource in ARM.|pipeline_name|pipelineName|

#### <a name="PipelinesCreateOrUpdate#Create">Command `az devops pipeline create`</a>

##### <a name="ExamplesPipelinesCreateOrUpdate#Create">Example</a>
```
az devops pipeline create --location "South India" --properties bootstrapConfiguration={"template":{"id":"ms.vss-contin\
uous-delivery-pipeline-templates.aspnet-windowswebapp","parameters":{"appInsightLocation":"South \
India","appServicePlan":"S1 Standard","azureAuth":"{\\"scheme\\":\\"ServicePrincipal\\",\\"parameters\\":{\\"tenantid\\\
":\\"{subscriptionTenantId}\\",\\"objectid\\":\\"{appObjectId}\\",\\"serviceprincipalid\\":\\"{appId}\\",\\"serviceprin\
cipalkey\\":\\"{appSecret}\\"}}","location":"South India","resourceGroup":"myAspNetWebAppPipeline-rg","subscriptionId":\
"{subscriptionId}","webAppName":"myAspNetWebApp"}}} organization={"name":"myAspNetWebAppPipeline-org"} \
project={"name":"myAspNetWebAppPipeline-project"} --pipeline-name "myAspNetWebAppPipeline" --resource-group \
"myAspNetWebAppPipeline-rg"
```
##### <a name="ParametersPipelinesCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group within the Azure subscription.|resource_group_name|resourceGroupName|
|**--pipeline-name**|string|The name of the Azure Pipeline resource in ARM.|pipeline_name|pipelineName|
|**--id**|string|Unique identifier of the pipeline template.|id|id|
|**--name**|string|Name of the Azure DevOps Project.|name|name|
|**--organization-reference-name**|string|Name of the Azure DevOps Organization.|organization_reference_name|name|
|**--tags**|dictionary|Resource Tags|tags|tags|
|**--location**|string|Resource Location|location|location|
|**--parameters**|dictionary|Dictionary of input parameters used in the pipeline template.|parameters|parameters|
|**--repository-type**|choice|Type of code repository.|repository_type|repositoryType|
|**--code-repository-id**|string|Unique immutable identifier of the code repository.|code_repository_id|id|
|**--default-branch**|string|Default branch used to configure Continuous Integration (CI) in the pipeline.|default_branch|defaultBranch|
|**--properties**|dictionary|Repository-specific properties.|properties|properties|
|**--authorization-parameters**|dictionary|Authorization parameters corresponding to the authorization type.|authorization_parameters|parameters|

#### <a name="PipelinesUpdate">Command `az devops pipeline update`</a>

##### <a name="ExamplesPipelinesUpdate">Example</a>
```
az devops pipeline update --name "myAspNetWebAppPipeline" --resource-group "myAspNetWebAppPipeline-rg" --tags \
tagKey="tagvalue"
```
##### <a name="ParametersPipelinesUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group within the Azure subscription.|resource_group_name|resourceGroupName|
|**--pipeline-name**|string|The name of the Azure Pipeline resource.|pipeline_name|pipelineName|
|**--tags**|dictionary|Dictionary of key-value pairs to be set as tags on the Azure Pipeline. This will overwrite any existing tags.|tags|tags|

#### <a name="PipelinesDelete">Command `az devops pipeline delete`</a>

##### <a name="ExamplesPipelinesDelete">Example</a>
```
az devops pipeline delete --name "myAspNetWebAppPipeline" --resource-group "myAspNetWebAppPipeline-rg"
```
##### <a name="ParametersPipelinesDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group within the Azure subscription.|resource_group_name|resourceGroupName|
|**--pipeline-name**|string|The name of the Azure Pipeline resource.|pipeline_name|pipelineName|

### group `az devops pipeline-template-definition`
#### <a name="PipelineTemplateDefinitionsList">Command `az devops pipeline-template-definition list`</a>

##### <a name="ExamplesPipelineTemplateDefinitionsList">Example</a>
```
az devops pipeline-template-definition list
```
##### <a name="ParametersPipelineTemplateDefinitionsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|