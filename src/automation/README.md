# Azure CLI automation Extension #
This is the extension for automation

### How to use ###
Install this extension using the below CLI command
```
az extension add --name automation
```

### Included Features ###
#### automation runbook ####
##### Create #####
```
az automation runbook create --automation-account-name "ContoseAutomationAccount" \
    --draft-parameters "{\\"name\\":\\"Get-AzureVMTutorial\\",\\"location\\":\\"East US 2\\",\\"properties\\":{\\"description\\":\\"Description of the Runbook\\",\\"logActivityTrace\\":1,\\"logProgress\\":true,\\"logVerbose\\":false,\\"publishContentLink\\":{\\"contentHash\\":{\\"algorithm\\":\\"SHA256\\",\\"value\\":\\"115775B8FF2BE672D8A946BD0B489918C724DDE15A440373CA54461D53010A80\\"},\\"uri\\":\\"https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-automation-runbook-getvms/Runbooks/Get-AzureVMTutorial.ps1\\"},\\"runbookType\\":\\"PowerShellWorkflow\\"},\\"tags\\":{\\"tag01\\":\\"value01\\",\\"tag02\\":\\"value02\\"}}" \
    --resource-group "rg" --runbook-name "Get-AzureVMTutorial" 
```
##### Create #####
```
az automation runbook create --automation-account-name "ContoseAutomationAccount" \
    --draft-parameters "{\\"name\\":\\"Get-AzureVMTutorial\\",\\"location\\":\\"East US 2\\",\\"properties\\":{\\"description\\":\\"Description of the Runbook\\",\\"draft\\":{},\\"logProgress\\":false,\\"logVerbose\\":false,\\"runbookType\\":\\"PowerShellWorkflow\\"},\\"tags\\":{\\"tag01\\":\\"value01\\",\\"tag02\\":\\"value02\\"}}" \
    --resource-group "rg" --runbook-name "Get-AzureVMTutorial" 
```
##### List #####
```
az automation runbook list --automation-account-name "ContoseAutomationAccount" --resource-group "rg"
```
##### Show #####
```
az automation runbook show --automation-account-name "ContoseAutomationAccount" --resource-group "rg" \
    --name "Get-AzureVMTutorial" 
```
##### Update #####
```
az automation runbook update --automation-account-name "ContoseAutomationAccount" \
    --description "Updated Description of the Runbook" --log-activity-trace 1 --log-progress true --log-verbose false \
    --resource-group "rg" --runbook-name "Get-AzureVMTutorial" 
```
##### Publish #####
```
az automation runbook publish --automation-account-name "ContoseAutomationAccount" --resource-group "rg" \
    --name "Get-AzureVMTutorial" 
```
##### Delete #####
```
az automation runbook delete --automation-account-name "ContoseAutomationAccount" --resource-group "rg" \
    --name "Get-AzureVMTutorial" 
```