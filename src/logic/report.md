# Azure CLI Module Creation Report

### logic integration-account create

create a logic integration-account.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
|**--sku**|object|The integration account sku.|sku|sku|
|**--integration_service_environment**|object|The integration service environment.|integration_service_environment|properties_integration_service_environment|
|**--state**|choice|The workflow state.|state|properties_state|
### logic integration-account delete

delete a logic integration-account.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
### logic integration-account list

list a logic integration-account.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--top**|integer|The number of items to be included in the result.|top|top|
### logic integration-account list-callback-url

list-callback-url a logic integration-account.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--not_after**|date-time|The expiry time.|not_after|not_after|
|**--key_type**|choice|The key type.|key_type|key_type|
### logic integration-account list-key-vault-key

list-key-vault-key a logic integration-account.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--key_vault**|object|The key vault reference.|key_vault|key_vault|
|**--skip_token**|string|The skip token.|skip_token|skip_token|
### logic integration-account log-tracking-event

log-tracking-event a logic integration-account.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--source_type**|string|The source type.|source_type|source_type|
|**--events**|array|The events.|events|events|
|**--track_events_options**|choice|The track events operation options.|track_events_options|track_events_options|
### logic integration-account regenerate-access-key

regenerate-access-key a logic integration-account.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--key_type**|choice|The key type.|key_type|key_type|
### logic integration-account show

show a logic integration-account.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
### logic integration-account update

update a logic integration-account.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
|**--sku**|object|The integration account sku.|sku|sku|
|**--integration_service_environment**|object|The integration service environment.|integration_service_environment|properties_integration_service_environment|
|**--state**|choice|The workflow state.|state|properties_state|
### logic integration-account-agreement create

create a logic integration-account-agreement.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--agreement_name**|string|The integration account agreement name.|agreement_name|agreement_name|
|**--agreement_type**|sealed-choice|The agreement type.|agreement_type|properties_agreement_type|
|**--host_partner**|string|The integration account partner that is set as host partner for this agreement.|host_partner|properties_host_partner|
|**--guest_partner**|string|The integration account partner that is set as guest partner for this agreement.|guest_partner|properties_guest_partner|
|**--host_identity**|object|The integration account partner's business identity.|host_identity|properties_host_identity|
|**--guest_identity**|object|The integration account partner's business identity.|guest_identity|properties_guest_identity|
|**--content**|object|The integration account agreement content.|content|properties_content|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
|**--metadata**|object|The metadata.|metadata|properties_metadata|
### logic integration-account-agreement delete

delete a logic integration-account-agreement.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--agreement_name**|string|The integration account agreement name.|agreement_name|agreement_name|
### logic integration-account-agreement list

list a logic integration-account-agreement.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--top**|integer|The number of items to be included in the result.|top|top|
|**--filter**|string|The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.|filter|filter|
### logic integration-account-agreement list-content-callback-url

list-content-callback-url a logic integration-account-agreement.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--agreement_name**|string|The integration account agreement name.|agreement_name|agreement_name|
|**--not_after**|date-time|The expiry time.|not_after|not_after|
|**--key_type**|choice|The key type.|key_type|key_type|
### logic integration-account-agreement show

show a logic integration-account-agreement.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--agreement_name**|string|The integration account agreement name.|agreement_name|agreement_name|
### logic integration-account-agreement update

create a logic integration-account-agreement.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--agreement_name**|string|The integration account agreement name.|agreement_name|agreement_name|
|**--agreement_type**|sealed-choice|The agreement type.|agreement_type|properties_agreement_type|
|**--host_partner**|string|The integration account partner that is set as host partner for this agreement.|host_partner|properties_host_partner|
|**--guest_partner**|string|The integration account partner that is set as guest partner for this agreement.|guest_partner|properties_guest_partner|
|**--host_identity**|object|The integration account partner's business identity.|host_identity|properties_host_identity|
|**--guest_identity**|object|The integration account partner's business identity.|guest_identity|properties_guest_identity|
|**--content**|object|The integration account agreement content.|content|properties_content|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
|**--metadata**|object|The metadata.|metadata|properties_metadata|
### logic integration-account-assembly create

create a logic integration-account-assembly.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--assembly_artifact_name**|string|The assembly artifact name.|assembly_artifact_name|assembly_artifact_name|
|**--properties**|object|The assembly properties definition.|properties|properties|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
### logic integration-account-assembly delete

