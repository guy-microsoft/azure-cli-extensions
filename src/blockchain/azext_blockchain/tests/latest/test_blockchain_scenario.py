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
def setup(test, rg):
    pass


# EXAMPLE: /BlockchainMemberOperationResults/get/BlockchainMemberOperationResults_Get
@try_manual
def step__blockchainmemberoperationresults_get_blockchainmemberoperationresults_get(test, rg):
    test.cmd('az blockchain blockchain-member-operation-result show '
             '--operation-id "12f4b309-01e3-4fcf-bc0b-1cc034ca03f8" '
             '--location-name "{southeastasia}"',
             checks=[])


# EXAMPLE: /BlockchainMembers/put/BlockchainMembers_Create
@try_manual
def step__blockchainmembers_put_blockchainmembers_create(test, rg):
    test.cmd('az blockchain blockchain-member create '
             '--location "southeastasia" '
             '--consortium "ContoseConsortium" '
             '--consortium-management-account-password "1234abcdEFG1" '
             '--password "1234abcdEFG1" '
             '--validator-nodes-sku capacity=2 '
             '--protocol "Quorum" '
             '--blockchain-member-name "{contosemember1}" '
             '--resource-group "{rg}"',
             checks=[])
    test.cmd('az blockchain blockchain-member wait --created '
             '--blockchain-member-name "{contosemember1}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /BlockchainMembers/get/BlockchainMembers_Get
@try_manual
def step__blockchainmembers_get_blockchainmembers_get(test, rg):
    test.cmd('az blockchain blockchain-member show '
             '--blockchain-member-name "{contosemember1}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /BlockchainMembers/get/BlockchainMembers_List
@try_manual
def step__blockchainmembers_get_blockchainmembers_list(test, rg):
    test.cmd('az blockchain blockchain-member list '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /BlockchainMembers/get/BlockchainMembers_ListAll
@try_manual
def step__blockchainmembers_get_blockchainmembers_listall(test, rg):
    test.cmd('az blockchain blockchain-member list-all',
             checks=[])


# EXAMPLE: /BlockchainMembers/get/BlockchainMembers_ListConsortiumMembers
@try_manual
def step__blockchainmembers_get_blockchainmembers_listconsortiummembers(test, rg):
    test.cmd('az blockchain blockchain-member list-consortium-member '
             '--blockchain-member-name "{contosemember1}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /BlockchainMembers/post/BlockchainMembers_ListApiKeys
@try_manual
def step__blockchainmembers_post_blockchainmembers_listapikeys(test, rg):
    test.cmd('az blockchain blockchain-member list-api-key '
             '--blockchain-member-name "{contosemember1}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /BlockchainMembers/post/BlockchainMembers_ListRegenerateApiKeys
@try_manual
def step__blockchainmembers_post_blockchainmembers_listregenerateapikeys(test, rg):
    test.cmd('az blockchain blockchain-member regenerate-api-key '
             '--key-name "key1" '
             '--blockchain-member-name "{contosemember1}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /BlockchainMembers/patch/BlockchainMembers_Update
@try_manual
def step__blockchainmembers_patch_blockchainmembers_update(test, rg):
    test.cmd('az blockchain blockchain-member update '
             '--consortium-management-account-password "1234abcdEFG1" '
             '--password "1234abcdEFG1" '
             '--blockchain-member-name "{BlockchainMembers_2}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Locations/post/Locations_ListConsortiums
@try_manual
def step__locations_post_locations_listconsortiums(test, rg):
    test.cmd('az blockchain consortium list '
             '--location-name "{southeastasia}"',
             checks=[])


# EXAMPLE: /Skus/get/Skus_List
@try_manual
def step__skus_get_skus_list(test, rg):
    test.cmd('az blockchain sku list',
             checks=[])


# EXAMPLE: /TransactionNodes/put/TransactionNodes_Create
@try_manual
def step__transactionnodes_put_transactionnodes_create(test, rg):
    test.cmd('az blockchain transaction-node create '
             '--blockchain-member-name "{contosemember1}" '
             '--resource-group "{rg}" '
             '--location "southeastasia" '
             '--password "1234abcdEFG1" '
             '--transaction-node-name "{txnode2}"',
             checks=[])
    test.cmd('az blockchain transaction-node wait --created '
             '--resource-group "{rg}" '
             '--transaction-node-name "{txnode2}"',
             checks=[])


# EXAMPLE: /TransactionNodes/get/TransactionNodes_Get
@try_manual
def step__transactionnodes_get_transactionnodes_get(test, rg):
    test.cmd('az blockchain transaction-node show '
             '--blockchain-member-name "{contosemember1}" '
             '--resource-group "{rg}" '
             '--transaction-node-name "{txnode2}"',
             checks=[])


# EXAMPLE: /TransactionNodes/get/TransactionNodes_List
@try_manual
def step__transactionnodes_get_transactionnodes_list(test, rg):
    test.cmd('az blockchain transaction-node list '
             '--blockchain-member-name "{contosemember1}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /TransactionNodes/post/TransactionNodes_ListApiKeys
@try_manual
def step__transactionnodes_post_transactionnodes_listapikeys(test, rg):
    test.cmd('az blockchain transaction-node list-api-key '
             '--blockchain-member-name "{contosemember1}" '
             '--resource-group "{rg}" '
             '--transaction-node-name "{txnode2}"',
             checks=[])


# EXAMPLE: /TransactionNodes/post/TransactionNodes_ListRegenerateApiKeys
@try_manual
def step__transactionnodes_post_transactionnodes_listregenerateapikeys(test, rg):
    test.cmd('az blockchain transaction-node regenerate-api-key '
             '--key-name "key1" '
             '--blockchain-member-name "{contosemember1}" '
             '--resource-group "{rg}" '
             '--transaction-node-name "{txnode2}"',
             checks=[])


# EXAMPLE: /TransactionNodes/patch/TransactionNodes_Update
@try_manual
def step__transactionnodes_patch_transactionnodes_update(test, rg):
    test.cmd('az blockchain transaction-node update '
             '--blockchain-member-name "{contosemember1}" '
             '--resource-group "{rg}" '
             '--password "1234abcdEFG1" '
             '--transaction-node-name "{txnode2}"',
             checks=[])


# EXAMPLE: /TransactionNodes/delete/TransactionNodes_Delete
@try_manual
def step__transactionnodes_delete_transactionnodes_delete(test, rg):
    test.cmd('az blockchain transaction-node delete '
             '--blockchain-member-name "{contosemember1}" '
             '--resource-group "{rg}" '
             '--transaction-node-name "{TransactionNodes_2}"',
             checks=[])


# EXAMPLE: /BlockchainMembers/delete/BlockchainMembers_Delete
@try_manual
def step__blockchainmembers_delete_blockchainmembers_delete(test, rg):
    test.cmd('az blockchain blockchain-member delete '
             '--blockchain-member-name "{contosemember1}" '
             '--resource-group "{rg}"',
             checks=[])


@try_manual
def cleanup(test, rg):
    pass


@try_manual
def call_scenario(test, rg):
    setup(test, rg)
    step__blockchainmemberoperationresults_get_blockchainmemberoperationresults_get(test, rg)
    step__blockchainmembers_put_blockchainmembers_create(test, rg)
    step__blockchainmembers_get_blockchainmembers_get(test, rg)
    step__blockchainmembers_get_blockchainmembers_list(test, rg)
    step__blockchainmembers_get_blockchainmembers_listall(test, rg)
    step__blockchainmembers_get_blockchainmembers_listconsortiummembers(test, rg)
    step__blockchainmembers_post_blockchainmembers_listapikeys(test, rg)
    step__blockchainmembers_post_blockchainmembers_listregenerateapikeys(test, rg)
    step__blockchainmembers_patch_blockchainmembers_update(test, rg)
    step__locations_post_locations_listconsortiums(test, rg)
    step__skus_get_skus_list(test, rg)
    step__transactionnodes_put_transactionnodes_create(test, rg)
    step__transactionnodes_get_transactionnodes_get(test, rg)
    step__transactionnodes_get_transactionnodes_list(test, rg)
    step__transactionnodes_post_transactionnodes_listapikeys(test, rg)
    step__transactionnodes_post_transactionnodes_listregenerateapikeys(test, rg)
    step__transactionnodes_patch_transactionnodes_update(test, rg)
    step__transactionnodes_delete_transactionnodes_delete(test, rg)
    step__blockchainmembers_delete_blockchainmembers_delete(test, rg)
    cleanup(test, rg)


@try_manual
class BlockchainManagementClientScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestblockchain_mygroup'[:7], key='rg', parameter_name='rg')
    def test_blockchain(self, rg):

        self.kwargs.update({
            'contosemember1': 'contosemember1',
            'BlockchainMembers_2': 'BlockchainMembers_2',
            'southeastasia': 'southeastasia',
            'txnode2': 'txnode2',
            'TransactionNodes_2': 'TransactionNodes_2',
        })

        call_scenario(self, rg)
