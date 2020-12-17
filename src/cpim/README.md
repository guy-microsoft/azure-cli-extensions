# Azure CLI cpim Extension #
This is the extension for cpim

### How to use ###
Install this extension using the below CLI command
```
az extension add --name cpim
```

### Included Features ###
#### cpim b2-c-tenant ####
##### Create #####
```
az cpim b2-c-tenant create --location "United States" --properties display-name="Contoso" country-code="US" \
    --sku-name "Standard" --resource-group "contosoResourceGroup" --resource-name "contoso.onmicrosoft.com" 
```
##### Show #####
```
az cpim b2-c-tenant show --resource-group "contosoResourceGroup" --resource-name "contoso.onmicrosoft.com"
```
##### List #####
```
az cpim b2-c-tenant list --resource-group "contosoResourceGroup"
```
##### Update #####
```
az cpim b2-c-tenant update --resource-group "contosoResourceGroup" --resource-name "contoso.onmicrosoft.com" \
    --sku-name "PremiumP1" --tags key="value" 
```
##### Delete #####
```
az cpim b2-c-tenant delete --resource-group "rg1" --resource-name "contoso.onmicrosoft.com"
```
#### cpim operation ####
##### Get-async-status #####
```
az cpim operation get-async-status --operation-id "99999999-9999-9999-9999-999999999999"
```