# Azure CLI healthbot Extension #
This is the extension for healthbot

### How to use ###
Install this extension using the below CLI command
```
az extension add --name healthbot
```

### Included Features ###
#### healthbot bot ####
##### Create #####
```
az healthbot bot create --location "East US" --sku name="F0" --resource-group "healthbotClient"
```
##### Show #####
```
az healthbot bot show --resource-group "healthbotClient"
```
##### List #####
```
az healthbot bot list --resource-group "OneResourceGroupName"
```
##### Update #####
```
az healthbot bot update --sku name="F0" --resource-group "healthbotClient"
```
##### Delete #####
```
az healthbot bot delete --resource-group "healthbotClient"
```