delete a logic integration-account-assembly.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--assembly_artifact_name**|string|The assembly artifact name.|assembly_artifact_name|assembly_artifact_name|
### logic integration-account-assembly list

list a logic integration-account-assembly.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
### logic integration-account-assembly list-content-callback-url

list-content-callback-url a logic integration-account-assembly.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--assembly_artifact_name**|string|The assembly artifact name.|assembly_artifact_name|assembly_artifact_name|
### logic integration-account-assembly show

show a logic integration-account-assembly.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--assembly_artifact_name**|string|The assembly artifact name.|assembly_artifact_name|assembly_artifact_name|
### logic integration-account-assembly update

create a logic integration-account-assembly.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--assembly_artifact_name**|string|The assembly artifact name.|assembly_artifact_name|assembly_artifact_name|
|**--properties**|object|The assembly properties definition.|properties|properties|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
### logic integration-account-batch-configuration create

create a logic integration-account-batch-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--batch_configuration_name**|string|The batch configuration name.|batch_configuration_name|batch_configuration_name|
|**--properties**|object|The batch configuration properties definition.|properties|properties|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
### logic integration-account-batch-configuration delete

delete a logic integration-account-batch-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--batch_configuration_name**|string|The batch configuration name.|batch_configuration_name|batch_configuration_name|
### logic integration-account-batch-configuration list

list a logic integration-account-batch-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
### logic integration-account-batch-configuration show

show a logic integration-account-batch-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--batch_configuration_name**|string|The batch configuration name.|batch_configuration_name|batch_configuration_name|
### logic integration-account-batch-configuration update

create a logic integration-account-batch-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--batch_configuration_name**|string|The batch configuration name.|batch_configuration_name|batch_configuration_name|
|**--properties**|object|The batch configuration properties definition.|properties|properties|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
### logic integration-account-certificate create

create a logic integration-account-certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--certificate_name**|string|The integration account certificate name.|certificate_name|certificate_name|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
|**--metadata**|object|The metadata.|metadata|properties_metadata|
|**--key**|object|The reference to the key vault key.|key|properties_key|
|**--public_certificate**|string|The public certificate.|public_certificate|properties_public_certificate|
### logic integration-account-certificate delete

delete a logic integration-account-certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--certificate_name**|string|The integration account certificate name.|certificate_name|certificate_name|
### logic integration-account-certificate list

list a logic integration-account-certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--top**|integer|The number of items to be included in the result.|top|top|
### logic integration-account-certificate show

show a logic integration-account-certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--certificate_name**|string|The integration account certificate name.|certificate_name|certificate_name|
### logic integration-account-certificate update

create a logic integration-account-certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--certificate_name**|string|The integration account certificate name.|certificate_name|certificate_name|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
|**--metadata**|object|The metadata.|metadata|properties_metadata|
|**--key**|object|The reference to the key vault key.|key|properties_key|
|**--public_certificate**|string|The public certificate.|public_certificate|properties_public_certificate|
### logic integration-account-map create

create a logic integration-account-map.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--map_name**|string|The integration account map name.|map_name|map_name|
|**--map_type**|choice|The map type.|map_type|properties_map_type|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
|**--parameters_schema**|object|The parameters schema of integration account map.|parameters_schema|properties_parameters_schema|
|**--content**|string|The content.|content|properties_content|
|**--content_type**|string|The content type.|content_type|properties_content_type|
|**--metadata**|object|The metadata.|metadata|properties_metadata|
### logic integration-account-map delete

delete a logic integration-account-map.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--map_name**|string|The integration account map name.|map_name|map_name|
### logic integration-account-map list

list a logic integration-account-map.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--top**|integer|The number of items to be included in the result.|top|top|
|**--filter**|string|The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.|filter|filter|
### logic integration-account-map list-content-callback-url

list-content-callback-url a logic integration-account-map.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--map_name**|string|The integration account map name.|map_name|map_name|
|**--not_after**|date-time|The expiry time.|not_after|not_after|
|**--key_type**|choice|The key type.|key_type|key_type|
### logic integration-account-map show

show a logic integration-account-map.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--map_name**|string|The integration account map name.|map_name|map_name|
### logic integration-account-map update

create a logic integration-account-map.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--map_name**|string|The integration account map name.|map_name|map_name|
|**--map_type**|choice|The map type.|map_type|properties_map_type|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
|**--parameters_schema**|object|The parameters schema of integration account map.|parameters_schema|properties_parameters_schema|
|**--content**|string|The content.|content|properties_content|
|**--content_type**|string|The content type.|content_type|properties_content_type|
|**--metadata**|object|The metadata.|metadata|properties_metadata|
### logic integration-account-partner create

