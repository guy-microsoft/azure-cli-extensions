# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class CustomprovidersScenarioTest(ScenarioTest):

    def current_subscription(self):
        subs = self.cmd('az account show').get_output_in_json()
        return subs['id']

    @ResourceGroupPreparer(name_prefix='cli_test_customproviders_appRG'[:9], key='rg')
    @ResourceGroupPreparer(name_prefix='cli_test_customproviders_testRG'[:9], key='rg_2')
    def test_customproviders(self, resource_group):

        self.kwargs.update({
            'subscription_id': self.current_subscription()
        })

        self.kwargs.update({
            'associationName': self.create_random_name(prefix='cli_test_associations'[:9], length=24),
        })

        self.cmd('az customproviders association create '
                 '--properties-target-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Solutions/applications/applicationName" '
                 '--association-name "{associationName}" '
                 '--scope "scope"',
                 checks=[])

        self.cmd('az customproviders custom-resource-provider create '
                 '--resource-group "{rg_2}" '
                 '--location "eastus" '
                 '--properties-actions name=TestAction endpoint=https://mytestendpoint/ routing-type=Proxy '
                 '--properties-resource-types name=TestResource endpoint=https://mytestendpoint2/ routing-type=Proxy,Cache '
                 '--resource-provider-name "newrp"',
                 checks=[])

        self.cmd('az customproviders custom-resource-provider show '
                 '--resource-group "{rg_2}" '
                 '--resource-provider-name "newrp"',
                 checks=[])

        self.cmd('az customproviders association show '
                 '--association-name "{associationName}" '
                 '--scope "scope"',
                 checks=[])

        self.cmd('az customproviders custom-resource-provider list '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az customproviders custom-resource-provider list',
                 checks=[])

        self.cmd('az customproviders association list '
                 '--scope "scope"',
                 checks=[])

        self.cmd('az customproviders custom-resource-provider update '
                 '--resource-group "{rg_2}" '
                 '--resource-provider-name "newrp"',
                 checks=[])

        self.cmd('az customproviders custom-resource-provider delete '
                 '--resource-group "{rg_2}" '
                 '--resource-provider-name "newrp"',
                 checks=[])

        self.cmd('az customproviders association delete '
                 '--association-name "{associationName}" '
                 '--scope "scope"',
                 checks=[])
