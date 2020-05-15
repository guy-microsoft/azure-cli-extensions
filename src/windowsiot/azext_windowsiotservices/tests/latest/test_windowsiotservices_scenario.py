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
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest
from .. import try_manual
from azure.cli.testsdk import ResourceGroupPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


@try_manual
def setup(test, rg, rg_2, rg_3, rg_4):
    pass


# EXAMPLE: /Services/put/Service_Create
@try_manual
def step__services_put_service_create(test, rg, rg_2, rg_3, rg_4):
    test.cmd('az windowsiotservices service create '
             '--device-name "service4445" '
             '--admin-domain-name "d.e.f" '
             '--billing-domain-name "a.b.c" '
             '--notes "blah" '
             '--quantity 1000000 '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Services/get/Service_List
@try_manual
def step__services_get_service_list(test, rg, rg_2, rg_3, rg_4):
    test.cmd('az windowsiotservices service list',
             checks=[])


# EXAMPLE: /Services/get/Service_ListByResourceGroup
@try_manual
def step__services_get_service_listbyresourcegroup(test, rg, rg_2, rg_3, rg_4):
    test.cmd('az windowsiotservices service list '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: /Services/get/Services_GetProperties
@try_manual
def step__services_get_services_getproperties(test, rg, rg_2, rg_3, rg_4):
    test.cmd('az windowsiotservices service show '
             '--device-name "service8596" '
             '--resource-group "{rg_3}"',
             checks=[])


# EXAMPLE: /Services/post/Service_CheckNameAvailability
@try_manual
def step__services_post_service_checknameavailability(test, rg, rg_2, rg_3, rg_4):
    test.cmd('az windowsiotservices service check-device-service-name-availability '
             '--name "service3363"',
             checks=[])


# EXAMPLE: /Services/patch/Service_Update
@try_manual
def step__services_patch_service_update(test, rg, rg_2, rg_3, rg_4):
    test.cmd('az windowsiotservices service update '
             '--device-name "service8596" '
             '--admin-domain-name "d.e.f" '
             '--billing-domain-name "a.b.c" '
             '--notes "blah" '
             '--quantity 1000000 '
             '--resource-group "{rg_3}"',
             checks=[])


# EXAMPLE: /Services/delete/Service_Delete
@try_manual
def step__services_delete_service_delete(test, rg, rg_2, rg_3, rg_4):
    test.cmd('az windowsiotservices service delete '
             '--device-name "service2434" '
             '--resource-group "{rg_4}"',
             checks=[])


@try_manual
def cleanup(test, rg, rg_2, rg_3, rg_4):
    pass


@try_manual
def call_scenario(test, rg, rg_2, rg_3, rg_4):
    setup(test, rg, rg_2, rg_3, rg_4)
    step__services_put_service_create(test, rg, rg_2, rg_3, rg_4)
    step__services_get_service_list(test, rg, rg_2, rg_3, rg_4)
    step__services_get_service_listbyresourcegroup(test, rg, rg_2, rg_3, rg_4)
    step__services_get_services_getproperties(test, rg, rg_2, rg_3, rg_4)
    step__services_post_service_checknameavailability(test, rg, rg_2, rg_3, rg_4)
    step__services_patch_service_update(test, rg, rg_2, rg_3, rg_4)
    step__services_delete_service_delete(test, rg, rg_2, rg_3, rg_4)
    cleanup(test, rg, rg_2, rg_3, rg_4)


@try_manual
class DeviceServicesScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestwindowsiotservices_res9101'[:7], key='rg', parameter_name='rg')
    @ResourceGroupPreparer(name_prefix='clitestwindowsiotservices_res6117'[:7], key='rg_2', parameter_name='rg_2')
    @ResourceGroupPreparer(name_prefix='clitestwindowsiotservices_res9407'[:7], key='rg_3', parameter_name='rg_3')
    @ResourceGroupPreparer(name_prefix='clitestwindowsiotservices_res4228'[:7], key='rg_4', parameter_name='rg_4')
    def test_windowsiotservices(self, rg, rg_2, rg_3, rg_4):

        call_scenario(self, rg, rg_2, rg_3, rg_4)