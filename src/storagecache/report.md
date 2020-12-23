# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az storagecache|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az storagecache` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az storagecache sku|Skus|[commands](#CommandsInSkus)|
|az storagecache usage-model|UsageModels|[commands](#CommandsInUsageModels)|
|az storagecache asc-operation|AscOperations|[commands](#CommandsInAscOperations)|
|az storagecache cache|Caches|[commands](#CommandsInCaches)|
|az storagecache storage-target|StorageTargets|[commands](#CommandsInStorageTargets)|

## COMMANDS
### <a name="CommandsInAscOperations">Commands in `az storagecache asc-operation` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az storagecache asc-operation show](#AscOperationsGet)|Get|[Parameters](#ParametersAscOperationsGet)|[Example](#ExamplesAscOperationsGet)|

### <a name="CommandsInCaches">Commands in `az storagecache cache` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az storagecache cache list](#CachesListByResourceGroup)|ListByResourceGroup|[Parameters](#ParametersCachesListByResourceGroup)|[Example](#ExamplesCachesListByResourceGroup)|
|[az storagecache cache list](#CachesList)|List|[Parameters](#ParametersCachesList)|[Example](#ExamplesCachesList)|
|[az storagecache cache show](#CachesGet)|Get|[Parameters](#ParametersCachesGet)|[Example](#ExamplesCachesGet)|
|[az storagecache cache create](#CachesCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersCachesCreateOrUpdate#Create)|[Example](#ExamplesCachesCreateOrUpdate#Create)|
|[az storagecache cache update](#CachesUpdate)|Update|[Parameters](#ParametersCachesUpdate)|[Example](#ExamplesCachesUpdate)|
|[az storagecache cache delete](#CachesDelete)|Delete|[Parameters](#ParametersCachesDelete)|[Example](#ExamplesCachesDelete)|
|[az storagecache cache debug-info](#CachesDebugInfo)|DebugInfo|[Parameters](#ParametersCachesDebugInfo)|[Example](#ExamplesCachesDebugInfo)|
|[az storagecache cache flush](#CachesFlush)|Flush|[Parameters](#ParametersCachesFlush)|[Example](#ExamplesCachesFlush)|
|[az storagecache cache start](#CachesStart)|Start|[Parameters](#ParametersCachesStart)|[Example](#ExamplesCachesStart)|
|[az storagecache cache stop](#CachesStop)|Stop|[Parameters](#ParametersCachesStop)|[Example](#ExamplesCachesStop)|
|[az storagecache cache upgrade-firmware](#CachesUpgradeFirmware)|UpgradeFirmware|[Parameters](#ParametersCachesUpgradeFirmware)|[Example](#ExamplesCachesUpgradeFirmware)|

### <a name="CommandsInSkus">Commands in `az storagecache sku` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az storagecache sku list](#SkusList)|List|[Parameters](#ParametersSkusList)|[Example](#ExamplesSkusList)|

### <a name="CommandsInStorageTargets">Commands in `az storagecache storage-target` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az storagecache storage-target list](#StorageTargetsListByCache)|ListByCache|[Parameters](#ParametersStorageTargetsListByCache)|[Example](#ExamplesStorageTargetsListByCache)|
|[az storagecache storage-target show](#StorageTargetsGet)|Get|[Parameters](#ParametersStorageTargetsGet)|[Example](#ExamplesStorageTargetsGet)|
|[az storagecache storage-target create](#StorageTargetsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersStorageTargetsCreateOrUpdate#Create)|[Example](#ExamplesStorageTargetsCreateOrUpdate#Create)|
|[az storagecache storage-target update](#StorageTargetsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersStorageTargetsCreateOrUpdate#Update)|Not Found|
|[az storagecache storage-target delete](#StorageTargetsDelete)|Delete|[Parameters](#ParametersStorageTargetsDelete)|[Example](#ExamplesStorageTargetsDelete)|

### <a name="CommandsInUsageModels">Commands in `az storagecache usage-model` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az storagecache usage-model list](#UsageModelsList)|List|[Parameters](#ParametersUsageModelsList)|[Example](#ExamplesUsageModelsList)|


## COMMAND DETAILS

### group `az storagecache asc-operation`
#### <a name="AscOperationsGet">Command `az storagecache asc-operation show`</a>

##### <a name="ExamplesAscOperationsGet">Example</a>
```
az storagecache asc-operation show --operation-id "testoperationid" --location "westus"
```
##### <a name="ParametersAscOperationsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|The name of the region used to look up the operation.|location|location|
|**--operation-id**|string|The operation id which uniquely identifies the asynchronous operation.|operation_id|operationId|

### group `az storagecache cache`
#### <a name="CachesListByResourceGroup">Command `az storagecache cache list`</a>

##### <a name="ExamplesCachesListByResourceGroup">Example</a>
```
az storagecache cache list --resource-group "scgroup"
```
##### <a name="ParametersCachesListByResourceGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Target resource group.|resource_group_name|resourceGroupName|

#### <a name="CachesList">Command `az storagecache cache list`</a>

##### <a name="ExamplesCachesList">Example</a>
```
az storagecache cache list
```
##### <a name="ParametersCachesList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="CachesGet">Command `az storagecache cache show`</a>

##### <a name="ExamplesCachesGet">Example</a>
```
az storagecache cache show --cache-name "sc1" --resource-group "scgroup"
```
##### <a name="ParametersCachesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Target resource group.|resource_group_name|resourceGroupName|
|**--cache-name**|string|Name of Cache. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.|cache_name|cacheName|

#### <a name="CachesCreateOrUpdate#Create">Command `az storagecache cache create`</a>

##### <a name="ExamplesCachesCreateOrUpdate#Create">Example</a>
```
az storagecache cache create --location "westus" --cache-size-gb 3072 --subnet "/subscriptions/00000000-0000-0000-0000-\
000000000000/resourceGroups/scgroup/providers/Microsoft.Network/virtualNetworks/scvnet/subnets/sub1" --sku-name \
"Standard_2G" --tags "{\\"Dept\\":\\"ContosoAds\\"}" --cache-name "sc1" --resource-group "scgroup"
```
##### <a name="ExamplesCachesCreateOrUpdate#Create">Example</a>
```
az storagecache cache create --location "westus" --cache-size-gb 3072 --subnet "/subscriptions/00000000-0000-0000-0000-\
000000000000/resourceGroups/scgroup/providers/Microsoft.Network/virtualNetworks/scvnet/subnets/sub1" --sku-name \
"Standard_2G" --tags "{\\"Dept\\":\\"ContosoAds\\"}" --cache-name "sc1" --resource-group "scgroup"
```
##### <a name="ParametersCachesCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Target resource group.|resource_group_name|resourceGroupName|
|**--cache-name**|string|Name of Cache. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.|cache_name|cacheName|
|**--tags**|any|ARM tags as name/value pairs.|tags|tags|
|**--location**|string|Region name string.|location|location|
|**--cache-size-gb**|integer|The size of this Cache, in GB.|cache_size_gb|cacheSizeGB|
|**--provisioning-state**|choice|ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property|provisioning_state|provisioningState|
|**--subnet**|string|Subnet used for the Cache.|subnet|subnet|
|**--directory-services-settings-username-download-extended-groups-enabled**|boolean|Whether or not Extended Groups is enabled.|extended_groups_enabled|extendedGroupsEnabled|
|**--directory-services-settings-username-download-username-source**|choice|This setting determines how the cache gets username and group names for clients.|username_source|usernameSource|
|**--directory-services-settings-username-download-group-file-uri**|string|The URI of the file containing group information (in /etc/group file format). This field must be populated when 'usernameSource' is set to 'File'.|group_file_uri|groupFileURI|
|**--directory-services-settings-username-download-user-file-uri**|string|The URI of the file containing user information (in /etc/passwd file format). This field must be populated when 'usernameSource' is set to 'File'.|user_file_uri|userFileURI|
|**--directory-services-settings-username-download-ldap-server**|string|The fully qualified domain name or IP address of the LDAP server to use.|ldap_server|ldapServer|
|**--directory-services-settings-username-download-ldap-base-dn**|string|The base distinguished name for the LDAP domain.|ldap_base_dn|ldapBaseDn|
|**--directory-services-settings-username-download-encrypt-ldap-connection**|boolean|Whether or not the LDAP connection should be encrypted.|encrypt_ldap_connection|encryptLdapConnection|
|**--directory-services-settings-username-download-require-valid-certificate**|boolean|Determines if the certificates must be validated by a certificate authority. When true, caCertificateURI must be provided.|require_valid_certificate|requireValidCertificate|
|**--directory-services-settings-username-download-auto-download-certificate**|boolean|Determines if the certificate should be automatically downloaded. This applies to 'caCertificateURI' only if 'requireValidCertificate' is true.|auto_download_certificate|autoDownloadCertificate|
|**--directory-services-settings-username-download-ca-certificate-uri**|string|The URI of the CA certificate to validate the LDAP secure connection. This field must be populated when 'requireValidCertificate' is set to true.|ca_certificate_uri|caCertificateURI|
|**--directory-services-settings-username-download-credentials**|object|When present, these are the credentials for the secure LDAP connection.|credentials|credentials|
|**--directory-services-settings-active-directory-primary-dns-ip-address**|string|Primary DNS IP address used to resolve the Active Directory domain controller's fully qualified domain name.|primary_dns_ip_address|primaryDnsIpAddress|
|**--directory-services-settings-active-directory-secondary-dns-ip-address**|string|Secondary DNS IP address used to resolve the Active Directory domain controller's fully qualified domain name.|secondary_dns_ip_address|secondaryDnsIpAddress|
|**--directory-services-settings-active-directory-domain-name**|string|The fully qualified domain name of the Active Directory domain controller.|domain_name|domainName|
|**--directory-services-settings-active-directory-domain-net-bios-name**|string|The Active Directory domain's NetBIOS name.|domain_net_bios_name|domainNetBiosName|
|**--directory-services-settings-active-directory-cache-net-bios-name**|string|The NetBIOS name to assign to the HPC Cache when it joins the Active Directory domain as a server. Length must 1-15 characters from the class [-0-9a-zA-Z].|cache_net_bios_name|cacheNetBiosName|
|**--security-settings-access-policies**|array|NFS access policies defined for this cache.|access_policies|accessPolicies|
|**--encryption-settings-key-encryption-key-key-url**|string|The URL referencing a key encryption key in Key Vault.|key_url|keyUrl|
|**--encryption-settings-key-encryption-key-source-vault-id**|string|Resource Id.|id|id|
|**--network-settings-mtu**|integer|The IPv4 maximum transmission unit configured for the subnet.|mtu|mtu|
|**--sku-name**|string|SKU name for this Cache.|name|name|
|**--identity-type**|sealed-choice|The type of identity used for the cache|type|type|

#### <a name="CachesUpdate">Command `az storagecache cache update`</a>

##### <a name="ExamplesCachesUpdate">Example</a>
```
az storagecache cache update --location "westus" --cache-size-gb 3072 --subnet "/subscriptions/00000000-0000-0000-0000-\
000000000000/resourceGroups/scgroup/providers/Microsoft.Network/virtualNetworks/scvnet/subnets/sub1" --sku-name \
"Standard_2G" --tags "{\\"Dept\\":\\"ContosoAds\\"}" --cache-name "sc1" --resource-group "scgroup"
```
##### <a name="ExamplesCachesUpdate">Example</a>
```
az storagecache cache update --location "westus" --cache-size-gb 3072 --subnet "/subscriptions/00000000-0000-0000-0000-\
000000000000/resourceGroups/scgroup/providers/Microsoft.Network/virtualNetworks/scvnet/subnets/sub1" --sku-name \
"Standard_2G" --tags "{\\"Dept\\":\\"ContosoAds\\"}" --cache-name "sc1" --resource-group "scgroup"
```
##### <a name="ParametersCachesUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Target resource group.|resource_group_name|resourceGroupName|
|**--cache-name**|string|Name of Cache. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.|cache_name|cacheName|
|**--tags**|any|ARM tags as name/value pairs.|tags|tags|
|**--location**|string|Region name string.|location|location|
|**--cache-size-gb**|integer|The size of this Cache, in GB.|cache_size_gb|cacheSizeGB|
|**--provisioning-state**|choice|ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property|provisioning_state|provisioningState|
|**--subnet**|string|Subnet used for the Cache.|subnet|subnet|
|**--directory-services-settings-username-download-extended-groups-enabled**|boolean|Whether or not Extended Groups is enabled.|extended_groups_enabled|extendedGroupsEnabled|
|**--directory-services-settings-username-download-username-source**|choice|This setting determines how the cache gets username and group names for clients.|username_source|usernameSource|
|**--directory-services-settings-username-download-group-file-uri**|string|The URI of the file containing group information (in /etc/group file format). This field must be populated when 'usernameSource' is set to 'File'.|group_file_uri|groupFileURI|
|**--directory-services-settings-username-download-user-file-uri**|string|The URI of the file containing user information (in /etc/passwd file format). This field must be populated when 'usernameSource' is set to 'File'.|user_file_uri|userFileURI|
|**--directory-services-settings-username-download-ldap-server**|string|The fully qualified domain name or IP address of the LDAP server to use.|ldap_server|ldapServer|
|**--directory-services-settings-username-download-ldap-base-dn**|string|The base distinguished name for the LDAP domain.|ldap_base_dn|ldapBaseDn|
|**--directory-services-settings-username-download-encrypt-ldap-connection**|boolean|Whether or not the LDAP connection should be encrypted.|encrypt_ldap_connection|encryptLdapConnection|
|**--directory-services-settings-username-download-require-valid-certificate**|boolean|Determines if the certificates must be validated by a certificate authority. When true, caCertificateURI must be provided.|require_valid_certificate|requireValidCertificate|
|**--directory-services-settings-username-download-auto-download-certificate**|boolean|Determines if the certificate should be automatically downloaded. This applies to 'caCertificateURI' only if 'requireValidCertificate' is true.|auto_download_certificate|autoDownloadCertificate|
|**--directory-services-settings-username-download-ca-certificate-uri**|string|The URI of the CA certificate to validate the LDAP secure connection. This field must be populated when 'requireValidCertificate' is set to true.|ca_certificate_uri|caCertificateURI|
|**--directory-services-settings-username-download-credentials**|object|When present, these are the credentials for the secure LDAP connection.|credentials|credentials|
|**--directory-services-settings-active-directory-primary-dns-ip-address**|string|Primary DNS IP address used to resolve the Active Directory domain controller's fully qualified domain name.|primary_dns_ip_address|primaryDnsIpAddress|
|**--directory-services-settings-active-directory-secondary-dns-ip-address**|string|Secondary DNS IP address used to resolve the Active Directory domain controller's fully qualified domain name.|secondary_dns_ip_address|secondaryDnsIpAddress|
|**--directory-services-settings-active-directory-domain-name**|string|The fully qualified domain name of the Active Directory domain controller.|domain_name|domainName|
|**--directory-services-settings-active-directory-domain-net-bios-name**|string|The Active Directory domain's NetBIOS name.|domain_net_bios_name|domainNetBiosName|
|**--directory-services-settings-active-directory-cache-net-bios-name**|string|The NetBIOS name to assign to the HPC Cache when it joins the Active Directory domain as a server. Length must 1-15 characters from the class [-0-9a-zA-Z].|cache_net_bios_name|cacheNetBiosName|
|**--security-settings-access-policies**|array|NFS access policies defined for this cache.|access_policies|accessPolicies|
|**--encryption-settings-key-encryption-key-key-url**|string|The URL referencing a key encryption key in Key Vault.|key_url|keyUrl|
|**--encryption-settings-key-encryption-key-source-vault-id**|string|Resource Id.|id|id|
|**--network-settings-mtu**|integer|The IPv4 maximum transmission unit configured for the subnet.|mtu|mtu|
|**--sku-name**|string|SKU name for this Cache.|name|name|
|**--identity-type**|sealed-choice|The type of identity used for the cache|type|type|

#### <a name="CachesDelete">Command `az storagecache cache delete`</a>

##### <a name="ExamplesCachesDelete">Example</a>
```
az storagecache cache delete --cache-name "sc" --resource-group "scgroup"
```
##### <a name="ParametersCachesDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Target resource group.|resource_group_name|resourceGroupName|
|**--cache-name**|string|Name of Cache. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.|cache_name|cacheName|

#### <a name="CachesDebugInfo">Command `az storagecache cache debug-info`</a>

##### <a name="ExamplesCachesDebugInfo">Example</a>
```
az storagecache cache debug-info --cache-name "sc" --resource-group "scgroup"
```
##### <a name="ParametersCachesDebugInfo">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Target resource group.|resource_group_name|resourceGroupName|
|**--cache-name**|string|Name of Cache. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.|cache_name|cacheName|

#### <a name="CachesFlush">Command `az storagecache cache flush`</a>

##### <a name="ExamplesCachesFlush">Example</a>
```
az storagecache cache flush --cache-name "sc" --resource-group "scgroup"
```
##### <a name="ParametersCachesFlush">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Target resource group.|resource_group_name|resourceGroupName|
|**--cache-name**|string|Name of Cache. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.|cache_name|cacheName|

#### <a name="CachesStart">Command `az storagecache cache start`</a>

##### <a name="ExamplesCachesStart">Example</a>
```
az storagecache cache start --cache-name "sc" --resource-group "scgroup"
```
##### <a name="ParametersCachesStart">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Target resource group.|resource_group_name|resourceGroupName|
|**--cache-name**|string|Name of Cache. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.|cache_name|cacheName|

#### <a name="CachesStop">Command `az storagecache cache stop`</a>

##### <a name="ExamplesCachesStop">Example</a>
```
az storagecache cache stop --cache-name "sc" --resource-group "scgroup"
```
##### <a name="ParametersCachesStop">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Target resource group.|resource_group_name|resourceGroupName|
|**--cache-name**|string|Name of Cache. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.|cache_name|cacheName|

#### <a name="CachesUpgradeFirmware">Command `az storagecache cache upgrade-firmware`</a>

##### <a name="ExamplesCachesUpgradeFirmware">Example</a>
```
az storagecache cache upgrade-firmware --cache-name "sc1" --resource-group "scgroup"
```
##### <a name="ParametersCachesUpgradeFirmware">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Target resource group.|resource_group_name|resourceGroupName|
|**--cache-name**|string|Name of Cache. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.|cache_name|cacheName|

### group `az storagecache sku`
#### <a name="SkusList">Command `az storagecache sku list`</a>

##### <a name="ExamplesSkusList">Example</a>
```
az storagecache sku list
```
##### <a name="ParametersSkusList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
### group `az storagecache storage-target`
#### <a name="StorageTargetsListByCache">Command `az storagecache storage-target list`</a>

##### <a name="ExamplesStorageTargetsListByCache">Example</a>
```
az storagecache storage-target list --cache-name "sc1" --resource-group "scgroup"
```
##### <a name="ParametersStorageTargetsListByCache">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Target resource group.|resource_group_name|resourceGroupName|
|**--cache-name**|string|Name of Cache. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.|cache_name|cacheName|

#### <a name="StorageTargetsGet">Command `az storagecache storage-target show`</a>

##### <a name="ExamplesStorageTargetsGet">Example</a>
```
az storagecache storage-target show --cache-name "sc1" --resource-group "scgroup" --name "st1"
```
##### <a name="ParametersStorageTargetsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Target resource group.|resource_group_name|resourceGroupName|
|**--cache-name**|string|Name of Cache. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.|cache_name|cacheName|
|**--storage-target-name**|string|Name of the Storage Target. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.|storage_target_name|storageTargetName|

#### <a name="StorageTargetsCreateOrUpdate#Create">Command `az storagecache storage-target create`</a>

##### <a name="ExamplesStorageTargetsCreateOrUpdate#Create">Example</a>
```
az storagecache storage-target create --cache-name "sc1" --resource-group "scgroup" --name "st1" --junctions \
namespace-path="/path/on/cache" nfs-access-policy="default" nfs-export="exp1" target-path="/path/on/exp1" --junctions \
namespace-path="/path2/on/cache" nfs-access-policy="rootSquash" nfs-export="exp2" target-path="/path2/on/exp2" --nfs3 \
target="10.0.44.44" usage-model="READ_HEAVY_INFREQ"
```
##### <a name="ExamplesStorageTargetsCreateOrUpdate#Create">Example</a>
```
az storagecache storage-target create --cache-name "sc1" --resource-group "scgroup" --name "st1" --nfs3 \
target="10.0.44.44" usage-model="READ_HEAVY_INFREQ"
```
##### <a name="ParametersStorageTargetsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Target resource group.|resource_group_name|resourceGroupName|
|**--cache-name**|string|Name of Cache. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.|cache_name|cacheName|
|**--storage-target-name**|string|Name of the Storage Target. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.|storage_target_name|storageTargetName|
|**--junctions**|array|List of Cache namespace junctions to target for namespace associations.|junctions|junctions|
|**--provisioning-state**|choice|ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property|provisioning_state|provisioningState|
|**--nfs3**|object|Properties when targetType is nfs3.|nfs3|nfs3|
|**--unknown-unknown-map**|dictionary|Dictionary of string->string pairs containing information about the Storage Target.|unknown_map|unknownMap|
|**--clfs-target**|string|Resource ID of storage container.|target|target|

#### <a name="StorageTargetsCreateOrUpdate#Update">Command `az storagecache storage-target update`</a>

##### <a name="ParametersStorageTargetsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Target resource group.|resource_group_name|resourceGroupName|
|**--cache-name**|string|Name of Cache. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.|cache_name|cacheName|
|**--storage-target-name**|string|Name of the Storage Target. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.|storage_target_name|storageTargetName|
|**--junctions**|array|List of Cache namespace junctions to target for namespace associations.|junctions|junctions|
|**--provisioning-state**|choice|ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property|provisioning_state|provisioningState|
|**--nfs3**|object|Properties when targetType is nfs3.|nfs3|nfs3|
|**--unknown-unknown-map**|dictionary|Dictionary of string->string pairs containing information about the Storage Target.|unknown_map|unknownMap|
|**--clfs-target**|string|Resource ID of storage container.|target|target|

#### <a name="StorageTargetsDelete">Command `az storagecache storage-target delete`</a>

##### <a name="ExamplesStorageTargetsDelete">Example</a>
```
az storagecache storage-target delete --cache-name "sc1" --resource-group "scgroup" --name "st1"
```
##### <a name="ParametersStorageTargetsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Target resource group.|resource_group_name|resourceGroupName|
|**--cache-name**|string|Name of Cache. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class.|cache_name|cacheName|
|**--storage-target-name**|string|Name of Storage Target.|storage_target_name|storageTargetName|

### group `az storagecache usage-model`
#### <a name="UsageModelsList">Command `az storagecache usage-model list`</a>

##### <a name="ExamplesUsageModelsList">Example</a>
```
az storagecache usage-model list
```
##### <a name="ParametersUsageModelsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|