# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_machine_extension_create
from .example_steps import step_machine_extension_list
from .example_steps import step_machine_extension_show
from .example_steps import step_machine_extension_update
from .example_steps import step_machine_extension_delete
from .example_steps import step_show
from .example_steps import step_list
from .example_steps import step_delete
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test, rg):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test, rg):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test, rg):
    setup_scenario(test, rg)
    step_machine_extension_create(test, rg, checks=[])
    step_machine_extension_list(test, rg, checks=[])
    step_machine_extension_show(test, rg, checks=[])
    step_machine_extension_update(test, rg, checks=[])
    step_machine_extension_delete(test, rg, checks=[])
    step_show(test, rg, checks=[])
    step_list(test, rg, checks=[])
    step_list(test, rg, checks=[])
    step_delete(test, rg, checks=[])
    cleanup_scenario(test, rg)


# Test class for Scenario
@try_manual
class ConnectedmachineScenarioTest(ScenarioTest):

    def __init__(self, *args, **kwargs):
        super(ConnectedmachineScenarioTest, self).__init__(*args, **kwargs)


    @ResourceGroupPreparer(name_prefix='clitestconnectedmachine_myResourceGroup'[:7], key='rg', parameter_name='rg')
    def test_connectedmachine_Scenario(self, rg):
        call_scenario(self, rg)
        calc_coverage(__file__)
        raise_if()