create a logic integration-account-partner.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--partner_name**|string|The integration account partner name.|partner_name|partner_name|
|**--partner_type**|choice|The partner type.|partner_type|properties_partner_type|
|**--content**|object|The integration account partner content.|content|properties_content|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
|**--metadata**|object|The metadata.|metadata|properties_metadata|
### logic integration-account-partner delete

delete a logic integration-account-partner.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--partner_name**|string|The integration account partner name.|partner_name|partner_name|
### logic integration-account-partner list

list a logic integration-account-partner.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--top**|integer|The number of items to be included in the result.|top|top|
|**--filter**|string|The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.|filter|filter|
### logic integration-account-partner list-content-callback-url

list-content-callback-url a logic integration-account-partner.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--partner_name**|string|The integration account partner name.|partner_name|partner_name|
|**--not_after**|date-time|The expiry time.|not_after|not_after|
|**--key_type**|choice|The key type.|key_type|key_type|
### logic integration-account-partner show

show a logic integration-account-partner.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--partner_name**|string|The integration account partner name.|partner_name|partner_name|
### logic integration-account-partner update

create a logic integration-account-partner.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--partner_name**|string|The integration account partner name.|partner_name|partner_name|
|**--partner_type**|choice|The partner type.|partner_type|properties_partner_type|
|**--content**|object|The integration account partner content.|content|properties_content|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
|**--metadata**|object|The metadata.|metadata|properties_metadata|
### logic integration-account-schema create

create a logic integration-account-schema.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--schema_name**|string|The integration account schema name.|schema_name|schema_name|
|**--schema_type**|choice|The schema type.|schema_type|properties_schema_type|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
|**--target_namespace**|string|The target namespace of the schema.|target_namespace|properties_target_namespace|
|**--document_name**|string|The document name.|document_name|properties_document_name|
|**--file_name**|string|The file name.|file_name|properties_file_name|
|**--metadata**|object|The metadata.|metadata|properties_metadata|
|**--content**|string|The content.|content|properties_content|
|**--content_type**|string|The content type.|content_type|properties_content_type|
### logic integration-account-schema delete

delete a logic integration-account-schema.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--schema_name**|string|The integration account schema name.|schema_name|schema_name|
### logic integration-account-schema list

list a logic integration-account-schema.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--top**|integer|The number of items to be included in the result.|top|top|
|**--filter**|string|The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.|filter|filter|
### logic integration-account-schema list-content-callback-url

list-content-callback-url a logic integration-account-schema.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--schema_name**|string|The integration account schema name.|schema_name|schema_name|
|**--not_after**|date-time|The expiry time.|not_after|not_after|
|**--key_type**|choice|The key type.|key_type|key_type|
### logic integration-account-schema show

show a logic integration-account-schema.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--schema_name**|string|The integration account schema name.|schema_name|schema_name|
### logic integration-account-schema update

create a logic integration-account-schema.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--schema_name**|string|The integration account schema name.|schema_name|schema_name|
|**--schema_type**|choice|The schema type.|schema_type|properties_schema_type|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
|**--target_namespace**|string|The target namespace of the schema.|target_namespace|properties_target_namespace|
|**--document_name**|string|The document name.|document_name|properties_document_name|
|**--file_name**|string|The file name.|file_name|properties_file_name|
|**--metadata**|object|The metadata.|metadata|properties_metadata|
|**--content**|string|The content.|content|properties_content|
|**--content_type**|string|The content type.|content_type|properties_content_type|
### logic integration-account-session create

create a logic integration-account-session.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--session_name**|string|The integration account session name.|session_name|session_name|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
|**--content**|object||content|properties_content|
### logic integration-account-session delete

delete a logic integration-account-session.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--session_name**|string|The integration account session name.|session_name|session_name|
### logic integration-account-session list

list a logic integration-account-session.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--top**|integer|The number of items to be included in the result.|top|top|
|**--filter**|string|The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.|filter|filter|
### logic integration-account-session show

show a logic integration-account-session.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--session_name**|string|The integration account session name.|session_name|session_name|
### logic integration-account-session update

create a logic integration-account-session.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--integration_account_name**|string|The integration account name.|integration_account_name|integration_account_name|
|**--session_name**|string|The integration account session name.|session_name|session_name|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
|**--content**|object||content|properties_content|
### logic integration-service-environment create

