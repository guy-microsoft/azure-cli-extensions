# Azure CLI healthbot Extension #
This is the extension for healthbot

### How to use ###
Install this extension using the below CLI command
```
az extension add --name healthbot
```

### Included Features ###
#### healthbot ####
##### Create #####
```
az healthbot create --name "samplebotname" --location "East US" --sku-name "F0" --resource-group "healthbotClient"
```
##### Show #####
```
az healthbot show --name "samplebotname" --resource-group "healthbotClient"
```
##### List #####
```
az healthbot list --resource-group "OneResourceGroupName"
```
##### Update #####
```
az healthbot update --name "samplebotname" --sku-name "F0" --resource-group "healthbotClient"
```
##### Delete #####
```
az healthbot delete --name "samplebotname" --resource-group "healthbotClient"
```