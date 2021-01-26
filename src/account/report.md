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
|[az account subscription list-location](#SubscriptionsListLocations)|ListLocations|[Parameters](#ParametersSubscriptionsListLocations)|[Example](#ExamplesSubscriptionsListLocations)|

### <a name="CommandsInSubscription">Commands in `az account subscription` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az account subscription create](#SubscriptionCreateAlias)|CreateAlias|[Parameters](#ParametersSubscriptionCreateAlias)|[Example](#ExamplesSubscriptionCreateAlias)|
|[az account subscription redeem](#SubscriptionRedeem)|Redeem|[Parameters](#ParametersSubscriptionRedeem)|[Example](#ExamplesSubscriptionRedeem)|

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

#### <a name="SubscriptionsListLocations">Command `az account subscription list-location`</a>

##### <a name="ExamplesSubscriptionsListLocations">Example</a>
```
az account subscription list-location --subscription-id "83aa47df-e3e9-49ff-877b-94304bf3d3ad"
```
##### <a name="ParametersSubscriptionsListLocations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscription-id**|string|The ID of the target subscription.|subscription_id|subscriptionId|

### group `az account subscription`
#### <a name="SubscriptionCreateAlias">Command `az account subscription create`</a>

##### <a name="ExamplesSubscriptionCreateAlias">Example</a>
```
az account subscription create --alias-name "aliasForNewSub" --management-group-id "testManagementGroupId" \
--subscription-owner-id "testOwnerId" --subscription-tenant-id "testTenantId" --tags tag1="testTag" --billing-scope \
"/providers/Microsoft.Billing/billingAccounts/e879cf0f-2b4d-5431-109a-f72fc9868693:024cabf4-7321-4cf9-be59-df0c77ca51de\
_2019-05-31/billingProfiles/PE2Q-NOIT-BG7-TGB/invoiceSections/MTT4-OBS7-PJA-TGB" --display-name "Contoso MCA \
subscription" --reseller-id "testResellerId" --subscription-id "testSubGUID" --workload "Production"
```
##### <a name="ParametersSubscriptionCreateAlias">Parameters</a> 
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

#### <a name="SubscriptionRedeem">Command `az account subscription redeem`</a>

##### <a name="ExamplesSubscriptionRedeem">Example</a>
```
az account subscription redeem --management-group-id "testManagementGroupId" --tags tag1="testTag" --subscription-id \
"subscriptionId"
```
##### <a name="ParametersSubscriptionRedeem">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscription-id**|string|Subscription Id.|subscription_id|subscriptionId|
|**--management-group-id**|string|Management group Id for the subscription.|management_group_id|managementGroupId|
|**--tags**|dictionary|tags for the subscription|tags|tags|

### group `az account tenant`
#### <a name="TenantsList">Command `az account tenant list`</a>

##### <a name="ExamplesTenantsList">Example</a>
```
az account tenant list
```
##### <a name="ParametersTenantsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|