# Azure CLI Module Creation Report

### storagecache cache create

create a storagecache cache.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Target resource group.|resource_group_name|resource_group_name|
|**--cache_name**|string|Name of Cache.|cache_name|cache_name|
|**--tags**|object|ARM tags as name/value pairs.|tags|tags|
|**--location**|string|Region name string.|location|location|
|**--sku**|object|SKU for the Cache.|sku|sku|
|**--cache_size_gb**|integer|The size of this Cache, in GB.|cache_size_gb|properties_cache_size_gb|
|**--provisioning_state**|choice|ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property|provisioning_state|properties_provisioning_state|
|**--subnet**|string|A fully qualified URL.|subnet|properties_subnet|
|**--upgrade_status**|object|Properties describing the software upgrade state of the Cache.|upgrade_status|properties_upgrade_status|
### storagecache cache delete

delete a storagecache cache.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Target resource group.|resource_group_name|resource_group_name|
|**--cache_name**|string|Name of Cache.|cache_name|cache_name|
### storagecache cache flush

flush a storagecache cache.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Target resource group.|resource_group_name|resource_group_name|
|**--cache_name**|string|Name of Cache.|cache_name|cache_name|
### storagecache cache list

list a storagecache cache.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Target resource group.|resource_group_name|resource_group_name|
### storagecache cache show

show a storagecache cache.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Target resource group.|resource_group_name|resource_group_name|
|**--cache_name**|string|Name of Cache.|cache_name|cache_name|
### storagecache cache start

start a storagecache cache.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Target resource group.|resource_group_name|resource_group_name|
|**--cache_name**|string|Name of Cache.|cache_name|cache_name|
### storagecache cache stop

stop a storagecache cache.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Target resource group.|resource_group_name|resource_group_name|
|**--cache_name**|string|Name of Cache.|cache_name|cache_name|
### storagecache cache update

update a storagecache cache.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Target resource group.|resource_group_name|resource_group_name|
|**--cache_name**|string|Name of Cache.|cache_name|cache_name|
|**--tags**|object|ARM tags as name/value pairs.|tags|tags|
|**--location**|string|Region name string.|location|location|
|**--sku**|object|SKU for the Cache.|sku|sku|
|**--cache_size_gb**|integer|The size of this Cache, in GB.|cache_size_gb|properties_cache_size_gb|
|**--provisioning_state**|choice|ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property|provisioning_state|properties_provisioning_state|
|**--subnet**|string|A fully qualified URL.|subnet|properties_subnet|
|**--upgrade_status**|object|Properties describing the software upgrade state of the Cache.|upgrade_status|properties_upgrade_status|
### storagecache cache upgrade-firmware

upgrade-firmware a storagecache cache.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Target resource group.|resource_group_name|resource_group_name|
|**--cache_name**|string|Name of Cache.|cache_name|cache_name|
### storagecache sku list

list a storagecache sku.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
### storagecache storage-target create

create a storagecache storage-target.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Target resource group.|resource_group_name|resource_group_name|
|**--cache_name**|string|Name of Cache.|cache_name|cache_name|
|**--storage_target_name**|string|Name of Storage Target.|storage_target_name|storage_target_name|
|**--junctions**|array|List of Cache namespace junctions to target for namespace associations.|junctions|properties_junctions|
|**--target_type**|choice|Type of the Storage Target.|target_type|properties_target_type|
|**--provisioning_state**|choice|ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property|provisioning_state|properties_provisioning_state|
|**--nfs3**|object|An NFSv3 mount point for use as a Storage Target.|nfs3|properties_nfs3|
|**--clfs**|object|Storage container for use as a CLFS Storage Target.|clfs|properties_clfs|
|**--unknown**|object|Storage container for use as an Unknown Storage Target.|unknown|properties_unknown|
### storagecache storage-target delete

delete a storagecache storage-target.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Target resource group.|resource_group_name|resource_group_name|
|**--cache_name**|string|Name of Cache.|cache_name|cache_name|
|**--storage_target_name**|string|Name of Storage Target.|storage_target_name|storage_target_name|
### storagecache storage-target list

list a storagecache storage-target.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Target resource group.|resource_group_name|resource_group_name|
|**--cache_name**|string|Name of Cache.|cache_name|cache_name|
### storagecache storage-target show

show a storagecache storage-target.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Target resource group.|resource_group_name|resource_group_name|
|**--cache_name**|string|Name of Cache.|cache_name|cache_name|
|**--storage_target_name**|string|Name of Storage Target.|storage_target_name|storage_target_name|
### storagecache storage-target update

create a storagecache storage-target.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|Target resource group.|resource_group_name|resource_group_name|
|**--cache_name**|string|Name of Cache.|cache_name|cache_name|
|**--storage_target_name**|string|Name of Storage Target.|storage_target_name|storage_target_name|
|**--junctions**|array|List of Cache namespace junctions to target for namespace associations.|junctions|properties_junctions|
|**--target_type**|choice|Type of the Storage Target.|target_type|properties_target_type|
|**--provisioning_state**|choice|ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property|provisioning_state|properties_provisioning_state|
|**--nfs3**|object|An NFSv3 mount point for use as a Storage Target.|nfs3|properties_nfs3|
|**--clfs**|object|Storage container for use as a CLFS Storage Target.|clfs|properties_clfs|
|**--unknown**|object|Storage container for use as an Unknown Storage Target.|unknown|properties_unknown|
### storagecache usage-model list

list a storagecache usage-model.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|