create a logic integration-service-environment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|string|The resource group.|resource_group|resource_group|
|**--integration_service_environment_name**|string|The integration service environment name.|integration_service_environment_name|integration_service_environment_name|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
|**--properties**|object|The integration service environment properties.|properties|properties|
|**--sku**|object|The integration service environment sku.|sku|sku|
### logic integration-service-environment delete

delete a logic integration-service-environment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|string|The resource group.|resource_group|resource_group|
|**--integration_service_environment_name**|string|The integration service environment name.|integration_service_environment_name|integration_service_environment_name|
### logic integration-service-environment list

list a logic integration-service-environment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|string|The resource group.|resource_group|resource_group|
|**--top**|integer|The number of items to be included in the result.|top|top|
### logic integration-service-environment restart

restart a logic integration-service-environment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|string|The resource group.|resource_group|resource_group|
|**--integration_service_environment_name**|string|The integration service environment name.|integration_service_environment_name|integration_service_environment_name|
### logic integration-service-environment show

show a logic integration-service-environment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|string|The resource group.|resource_group|resource_group|
|**--integration_service_environment_name**|string|The integration service environment name.|integration_service_environment_name|integration_service_environment_name|
### logic integration-service-environment update

update a logic integration-service-environment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|string|The resource group.|resource_group|resource_group|
|**--integration_service_environment_name**|string|The integration service environment name.|integration_service_environment_name|integration_service_environment_name|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
|**--properties**|object|The integration service environment properties.|properties|properties|
|**--sku**|object|The integration service environment sku.|sku|sku|
### logic integration-service-environment-managed-api delete

delete a logic integration-service-environment-managed-api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|string|The resource group.|resource_group|resource_group|
|**--integration_service_environment_name**|string|The integration service environment name.|integration_service_environment_name|integration_service_environment_name|
|**--api_name**|string|The api name.|api_name|api_name|
### logic integration-service-environment-managed-api list

list a logic integration-service-environment-managed-api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|string|The resource group.|resource_group|resource_group|
|**--integration_service_environment_name**|string|The integration service environment name.|integration_service_environment_name|integration_service_environment_name|
### logic integration-service-environment-managed-api put

put a logic integration-service-environment-managed-api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|string|The resource group.|resource_group|resource_group|
|**--integration_service_environment_name**|string|The integration service environment name.|integration_service_environment_name|integration_service_environment_name|
|**--api_name**|string|The api name.|api_name|api_name|
### logic integration-service-environment-managed-api show

show a logic integration-service-environment-managed-api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|string|The resource group.|resource_group|resource_group|
|**--integration_service_environment_name**|string|The integration service environment name.|integration_service_environment_name|integration_service_environment_name|
|**--api_name**|string|The api name.|api_name|api_name|
### logic integration-service-environment-managed-api-operation list

list a logic integration-service-environment-managed-api-operation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|string|The resource group.|resource_group|resource_group|
|**--integration_service_environment_name**|string|The integration service environment name.|integration_service_environment_name|integration_service_environment_name|
|**--api_name**|string|The api name.|api_name|api_name|
### logic integration-service-environment-network-health show

show a logic integration-service-environment-network-health.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|string|The resource group.|resource_group|resource_group|
|**--integration_service_environment_name**|string|The integration service environment name.|integration_service_environment_name|integration_service_environment_name|
### logic integration-service-environment-sku list

list a logic integration-service-environment-sku.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|string|The resource group.|resource_group|resource_group|
|**--integration_service_environment_name**|string|The integration service environment name.|integration_service_environment_name|integration_service_environment_name|
### logic workflow create

create a logic workflow.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
|**--state**|choice|The workflow state.|state|properties_state|
|**--endpoints_configuration**|object|The endpoints configuration.|endpoints_configuration|properties_endpoints_configuration|
|**--integration_account**|object|The resource reference.|integration_account|properties_integration_account|
|**--integration_service_environment**|object|The resource reference.|integration_service_environment|properties_integration_service_environment|
|**--definition**|object||definition|properties_definition|
|**--parameters**|dictionary|The parameters.|parameters|properties_parameters|
### logic workflow delete

delete a logic workflow.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
### logic workflow disable

disable a logic workflow.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
### logic workflow enable

enable a logic workflow.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
### logic workflow generate-upgraded-definition

