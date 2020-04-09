# Azure CLI Module Creation Report

### customproviders association create

create a customproviders association.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--scope**|string|The scope of the association. The scope can be any valid REST resource instance. For example, use '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.Compute/virtualMachines/{vm-name}' for a virtual machine resource.|scope|scope|
|**--association_name**|string|The name of the association.|association_name|association_name|
|**--target_resource_id**|string|The REST resource instance of the target resource for this association.|target_resource_id|properties_target_resource_id|
### customproviders association delete

delete a customproviders association.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--scope**|string|The scope of the association. The scope can be any valid REST resource instance. For example, use '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.Compute/virtualMachines/{vm-name}' for a virtual machine resource.|scope|scope|
|**--association_name**|string|The name of the association.|association_name|association_name|
### customproviders association list

list a customproviders association.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--scope**|string|The scope of the association. The scope can be any valid REST resource instance. For example, use '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.Compute/virtualMachines/{vm-name}' for a virtual machine resource.|scope|scope|
### customproviders association show

show a customproviders association.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--scope**|string|The scope of the association. The scope can be any valid REST resource instance. For example, use '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.Compute/virtualMachines/{vm-name}' for a virtual machine resource.|scope|scope|
|**--association_name**|string|The name of the association.|association_name|association_name|
### customproviders association update

create a customproviders association.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--scope**|string|The scope of the association. The scope can be any valid REST resource instance. For example, use '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.Compute/virtualMachines/{vm-name}' for a virtual machine resource.|scope|scope|
|**--association_name**|string|The name of the association.|association_name|association_name|
|**--target_resource_id**|string|The REST resource instance of the target resource for this association.|target_resource_id|properties_target_resource_id|
### customproviders custom-resource-provider create

create a customproviders custom-resource-provider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group.|resource_group_name|resource_group_name|
|**--resource_provider_name**|string|The name of the resource provider.|resource_provider_name|resource_provider_name|
|**--location**|string|Resource location|location|location|
|**--tags**|dictionary|Resource tags|tags|tags|
|**--actions**|array|A list of actions that the custom resource provider implements.|actions|properties_actions|
|**--resource_types**|array|A list of resource types that the custom resource provider implements.|resource_types|properties_resource_types|
|**--validations**|array|A list of validations to run on the custom resource provider's requests.|validations|properties_validations|
### customproviders custom-resource-provider delete

delete a customproviders custom-resource-provider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group.|resource_group_name|resource_group_name|
|**--resource_provider_name**|string|The name of the resource provider.|resource_provider_name|resource_provider_name|
### customproviders custom-resource-provider list

list a customproviders custom-resource-provider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group.|resource_group_name|resource_group_name|
### customproviders custom-resource-provider show

show a customproviders custom-resource-provider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group.|resource_group_name|resource_group_name|
|**--resource_provider_name**|string|The name of the resource provider.|resource_provider_name|resource_provider_name|
### customproviders custom-resource-provider update

update a customproviders custom-resource-provider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group.|resource_group_name|resource_group_name|
|**--resource_provider_name**|string|The name of the resource provider.|resource_provider_name|resource_provider_name|
|**--tags**|dictionary|Resource tags|tags|tags|