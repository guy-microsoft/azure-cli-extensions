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
def setup(test, rg):
    pass


# EXAMPLE: /Environments/put/EnvironmentsCreate
@try_manual
def step__environments_put_environmentscreate(test, rg):
    test.cmd('az timeseriesinsights environment create '
             '--name "{myEnvironment}" '
             '--parameters "{{\\"kind\\":\\"Gen1\\",\\"location\\":\\"West US\\",\\"properties\\":{{\\"dataRetentionTim'
             'e\\":\\"P31D\\",\\"partitionKeyProperties\\":[{{\\"name\\":\\"DeviceId1\\",\\"type\\":\\"String\\"}}]}},'
             '\\"sku\\":{{\\"name\\":\\"S1\\",\\"capacity\\":1}}}}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("name", "{myEnvironment}", case_sensitive=False),
             ])


# EXAMPLE: /Environments/get/EnvironmentsByResourceGroup
@try_manual
def step__environments_get_environmentsbyresourcegroup(test, rg):
    test.cmd('az timeseriesinsights environment list '
             '--resource-group "{rg}"',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: /Environments/get/EnvironmentsBySubscription
@try_manual
def step__environments_get_environmentsbysubscription(test, rg):
    test.cmd('az timeseriesinsights environment list '
             '-g ""',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: /Environments/get/EnvironmentsGet
@try_manual
def step__environments_get_environmentsget(test, rg):
    test.cmd('az timeseriesinsights environment show '
             '--name "{myEnvironment}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("name", "{myEnvironment}", case_sensitive=False),
             ])


# EXAMPLE: /Environments/patch/EnvironmentsUpdate
@try_manual
def step__environments_patch_environmentsupdate(test, rg):
    test.cmd('az timeseriesinsights environment update '
             '--name "{myEnvironment}" '
             '--tags someTag="someTagValue" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("name", "{myEnvironment}", case_sensitive=False),
                 test.check("tags.someTag", "someTagValue", case_sensitive=False),
             ])


# EXAMPLE: /AccessPolicies/put/AccessPoliciesCreate
@try_manual
def step__accesspolicies_put_accesspoliciescreate(test, rg):
    test.cmd('az timeseriesinsights access-policy create '
             '--name "{myAccessPolicy}" '
             '--environment-name "{myEnvironment}" '
             '--description "some description" '
             '--principal-object-id "aGuid" '
             '--roles "Reader" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("name", "{myAccessPolicy}", case_sensitive=False),
                 test.check("description", "some description", case_sensitive=False),
                 test.check("principalObjectId", "aGuid", case_sensitive=False),
             ])


# EXAMPLE: /AccessPolicies/get/AccessPoliciesByEnvironment
@try_manual
def step__accesspolicies_get(test, rg):
    test.cmd('az timeseriesinsights access-policy list '
             '--environment-name "{myEnvironment}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: /AccessPolicies/get/AccessPoliciesGet
@try_manual
def step__accesspolicies_get_accesspoliciesget(test, rg):
    test.cmd('az timeseriesinsights access-policy show '
             '--name "{myAccessPolicy}" '
             '--environment-name "{myEnvironment}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("name", "{myAccessPolicy}", case_sensitive=False),
                 test.check("description", "some description", case_sensitive=False),
                 test.check("principalObjectId", "aGuid", case_sensitive=False),
             ])


# EXAMPLE: /AccessPolicies/patch/AccessPoliciesUpdate
@try_manual
def step__accesspolicies_patch_accesspoliciesupdate(test, rg):
    test.cmd('az timeseriesinsights access-policy update '
             '--name "{myAccessPolicy}" '
             '--roles "Reader" '
             '--roles "Contributor" '
             '--environment-name "{myEnvironment}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("name", "{myAccessPolicy}", case_sensitive=False),
                 test.check("description", "some description", case_sensitive=False),
                 test.check("principalObjectId", "aGuid", case_sensitive=False),
             ])


# EXAMPLE: /AccessPolicies/delete/AccessPoliciesDelete
@try_manual
def step__accesspolicies_delete_accesspoliciesdelete(test, rg):
    test.cmd('az timeseriesinsights access-policy delete -y '
             '--name "{myAccessPolicy}" '
             '--environment-name "{myEnvironment}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /EventSources/put/CreateEventHubEventSource
@try_manual
def step__eventsources_put_createeventhubeventsource(test, rg):
    test.cmd('az timeseriesinsights event-source create '
             '--environment-name "{myEnvironment}" '
             '--name "{myEventSource}" '
             '--event-hub-event-source-create-or-update-parameters location="West US" timestamp-property-name="someTime'
             'stampProperty" event-source-resource-id="somePathInArm" service-bus-namespace="sbn" event-hub-name="ehn" '
             'consumer-group-name="cgn" key-name="managementKey" shared-access-key="someSecretvalue" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("name", "{myEventSource}", case_sensitive=False),
             ])


# EXAMPLE: /EventSources/get/GetEventHubEventSource
@try_manual
def step__eventsources_get_geteventhubeventsource(test, rg):
    test.cmd('az timeseriesinsights event-source show '
             '--environment-name "{myEnvironment}" '
             '--name "{myEventSource}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("name", "{myEventSource}", case_sensitive=False),
             ])


