# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az cpim|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az cpim` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az cpim b2-c-tenant|B2CTenants|[commands](#CommandsInB2CTenants)|
|az cpim operation|Operations|[commands](#CommandsInOperations)|

## COMMANDS
### <a name="CommandsInB2CTenants">Commands in `az cpim b2-c-tenant` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cpim b2-c-tenant list](#B2CTenantsListByResourceGroup)|ListByResourceGroup|[Parameters](#ParametersB2CTenantsListByResourceGroup)|[Example](#ExamplesB2CTenantsListByResourceGroup)|
|[az cpim b2-c-tenant list](#B2CTenantsListBySubscription)|ListBySubscription|[Parameters](#ParametersB2CTenantsListBySubscription)|[Example](#ExamplesB2CTenantsListBySubscription)|
|[az cpim b2-c-tenant show](#B2CTenantsGet)|Get|[Parameters](#ParametersB2CTenantsGet)|[Example](#ExamplesB2CTenantsGet)|
|[az cpim b2-c-tenant create](#B2CTenantsCreate)|Create|[Parameters](#ParametersB2CTenantsCreate)|[Example](#ExamplesB2CTenantsCreate)|
|[az cpim b2-c-tenant update](#B2CTenantsUpdate)|Update|[Parameters](#ParametersB2CTenantsUpdate)|[Example](#ExamplesB2CTenantsUpdate)|
|[az cpim b2-c-tenant delete](#B2CTenantsDelete)|Delete|[Parameters](#ParametersB2CTenantsDelete)|[Example](#ExamplesB2CTenantsDelete)|

### <a name="CommandsInOperations">Commands in `az cpim operation` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az cpim operation get-async-status](#OperationsGetAsyncStatus)|GetAsyncStatus|[Parameters](#ParametersOperationsGetAsyncStatus)|[Example](#ExamplesOperationsGetAsyncStatus)|


## COMMAND DETAILS

### group `az cpim b2-c-tenant`
#### <a name="B2CTenantsListByResourceGroup">Command `az cpim b2-c-tenant list`</a>

##### <a name="ExamplesB2CTenantsListByResourceGroup">Example</a>
```
az cpim b2-c-tenant list --resource-group "contosoResourceGroup"
```
##### <a name="ParametersB2CTenantsListByResourceGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group.|resource_group_name|resourceGroupName|

#### <a name="B2CTenantsListBySubscription">Command `az cpim b2-c-tenant list`</a>

##### <a name="ExamplesB2CTenantsListBySubscription">Example</a>
```
az cpim b2-c-tenant list
```
##### <a name="ParametersB2CTenantsListBySubscription">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="B2CTenantsGet">Command `az cpim b2-c-tenant show`</a>

##### <a name="ExamplesB2CTenantsGet">Example</a>
```
az cpim b2-c-tenant show --resource-group "contosoResourceGroup" --resource-name "contoso.onmicrosoft.com"
```
##### <a name="ParametersB2CTenantsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group.|resource_group_name|resourceGroupName|
|**--resource-name**|string|The initial domain name of the B2C tenant.|resource_name|resourceName|

#### <a name="B2CTenantsCreate">Command `az cpim b2-c-tenant create`</a>

##### <a name="ExamplesB2CTenantsCreate">Example</a>
```
az cpim b2-c-tenant create --location "United States" --properties display-name="Contoso" country-code="US" --sku-name \
"Standard" --resource-group "contosoResourceGroup" --resource-name "contoso.onmicrosoft.com"
```
##### <a name="ParametersB2CTenantsCreate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group.|resource_group_name|resourceGroupName|
|**--resource-name**|string|The initial domain name of the B2C tenant.|resource_name|resourceName|
|**--location**|string|The location in which the resource is hosted and data resides. Refer to `this documentation <https://aka.ms/B2CDataResidency>`_ to see valid data residency locations. Please choose one of 'United States', 'Europe', and 'Asia Pacific'.|location|location|
|**--properties**|object||properties|properties|
|**--tags**|dictionary|Resource Tags|tags|tags|
|**--sku-name**|sealed-choice|The name of the SKU for the tenant.|name|name|

#### <a name="B2CTenantsUpdate">Command `az cpim b2-c-tenant update`</a>

##### <a name="ExamplesB2CTenantsUpdate">Example</a>
```
az cpim b2-c-tenant update --resource-group "contosoResourceGroup" --resource-name "contoso.onmicrosoft.com" \
--sku-name "PremiumP1" --tags key="value"
```
##### <a name="ParametersB2CTenantsUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group.|resource_group_name|resourceGroupName|
|**--resource-name**|string|The initial domain name of the B2C tenant.|resource_name|resourceName|
|**--tags**|dictionary|Resource Tags|tags|tags|
|**--tenant-id**|string|An identifier of the B2C tenant.|tenant_id|tenantId|
|**--billing-config-billing-type**|sealed-choice|The type of billing. Will be MAU for all new customers. If 'Auths', it can be updated to 'MAU'. Cannot be changed if value is 'MAU'. Learn more about Azure AD B2C billing at `aka.ms/b2cBilling <https://aka.ms/b2cbilling>`_.|billing_type|billingType|
|**--sku-name**|sealed-choice|The name of the SKU for the tenant.|name|name|

#### <a name="B2CTenantsDelete">Command `az cpim b2-c-tenant delete`</a>

##### <a name="ExamplesB2CTenantsDelete">Example</a>
```
az cpim b2-c-tenant delete --resource-group "rg1" --resource-name "contoso.onmicrosoft.com"
```
##### <a name="ParametersB2CTenantsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group.|resource_group_name|resourceGroupName|
|**--resource-name**|string|The initial domain name of the B2C tenant.|resource_name|resourceName|

### group `az cpim operation`
#### <a name="OperationsGetAsyncStatus">Command `az cpim operation get-async-status`</a>

##### <a name="ExamplesOperationsGetAsyncStatus">Example</a>
```
az cpim operation get-async-status --operation-id "99999999-9999-9999-9999-999999999999"
```
##### <a name="ParametersOperationsGetAsyncStatus">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--operation-id**|string|The operation ID.|operation_id|operationId|
