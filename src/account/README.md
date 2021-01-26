# Azure CLI account Extension #
This is the extension for account

### How to use ###
Install this extension using the below CLI command
```
az extension add --name account
```

### Included Features ###
#### account subscription ####
##### Create #####
```
az account subscription create --alias-name "aliasForNewSub" --management-group-id "testManagementGroupId" \
    --subscription-owner-id "testOwnerId" --subscription-tenant-id "testTenantId" --tags tag1="testTag" \
    --billing-scope "/providers/Microsoft.Billing/billingAccounts/e879cf0f-2b4d-5431-109a-f72fc9868693:024cabf4-7321-4cf9-be59-df0c77ca51de_2019-05-31/billingProfiles/PE2Q-NOIT-BG7-TGB/invoiceSections/MTT4-OBS7-PJA-TGB" \
    --display-name "Contoso MCA subscription" --reseller-id "testResellerId" --subscription-id "testSubGUID" \
    --workload "Production" 
```
##### Show #####
```
az account subscription show --subscription-id "83aa47df-e3e9-49ff-877b-94304bf3d3ad"
```
##### List #####
```
az account subscription list
```
##### Create-csp-subscription #####
```
az account subscription create-csp-subscription \
    --billing-account-name "2bc54a6f-8d8a-5be1-5bff-bb4f285f512b:11a72812-d9a4-446e-9a1e-70c8bcadf5c0_2019-05-31" \
    --display-name "Contoso MCA subscription" --sku-id "0001" --customer-name "e33ba30d-3718-4b15-bfaa-5627a57cda6f" 
```
##### Create-subscription #####
```
az account subscription create-subscription \
    --billing-account-name "0aa27f2b-ec7f-5a65-71f6-a5ff0897bd55:ae0dae1e-de9a-41f6-8257-76b055d98372_2019-05-31" \
    --billing-profile-name "27VR-HDWX-BG7-TGB" \
    --additional-parameters "{\\"customData\\":{\\"key1\\":\\"value1\\",\\"key2\\":true}}" --cost-center "135366376" \
    --display-name "Contoso MCA subscription" --object-id "973034ff-acb7-409c-b731-e789672c7b32" --sku-id "0001" \
    --invoice-section-name "JGF7-NSBG-PJA-TGB" 
```
##### Create-subscription-in-enrollment-account #####
```
az account subscription create-subscription-in-enrollment-account \
    --additional-parameters "{\\"customData\\":{\\"key1\\":\\"value1\\",\\"key2\\":true}}" \
    --display-name "Test Ea Azure Sub" --offer-type "MS-AZR-0017P" \
    --owners object-id="973034ff-acb7-409c-b731-e789672c7b31" \
    --owners object-id="67439a9e-8519-4016-a630-f5f805eba567" \
    --enrollment-account-name "73f8ab6e-cfa0-42be-b886-be6e77c2980c" 
```
##### List-alias #####
```
az account subscription list-alias
```
##### List-location #####
```
az account subscription list-location --subscription-id "83aa47df-e3e9-49ff-877b-94304bf3d3ad"
```
##### Redeem #####
```
az account subscription redeem --management-group-id "testManagementGroupId" --tags tag1="testTag" \
    --subscription-id "291bba3f-e0a5-47bc-a099-3bdcb2a50a05" 
```
##### Show-alias #####
```
az account subscription show-alias --alias-name "aliasForNewSub"
```
##### Delete #####
```
az account subscription delete --alias-name "aliasForNewSub"
```
#### account tenant ####
##### List #####
```
az account tenant list
```
#### account subscription ####
##### Cancel #####
```
az account subscription cancel --subscription-id "83aa47df-e3e9-49ff-877b-94304bf3d3ad"
```
##### Enable #####
```
az account subscription enable --subscription-id "7948bcee-488c-47ce-941c-38e20ede803d"
```
##### Rename #####
```
az account subscription rename --name "Test Sub" --subscription-id "83aa47df-e3e9-49ff-877b-94304bf3d3ad"
```
#### account subscription-operation ####
##### Show #####
```
az account subscription-operation show --operation-id "e4b8d068-f574-462a-a76f-6fa0afc613c9"
```
#### account subscription-policy ####
##### Add-update-policy-for-tenant #####
```
az account subscription-policy add-update-policy-for-tenant --block-subscriptions-into-tenant true \
    --block-subscriptions-leaving-tenant true \
    --exempted-principals "e879cf0f-2b4d-5431-109a-f72fc9868693" "9792da87-c97b-410d-a97d-27021ba09ce6" 
```
##### List-policy-for-tenant #####
```
az account subscription-policy list-policy-for-tenant
```
##### Show-policy-for-tenant #####
```
az account subscription-policy show-policy-for-tenant
```
#### account billing-account ####
##### Show-policy #####
```
az account billing-account show-policy --billing-account-id "testBillingAccountId"
```