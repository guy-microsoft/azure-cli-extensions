# Azure CLI Module Creation Report

### kusto attached-database-configuration create

create a kusto attached-database-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--attached_database_configuration_name**|string|The name of the attached database configuration.|attached_database_configuration_name|attached_database_configuration_name|
|**--location**|string|Resource location.|location|location|
|**--database_name**|string|The name of the database which you would like to attach, use * if you want to follow all current and future databases.|database_name|properties_database_name|
|**--cluster_resource_id**|string|The resource id of the cluster where the databases you would like to attach reside.|cluster_resource_id|properties_cluster_resource_id|
|**--default_principals_modification_kind**|choice|The default principals modification kind|default_principals_modification_kind|properties_default_principals_modification_kind|
### kusto attached-database-configuration delete

delete a kusto attached-database-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--attached_database_configuration_name**|string|The name of the attached database configuration.|attached_database_configuration_name|attached_database_configuration_name|
### kusto attached-database-configuration list

list a kusto attached-database-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
### kusto attached-database-configuration show

show a kusto attached-database-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--attached_database_configuration_name**|string|The name of the attached database configuration.|attached_database_configuration_name|attached_database_configuration_name|
### kusto attached-database-configuration update

create a kusto attached-database-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--attached_database_configuration_name**|string|The name of the attached database configuration.|attached_database_configuration_name|attached_database_configuration_name|
|**--location**|string|Resource location.|location|location|
|**--database_name**|string|The name of the database which you would like to attach, use * if you want to follow all current and future databases.|database_name|properties_database_name|
|**--cluster_resource_id**|string|The resource id of the cluster where the databases you would like to attach reside.|cluster_resource_id|properties_cluster_resource_id|
|**--default_principals_modification_kind**|choice|The default principals modification kind|default_principals_modification_kind|properties_default_principals_modification_kind|
### kusto cluster add-language-extension

add-language-extension a kusto cluster.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--value**|array|The list of language extensions.|value|value|
### kusto cluster create

create a kusto cluster.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--location**|string|The geo-location where the resource lives|location|location|
|**--sku**|object|Azure SKU definition.|sku|sku|
|**--tags**|dictionary|Resource tags.|tags|tags|
|**--zones**|array|An array represents the availability zones of the cluster.|zones|zones|
|**--identity**|object|Identity for the resource.|identity|identity|
|**--trusted_external_tenants**|array|The cluster's external tenants.|trusted_external_tenants|properties_trusted_external_tenants|
|**--optimized_autoscale**|object|A class that contains the optimized auto scale definition.|optimized_autoscale|properties_optimized_autoscale|
|**--enable_disk_encryption**|boolean|A boolean value that indicates if the cluster's disks are encrypted.|enable_disk_encryption|properties_enable_disk_encryption|
|**--enable_streaming_ingest**|boolean|A boolean value that indicates if the streaming ingest is enabled.|enable_streaming_ingest|properties_enable_streaming_ingest|
|**--virtual_network_configuration**|object|A class that contains virtual network definition.|virtual_network_configuration|properties_virtual_network_configuration|
|**--key_vault_properties**|object|Properties of the key vault.|key_vault_properties|properties_key_vault_properties|
|**--enable_purge**|boolean|A boolean value that indicates if the purge operations are enabled.|enable_purge|properties_enable_purge|
|**--language_extensions**|object|The list of language extension objects.|language_extensions|properties_language_extensions|
### kusto cluster delete

delete a kusto cluster.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
### kusto cluster detach-follower-database

detach-follower-database a kusto cluster.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--cluster_resource_id**|string|Resource id of the cluster that follows a database owned by this cluster.|cluster_resource_id|cluster_resource_id|
|**--attached_database_configuration_name**|string|Resource name of the attached database configuration in the follower cluster.|attached_database_configuration_name|attached_database_configuration_name|
### kusto cluster diagnose-virtual-network

diagnose-virtual-network a kusto cluster.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
### kusto cluster list

list a kusto cluster.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
### kusto cluster list-follower-database

list-follower-database a kusto cluster.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
### kusto cluster list-language-extension

list-language-extension a kusto cluster.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
### kusto cluster remove-language-extension

