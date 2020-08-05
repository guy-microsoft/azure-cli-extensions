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

from knack.arguments import CLIArgumentType
from azure.cli.core.commands.parameters import (
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azext_guestconfig.action import (
    AddGuestConfigurationConfigurationParameter,
    AddGuestConfigurationConfigurationSetting
)


def load_arguments(self, _):

    with self.argument_context('guestconfig guest-configuration-assignment list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('vm_name', help='The name of the virtual machine.')

    with self.argument_context('guestconfig guest-configuration-assignment show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('guest_configuration_assignment_name', options_list=['--name', '-n'], help='The guest configuration '
                   'assignment name.', id_part='child_name_1')
        c.argument('vm_name', help='The name of the virtual machine.', id_part='name')

    with self.argument_context('guestconfig guest-configuration-assignment create') as c:
        c.argument('guest_configuration_assignment_name', help='Name of the guest configuration assignment.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('vm_name', help='The name of the virtual machine.')
        c.argument('name', help='Name of the guest configuration assignment.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('context', help='The source which initiated the guest configuration assignment. Ex: Azure Policy')
        c.argument('latest_assignment_report_assignment', arg_type=CLIArgumentType(options_list=['--latest-assignment-r'
                   'eport-assignment'], help='Configuration details of the guest configuration assignment. Expected val'
                   'ue: json-string/@json-file.'))
        c.argument('guest_configuration_name', help='Name of the guest configuration.')
        c.argument('guest_configuration_version', help='Version of the guest configuration.')
        c.argument('guest_configuration_configuration_parameter', action=AddGuestConfigurationConfigurationParameter,
                   nargs='+', help='The configuration parameters for the guest configuration.')
        c.argument('guest_configuration_configuration_setting', action=AddGuestConfigurationConfigurationSetting,
                   nargs='+', help='The configuration setting for the guest configuration.')

    with self.argument_context('guestconfig guest-configuration-assignment update') as c:
        c.argument('guest_configuration_assignment_name', help='Name of the guest configuration assignment.', id_part=
                   'child_name_1')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('vm_name', help='The name of the virtual machine.', id_part='name')
        c.argument('name', help='Name of the guest configuration assignment.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('context', help='The source which initiated the guest configuration assignment. Ex: Azure Policy')
        c.argument('latest_assignment_report_assignment', arg_type=CLIArgumentType(options_list=['--latest-assignment-r'
                   'eport-assignment'], help='Configuration details of the guest configuration assignment. Expected val'
                   'ue: json-string/@json-file.'))
        c.argument('guest_configuration_name', help='Name of the guest configuration.')
        c.argument('guest_configuration_version', help='Version of the guest configuration.')
        c.argument('guest_configuration_configuration_parameter', action=AddGuestConfigurationConfigurationParameter,
                   nargs='+', help='The configuration parameters for the guest configuration.')
        c.argument('guest_configuration_configuration_setting', action=AddGuestConfigurationConfigurationSetting,
                   nargs='+', help='The configuration setting for the guest configuration.')

    with self.argument_context('guestconfig guest-configuration-assignment wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('guest_configuration_assignment_name', options_list=['--name', '-n'], help='The guest configuration '
                   'assignment name.', id_part='child_name_1')
        c.argument('vm_name', help='The name of the virtual machine.', id_part='name')

    with self.argument_context('guestconfig guest-configuration-assignment-report list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('guest_configuration_assignment_name', help='The guest configuration assignment name.')
        c.argument('vm_name', help='The name of the virtual machine.')

    with self.argument_context('guestconfig guest-configuration-assignment-report show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('guest_configuration_assignment_name', help='The guest configuration assignment name.', id_part='chi'
                   'ld_name_1')
        c.argument('report_id', help='The GUID for the guest configuration assignment report.',
                   id_part='child_name_2')
        c.argument('vm_name', help='The name of the virtual machine.', id_part='name')

    with self.argument_context('guestconfig guest-configuration-hcrp-assignment list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('machine_name', help='The name of the ARC machine.')

    with self.argument_context('guestconfig guest-configuration-hcrp-assignment show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('guest_configuration_assignment_name', help='The guest configuration assignment name.', id_part='chi'
                   'ld_name_1')
        c.argument('machine_name', help='The name of the ARC machine.', id_part='name')

    with self.argument_context('guestconfig guest-configuration-hcrp-assignment create') as c:
        c.argument('guest_configuration_assignment_name', help='Name of the guest configuration assignment.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('machine_name', help='The name of the ARC machine.')
        c.argument('name', help='Name of the guest configuration assignment.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('context', help='The source which initiated the guest configuration assignment. Ex: Azure Policy')
        c.argument('latest_assignment_report_assignment', arg_type=CLIArgumentType(options_list=['--latest-assignment-r'
                   'eport-assignment'], help='Configuration details of the guest configuration assignment. Expected val'
                   'ue: json-string/@json-file.'))
        c.argument('guest_configuration_name', help='Name of the guest configuration.')
        c.argument('guest_configuration_version', help='Version of the guest configuration.')
        c.argument('guest_configuration_configuration_parameter', action=AddGuestConfigurationConfigurationParameter,
                   nargs='+', help='The configuration parameters for the guest configuration.')
        c.argument('guest_configuration_configuration_setting', action=AddGuestConfigurationConfigurationSetting,
                   nargs='+', help='The configuration setting for the guest configuration.')

    with self.argument_context('guestconfig guest-configuration-hcrp-assignment update') as c:
        c.argument('guest_configuration_assignment_name', help='Name of the guest configuration assignment.', id_part=
                   'child_name_1')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('machine_name', help='The name of the ARC machine.', id_part='name')
        c.argument('name', help='Name of the guest configuration assignment.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('context', help='The source which initiated the guest configuration assignment. Ex: Azure Policy')
        c.argument('latest_assignment_report_assignment', arg_type=CLIArgumentType(options_list=['--latest-assignment-r'
                   'eport-assignment'], help='Configuration details of the guest configuration assignment. Expected val'
                   'ue: json-string/@json-file.'))
        c.argument('guest_configuration_name', help='Name of the guest configuration.')
        c.argument('guest_configuration_version', help='Version of the guest configuration.')
        c.argument('guest_configuration_configuration_parameter', action=AddGuestConfigurationConfigurationParameter,
                   nargs='+', help='The configuration parameters for the guest configuration.')
        c.argument('guest_configuration_configuration_setting', action=AddGuestConfigurationConfigurationSetting,
                   nargs='+', help='The configuration setting for the guest configuration.')

    with self.argument_context('guestconfig guest-configuration-hcrp-assignment wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('guest_configuration_assignment_name', help='The guest configuration assignment name.', id_part='chi'
                   'ld_name_1')
        c.argument('machine_name', help='The name of the ARC machine.', id_part='name')

    with self.argument_context('guestconfig guest-configuration-hcrp-assignment-report list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('guest_configuration_assignment_name', help='The guest configuration assignment name.')
        c.argument('machine_name', help='The name of the ARC machine.')

    with self.argument_context('guestconfig guest-configuration-hcrp-assignment-report show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('guest_configuration_assignment_name', help='The guest configuration assignment name.', id_part='chi'
                   'ld_name_1')
        c.argument('report_id', help='The GUID for the guest configuration assignment report.',
                   id_part='child_name_2')
        c.argument('machine_name', help='The name of the ARC machine.', id_part='name')