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
from .. import try_manual, raise_if, calc_coverage
from azure.cli.testsdk import ResourceGroupPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


@try_manual
def setup(test, rg):
    pass


# EXAMPLE: /Accounts/put/Put account
@try_manual
def step__accounts_put_put_account(test, rg):
    test.cmd('az adp account create '
             '--name "{myAccount}" '
             '--location "Global" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("location", "Global", case_sensitive=False),
             ])
    test.cmd('az adp account wait --created '
             '--name "{myAccount}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Accounts/get/Get account
@try_manual
def step__accounts_get_get_account(test, rg):
    test.cmd('az adp account show '
             '--name "{myAccount}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("location", "Global", case_sensitive=False),
             ])


# EXAMPLE: /Accounts/get/List accounts
@try_manual
def step__accounts_get_list_accounts(test, rg):
    test.cmd('az adp account list '
             '-g ""',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: /Accounts/get/List accounts by resource group
@try_manual
def step__accounts_get_list_accounts_by_resource_group(test, rg):
    test.cmd('az adp account list '
             '--resource-group "{rg}"',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: /Accounts/patch/Patch account
@try_manual
def step__accounts_patch_patch_account(test, rg):
    test.cmd('az adp account update '
             '--name "{myAccount}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("location", "Global", case_sensitive=False),
             ])


# EXAMPLE: /DataPools/put/Put Data Pool
@try_manual
def step__datapools_put_put_data_pool(test, rg):
    test.cmd('az adp data-pool create '
             '--account-name "{myAccount}" '
             '--name "{myDataPool}" '
             '--locations name="westus" '
             '--resource-group "{rg}"',
             checks=[])
    test.cmd('az adp data-pool wait --created '
             '--name "{myDataPool}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /DataPools/get/Get Data Pool
@try_manual
def step__datapools_get_get_data_pool(test, rg):
    test.cmd('az adp data-pool show '
             '--account-name "{myAccount}" '
             '--name "{myDataPool}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /DataPools/get/List Data Pools
@try_manual
def step__datapools_get_list_data_pools(test, rg):
    test.cmd('az adp data-pool list '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: /DataPools/patch/Patch Data Pool
@try_manual
def step__datapools_patch_patch_data_pool(test, rg):
    test.cmd('az adp data-pool update '
             '--account-name "{myAccount}" '
             '--name "{myDataPool}" '
             '--locations name="westus" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /DataPools/delete/Delete Data Pool
@try_manual
def step__datapools_delete_delete_data_pool(test, rg):
    test.cmd('az adp data-pool delete -y '
             '--account-name "{myAccount}" '
             '--name "{myDataPool}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Accounts/delete/Delete account
@try_manual
def step__accounts_delete_delete_account(test, rg):
    test.cmd('az adp account delete -y '
             '--name "{myAccount}" '
             '--resource-group "{rg}"',
             checks=[])


@try_manual
def cleanup(test, rg):
    pass


@try_manual
def call_scenario(test, rg):
    setup(test, rg)
    step__accounts_put_put_account(test, rg)
    step__accounts_get_get_account(test, rg)
    step__accounts_get_list_accounts(test, rg)
    step__accounts_get_list_accounts_by_resource_group(test, rg)
    step__accounts_patch_patch_account(test, rg)
    step__datapools_put_put_data_pool(test, rg)
    step__datapools_get_get_data_pool(test, rg)
    step__datapools_get_list_data_pools(test, rg)
    step__datapools_patch_patch_data_pool(test, rg)
    step__datapools_delete_delete_data_pool(test, rg)
    step__accounts_delete_delete_account(test, rg)
    cleanup(test, rg)


@try_manual
class AdpManagementClientScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestadp_adpClient'[:7], key='rg', parameter_name='rg')
    def test_adp(self, rg):

        self.kwargs.update({
            'myAccount': 'sampleacct',
            'myDataPool': 'sampledp',
        })

        call_scenario(self, rg)
        calc_coverage(__file__)
        raise_if()