remove-language-extension a kusto cluster.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--value**|array|The list of language extensions.|value|value|
### kusto cluster show

show a kusto cluster.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
### kusto cluster start

start a kusto cluster.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
### kusto cluster stop

stop a kusto cluster.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
### kusto cluster update

update a kusto cluster.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--tags**|dictionary|Resource tags.|tags|tags|
|**--location**|string|Resource location.|location|location|
|**--sku**|object|Azure SKU definition.|sku|sku|
|**--identity**|object|Identity for the resource.|identity|identity|
|**--trusted_external_tenants**|array|The cluster's external tenants.|trusted_external_tenants|properties_trusted_external_tenants|
|**--optimized_autoscale**|object|A class that contains the optimized auto scale definition.|optimized_autoscale|properties_optimized_autoscale|
|**--enable_disk_encryption**|boolean|A boolean value that indicates if the cluster's disks are encrypted.|enable_disk_encryption|properties_enable_disk_encryption|
|**--enable_streaming_ingest**|boolean|A boolean value that indicates if the streaming ingest is enabled.|enable_streaming_ingest|properties_enable_streaming_ingest|
|**--virtual_network_configuration**|object|A class that contains virtual network definition.|virtual_network_configuration|properties_virtual_network_configuration|
|**--key_vault_properties**|object|Properties of the key vault.|key_vault_properties|properties_key_vault_properties|
|**--enable_purge**|boolean|A boolean value that indicates if the purge operations are enabled.|enable_purge|properties_enable_purge|
|**--language_extensions**|object|The list of language extension objects.|language_extensions|properties_language_extensions|
### kusto cluster-principal-assignment create

create a kusto cluster-principal-assignment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--principal_assignment_name**|string|The name of the Kusto principalAssignment.|principal_assignment_name|principal_assignment_name|
|**--principal_id**|string|The principal ID assigned to the cluster principal. It can be a user email, application ID, or security group name.|principal_id|properties_principal_id|
|**--role**|choice|Cluster principal role.|role|properties_role|
|**--tenant_id**|string|The tenant id of the principal|tenant_id|properties_tenant_id|
|**--principal_type**|choice|Principal type.|principal_type|properties_principal_type|
### kusto cluster-principal-assignment delete

delete a kusto cluster-principal-assignment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--principal_assignment_name**|string|The name of the Kusto principalAssignment.|principal_assignment_name|principal_assignment_name|
### kusto cluster-principal-assignment list

list a kusto cluster-principal-assignment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
### kusto cluster-principal-assignment show

show a kusto cluster-principal-assignment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--principal_assignment_name**|string|The name of the Kusto principalAssignment.|principal_assignment_name|principal_assignment_name|
### kusto cluster-principal-assignment update

create a kusto cluster-principal-assignment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--principal_assignment_name**|string|The name of the Kusto principalAssignment.|principal_assignment_name|principal_assignment_name|
|**--principal_id**|string|The principal ID assigned to the cluster principal. It can be a user email, application ID, or security group name.|principal_id|properties_principal_id|
|**--role**|choice|Cluster principal role.|role|properties_role|
|**--tenant_id**|string|The tenant id of the principal|tenant_id|properties_tenant_id|
|**--principal_type**|choice|Principal type.|principal_type|properties_principal_type|
### kusto data-connection create

create a kusto data-connection.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--database_name**|string|The name of the database in the Kusto cluster.|database_name|database_name|
|**--data_connection_name**|string|The name of the data connection.|data_connection_name|data_connection_name|
|**--kind**|choice|Kind of the database|kind|kind|
|**--location**|string|Resource location.|location|location|
### kusto data-connection data-connection-validation

data-connection-validation a kusto data-connection.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--database_name**|string|The name of the database in the Kusto cluster.|database_name|database_name|
|**--data_connection_name**|string|The name of the data connection.|data_connection_name|data_connection_name|
|**--properties**|object|Class representing an data connection.|properties|properties|
### kusto data-connection delete

delete a kusto data-connection.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--database_name**|string|The name of the database in the Kusto cluster.|database_name|database_name|
|**--data_connection_name**|string|The name of the data connection.|data_connection_name|data_connection_name|
### kusto data-connection list

