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


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup
@try_manual
def setup(test):
    pass


# EXAMPLE: /Alias/put/CreateAlias
@try_manual
def step__alias_put_createalias(test):
    test.cmd('az account alias create '
             '--name "{myAlias}" '
             '--properties billing-scope="/providers/Microsoft.Billing/billingAccounts/e879cf0f-2b4d-5431-109a-f72fc986'
             '8693:024cabf4-7321-4cf9-be59-df0c77ca51de_2019-05-31/billingProfiles/PE2Q-NOIT-BG7-TGB/invoiceSections/MT'
             'T4-OBS7-PJA-TGB" display-name="Contoso MCA subscription" workload="Production"',
             checks=[
                 test.check("name", "{myAlias}", case_sensitive=False),
             ])


# EXAMPLE: /Alias/get/GetAlias
@try_manual
def step__alias_get_getalias(test):
    test.cmd('az account alias list',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: /Alias/get/GetAlias
@try_manual
def step__alias_get_getalias(test):
    test.cmd('az account alias list',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: /Alias/delete/DeleteAlias
@try_manual
def step__alias_delete_deletealias(test):
    test.cmd('az account alias delete -y '
             '--name "{myAlias}"',
             checks=[])


# EXAMPLE: /Subscriptions/get/getSubscription
@try_manual
def step__subscriptions_get_getsubscription(test):
    test.cmd('az account subscription show '
             '--subscription-id "83aa47df-e3e9-49ff-877b-94304bf3d3ad"',
             checks=[])


# EXAMPLE: /Subscriptions/get/listLocations
@try_manual
def step__subscriptions_get_listlocations(test):
    test.cmd('az account subscription list-location '
             '--subscription-id "83aa47df-e3e9-49ff-877b-94304bf3d3ad"',
             checks=[])


# EXAMPLE: /Subscriptions/get/listSubscriptions
@try_manual
def step__subscriptions_get_listsubscriptions(test):
    test.cmd('az account subscription list',
             checks=[])


# EXAMPLE: /Subscription/post/cancelSubscription
@try_manual
def step__subscription_post_cancelsubscription(test):
    test.cmd('az account subscription cancel '
             '--subscription-id "83aa47df-e3e9-49ff-877b-94304bf3d3ad"',
             checks=[])


# EXAMPLE: /Subscription/post/enableSubscription
@try_manual
def step__subscription_post_enablesubscription(test):
    test.cmd('az account subscription enable '
             '--subscription-id "7948bcee-488c-47ce-941c-38e20ede803d"',
             checks=[])


# EXAMPLE: /Subscription/post/renameSubscription
@try_manual
def step__subscription_post_renamesubscription(test):
    test.cmd('az account subscription rename '
             '--name "{mySubscription}" '
             '--subscription-id "83aa47df-e3e9-49ff-877b-94304bf3d3ad"',
             checks=[])


# EXAMPLE: /Tenants/get/listTenants
@try_manual
def step__tenants_get_listtenants(test):
    test.cmd('az account tenant list',
             checks=[])


# Env cleanup
@try_manual
def cleanup(test):
    pass


# Testcase
@try_manual
def call_scenario(test):
    setup(test)
    step__alias_put_createalias(test)
    step__alias_get_getalias(test)
    step__alias_get_getalias(test)
    step__alias_delete_deletealias(test)
    step__subscriptions_get_getsubscription(test)
    step__subscriptions_get_listlocations(test)
    step__subscriptions_get_listsubscriptions(test)
    step__subscription_post_cancelsubscription(test)
    step__subscription_post_enablesubscription(test)
    step__subscription_post_renamesubscription(test)
    step__tenants_get_listtenants(test)
    cleanup(test)


@try_manual
class SubscriptionClientScenarioTest(ScenarioTest):

    def test_account(self):

        self.kwargs.update({
            'mySubscription': 'Test Sub',
            'myAlias': 'aliasForNewSub',
        })

        call_scenario(self)
        calc_coverage(__file__)
        raise_if()
