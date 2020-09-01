# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=line-too-long

import os
from azure.cli.testsdk import ScenarioTest
from .. import try_manual, raise_if
from azure.cli.testsdk import ResourceGroupPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


@try_manual
def setup(test, rg):
    pass


# EXAMPLE: /GuestConfigurationAssignments/put/Create or update guest configuration assignment
@try_manual
def step__guestconfigurationassignments_put_create_or_update_guest_configuration_assignment(test, rg):
    test.cmd('az guestconfig guest-configuration-assignment create '
             '--guest-configuration-assignment-name "{WhitelistedApplication}" '
             '--guest-configuration-name "WhitelistedApplication" '
             '--location "westcentralus" '
             '--context "Azure policy" '
             '--guest-configuration-name "WhitelistedApplication" '
             '--guest-configuration-configuration-parameter name="[InstalledApplication]bwhitelistedapp;Name" value="No'
             'tePad,sql" '
             '--guest-configuration-configuration-setting action-after-reboot="ContinueConfiguration" configuration-mod'
             'e="MonitorOnly" configuration-mode-frequency-mins=15 reboot-if-needed="False" '
             '--guest-configuration-version "1.*" '
             '--resource-group "{rg}" '
             '--vm-name "myVMName"',
             checks=[])
    test.cmd('az guestconfig guest-configuration-assignment wait --created '
             '--guest-configuration-assignment-name "{WhitelistedApplication}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /GuestConfigurationAssignments/get/Get a guest configuration assignment
@try_manual
def step__guestconfigurationassignments_get_get_a_guest_configuration_assignment(test, rg):
    test.cmd('az guestconfig guest-configuration-assignment show '
             '--name "{GuestConfigurationAssignments_2}" '
             '--resource-group "{rg}" '
             '--vm-name "myVMName"',
             checks=[])


# EXAMPLE: /GuestConfigurationAssignments/get/List all guest configuration assignments for a virtual machine
@try_manual
def step__guestconfigurationassignments_get_list_all_guest_configuration_assignments_for_a_virtual_machine(test, rg):
    test.cmd('az guestconfig guest-configuration-assignment list '
             '--resource-group "{rg}" '
             '--vm-name "myVMName"',
             checks=[])


# EXAMPLE: /GuestConfigurationAssignmentReports/get/Get a guest configuration assignment report by Id for a virtual machine
@try_manual
def step__guestconfigurationassignmentreports_get_get_a_guest_configuration_assignment_report_by_id_for_a_virtual_machine(test,
                                                                                                                           rg):
    test.cmd('az guestconfig guest-configuration-assignment-report show '
             '--guest-configuration-assignment-name "{GuestConfigurationAssignments_3}" '
             '--report-id "7367cbb8-ae99-47d0-a33b-a283564d2cb1" '
             '--resource-group "{rg}" '
             '--vm-name "myvm"',
             checks=[])


# EXAMPLE: /GuestConfigurationAssignmentReports/get/List all guest configuration assignments for a virtual machine
@try_manual
def step__guestconfigurationassignmentreports_get_list_all_guest_configuration_assignments_for_a_virtual_machine(test,
                                                                                                                 rg):
    test.cmd('az guestconfig guest-configuration-assignment-report list '
             '--guest-configuration-assignment-name "{GuestConfigurationAssignments_3}" '
             '--resource-group "{rg}" '
             '--vm-name "myVMName"',
             checks=[])


# EXAMPLE: /GuestConfigurationHCRPAssignmentReports/get/Get a guest configuration assignment report by Id for a virtual machine
@try_manual
def step__guestconfigurationhcrpassignmentreports_get_get_a_guest_configuration_assignment_report_by_id_for_a_virtual_machine(test,
                                                                                                                               rg):
    test.cmd('az guestconfig guest-configuration-hcrp-assignment-report show '
             '--guest-configuration-assignment-name "{GuestConfigurationAssignments_3}" '
             '--machine-name "myMachineName" '
             '--report-id "7367cbb8-ae99-47d0-a33b-a283564d2cb1" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /GuestConfigurationHCRPAssignmentReports/get/List all guest configuration assignments for a virtual machine
@try_manual
def step__guestconfigurationhcrpassignmentreports_get_list_all_guest_configuration_assignments_for_a_virtual_machine(test,
                                                                                                                      rg):
    test.cmd('az guestconfig guest-configuration-hcrp-assignment-report list '
             '--guest-configuration-assignment-name "{GuestConfigurationAssignments_3}" '
             '--machine-name "myMachineName" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /GuestConfigurationHCRPAssignments/put/Create or update guest configuration assignment
@try_manual
def step__guestconfigurationhcrpassignments_put_create_or_update_guest_configuration_assignment(test, rg):
    test.cmd('az guestconfig guest-configuration-hcrp-assignment create '
             '--guest-configuration-assignment-name "{WhitelistedApplication}" '
             '--machine-name "myMachineName" '
             '--guest-configuration-name "WhitelistedApplication" '
             '--location "westcentralus" '
             '--context "Azure policy" '
             '--guest-configuration-name "WhitelistedApplication" '
             '--guest-configuration-configuration-parameter name="[InstalledApplication]bwhitelistedapp;Name" value="No'
             'tePad,sql" '
             '--guest-configuration-configuration-setting action-after-reboot="ContinueConfiguration" configuration-mod'
             'e="MonitorOnly" configuration-mode-frequency-mins=15 reboot-if-needed="False" '
             '--guest-configuration-version "1.*" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /GuestConfigurationHCRPAssignments/get/Get a guest configuration assignment
@try_manual
def step__guestconfigurationhcrpassignments_get_get_a_guest_configuration_assignment(test, rg):
    test.cmd('az guestconfig guest-configuration-hcrp-assignment show '
             '--guest-configuration-assignment-name "{GuestConfigurationAssignments_2}" '
             '--machine-name "myMachineName" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /GuestConfigurationHCRPAssignments/get/List all guest configuration assignments for a virtual machine
@try_manual
def step__guestconfigurationhcrpassignments_get_list_all_guest_configuration_assignments_for_a_virtual_machine(test,
                                                                                                               rg):
    test.cmd('az guestconfig guest-configuration-hcrp-assignment list '
             '--machine-name "myMachineName" '
             '--resource-group "{rg}"',
             checks=[])


@try_manual
def cleanup(test, rg):
    pass


@try_manual
def call_scenario(test, rg):
    setup(test, rg)
    step__guestconfigurationassignments_put_create_or_update_guest_configuration_assignment(test, rg)
    step__guestconfigurationassignments_get_get_a_guest_configuration_assignment(test, rg)
    step__guestconfigurationassignments_get_list_all_guest_configuration_assignments_for_a_virtual_machine(test, rg)
    step__guestconfigurationassignmentreports_get_get_a_guest_configuration_assignment_report_by_id_for_a_virtual_machine(test,
                                                                                                                           rg)
    step__guestconfigurationassignmentreports_get_list_all_guest_configuration_assignments_for_a_virtual_machine(test,
                                                                                                                 rg)
    step__guestconfigurationhcrpassignmentreports_get_get_a_guest_configuration_assignment_report_by_id_for_a_virtual_machine(test,
                                                                                                                               rg)
    step__guestconfigurationhcrpassignmentreports_get_list_all_guest_configuration_assignments_for_a_virtual_machine(test,
                                                                                                                      rg)
    step__guestconfigurationhcrpassignments_put_create_or_update_guest_configuration_assignment(test, rg)
    step__guestconfigurationhcrpassignments_get_get_a_guest_configuration_assignment(test, rg)
    step__guestconfigurationhcrpassignments_get_list_all_guest_configuration_assignments_for_a_virtual_machine(test,
                                                                                                               rg)
    cleanup(test, rg)


@try_manual
class GuestConfigurationClientScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestguestconfig_myResourceGroupName'[:7], key='rg', parameter_name='rg')
    def test_guestconfig(self, rg):

        self.kwargs.update({
            'WhitelistedApplication': 'WhitelistedApplication',
            'GuestConfigurationAssignments_2': 'SecureProtocol',
            'GuestConfigurationAssignments_3': 'AuditSecureProtocol',
        })

        call_scenario(self, rg)
        raise_if()