list a kusto data-connection.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--database_name**|string|The name of the database in the Kusto cluster.|database_name|database_name|
### kusto data-connection show

show a kusto data-connection.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--database_name**|string|The name of the database in the Kusto cluster.|database_name|database_name|
|**--data_connection_name**|string|The name of the data connection.|data_connection_name|data_connection_name|
### kusto data-connection update

update a kusto data-connection.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--database_name**|string|The name of the database in the Kusto cluster.|database_name|database_name|
|**--data_connection_name**|string|The name of the data connection.|data_connection_name|data_connection_name|
|**--kind**|choice|Kind of the database|kind|kind|
|**--location**|string|Resource location.|location|location|
### kusto database add-principal

add-principal a kusto database.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--database_name**|string|The name of the database in the Kusto cluster.|database_name|database_name|
|**--value**|array|The list of Kusto database principals.|value|value|
### kusto database create

create a kusto database.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--database_name**|string|The name of the database in the Kusto cluster.|database_name|database_name|
|**--kind**|choice|Kind of the database|kind|kind|
|**--location**|string|Resource location.|location|location|
### kusto database delete

delete a kusto database.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--database_name**|string|The name of the database in the Kusto cluster.|database_name|database_name|
### kusto database list

list a kusto database.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
### kusto database list-principal

list-principal a kusto database.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--database_name**|string|The name of the database in the Kusto cluster.|database_name|database_name|
### kusto database remove-principal

remove-principal a kusto database.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--database_name**|string|The name of the database in the Kusto cluster.|database_name|database_name|
|**--value**|array|The list of Kusto database principals.|value|value|
### kusto database show

show a kusto database.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--database_name**|string|The name of the database in the Kusto cluster.|database_name|database_name|
### kusto database update

update a kusto database.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--database_name**|string|The name of the database in the Kusto cluster.|database_name|database_name|
|**--kind**|choice|Kind of the database|kind|kind|
|**--location**|string|Resource location.|location|location|
### kusto database-principal-assignment create

create a kusto database-principal-assignment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--database_name**|string|The name of the database in the Kusto cluster.|database_name|database_name|
|**--principal_assignment_name**|string|The name of the Kusto principalAssignment.|principal_assignment_name|principal_assignment_name|
|**--principal_id**|string|The principal ID assigned to the database principal. It can be a user email, application ID, or security group name.|principal_id|properties_principal_id|
|**--role**|choice|Database principal role.|role|properties_role|
|**--tenant_id**|string|The tenant id of the principal|tenant_id|properties_tenant_id|
|**--principal_type**|choice|Principal type.|principal_type|properties_principal_type|
### kusto database-principal-assignment delete

delete a kusto database-principal-assignment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--database_name**|string|The name of the database in the Kusto cluster.|database_name|database_name|
|**--principal_assignment_name**|string|The name of the Kusto principalAssignment.|principal_assignment_name|principal_assignment_name|
### kusto database-principal-assignment list

list a kusto database-principal-assignment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--database_name**|string|The name of the database in the Kusto cluster.|database_name|database_name|
### kusto database-principal-assignment show

show a kusto database-principal-assignment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--database_name**|string|The name of the database in the Kusto cluster.|database_name|database_name|
|**--principal_assignment_name**|string|The name of the Kusto principalAssignment.|principal_assignment_name|principal_assignment_name|
### kusto database-principal-assignment update

create a kusto database-principal-assignment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The name of the resource group containing the Kusto cluster.|resource_group_name|resource_group_name|
|**--cluster_name**|string|The name of the Kusto cluster.|cluster_name|cluster_name|
|**--database_name**|string|The name of the database in the Kusto cluster.|database_name|database_name|
|**--principal_assignment_name**|string|The name of the Kusto principalAssignment.|principal_assignment_name|principal_assignment_name|
|**--principal_id**|string|The principal ID assigned to the database principal. It can be a user email, application ID, or security group name.|principal_id|properties_principal_id|
|**--role**|choice|Database principal role.|role|properties_role|
|**--tenant_id**|string|The tenant id of the principal|tenant_id|properties_tenant_id|
|**--principal_type**|choice|Principal type.|principal_type|properties_principal_type|