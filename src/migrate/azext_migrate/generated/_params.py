# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azext_migrate.action import (
    AddProjectsProperties,
    AddGroupsProperties,
    AddVmUptime,
    AddAgentPropertiesSpnDetails
)


def load_arguments(self, _):

    with self.argument_context('migrate project list') as c:
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('migrate project show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', options_list=['--name', '-n'], help='Name of the Azure Migrate project.')

    with self.argument_context('migrate project create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', options_list=['--name', '-n'], help='Name of the Azure Migrate project.')
        c.argument('e_tag', help='For optimistic concurrency control.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)
        c.argument('properties', action=AddProjectsProperties, nargs='+', help='Properties of the project.')

    with self.argument_context('migrate project update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', options_list=['--name', '-n'], help='Name of the Azure Migrate project.')
        c.argument('e_tag', help='For optimistic concurrency control.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)
        c.argument('properties', action=AddProjectsProperties, nargs='+', help='Properties of the project.')

    with self.argument_context('migrate project delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', options_list=['--name', '-n'], help='Name of the Azure Migrate project.')

    with self.argument_context('migrate project assessment-option') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', options_list=['--name', '-n'], help='Name of the Azure Migrate project.')
        c.argument('assessment_options_name',
                   help='Name of the assessment options. The only name accepted in default.')

    with self.argument_context('migrate project assessment-option-list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', options_list=['--name', '-n'], help='Name of the Azure Migrate project.')

    with self.argument_context('migrate machine list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', help='Name of the Azure Migrate project.')

    with self.argument_context('migrate machine show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', help='Name of the Azure Migrate project.', id_part='name')
        c.argument('machine_name', options_list=['--name', '-n'], help='Unique name of a machine in private datacenter.'
                   '', id_part='child_name_1')

    with self.argument_context('migrate group list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', help='Name of the Azure Migrate project.')

    with self.argument_context('migrate group show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', help='Name of the Azure Migrate project.', id_part='name')
        c.argument('group_name', options_list=['--name', '-n'], help='Unique name of a group within a project.',
                   id_part='child_name_1')

    with self.argument_context('migrate group create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', help='Name of the Azure Migrate project.')
        c.argument('group_name', options_list=['--name', '-n'], help='Unique name of a group within a project.')
        c.argument('e_tag', help='For optimistic concurrency control.')

    with self.argument_context('migrate group delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', help='Name of the Azure Migrate project.', id_part='name')
        c.argument('group_name', options_list=['--name', '-n'], help='Unique name of a group within a project.',
                   id_part='child_name_1')

    with self.argument_context('migrate group update-machine') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', help='Name of the Azure Migrate project.', id_part='name')
        c.argument('group_name', options_list=['--name', '-n'], help='Unique name of a group within a project.',
                   id_part='child_name_1')
        c.argument('e_tag', help='For optimistic concurrency control.')
        c.argument('properties', action=AddGroupsProperties, nargs='+', help='Properties of the group.')

    with self.argument_context('migrate assessment list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', help='Name of the Azure Migrate project.')
        c.argument('group_name', help='Unique name of a group within a project.')

    with self.argument_context('migrate assessment show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', help='Name of the Azure Migrate project.', id_part='name')
        c.argument('group_name', help='Unique name of a group within a project.', id_part='child_name_1')
        c.argument('assessment_name', options_list=['--name', '-n'], help='Unique name of an assessment within a projec'
                   't.', id_part='child_name_2')

    with self.argument_context('migrate assessment create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', help='Name of the Azure Migrate project.')
        c.argument('group_name', help='Unique name of a group within a project.')
        c.argument('assessment_name', options_list=['--name', '-n'], help='Unique name of an assessment within a projec'
                   't.')
        c.argument('e_tag', help='For optimistic concurrency control.')
        c.argument('azure_location', arg_type=get_enum_type(['Unknown', 'EastAsia', 'SoutheastAsia', 'AustraliaEast', 
                   'AustraliaSoutheast', 'BrazilSouth', 'CanadaCentral', 'CanadaEast', 'WestEurope', 'NorthEurope', 'Ce'
                   'ntralIndia', 'SouthIndia', 'WestIndia', 'JapanEast', 'JapanWest', 'KoreaCentral', 'KoreaSouth', 'Uk'
                   'West', 'UkSouth', 'NorthCentralUs', 'EastUs', 'WestUs2', 'SouthCentralUs', 'CentralUs', 'EastUs2',
                   'WestUs', 'WestCentralUs', 'GermanyCentral', 'GermanyNortheast', 'ChinaNorth', 'ChinaEast', 'USGovAr'
                   'izona', 'USGovTexas', 'USGovIowa', 'USGovVirginia', 'USDoDCentral', 'USDoDEast']), help='Target Azu'
                   're location for which the machines should be assessed. These enums are the same as used by Compute '
                   'API.')
        c.argument('azure_offer_code', arg_type=get_enum_type(['Unknown', 'MSAZR0003P', 'MSAZR0044P', 'MSAZR0059P', 'MS'
                   'AZR0060P', 'MSAZR0062P', 'MSAZR0063P', 'MSAZR0064P', 'MSAZR0029P', 'MSAZR0022P', 'MSAZR0023P', 'MSA'
                   'ZR0148P', 'MSAZR0025P', 'MSAZR0036P', 'MSAZR0120P', 'MSAZR0121P', 'MSAZR0122P', 'MSAZR0123P', 'MSAZ'
                   'R0124P', 'MSAZR0125P', 'MSAZR0126P', 'MSAZR0127P', 'MSAZR0128P', 'MSAZR0129P', 'MSAZR0130P', 'MSAZR'
                   '0111P', 'MSAZR0144P', 'MSAZR0149P', 'MSMCAZR0044P', 'MSMCAZR0059P', 'MSMCAZR0060P', 'MSMCAZR0063P',
                    'MSMCAZR0120P', 'MSMCAZR0121P', 'MSMCAZR0125P', 'MSMCAZR0128P', 'MSAZRDE0003P', 'MSAZRDE0044P', 'MS'
                   'AZRUSGOV0003P', 'EA']), help='Offer code according to which cost estimation is done.')
        c.argument('azure_pricing_tier', arg_type=get_enum_type(['Standard', 'Basic']), help='Pricing tier for Size eva'
                   'luation.')
        c.argument('azure_storage_redundancy', arg_type=get_enum_type(['Unknown', 'LocallyRedundant', 'ZoneRedundant',
                   'GeoRedundant', 'ReadAccessGeoRedundant']), help='Storage Redundancy type offered by Azure.')
        c.argument('scaling_factor', help='Scaling factor used over utilization data to add a performance buffer for ne'
                   'w machines to be created in Azure. Min Value = 1.0, Max value = 1.9, Default = 1.3.')
        c.argument('percentile', arg_type=get_enum_type(['Percentile50', 'Percentile90', 'Percentile95',
                   'Percentile99']), help='Percentile of performance data used to recommend Azure size.')
        c.argument('time_range', arg_type=get_enum_type(['Day', 'Week', 'Month', 'Custom']), help='Time range of perfor'
                   'mance data used to recommend a size.')
        c.argument('stage', arg_type=get_enum_type(['InProgress', 'UnderReview', 'Approved']), help='User configurable '
                   'setting that describes the status of the assessment.')
        c.argument('currency', arg_type=get_enum_type(['Unknown', 'USD', 'DKK', 'CAD', 'IDR', 'JPY', 'KRW', 'NZD', 'NOK'
                   '', 'RUB', 'SAR', 'ZAR', 'SEK', 'TRY', 'GBP', 'MXN', 'MYR', 'INR', 'HKD', 'BRL', 'TWD', 'EUR',
                   'CHF', 'ARS', 'AUD', 'CNY']), help='Currency to report prices in.')
        c.argument('azure_hybrid_use_benefit', arg_type=get_enum_type(['Unknown', 'Yes', 'No']), help='AHUB discount on'
                   ' windows virtual machines.')
        c.argument('discount_percentage', help='Custom discount percentage to be applied on final costs. Can be in the '
                   'range [0, 100].')
        c.argument('sizing_criterion', arg_type=get_enum_type(['PerformanceBased', 'AsOnPremises']), help='Assessment s'
                   'izing criterion.')
        c.argument('reserved_instance', arg_type=get_enum_type(['None', 'RI1Year', 'RI3Year']), help='Azure reserved in'
                   'stance.')
        c.argument('azure_vm_families', nargs='+', help='List of azure VM families.')
        c.argument('azure_disk_type', arg_type=get_enum_type(['Unknown', 'Standard', 'Premium', 'StandardSSD', 'Standar'
                   'dOrPremium']), help='Storage type selected for this disk.')
        c.argument('vm_uptime', action=AddVmUptime, nargs='+', help='Specify the duration for which the VMs are up in t'
                   'he on-premises environment.')

    with self.argument_context('migrate assessment delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', help='Name of the Azure Migrate project.', id_part='name')
        c.argument('group_name', help='Unique name of a group within a project.', id_part='child_name_1')
        c.argument('assessment_name', options_list=['--name', '-n'], help='Unique name of an assessment within a projec'
                   't.', id_part='child_name_2')

    with self.argument_context('migrate assessment get-report-download-url') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', help='Name of the Azure Migrate project.', id_part='name')
        c.argument('group_name', help='Unique name of a group within a project.', id_part='child_name_1')
        c.argument('assessment_name', options_list=['--name', '-n'], help='Unique name of an assessment within a projec'
                   't.', id_part='child_name_2')

    with self.argument_context('migrate assessed-machine list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', help='Name of the Azure Migrate project.')
        c.argument('group_name', help='Unique name of a group within a project.')
        c.argument('assessment_name', help='Unique name of an assessment within a project.')

    with self.argument_context('migrate assessed-machine show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', help='Name of the Azure Migrate project.', id_part='name')
        c.argument('group_name', help='Unique name of a group within a project.', id_part='child_name_1')
        c.argument('assessment_name', help='Unique name of an assessment within a project.', id_part='child_name_2')
        c.argument('assessed_machine_name', options_list=['--name', '-n'], help='Unique name of an assessed machine eva'
                   'luated as part of an assessment.', id_part='child_name_3')

    with self.argument_context('migrate hyper-v-collector list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', help='Name of the Azure Migrate project.')

    with self.argument_context('migrate hyper-v-collector show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', help='Name of the Azure Migrate project.', id_part='name')
        c.argument('hyper_v_collector_name', options_list=['--name', '-n'], help='Unique name of a Hyper-V collector wi'
                   'thin a project.', id_part='child_name_1')

    with self.argument_context('migrate hyper-v-collector create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', help='Name of the Azure Migrate project.')
        c.argument('hyper_v_collector_name', options_list=['--name', '-n'], help='Unique name of a Hyper-V collector wi'
                   'thin a project.')
        c.argument('e_tag', help='')
        c.argument('discovery_site_id', help='The ARM id of the discovery service site.')
        c.argument('agent_properties_spn_details', action=AddAgentPropertiesSpnDetails, nargs='+', help='')

    with self.argument_context('migrate hyper-v-collector delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', help='Name of the Azure Migrate project.', id_part='name')
        c.argument('hyper_v_collector_name', options_list=['--name', '-n'], help='Unique name of a Hyper-V collector wi'
                   'thin a project.', id_part='child_name_1')

    with self.argument_context('migrate v-mware-collector list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', help='Name of the Azure Migrate project.')

    with self.argument_context('migrate v-mware-collector show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', help='Name of the Azure Migrate project.', id_part='name')
        c.argument('vm_ware_collector_name', options_list=['--name', '-n'], help='Unique name of a VMware collector wit'
                   'hin a project.', id_part='child_name_1')

    with self.argument_context('migrate v-mware-collector create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', help='Name of the Azure Migrate project.')
        c.argument('vm_ware_collector_name', options_list=['--name', '-n'], help='Unique name of a VMware collector wit'
                   'hin a project.')
        c.argument('e_tag', help='')
        c.argument('discovery_site_id', help='The ARM id of the discovery service site.')
        c.argument('agent_properties_spn_details', action=AddAgentPropertiesSpnDetails, nargs='+', help='')

    with self.argument_context('migrate v-mware-collector delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', help='Name of the Azure Migrate project.', id_part='name')
        c.argument('vm_ware_collector_name', options_list=['--name', '-n'], help='Unique name of a VMware collector wit'
                   'hin a project.', id_part='child_name_1')
