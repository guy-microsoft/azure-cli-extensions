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
from .preparers import VirtualNetworkPreparer
from .example_steps import step_asc_operation_show
from .example_steps import step_create
from .example_steps import step_create2
from .example_steps import step_show
from .example_steps import step_list
from .example_steps import step_list2
from .example_steps import step_update
from .example_steps import step_update2
from .example_steps import step_debug_info
from .example_steps import step_flush
from .example_steps import step_start
from .example_steps import step_stop
from .example_steps import step_upgrade_firmware
from .example_steps import step_delete
from .example_steps import step_sku_list
from .example_steps import step_storage_target_create
from .example_steps import step_storage_target_create2
from .example_steps import step_storage_target_show
from .example_steps import step_storage_target_list
from .example_steps import step_storage_target_delete
from .example_steps import step_usage_model_list
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
    step_asc_operation_show(test, rg, checks=[])
    step_create(test, rg, checks=[])
    step_create2(test, rg, checks=[])
    step_show(test, rg, checks=[])
    step_list(test, rg, checks=[])
    step_list2(test, rg, checks=[])
    step_update(test, rg, checks=[])
    step_update2(test, rg, checks=[])
    step_debug_info(test, rg, checks=[])
    step_flush(test, rg, checks=[])
    step_start(test, rg, checks=[])
    step_stop(test, rg, checks=[])
    step_upgrade_firmware(test, rg, checks=[])
    step_delete(test, rg, checks=[])
    step_sku_list(test, rg, checks=[])
    step_storage_target_create(test, rg, checks=[
        test.check("name", "{myStorageTarget}", case_sensitive=False),
        test.check("nfs3.target", "10.0.44.44", case_sensitive=False),
        test.check("nfs3.usageModel", "READ_HEAVY_INFREQ", case_sensitive=False),
    ])
    step_storage_target_create2(test, rg, checks=[
        test.check("name", "{myStorageTarget}", case_sensitive=False),
        test.check("nfs3.target", "10.0.44.44", case_sensitive=False),
        test.check("nfs3.usageModel", "READ_HEAVY_INFREQ", case_sensitive=False),
    ])
    step_storage_target_show(test, rg, checks=[
        test.check("name", "{myStorageTarget}", case_sensitive=False),
    ])
    step_storage_target_list(test, rg, checks=[
        test.check('length(@)', 1),
    ])
    step_storage_target_delete(test, rg, checks=[])
    step_usage_model_list(test, rg, checks=[])
    cleanup_scenario(test, rg)


# Test class for Scenario
@try_manual
class StoragecacheScenarioTest(ScenarioTest):

    def __init__(self, *args, **kwargs):
        super(StoragecacheScenarioTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myStorageTarget': 'st1',
        })


    @ResourceGroupPreparer(name_prefix='cliteststoragecache_scgroup'[:7], key='rg', parameter_name='rg')
    @VirtualNetworkPreparer(name_prefix='cliteststoragecache_scvnet'[:7], key='vn', resource_group_key='rg')
    def test_storagecache_Scenario(self, rg):
        call_scenario(self, rg)
        calc_coverage(__file__)
        raise_if()