generate-upgraded-definition a logic workflow.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--target_schema_version**|string|The target schema version.|target_schema_version|target_schema_version|
### logic workflow list

list a logic workflow.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--top**|integer|The number of items to be included in the result.|top|top|
|**--filter**|string|The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.|filter|filter|
### logic workflow list-callback-url

list-callback-url a logic workflow.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--not_after**|date-time|The expiry time.|not_after|not_after|
|**--key_type**|choice|The key type.|key_type|key_type|
### logic workflow list-swagger

list-swagger a logic workflow.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
### logic workflow move

move a logic workflow.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
|**--state**|choice|The workflow state.|state|properties_state|
|**--endpoints_configuration**|object|The endpoints configuration.|endpoints_configuration|properties_endpoints_configuration|
|**--integration_account**|object|The resource reference.|integration_account|properties_integration_account|
|**--integration_service_environment**|object|The resource reference.|integration_service_environment|properties_integration_service_environment|
|**--definition**|object||definition|properties_definition|
|**--parameters**|dictionary|The parameters.|parameters|properties_parameters|
### logic workflow regenerate-access-key

regenerate-access-key a logic workflow.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--key_type**|choice|The key type.|key_type|key_type|
### logic workflow show

show a logic workflow.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
### logic workflow update

update a logic workflow.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
|**--state**|choice|The workflow state.|state|properties_state|
|**--endpoints_configuration**|object|The endpoints configuration.|endpoints_configuration|properties_endpoints_configuration|
|**--integration_account**|object|The resource reference.|integration_account|properties_integration_account|
|**--integration_service_environment**|object|The resource reference.|integration_service_environment|properties_integration_service_environment|
|**--definition**|object||definition|properties_definition|
|**--parameters**|dictionary|The parameters.|parameters|properties_parameters|
### logic workflow validate-by-location

validate-by-location a logic workflow.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--location**|string|The workflow location.|location|location|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
### logic workflow validate-by-resource-group

validate-by-resource-group a logic workflow.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--location**|string|The resource location.|location|location|
|**--tags**|dictionary|The resource tags.|tags|tags|
|**--state**|choice|The workflow state.|state|properties_state|
|**--endpoints_configuration**|object|The endpoints configuration.|endpoints_configuration|properties_endpoints_configuration|
|**--integration_account**|object|The resource reference.|integration_account|properties_integration_account|
|**--integration_service_environment**|object|The resource reference.|integration_service_environment|properties_integration_service_environment|
|**--definition**|object||definition|properties_definition|
|**--parameters**|dictionary|The parameters.|parameters|properties_parameters|
### logic workflow-run cancel

cancel a logic workflow-run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--run_name**|string|The workflow run name.|run_name|run_name|
### logic workflow-run list

list a logic workflow-run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--top**|integer|The number of items to be included in the result.|top|top|
|**--filter**|string|The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.|filter|filter|
### logic workflow-run show

show a logic workflow-run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--run_name**|string|The workflow run name.|run_name|run_name|
### logic workflow-run-action list

list a logic workflow-run-action.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--run_name**|string|The workflow run name.|run_name|run_name|
|**--top**|integer|The number of items to be included in the result.|top|top|
|**--filter**|string|The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.|filter|filter|
### logic workflow-run-action list-expression-trace

list-expression-trace a logic workflow-run-action.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--run_name**|string|The workflow run name.|run_name|run_name|
|**--action_name**|string|The workflow action name.|action_name|action_name|
### logic workflow-run-action show

show a logic workflow-run-action.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--run_name**|string|The workflow run name.|run_name|run_name|
|**--action_name**|string|The workflow action name.|action_name|action_name|
### logic workflow-run-action-repetition list

list a logic workflow-run-action-repetition.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--run_name**|string|The workflow run name.|run_name|run_name|
|**--action_name**|string|The workflow action name.|action_name|action_name|
### logic workflow-run-action-repetition list-expression-trace

list-expression-trace a logic workflow-run-action-repetition.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--run_name**|string|The workflow run name.|run_name|run_name|
|**--action_name**|string|The workflow action name.|action_name|action_name|
|**--repetition_name**|string|The workflow repetition.|repetition_name|repetition_name|
### logic workflow-run-action-repetition show

show a logic workflow-run-action-repetition.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--run_name**|string|The workflow run name.|run_name|run_name|
|**--action_name**|string|The workflow action name.|action_name|action_name|
|**--repetition_name**|string|The workflow repetition.|repetition_name|repetition_name|
### logic workflow-run-action-repetition-request-history list

