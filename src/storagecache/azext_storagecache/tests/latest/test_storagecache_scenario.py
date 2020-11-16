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
from .preparers import VirtualNetworkPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup
@try_manual
def setup(test, rg):
    pass


# EXAMPLE: /AscOperations/get/AscOperations_Get
@try_manual
def step__ascoperations_get_ascoperations_get(test, rg):
    test.cmd('az storagecache asc-operation show '
             '--operation-id "testoperationid" '
             '--location "West US"',
             checks=[])


# EXAMPLE: /Caches/put/Caches_CreateOrUpdate
@try_manual
def step__caches_put_caches_createorupdate(test, rg):
    test.cmd('az storagecache cache create '
             '--location "westus" '
             '--cache-size-gb 3072 '
             '--subnet "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Network/virtualNetwork'
             's/{vn}/subnets/default" '
             '--sku-name "Standard_2G" '
             '--tags "{{\\"Dept\\":\\"ContosoAds\\"}}" '
             '--cache-name "sc1" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Caches/get/Caches_Get
@try_manual
def step__caches_get_caches_get(test, rg):
    test.cmd('az storagecache cache show '
             '--cache-name "sc1" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Caches/get/Caches_List
@try_manual
def step__caches_get_caches_list(test, rg):
    test.cmd('az storagecache cache list '
             '-g ""',
             checks=[])


# EXAMPLE: /Caches/get/Caches_ListByResourceGroup
@try_manual
def step__caches_get_caches_listbyresourcegroup(test, rg):
    test.cmd('az storagecache cache list '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Caches/patch/Caches_Update
@try_manual
def step__caches_patch_caches_update(test, rg):
    test.cmd('az storagecache cache update '
             '--location "westus" '
             '--cache-size-gb 3072 '
             '--subnet "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Network/virtualNetwork'
             's/{vn}/subnets/default" '
             '--sku-name "Standard_2G" '
             '--tags "{{\\"Dept\\":\\"ContosoAds\\"}}" '
             '--cache-name "sc1" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Caches/post/Caches_Flush
@try_manual
def step__caches_post_caches_flush(test, rg):
    test.cmd('az storagecache cache flush '
             '--cache-name "sc" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Caches/post/Caches_Start
@try_manual
def step__caches_post_caches_start(test, rg):
    test.cmd('az storagecache cache start '
             '--cache-name "sc" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Caches/post/Caches_Stop
@try_manual
def step__caches_post_caches_stop(test, rg):
    test.cmd('az storagecache cache stop '
             '--cache-name "sc" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Caches/post/Caches_UpgradeFirmware
@try_manual
def step__caches_post_caches_upgradefirmware(test, rg):
    test.cmd('az storagecache cache upgrade-firmware '
             '--cache-name "sc1" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Caches/delete/Caches_Delete
@try_manual
def step__caches_delete_caches_delete(test, rg):
    test.cmd('az storagecache cache delete -y '
             '--cache-name "sc" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Skus/get/Skus_List
@try_manual
def step__skus_get_skus_list(test, rg):
    test.cmd('az storagecache sku list',
             checks=[])


# EXAMPLE: /StorageTargets/put/StorageTargets_CreateOrUpdate
@try_manual
def step__storagetargets_put(test, rg):
    test.cmd('az storagecache storage-target create '
             '--cache-name "sc1" '
             '--resource-group "{rg}" '
             '--name "{myStorageTarget}" '
             '--junctions namespace-path="/path/on/cache" nfs-export="exp1" target-path="/path/on/exp1" '
             '--junctions namespace-path="/path2/on/cache" nfs-export="exp2" target-path="/path2/on/exp2" '
             '--nfs3 target="10.0.44.44" usage-model="READ_HEAVY_INFREQ"',
             checks=[
                 test.check("name", "{myStorageTarget}", case_sensitive=False),
                 test.check("nfs3.target", "10.0.44.44", case_sensitive=False),
                 test.check("nfs3.usageModel", "READ_HEAVY_INFREQ", case_sensitive=False),
             ])
    test.cmd('az storagecache storage-target wait --created '
             '--resource-group "{rg}" '
             '--name "{myStorageTarget}"',
             checks=[])


# EXAMPLE: /StorageTargets/get/StorageTargets_Get
@try_manual
def step__storagetargets_get_storagetargets_get(test, rg):
    test.cmd('az storagecache storage-target show '
             '--cache-name "sc1" '
             '--resource-group "{rg}" '
             '--name "{myStorageTarget}"',
             checks=[
                 test.check("name", "{myStorageTarget}", case_sensitive=False),
             ])


# EXAMPLE: /StorageTargets/get/StorageTargets_List
@try_manual
def step__storagetargets_get_storagetargets_list(test, rg):
    test.cmd('az storagecache storage-target list '
             '--cache-name "sc1" '
             '--resource-group "{rg}"',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: /StorageTargets/delete/StorageTargets_Delete
@try_manual
def step__storagetargets_delete_storagetargets_delete(test, rg):
    test.cmd('az storagecache storage-target delete -y '
             '--cache-name "sc1" '
             '--resource-group "{rg}" '
             '--name "{myStorageTarget}"',
             checks=[])


# EXAMPLE: /UsageModels/get/UsageModels_List
@try_manual
def step__usagemodels_get_usagemodels_list(test, rg):
    test.cmd('az storagecache usage-model list',
             checks=[])


# Env cleanup
@try_manual
def cleanup(test, rg):
    pass


# Testcase
@try_manual
def call_scenario(test, rg):
    setup(test, rg)
    step__ascoperations_get_ascoperations_get(test, rg)
    step__caches_put_caches_createorupdate(test, rg)
    step__caches_get_caches_get(test, rg)
    step__caches_get_caches_list(test, rg)
    step__caches_get_caches_listbyresourcegroup(test, rg)
    step__caches_patch_caches_update(test, rg)
    step__caches_post_caches_flush(test, rg)
    step__caches_post_caches_start(test, rg)
    step__caches_post_caches_stop(test, rg)
    step__caches_post_caches_upgradefirmware(test, rg)
    step__caches_delete_caches_delete(test, rg)
    step__skus_get_skus_list(test, rg)
    step__storagetargets_put(test, rg)
    step__storagetargets_get_storagetargets_get(test, rg)
    step__storagetargets_get_storagetargets_list(test, rg)
    step__storagetargets_delete_storagetargets_delete(test, rg)
    step__usagemodels_get_usagemodels_list(test, rg)
    cleanup(test, rg)


@try_manual
class StorageCacheManagementClientScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cliteststoragecache_scgroup'[:7], key='rg', parameter_name='rg')
    @VirtualNetworkPreparer(name_prefix='cliteststoragecache_scvnet'[:7], key='vn', resource_group_key='rg')
    def test_storagecache(self, rg):

        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myStorageTarget': 'st1',
        })

        call_scenario(self, rg)
        calc_coverage(__file__)
        raise_if()