# EXAMPLE: /EventSources/get/ListEventSourcesByEnvironment
@try_manual
def step__eventsources_get(test, rg):
    test.cmd('az timeseriesinsights event-source list '
             '--environment-name "{myEnvironment}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: /EventSources/patch/UpdateEventSource
@try_manual
def step__eventsources_patch_updateeventsource(test, rg):
    test.cmd('az timeseriesinsights event-source update '
             '--environment-name "{myEnvironment}" '
             '--name "{myEventSource}" '
             '--tags someKey="someValue" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("name", "{myEventSource}", case_sensitive=False),
                 test.check("tags.someKey", "someValue", case_sensitive=False),
             ])


# EXAMPLE: /EventSources/delete/DeleteEventSource
@try_manual
def step__eventsources_delete_deleteeventsource(test, rg):
    test.cmd('az timeseriesinsights event-source delete -y '
             '--environment-name "{myEnvironment}" '
             '--name "{myEventSource}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /ReferenceDataSets/put/ReferenceDataSetsCreate
@try_manual
def step__referencedatasets_put(test, rg):
    test.cmd('az timeseriesinsights reference-data-set create '
             '--environment-name "{myEnvironment}" '
             '--location "West US" '
             '--key-properties name="DeviceId1" type="String" '
             '--key-properties name="DeviceFloor" type="Double" '
             '--name "{myReferenceDataSet}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("location", "West US", case_sensitive=False),
                 test.check("name", "{myReferenceDataSet}", case_sensitive=False),
             ])


# EXAMPLE: /ReferenceDataSets/get/ReferenceDataSetsGet
@try_manual
def step__referencedatasets_get_referencedatasetsget(test, rg):
    test.cmd('az timeseriesinsights reference-data-set show '
             '--environment-name "{myEnvironment}" '
             '--name "{myReferenceDataSet}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("location", "West US", case_sensitive=False),
                 test.check("name", "{myReferenceDataSet}", case_sensitive=False),
             ])


# EXAMPLE: /ReferenceDataSets/get/ReferenceDataSetsListByEnvironment
@try_manual
def step__referencedatasets_get(test, rg):
    test.cmd('az timeseriesinsights reference-data-set list '
             '--environment-name "{myEnvironment}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: /ReferenceDataSets/patch/ReferenceDataSetsUpdate
@try_manual
def step__referencedatasets_patch(test, rg):
    test.cmd('az timeseriesinsights reference-data-set update '
             '--environment-name "{myEnvironment}" '
             '--name "{myReferenceDataSet}" '
             '--tags someKey="someValue" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("location", "West US", case_sensitive=False),
                 test.check("name", "{myReferenceDataSet}", case_sensitive=False),
                 test.check("tags.someKey", "someValue", case_sensitive=False),
             ])


# EXAMPLE: /ReferenceDataSets/delete/ReferenceDataSetsDelete
@try_manual
def step__referencedatasets_delete(test, rg):
    test.cmd('az timeseriesinsights reference-data-set delete -y '
             '--environment-name "{myEnvironment}" '
             '--name "{myReferenceDataSet}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Environments/delete/EnvironmentsDelete
@try_manual
def step__environments_delete_environmentsdelete(test, rg):
    test.cmd('az timeseriesinsights environment delete -y '
             '--name "{myEnvironment}" '
             '--resource-group "{rg}"',
             checks=[])


# Env cleanup
@try_manual
def cleanup(test, rg):
    pass


# Testcase
@try_manual
def call_scenario(test, rg):
    setup(test, rg)
    step__environments_put_environmentscreate(test, rg)
    step__environments_get_environmentsbyresourcegroup(test, rg)
    step__environments_get_environmentsbysubscription(test, rg)
    step__environments_get_environmentsget(test, rg)
    step__environments_patch_environmentsupdate(test, rg)
    step__accesspolicies_put_accesspoliciescreate(test, rg)
    step__accesspolicies_get(test, rg)
    step__accesspolicies_get_accesspoliciesget(test, rg)
    step__accesspolicies_patch_accesspoliciesupdate(test, rg)
    step__accesspolicies_delete_accesspoliciesdelete(test, rg)
    step__eventsources_put_createeventhubeventsource(test, rg)
    step__eventsources_get_geteventhubeventsource(test, rg)
    step__eventsources_get(test, rg)
    step__eventsources_patch_updateeventsource(test, rg)
    step__eventsources_delete_deleteeventsource(test, rg)
    step__referencedatasets_put(test, rg)
    step__referencedatasets_get_referencedatasetsget(test, rg)
    step__referencedatasets_get(test, rg)
    step__referencedatasets_patch(test, rg)
    step__referencedatasets_delete(test, rg)
    step__environments_delete_environmentsdelete(test, rg)
    cleanup(test, rg)


@try_manual
class TimeSeriesInsightsClientScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitesttimeseriesinsights_rg1'[:7], key='rg', parameter_name='rg')
    def test_timeseriesinsights(self, rg):

        self.kwargs.update({
            'myEnvironment': 'env1',
            'myEventSource': 'es1',
            'myReferenceDataSet': 'rds1',
            'myAccessPolicy': 'ap1',
        })

        call_scenario(self, rg)
        calc_coverage(__file__)
        raise_if()