list a logic workflow-run-action-repetition-request-history.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--run_name**|string|The workflow run name.|run_name|run_name|
|**--action_name**|string|The workflow action name.|action_name|action_name|
|**--repetition_name**|string|The workflow repetition.|repetition_name|repetition_name|
### logic workflow-run-action-repetition-request-history show

show a logic workflow-run-action-repetition-request-history.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--run_name**|string|The workflow run name.|run_name|run_name|
|**--action_name**|string|The workflow action name.|action_name|action_name|
|**--repetition_name**|string|The workflow repetition.|repetition_name|repetition_name|
|**--request_history_name**|string|The request history name.|request_history_name|request_history_name|
### logic workflow-run-action-request-history list

list a logic workflow-run-action-request-history.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--run_name**|string|The workflow run name.|run_name|run_name|
|**--action_name**|string|The workflow action name.|action_name|action_name|
### logic workflow-run-action-request-history show

show a logic workflow-run-action-request-history.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--run_name**|string|The workflow run name.|run_name|run_name|
|**--action_name**|string|The workflow action name.|action_name|action_name|
|**--request_history_name**|string|The request history name.|request_history_name|request_history_name|
### logic workflow-run-action-scope-repetition list

list a logic workflow-run-action-scope-repetition.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--run_name**|string|The workflow run name.|run_name|run_name|
|**--action_name**|string|The workflow action name.|action_name|action_name|
### logic workflow-run-action-scope-repetition show

show a logic workflow-run-action-scope-repetition.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--run_name**|string|The workflow run name.|run_name|run_name|
|**--action_name**|string|The workflow action name.|action_name|action_name|
|**--repetition_name**|string|The workflow repetition.|repetition_name|repetition_name|
### logic workflow-run-operation show

show a logic workflow-run-operation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--run_name**|string|The workflow run name.|run_name|run_name|
|**--operation_id**|string|The workflow operation id.|operation_id|operation_id|
### logic workflow-trigger list

list a logic workflow-trigger.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--top**|integer|The number of items to be included in the result.|top|top|
|**--filter**|string|The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.|filter|filter|
### logic workflow-trigger list-callback-url

list-callback-url a logic workflow-trigger.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--trigger_name**|string|The workflow trigger name.|trigger_name|trigger_name|
### logic workflow-trigger reset

reset a logic workflow-trigger.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--trigger_name**|string|The workflow trigger name.|trigger_name|trigger_name|
|**--source**|object|The workflow trigger.|source|source|
### logic workflow-trigger run

run a logic workflow-trigger.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--trigger_name**|string|The workflow trigger name.|trigger_name|trigger_name|
### logic workflow-trigger show

show a logic workflow-trigger.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--trigger_name**|string|The workflow trigger name.|trigger_name|trigger_name|
### logic workflow-trigger-history list

list a logic workflow-trigger-history.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--trigger_name**|string|The workflow trigger name.|trigger_name|trigger_name|
|**--top**|integer|The number of items to be included in the result.|top|top|
|**--filter**|string|The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.|filter|filter|
### logic workflow-trigger-history resubmit

resubmit a logic workflow-trigger-history.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--trigger_name**|string|The workflow trigger name.|trigger_name|trigger_name|
|**--history_name**|string|The workflow trigger history name. Corresponds to the run name for triggers that resulted in a run.|history_name|history_name|
### logic workflow-trigger-history show

show a logic workflow-trigger-history.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--trigger_name**|string|The workflow trigger name.|trigger_name|trigger_name|
|**--history_name**|string|The workflow trigger history name. Corresponds to the run name for triggers that resulted in a run.|history_name|history_name|
### logic workflow-version list

list a logic workflow-version.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--top**|integer|The number of items to be included in the result.|top|top|
### logic workflow-version show

show a logic workflow-version.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--version_id**|string|The workflow versionId.|version_id|version_id|
### logic workflow-version-trigger list-callback-url

list-callback-url a logic workflow-version-trigger.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group_name**|string|The resource group name.|resource_group_name|resource_group_name|
|**--workflow_name**|string|The workflow name.|workflow_name|workflow_name|
|**--version_id**|string|The workflow versionId.|version_id|version_id|
|**--trigger_name**|string|The workflow trigger name.|trigger_name|trigger_name|
|**--not_after**|date-time|The expiry time.|not_after|not_after|
|**--key_type**|choice|The key type.|key_type|key_type|