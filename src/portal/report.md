# Azure CLI Module Creation Report

### portal dashboard create

create a portal dashboard.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|portal dashboard|Dashboards|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|CreateOrUpdate#Create|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group.|resource_group_name|resourceGroupName|
|**--dashboard-name**|string|The name of the dashboard.|dashboard_name|dashboardName|
|**--location**|string|Resource location|location|location|
|**--tags**|dictionary|Resource tags|tags|tags|
|**--lenses**|dictionary|The dashboard lenses.|lenses|lenses|
|**--metadata**|dictionary|The dashboard metadata.|metadata|metadata|

### portal dashboard delete

delete a portal dashboard.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|portal dashboard|Dashboards|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|Delete|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group.|resource_group_name|resourceGroupName|
|**--dashboard-name**|string|The name of the dashboard.|dashboard_name|dashboardName|

### portal dashboard list

list a portal dashboard.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|portal dashboard|Dashboards|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListByResourceGroup|
|list|ListBySubscription|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group.|resource_group_name|resourceGroupName|

### portal dashboard show

show a portal dashboard.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|portal dashboard|Dashboards|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|show|Get|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group.|resource_group_name|resourceGroupName|
|**--dashboard-name**|string|The name of the dashboard.|dashboard_name|dashboardName|

### portal dashboard update

update a portal dashboard.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|portal dashboard|Dashboards|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|Update|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group.|resource_group_name|resourceGroupName|
|**--dashboard-name**|string|The name of the dashboard.|dashboard_name|dashboardName|
|**--tags**|dictionary|Resource tags|tags|tags|
|**--lenses**|dictionary|The dashboard lenses.|lenses|lenses|
|**--metadata**|dictionary|The dashboard metadata.|metadata|metadata|
