# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .preparers import VirtualNetworkPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class StorageCacheManagementClientScenarioTest(ScenarioTest):

    def current_subscription(self):
        subs = self.cmd('az account show').get_output_in_json()
        return subs['id']

    @ResourceGroupPreparer(name_prefix='cli_test_storagecache_scgroup'[:9], key='rg')
    @VirtualNetworkPreparer(name_prefix='cli_test_storagecache_scvnet'[:9], key='vn', resource_group_key='rg')
    def test_storagecache(self, resource_group):

        self.kwargs.update({
            'subscription_id': self.current_subscription()
        })

        self.kwargs.update({
            'sc1': self.create_random_name(prefix='cli_test_caches'[:9], length=24),
            'Caches_2': self.create_random_name(prefix='cli_test_caches'[:9], length=24),
            'st1': self.create_random_name(prefix='cli_test_storage_targets'[:9], length=24),
        })

        self.cmd('az storagecache cache create '
                 '--location "westus" '
                 '--properties-subnet "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Network/virtualNetworks/{vn}/subnets/default" '
                 '--sku name=Standard_2G '
                 '--tags Dept=Initech '
                 '--cache-name "{sc1}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az storagecache storage-target create '
                 '--cache-name "{sc1}" '
                 '--resource-group "{rg}" '
                 '--storage-target-name "{st1}" '
                 '--properties-junctions namespace-path=/path/on/cache nfs-export=exp1 target-path=/path/on/exp1 '
                 '--properties-junctions namespace-path=/path2/on/cache nfs-export=exp2 target-path=/path2/on/exp2 '
                 '--properties-nfs3 target=10.0.44.44 usage-model=READ_HEAVY_INFREQ '
                 '--properties-target-type "nfs3"',
                 checks=[])

        self.cmd('az storagecache storage-target show '
                 '--cache-name "{sc1}" '
                 '--resource-group "{rg}" '
                 '--storage-target-name "{st1}"',
                 checks=[])

        self.cmd('az storagecache cache show '
                 '--cache-name "{sc1}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az storagecache storage-target list '
                 '--cache-name "{sc1}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az storagecache cache list '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az storagecache usage-model list',
                 checks=[])

        self.cmd('az storagecache cache list',
                 checks=[])

        self.cmd('az storagecache sku list',
                 checks=[])

        self.cmd('az storagecache cache upgrade-firmware '
                 '--cache-name "{sc1}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az storagecache cache flush '
                 '--cache-name "{Caches_2}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az storagecache cache start '
                 '--cache-name "{Caches_2}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az storagecache cache stop '
                 '--cache-name "{Caches_2}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az storagecache cache update '
                 '--location "westus" '
                 '--properties-subnet "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Network/virtualNetworks/{vn}/subnets/default" '
                 '--sku name=Standard_2G '
                 '--tags Dept=Initech '
                 '--cache-name "{sc1}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az storagecache storage-target delete '
                 '--cache-name "{sc1}" '
                 '--resource-group "{rg}" '
                 '--storage-target-name "{st1}"',
                 checks=[])

        self.cmd('az storagecache cache delete '
                 '--cache-name "{Caches_2}" '
                 '--resource-group "{rg}"',
                 checks=[])
