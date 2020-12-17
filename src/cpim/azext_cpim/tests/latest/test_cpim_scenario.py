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


# Env setup
@try_manual
def setup(test, rg, rg_2):
    pass


# EXAMPLE: /B2CTenants/put/Create tenant
@try_manual
def step__b2ctenants_put_create_tenant(test, rg, rg_2):
    test.cmd('az cpim b2-c-tenant create '
             '--location "United States" '
             '--properties display-name="Contoso" country-code="US" '
             '--sku-name "Standard" '
             '--resource-group "{rg}" '
             '--resource-name "contoso.onmicrosoft.com"',
             checks=[])


# EXAMPLE: /B2CTenants/get/B2CTenants_ListByResourceGroup
@try_manual
def step__b2ctenants_get(test, rg, rg_2):
    test.cmd('az cpim b2-c-tenant list '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /B2CTenants/get/B2CTenants_ListBySubscription
@try_manual
def step__b2ctenants_get_b2ctenants_listbysubscription(test, rg, rg_2):
    test.cmd('az cpim b2-c-tenant list '
             '-g ""',
             checks=[])


# EXAMPLE: /B2CTenants/get/Get tenant
@try_manual
def step__b2ctenants_get_get_tenant(test, rg, rg_2):
    test.cmd('az cpim b2-c-tenant show '
             '--resource-group "{rg}" '
             '--resource-name "contoso.onmicrosoft.com"',
             checks=[])


# EXAMPLE: /B2CTenants/patch/Get tenant
@try_manual
def step__b2ctenants_patch_get_tenant(test, rg, rg_2):
    test.cmd('az cpim b2-c-tenant update '
             '--resource-group "{rg}" '
             '--resource-name "contoso.onmicrosoft.com" '
             '--sku-name "PremiumP1" '
             '--tags key="value"',
             checks=[])


# EXAMPLE: /B2CTenants/delete/Delete tenant
@try_manual
def step__b2ctenants_delete_delete_tenant(test, rg, rg_2):
    test.cmd('az cpim b2-c-tenant delete -y '
             '--resource-group "{rg_2}" '
             '--resource-name "contoso.onmicrosoft.com"',
             checks=[])


# EXAMPLE: /Operations/get/Get Async Status
@try_manual
def step__operations_get_get_async_status(test, rg, rg_2):
    test.cmd('az cpim operation get-async-status '
             '--operation-id "99999999-9999-9999-9999-999999999999"',
             checks=[])


# Env cleanup
@try_manual
def cleanup(test, rg, rg_2):
    pass


# Testcase
@try_manual
def call_scenario(test, rg, rg_2):
    setup(test, rg, rg_2)
    step__b2ctenants_put_create_tenant(test, rg, rg_2)
    step__b2ctenants_get(test, rg, rg_2)
    step__b2ctenants_get_b2ctenants_listbysubscription(test, rg, rg_2)
    step__b2ctenants_get_get_tenant(test, rg, rg_2)
    step__b2ctenants_patch_get_tenant(test, rg, rg_2)
    step__b2ctenants_delete_delete_tenant(test, rg, rg_2)
    step__operations_get_get_async_status(test, rg, rg_2)
    cleanup(test, rg, rg_2)


@try_manual
class CPIMConfigurationClientScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestcpim_contosoResourceGroup'[:7], key='rg', parameter_name='rg')
    @ResourceGroupPreparer(name_prefix='clitestcpim_rg1'[:7], key='rg_2', parameter_name='rg_2')
    def test_cpim(self, rg, rg_2):

        call_scenario(self, rg, rg_2)
        calc_coverage(__file__)
        raise_if()
