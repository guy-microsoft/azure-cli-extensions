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
from .. import try_manual, raise_if
from azure.cli.testsdk import ResourceGroupPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


@try_manual
def setup(test, rg, rg_2, rg_3, rg_4, rg_5):
    pass


# EXAMPLE: /Projects/put/Projects_Create
@try_manual
def step__projects_put_projects_create(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate project create '
             '--e-tag "" '
             '--location "West Europe" '
             '--properties assessment-solution-id="/subscriptions/{subscription_id}/resourcegroups/{rg}/providers/micro'
             'soft.migrate/migrateprojects/abgoyalweselfhost/Solutions/Servers-Assessment-ServerAssessment" customer-wo'
             'rkspace-id=null customer-workspace-location=null project-status="Active" '
             '--tags "{{}}" '
             '--name "{abGoyalProject2}" '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /Projects/get/Projects_Get
@try_manual
def step__projects_get_projects_get(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate project show '
             '--name "{Projects_2}" '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /Projects/get/Projects_List
@try_manual
def step__projects_get_projects_list(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate project list '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /Projects/get/Projects_List
@try_manual
def step__projects_get_projects_list(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate project list '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /Projects/patch/Projects_Update
@try_manual
def step__projects_patch_projects_update(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate project update '
             '--e-tag "" '
             '--location "West Europe" '
             '--properties assessment-solution-id="/subscriptions/{subscription_id}/resourcegroups/{rg}/providers/micro'
             'soft.migrate/migrateprojects/abgoyalweselfhost/Solutions/Servers-Assessment-ServerAssessment" customer-wo'
             'rkspace-id=null customer-workspace-location=null project-status="Active" '
             '--tags "{{}}" '
             '--name "{abGoyalProject2}" '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /Groups/put/Groups_Create
@try_manual
def step__groups_put_groups_create(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate group create '
             '--e-tag "\\"1e000c2c-0000-0d00-0000-5cdaa4190000\\"" '
             '--name "{Group2}" '
             '--project-name "{Projects_2}" '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /Groups/get/Groups_Get
@try_manual
def step__groups_get_groups_get(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate group show '
             '--name "{Groups_2}" '
             '--project-name "{Projects_2}" '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /Groups/get/Groups_ListByProject
@try_manual
def step__groups_get_groups_listbyproject(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate group list '
             '--project-name "{Projects_2}" '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /Groups/post/Groups_UpdateMachines
@try_manual
def step__groups_post_groups_updatemachines(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate group update-machine '
             '--e-tag "\\"1e000c2c-0000-0d00-0000-5cdaa4190000\\"" '
             '--properties machines="/subscriptions/{subscription_id}/resourceGroups/{rg_2}/providers/Microsoft.Migrate'
             '/assessmentprojects/project01/machines/{amansing_vm1}" operation-type="Add" '
             '--name "{Group2}" '
             '--project-name "{Projects_2}" '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /Assessments/put/Assessments_Create
@try_manual
def step__assessments_put_assessments_create(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate assessment create '
             '--e-tag "\\"1e000c2c-0000-0d00-0000-5cdaa4190000\\"" '
             '--azure-disk-type "StandardOrPremium" '
             '--azure-hybrid-use-benefit "Yes" '
             '--azure-location "NorthEurope" '
             '--azure-offer-code "MSAZR0003P" '
             '--azure-pricing-tier "Standard" '
             '--azure-storage-redundancy "LocallyRedundant" '
             '--azure-vm-families "[\\"Dv2_series\\",\\"F_series\\",\\"Dv3_series\\",\\"DS_series\\",\\"DSv2_series\\",'
             '\\"Fs_series\\",\\"Dsv3_series\\",\\"Ev3_series\\",\\"Esv3_series\\",\\"D_series\\",\\"M_series\\",\\"Fsv'
             '2_series\\",\\"H_series\\"]" '
             '--currency "USD" '
             '--discount-percentage 100 '
             '--percentile "Percentile95" '
             '--reserved-instance "RI3Year" '
             '--scaling-factor 1 '
             '--sizing-criterion "PerformanceBased" '
             '--stage "InProgress" '
             '--time-range "Day" '
             '--vm-uptime days-per-month=31 hours-per-day=24 '
             '--name "{assessment_5_14_2019_16_48_47}" '
             '--group-name "{Group2}" '
             '--project-name "{Projects_2}" '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /Assessments/get/Assessments_Get
@try_manual
def step__assessments_get_assessments_get(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate assessment show '
             '--name "{Assessments_2}" '
             '--group-name "{Groups_2}" '
             '--project-name "{Projects_2}" '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /Assessments/get/Assessments_ListByGroup
@try_manual
def step__assessments_get_assessments_listbygroup(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate assessment list '
             '--group-name "{Groups_2}" '
             '--project-name "{Projects_2}" '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /Assessments/get/Assessments_ListByProject
@try_manual
def step__assessments_get_assessments_listbyproject(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate assessment list '
             '--project-name "{Projects_2}" '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /Assessments/post/Assessments_GetReportDownloadUrl
@try_manual
def step__assessments_post_assessments_getreportdownloadurl(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate assessment get-report-download-url '
             '--name "{Assessments_2}" '
             '--group-name "{Groups_2}" '
             '--project-name "{Projects_2}" '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /AssessedMachines/get/AssessedMachines_Get
@try_manual
def step__assessedmachines_get_assessedmachines_get(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate assessed-machine show '
             '--name "{f57fe432-3bd2-486a-a83a-6f4d99f1a952}" '
             '--assessment-name "{Assessments_2}" '
             '--group-name "{Groups_2}" '
             '--project-name "{Projects_2}" '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /AssessedMachines/get/AssessedMachines_ListByAssessment
@try_manual
def step__assessedmachines_get_assessedmachines_listbyassessment(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate assessed-machine list '
             '--assessment-name "{Assessments_2}" '
             '--group-name "{Groups_2}" '
             '--project-name "{Projects_2}" '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /Assessments/delete/Assessments_Delete
@try_manual
def step__assessments_delete_assessments_delete(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate assessment delete '
             '--name "{Assessments_2}" '
             '--group-name "{Groups_2}" '
             '--project-name "{Projects_2}" '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /HyperVCollectors/put/HyperVCollectors_Create
@try_manual
def step__hypervcollectors_put_hypervcollectors_create(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate hyper-v-collector create '
             '--e-tag "\\"00000981-0000-0300-0000-5d74cd5f0000\\"" '
             '--agent-properties-spn-details application-id="827f1053-44dc-439f-b832-05416dcce12b" audience="https://72'
             'f988bf-86f1-41af-91ab-2d7cd011db47/migrateprojectce73agentauthaadapp" authority="https://login.windows.ne'
             't/72f988bf-86f1-41af-91ab-2d7cd011db47" object-id="be75098e-c0fc-4ac4-98c7-282ebbcf8370" tenant-id="72f98'
             '8bf-86f1-41af-91ab-2d7cd011db47" '
             '--discovery-site-id "/subscriptions/{subscription_id}/resourceGroups/{rg_3}/providers/Microsoft.OffAzure/'
             'HyperVSites/migrateprojectce73site" '
             '--name "{migrateprojectce73collector}" '
             '--project-name "{Projects_3}" '
             '--resource-group "{rg_5}"',
             checks=[])


# EXAMPLE: /HyperVCollectors/get/HyperVCollectors_Get
@try_manual
def step__hypervcollectors_get_hypervcollectors_get(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate hyper-v-collector show '
             '--name "{migrateprojectce73collector}" '
             '--project-name "{Projects_3}" '
             '--resource-group "{rg_5}"',
             checks=[])


# EXAMPLE: /HyperVCollectors/get/HyperVCollectors_ListByProject
@try_manual
def step__hypervcollectors_get_hypervcollectors_listbyproject(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate hyper-v-collector list '
             '--project-name "{Projects_3}" '
             '--resource-group "{rg_5}"',
             checks=[])


# EXAMPLE: /Machines/get/Machines_Get
@try_manual
def step__machines_get_machines_get(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate machine show '
             '--name "{Machines_2}" '
             '--project-name "{Projects_2}" '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /Machines/get/Machines_ListByProject
@try_manual
def step__machines_get_machines_listbyproject(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate machine list '
             '--project-name "{Projects_2}" '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /Project/get/AssessmentOptions_Get
@try_manual
def step__project_get_assessmentoptions_get(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate project assessment-option '
             '--assessment-options-name "default" '
             '--name "{Projects_2}" '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /Project/get/AssessmentOptions_Get
@try_manual
def step__project_get_assessmentoptions_get(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate project assessment-option '
             '--assessment-options-name "default" '
             '--name "{Projects_2}" '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /VMwareCollectors/put/VMwareCollectors_Create
@try_manual
def step__vmwarecollectors_put_vmwarecollectors_create(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate v-mware-collector create '
             '--e-tag "\\"01003d32-0000-0d00-0000-5d74d2e50000\\"" '
             '--agent-properties-spn-details application-id="fc717575-8173-4b21-92a5-658b655e613e" audience="https://72'
             'f988bf-86f1-41af-91ab-2d7cd011db47/PortalvCenterbc2fagentauthaadapp" authority="https://login.windows.net'
             '/72f988bf-86f1-41af-91ab-2d7cd011db47" object-id="29d94f38-db94-4980-aec0-0cfd55ab1cd0" tenant-id="72f988'
             'bf-86f1-41af-91ab-2d7cd011db47" '
             '--discovery-site-id "/subscriptions/{subscription_id}/resourceGroups/{rg_4}/providers/Microsoft.OffAzure/'
             'VMwareSites/PortalvCenterbc2fsite" '
             '--project-name "{Projects_2}" '
             '--resource-group "{rg_4}" '
             '--name "{PortalvCenterbc2fcollector}"',
             checks=[])


# EXAMPLE: /VMwareCollectors/get/VMwareCollectors_Get
@try_manual
def step__vmwarecollectors_get_vmwarecollectors_get(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate v-mware-collector show '
             '--project-name "{Projects_2}" '
             '--resource-group "{rg_4}" '
             '--name "{PortalvCenterbc2fcollector}"',
             checks=[])


# EXAMPLE: /VMwareCollectors/get/VMwareCollectors_ListByProject
@try_manual
def step__vmwarecollectors_get_vmwarecollectors_listbyproject(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate v-mware-collector list '
             '--project-name "{Projects_2}" '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /Groups/delete/Groups_Delete
@try_manual
def step__groups_delete_groups_delete(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate group delete '
             '--name "{Groups_2}" '
             '--project-name "{Projects_2}" '
             '--resource-group "{rg_4}"',
             checks=[])


# EXAMPLE: /HyperVCollectors/delete/HyperVCollectors_Delete
@try_manual
def step__hypervcollectors_delete_hypervcollectors_delete(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate hyper-v-collector delete '
             '--name "{migrateprojectce73collector}" '
             '--project-name "{Projects_3}" '
             '--resource-group "{rg_5}"',
             checks=[])


# EXAMPLE: /VMwareCollectors/delete/VMwareCollectors_Delete
@try_manual
def step__vmwarecollectors_delete_vmwarecollectors_delete(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate v-mware-collector delete '
             '--project-name "{Projects_2}" '
             '--resource-group "{rg_4}" '
             '--name "{PortalvCenterbc2fcollector}"',
             checks=[])


# EXAMPLE: /Projects/delete/Projects_Delete
@try_manual
def step__projects_delete_projects_delete(test, rg, rg_2, rg_3, rg_4, rg_5):
    test.cmd('az migrate project delete '
             '--name "{abGoyalProject2}" '
             '--resource-group "{rg_4}"',
             checks=[])


@try_manual
def cleanup(test, rg, rg_2, rg_3, rg_4, rg_5):
    pass


@try_manual
def call_scenario(test, rg, rg_2, rg_3, rg_4, rg_5):
    setup(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__projects_put_projects_create(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__projects_get_projects_get(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__projects_get_projects_list(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__projects_get_projects_list(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__projects_patch_projects_update(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__groups_put_groups_create(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__groups_get_groups_get(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__groups_get_groups_listbyproject(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__groups_post_groups_updatemachines(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__assessments_put_assessments_create(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__assessments_get_assessments_get(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__assessments_get_assessments_listbygroup(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__assessments_get_assessments_listbyproject(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__assessments_post_assessments_getreportdownloadurl(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__assessedmachines_get_assessedmachines_get(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__assessedmachines_get_assessedmachines_listbyassessment(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__assessments_delete_assessments_delete(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__hypervcollectors_put_hypervcollectors_create(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__hypervcollectors_get_hypervcollectors_get(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__hypervcollectors_get_hypervcollectors_listbyproject(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__machines_get_machines_get(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__machines_get_machines_listbyproject(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__project_get_assessmentoptions_get(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__project_get_assessmentoptions_get(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__vmwarecollectors_put_vmwarecollectors_create(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__vmwarecollectors_get_vmwarecollectors_get(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__vmwarecollectors_get_vmwarecollectors_listbyproject(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__groups_delete_groups_delete(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__hypervcollectors_delete_hypervcollectors_delete(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__vmwarecollectors_delete_vmwarecollectors_delete(test, rg, rg_2, rg_3, rg_4, rg_5)
    step__projects_delete_projects_delete(test, rg, rg_2, rg_3, rg_4, rg_5)
    cleanup(test, rg, rg_2, rg_3, rg_4, rg_5)


@try_manual
class AzureMigrateV2ScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestmigrate_abgoyal-westeurope'[:7], key='rg', parameter_name='rg')
    @ResourceGroupPreparer(name_prefix='clitestmigrate_myResourceGroup'[:7], key='rg_2', parameter_name='rg_2')
    @ResourceGroupPreparer(name_prefix='clitestmigrate_ContosoITHyperV'[:7], key='rg_3', parameter_name='rg_3')
    @ResourceGroupPreparer(name_prefix='clitestmigrate_abgoyal-westEurope'[:7], key='rg_4', parameter_name='rg_4')
    @ResourceGroupPreparer(name_prefix='clitestmigrate_contosoithyperv'[:7], key='rg_5', parameter_name='rg_5')
    def test_migrate(self, rg, rg_2, rg_3, rg_4, rg_5):

        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'abGoyalProject2': 'abGoyalProject2',
            'Projects_2': 'abgoyalWEselfhostb72bproject',
            'Projects_3': 'migrateprojectce73project',
            'amansing_vm1': 'amansing_vm1',
            'Machines_2': '269ef295-a38d-4f8f-9779-77ce79088311',
            'Group2': 'Group2',
            'Groups_2': 'Test1',
            'assessment_5_14_2019_16_48_47': 'assessment_5_14_2019_16_48_47',
            'Assessments_2': 'assessment_5_9_2019_16_22_14',
            'f57fe432-3bd2-486a-a83a-6f4d99f1a952': 'f57fe432-3bd2-486a-a83a-6f4d99f1a952',
            'migrateprojectce73collector': 'migrateprojectce73collector',
            'PortalvCenterbc2fcollector': 'PortalvCenterbc2fcollector',
        })

        call_scenario(self, rg, rg_2, rg_3, rg_4, rg_5)
        raise_if()
