# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az account|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az account` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az account subscription|Subscriptions|[commands](#CommandsInSubscriptions)|
|az account tenant|Tenants|[commands](#CommandsInTenants)|
|az account subscription|Subscription|[commands](#CommandsInSubscription)|
|az account subscription-operation|SubscriptionOperation|[commands](#CommandsInSubscriptionOperation)|
|az account subscription-policy|SubscriptionPolicy|[commands](#CommandsInSubscriptionPolicy)|
|az account billing-account|BillingAccount|[commands](#CommandsInBillingAccount)|

## COMMANDS
### <a name="CommandsInBillingAccount">Commands in `az account billing-account` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az account billing-account show-policy](#BillingAccountGetPolicy)|GetPolicy|[Parameters](#ParametersBillingAccountGetPolicy)|[Example](#ExamplesBillingAccountGetPolicy)|

### <a name="CommandsInSubscriptions">Commands in `az account subscription` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az account subscription list](#SubscriptionsList)|List|[Parameters](#ParametersSubscriptionsList)|[Example](#ExamplesSubscriptionsList)|
|[az account subscription show](#SubscriptionsGet)|Get|[Parameters](#ParametersSubscriptionsGet)|[Example](#ExamplesSubscriptionsGet)|
|[az account subscription create](#SubscriptionsCreateAlias)|CreateAlias|[Parameters](#ParametersSubscriptionsCreateAlias)|[Example](#ExamplesSubscriptionsCreateAlias)|
|[az account subscription delete](#SubscriptionsDeleteAlias)|DeleteAlias|[Parameters](#ParametersSubscriptionsDeleteAlias)|[Example](#ExamplesSubscriptionsDeleteAlias)|
|[az account subscription create-csp-subscription](#SubscriptionsCreateCspSubscription)|CreateCspSubscription|[Parameters](#ParametersSubscriptionsCreateCspSubscription)|[Example](#ExamplesSubscriptionsCreateCspSubscription)|
|[az account subscription create-subscription](#SubscriptionsCreateSubscription)|CreateSubscription|[Parameters](#ParametersSubscriptionsCreateSubscription)|[Example](#ExamplesSubscriptionsCreateSubscription)|
|[az account subscription create-subscription-in-enrollment-account](#SubscriptionsCreateSubscriptionInEnrollmentAccount)|CreateSubscriptionInEnrollmentAccount|[Parameters](#ParametersSubscriptionsCreateSubscriptionInEnrollmentAccount)|[Example](#ExamplesSubscriptionsCreateSubscriptionInEnrollmentAccount)|
|[az account subscription list-alias](#SubscriptionsListAlias)|ListAlias|[Parameters](#ParametersSubscriptionsListAlias)|[Example](#ExamplesSubscriptionsListAlias)|
|[az account subscription list-location](#SubscriptionsListLocations)|ListLocations|[Parameters](#ParametersSubscriptionsListLocations)|[Example](#ExamplesSubscriptionsListLocations)|
|[az account subscription redeem](#SubscriptionsRedeem)|Redeem|[Parameters](#ParametersSubscriptionsRedeem)|[Example](#ExamplesSubscriptionsRedeem)|
|[az account subscription show-alias](#SubscriptionsGetAlias)|GetAlias|[Parameters](#ParametersSubscriptionsGetAlias)|[Example](#ExamplesSubscriptionsGetAlias)|

### <a name="CommandsInSubscription">Commands in `az account subscription` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az account subscription cancel](#SubscriptionCancel)|Cancel|[Parameters](#ParametersSubscriptionCancel)|[Example](#ExamplesSubscriptionCancel)|
|[az account subscription enable](#SubscriptionEnable)|Enable|[Parameters](#ParametersSubscriptionEnable)|[Example](#ExamplesSubscriptionEnable)|
|[az account subscription rename](#SubscriptionRename)|Rename|[Parameters](#ParametersSubscriptionRename)|[Example](#ExamplesSubscriptionRename)|

### <a name="CommandsInSubscriptionOperation">Commands in `az account subscription-operation` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az account subscription-operation show](#SubscriptionOperationGet)|Get|[Parameters](#ParametersSubscriptionOperationGet)|[Example](#ExamplesSubscriptionOperationGet)|

### <a name="CommandsInSubscriptionPolicy">Commands in `az account subscription-policy` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az account subscription-policy add-update-policy-for-tenant](#SubscriptionPolicyAddUpdatePolicyForTenant)|AddUpdatePolicyForTenant|[Parameters](#ParametersSubscriptionPolicyAddUpdatePolicyForTenant)|[Example](#ExamplesSubscriptionPolicyAddUpdatePolicyForTenant)|
|[az account subscription-policy list-policy-for-tenant](#SubscriptionPolicyListPolicyForTenant)|ListPolicyForTenant|[Parameters](#ParametersSubscriptionPolicyListPolicyForTenant)|[Example](#ExamplesSubscriptionPolicyListPolicyForTenant)|
|[az account subscription-policy show-policy-for-tenant](#SubscriptionPolicyGetPolicyForTenant)|GetPolicyForTenant|[Parameters](#ParametersSubscriptionPolicyGetPolicyForTenant)|[Example](#ExamplesSubscriptionPolicyGetPolicyForTenant)|

### <a name="CommandsInTenants">Commands in `az account tenant` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az account tenant list](#TenantsList)|List|[Parameters](#ParametersTenantsList)|[Example](#ExamplesTenantsList)|


## COMMAND DETAILS

### group `az account billing-account`
#### <a name="BillingAccountGetPolicy">Command `az account billing-account show-policy`</a>

##### <a name="ExamplesBillingAccountGetPolicy">Example</a>
```
az account billing-account show-policy --billing-account-id "testBillingAccountId"
```
##### <a name="ParametersBillingAccountGetPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--billing-account-id**|string|Billing Account Id.|billing_account_id|billingAccountId|

### group `az account subscription`
#### <a name="SubscriptionsList">Command `az account subscription list`</a>

##### <a name="ExamplesSubscriptionsList">Example</a>
```
az account subscription list
```
##### <a name="ParametersSubscriptionsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="SubscriptionsGet">Command `az account subscription show`</a>

##### <a name="ExamplesSubscriptionsGet">Example</a>
```
az account subscription show --subscription-id "83aa47df-e3e9-49ff-877b-94304bf3d3ad"
```
##### <a name="ParametersSubscriptionsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscription-id**|string|The ID of the target subscription.|subscription_id|subscriptionId|

#### <a name="SubscriptionsCreateAlias">Command `az account subscription create`</a>

##### <a name="ExamplesSubscriptionsCreateAlias">Example</a>
```
az account subscription create --alias-name "aliasForNewSub" --management-group-id "testManagementGroupId" \
--subscription-owner-id "testOwnerId" --subscription-tenant-id "testTenantId" --tags tag1="testTag" --billing-scope \
"/providers/Microsoft.Billing/billingAccounts/e879cf0f-2b4d-5431-109a-f72fc9868693:024cabf4-7321-4cf9-be59-df0c77ca51de\
_2019-05-31/billingProfiles/PE2Q-NOIT-BG7-TGB/invoiceSections/MTT4-OBS7-PJA-TGB" --display-name "Contoso MCA \
subscription" --reseller-id "testResellerId" --subscription-id "testSubGUID" --workload "Production"
```
##### <a name="ParametersSubscriptionsCreateAlias">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--alias-name**|string|Alias Name|alias_name|aliasName|
|**--display-name**|string|The friendly name of the subscription.|display_name|displayName|
|**--workload**|choice|The workload type of the subscription. It can be either Production or DevTest.|workload|workload|
|**--billing-scope**|string|Determines whether subscription is fieldLed, partnerLed or LegacyEA|billing_scope|billingScope|
|**--subscription-id**|string|This parameter can be used to create alias for existing subscription Id|subscription_id|subscriptionId|
|**--reseller-id**|string|Reseller Id|reseller_id|resellerId|
|**--management-group-id**|string|Management group Id for the subscription.|management_group_id|managementGroupId|
|**--subscription-tenant-id**|string|Tenant Id of the subscription|subscription_tenant_id|subscriptionTenantId|
|**--subscription-owner-id**|string|Owner Id of the subscription|subscription_owner_id|subscriptionOwnerId|
|**--tags**|dictionary|tags for the subscription|tags|tags|

#### <a name="SubscriptionsDeleteAlias">Command `az account subscription delete`</a>

##### <a name="ExamplesSubscriptionsDeleteAlias">Example</a>
```
az account subscription delete --alias-name "aliasForNewSub"
```
##### <a name="ParametersSubscriptionsDeleteAlias">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--alias-name**|string|Alias Name|alias_name|aliasName|

#### <a name="SubscriptionsCreateCspSubscription">Command `az account subscription create-csp-subscription`</a>

##### <a name="ExamplesSubscriptionsCreateCspSubscription">Example</a>
```
az account subscription create-csp-subscription --billing-account-name "2bc54a6f-8d8a-5be1-5bff-bb4f285f512b:11a72812-d\
9a4-446e-9a1e-70c8bcadf5c0_2019-05-31" --display-name "Contoso MCA subscription" --sku-id "0001" --customer-name \
"e33ba30d-3718-4b15-bfaa-5627a57cda6f"
```
##### <a name="ParametersSubscriptionsCreateCspSubscription">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--billing-account-name**|string|The name of the Microsoft Customer Agreement billing account for which you want to create the subscription.|billing_account_name|billingAccountName|
|**--customer-name**|string|The name of the customer.|customer_name|customerName|
|**--display-name**|string|The friendly name of the subscription.|display_name|displayName|
|**--sku-id**|string|The SKU ID of the Azure plan. Azure plan determines the pricing and service-level agreement of the subscription.  Use 001 for Microsoft Azure Plan and 002 for Microsoft Azure Plan for DevTest.|sku_id|skuId|
|**--reseller-id**|string|Reseller ID, basically MPN Id.|reseller_id|resellerId|

#### <a name="SubscriptionsCreateSubscription">Command `az account subscription create-subscription`</a>

##### <a name="ExamplesSubscriptionsCreateSubscription">Example</a>
```
az account subscription create-subscription --billing-account-name "0aa27f2b-ec7f-5a65-71f6-a5ff0897bd55:ae0dae1e-de9a-\
41f6-8257-76b055d98372_2019-05-31" --billing-profile-name "27VR-HDWX-BG7-TGB" --additional-parameters \
"{\\"customData\\":{\\"key1\\":\\"value1\\",\\"key2\\":true}}" --cost-center "135366376" --display-name "Contoso MCA \
subscription" --object-id "973034ff-acb7-409c-b731-e789672c7b32" --sku-id "0001" --invoice-section-name \
"JGF7-NSBG-PJA-TGB"
```
##### <a name="ParametersSubscriptionsCreateSubscription">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--billing-account-name**|string|The name of the Microsoft Customer Agreement billing account for which you want to create the subscription.|billing_account_name|billingAccountName|
|**--billing-profile-name**|string|The name of the billing profile in the billing account for which you want to create the subscription.|billing_profile_name|billingProfileName|
|**--invoice-section-name**|string|The name of the invoice section in the billing account for which you want to create the subscription.|invoice_section_name|invoiceSectionName|
|**--display-name**|string|The friendly name of the subscription.|display_name|displayName|
|**--sku-id**|string|The SKU ID of the Azure plan. Azure plan determines the pricing and service-level agreement of the subscription.  Use 001 for Microsoft Azure Plan and 002 for Microsoft Azure Plan for DevTest.|sku_id|skuId|
|**--cost-center**|string|If set, the cost center will show up on the Azure usage and charges file.|cost_center|costCenter|
|**--management-group-id**|string|The identifier of the management group to which this subscription will be associated.|management_group_id|managementGroupId|
|**--additional-parameters**|dictionary|Additional, untyped parameters to support custom subscription creation scenarios.|additional_parameters|additionalParameters|
|**--object-id**|string|Object id of the Principal|object_id|objectId|

#### <a name="SubscriptionsCreateSubscriptionInEnrollmentAccount">Command `az account subscription create-subscription-in-enrollment-account`</a>

##### <a name="ExamplesSubscriptionsCreateSubscriptionInEnrollmentAccount">Example</a>
```
az account subscription create-subscription-in-enrollment-account --additional-parameters \
"{\\"customData\\":{\\"key1\\":\\"value1\\",\\"key2\\":true}}" --display-name "Test Ea Azure Sub" --offer-type \
"MS-AZR-0017P" --owners object-id="973034ff-acb7-409c-b731-e789672c7b31" --owners object-id="67439a9e-8519-4016-a630-f5\
f805eba567" --enrollment-account-name "73f8ab6e-cfa0-42be-b886-be6e77c2980c"
```
##### <a name="ParametersSubscriptionsCreateSubscriptionInEnrollmentAccount">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--enrollment-account-name**|string|The name of the enrollment account to which the subscription will be billed.|enrollment_account_name|enrollmentAccountName|
|**--display-name**|string|The display name of the subscription.|display_name|displayName|
|**--management-group-id**|string|The Management Group Id.|management_group_id|managementGroupId|
|**--owners**|array|The list of principals that should be granted Owner access on the subscription. Principals should be of type User, Service Principal or Security Group.|owners|owners|
|**--offer-type**|choice|The offer type of the subscription. For example, MS-AZR-0017P (EnterpriseAgreement) and MS-AZR-0148P (EnterpriseAgreement devTest) are available. Only valid when creating a subscription in a enrollment account scope.|offer_type|offerType|
|**--additional-parameters**|dictionary|Additional, untyped parameters to support custom subscription creation scenarios.|additional_parameters|additionalParameters|

#### <a name="SubscriptionsListAlias">Command `az account subscription list-alias`</a>

##### <a name="ExamplesSubscriptionsListAlias">Example</a>
```
az account subscription list-alias
```
##### <a name="ParametersSubscriptionsListAlias">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="SubscriptionsListLocations">Command `az account subscription list-location`</a>

##### <a name="ExamplesSubscriptionsListLocations">Example</a>
```
az account subscription list-location --subscription-id "83aa47df-e3e9-49ff-877b-94304bf3d3ad"
```
##### <a name="ParametersSubscriptionsListLocations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscription-id**|string|The ID of the target subscription.|subscription_id|subscriptionId|

#### <a name="SubscriptionsRedeem">Command `az account subscription redeem`</a>

##### <a name="ExamplesSubscriptionsRedeem">Example</a>
```
az account subscription redeem --management-group-id "testManagementGroupId" --tags tag1="testTag" --subscription-id \
"291bba3f-e0a5-47bc-a099-3bdcb2a50a05"
```
##### <a name="ParametersSubscriptionsRedeem">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscription-id**|string|Subscription Id.|subscription_id|subscriptionId|
|**--management-group-id**|string|Management group Id for the subscription.|management_group_id|managementGroupId|
|**--tags**|dictionary|tags for the subscription|tags|tags|

#### <a name="SubscriptionsGetAlias">Command `az account subscription show-alias`</a>

##### <a name="ExamplesSubscriptionsGetAlias">Example</a>
```
az account subscription show-alias --alias-name "aliasForNewSub"
```
##### <a name="ParametersSubscriptionsGetAlias">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--alias-name**|string|Alias Name|alias_name|aliasName|

### group `az account subscription`
#### <a name="SubscriptionCancel">Command `az account subscription cancel`</a>

##### <a name="ExamplesSubscriptionCancel">Example</a>
```
az account subscription cancel --subscription-id "83aa47df-e3e9-49ff-877b-94304bf3d3ad"
```
##### <a name="ParametersSubscriptionCancel">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscription-id**|string|Subscription Id.|subscription_id|subscriptionId|

#### <a name="SubscriptionEnable">Command `az account subscription enable`</a>

##### <a name="ExamplesSubscriptionEnable">Example</a>
```
az account subscription enable --subscription-id "7948bcee-488c-47ce-941c-38e20ede803d"
```
##### <a name="ParametersSubscriptionEnable">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscription-id**|string|Subscription Id.|subscription_id|subscriptionId|

#### <a name="SubscriptionRename">Command `az account subscription rename`</a>

##### <a name="ExamplesSubscriptionRename">Example</a>
```
az account subscription rename --name "Test Sub" --subscription-id "83aa47df-e3e9-49ff-877b-94304bf3d3ad"
```
##### <a name="ParametersSubscriptionRename">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscription-id**|string|Subscription Id.|subscription_id|subscriptionId|
|**--subscription-name**|string|New subscription name|subscription_name|subscriptionName|

### group `az account subscription-operation`
#### <a name="SubscriptionOperationGet">Command `az account subscription-operation show`</a>

##### <a name="ExamplesSubscriptionOperationGet">Example</a>
```
az account subscription-operation show --operation-id "e4b8d068-f574-462a-a76f-6fa0afc613c9"
```
##### <a name="ParametersSubscriptionOperationGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--operation-id**|string|The operation ID, which can be found from the Location field in the generate recommendation response header.|operation_id|operationId|

### group `az account subscription-policy`
#### <a name="SubscriptionPolicyAddUpdatePolicyForTenant">Command `az account subscription-policy add-update-policy-for-tenant`</a>

##### <a name="ExamplesSubscriptionPolicyAddUpdatePolicyForTenant">Example</a>
```
az account subscription-policy add-update-policy-for-tenant --block-subscriptions-into-tenant true \
--block-subscriptions-leaving-tenant true --exempted-principals "e879cf0f-2b4d-5431-109a-f72fc9868693" \
"9792da87-c97b-410d-a97d-27021ba09ce6"
```
##### <a name="ParametersSubscriptionPolicyAddUpdatePolicyForTenant">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--block-subscriptions-leaving-tenant**|boolean|Blocks the leaving of subscriptions from user's tenant.|block_subscriptions_leaving_tenant|blockSubscriptionsLeavingTenant|
|**--block-subscriptions-into-tenant**|boolean|Blocks the entering of subscriptions into user's tenant.|block_subscriptions_into_tenant|blockSubscriptionsIntoTenant|
|**--exempted-principals**|array|List of user objectIds that are exempted from the set subscription tenant policies for the user's tenant.|exempted_principals|exemptedPrincipals|

#### <a name="SubscriptionPolicyListPolicyForTenant">Command `az account subscription-policy list-policy-for-tenant`</a>

##### <a name="ExamplesSubscriptionPolicyListPolicyForTenant">Example</a>
```
az account subscription-policy list-policy-for-tenant
```
##### <a name="ParametersSubscriptionPolicyListPolicyForTenant">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="SubscriptionPolicyGetPolicyForTenant">Command `az account subscription-policy show-policy-for-tenant`</a>

##### <a name="ExamplesSubscriptionPolicyGetPolicyForTenant">Example</a>
```
az account subscription-policy show-policy-for-tenant
```
##### <a name="ParametersSubscriptionPolicyGetPolicyForTenant">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
### group `az account tenant`
#### <a name="TenantsList">Command `az account tenant list`</a>

##### <a name="ExamplesTenantsList">Example</a>
```
az account tenant list
```
##### <a name="ParametersTenantsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|