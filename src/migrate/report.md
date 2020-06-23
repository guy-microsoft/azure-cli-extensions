# Azure CLI Module Creation Report

### migrate assessed-machine list

list a migrate assessed-machine.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
|**--group-name**|string|Unique name of a group within a project.|group_name|
|**--assessment-name**|string|Unique name of an assessment within a project.|assessment_name|
### migrate assessed-machine show

show a migrate assessed-machine.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
|**--group-name**|string|Unique name of a group within a project.|group_name|
|**--assessment-name**|string|Unique name of an assessment within a project.|assessment_name|
|**--assessed-machine-name**|string|Unique name of an assessed machine evaluated as part of an assessment.|assessed_machine_name|
### migrate assessment create

create a migrate assessment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
|**--group-name**|string|Unique name of a group within a project.|group_name|
|**--assessment-name**|string|Unique name of an assessment within a project.|assessment_name|
|**--azure-location**|choice|Target Azure location for which the machines should be assessed. These enums are the same as used by Compute API.|azure_location|
|**--azure-offer-code**|choice|Offer code according to which cost estimation is done.|azure_offer_code|
|**--azure-pricing-tier**|choice|Pricing tier for Size evaluation.|azure_pricing_tier|
|**--azure-storage-redundancy**|choice|Storage Redundancy type offered by Azure.|azure_storage_redundancy|
|**--scaling-factor**|number|Scaling factor used over utilization data to add a performance buffer for new machines to be created in Azure. Min Value = 1.0, Max value = 1.9, Default = 1.3.|scaling_factor|
|**--percentile**|choice|Percentile of performance data used to recommend Azure size.|percentile|
|**--time-range**|choice|Time range of performance data used to recommend a size.|time_range|
|**--stage**|choice|User configurable setting that describes the status of the assessment.|stage|
|**--currency**|choice|Currency to report prices in.|currency|
|**--azure-hybrid-use-benefit**|choice|AHUB discount on windows virtual machines.|azure_hybrid_use_benefit|
|**--discount-percentage**|number|Custom discount percentage to be applied on final costs. Can be in the range [0, 100].|discount_percentage|
|**--sizing-criterion**|choice|Assessment sizing criterion.|sizing_criterion|
|**--reserved-instance**|choice|Azure reserved instance.|reserved_instance|
|**--azure-vm-families**|array|List of azure VM families.|azure_vm_families|
|**--azure-disk-type**|choice|Storage type selected for this disk.|azure_disk_type|
|**--vm-uptime**|object|Specify the duration for which the VMs are up in the on-premises environment.|vm_uptime|
|**--e-tag**|string|For optimistic concurrency control.|e_tag|
### migrate assessment delete

delete a migrate assessment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
|**--group-name**|string|Unique name of a group within a project.|group_name|
|**--assessment-name**|string|Unique name of an assessment within a project.|assessment_name|
### migrate assessment get-report-download-url

get-report-download-url a migrate assessment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
|**--group-name**|string|Unique name of a group within a project.|group_name|
|**--assessment-name**|string|Unique name of an assessment within a project.|assessment_name|
### migrate assessment list

list a migrate assessment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
|**--group-name**|string|Unique name of a group within a project.|group_name|
### migrate assessment show

show a migrate assessment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
|**--group-name**|string|Unique name of a group within a project.|group_name|
|**--assessment-name**|string|Unique name of an assessment within a project.|assessment_name|
### migrate group create

create a migrate group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
|**--group-name**|string|Unique name of a group within a project.|group_name|
|**--e-tag**|string|For optimistic concurrency control.|e_tag|
### migrate group delete

delete a migrate group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
|**--group-name**|string|Unique name of a group within a project.|group_name|
### migrate group list

list a migrate group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
### migrate group show

show a migrate group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
|**--group-name**|string|Unique name of a group within a project.|group_name|
### migrate group update-machine

update-machine a migrate group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
|**--group-name**|string|Unique name of a group within a project.|group_name|
|**--e-tag**|string|For optimistic concurrency control.|e_tag|
|**--properties**|object|Properties of the group.|properties|
### migrate hyper-v-collector create

create a migrate hyper-v-collector.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
|**--hyper-v-collector-name**|string|Unique name of a Hyper-V collector within a project.|hyper_v_collector_name|
|**--e-tag**|string||e_tag|
|**--discovery-site-id**|string|The ARM id of the discovery service site.|discovery_site_id|
|**--agent-properties-spn-details**|object||spn_details|
### migrate hyper-v-collector delete

delete a migrate hyper-v-collector.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
|**--hyper-v-collector-name**|string|Unique name of a Hyper-V collector within a project.|hyper_v_collector_name|
### migrate hyper-v-collector list

list a migrate hyper-v-collector.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
### migrate hyper-v-collector show

show a migrate hyper-v-collector.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
|**--hyper-v-collector-name**|string|Unique name of a Hyper-V collector within a project.|hyper_v_collector_name|
### migrate machine list

list a migrate machine.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
### migrate machine show

show a migrate machine.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
|**--machine-name**|string|Unique name of a machine in private datacenter.|machine_name|
### migrate project assessment-option

assessment-option a migrate project.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
|**--assessment-options-name**|string|Name of the assessment options. The only name accepted in default.|assessment_options_name|
### migrate project assessment-option-list

assessment-option-list a migrate project.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
### migrate project create

create a migrate project.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
|**--e-tag**|string|For optimistic concurrency control.|e_tag|
|**--location**|string|Azure location in which project is created.|location|
|**--tags**|any|Tags provided by Azure Tagging service.|tags|
|**--properties**|object|Properties of the project.|properties|
### migrate project delete

delete a migrate project.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
### migrate project list

list a migrate project.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
### migrate project show

show a migrate project.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
### migrate project update

update a migrate project.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
|**--e-tag**|string|For optimistic concurrency control.|e_tag|
|**--location**|string|Azure location in which project is created.|location|
|**--tags**|any|Tags provided by Azure Tagging service.|tags|
|**--properties**|object|Properties of the project.|properties|
### migrate v-mware-collector create

create a migrate v-mware-collector.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
|**--vm-ware-collector-name**|string|Unique name of a VMware collector within a project.|vm_ware_collector_name|
|**--e-tag**|string||e_tag|
|**--discovery-site-id**|string|The ARM id of the discovery service site.|discovery_site_id|
|**--agent-properties-spn-details**|object||spn_details|
### migrate v-mware-collector delete

delete a migrate v-mware-collector.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
|**--vm-ware-collector-name**|string|Unique name of a VMware collector within a project.|vm_ware_collector_name|
### migrate v-mware-collector list

list a migrate v-mware-collector.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
### migrate v-mware-collector show

show a migrate v-mware-collector.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of the Azure Resource Group that project is part of.|resource_group_name|
|**--project-name**|string|Name of the Azure Migrate project.|project_name|
|**--vm-ware-collector-name**|string|Unique name of a VMware collector within a project.|vm_ware_collector_name|