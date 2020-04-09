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


class KustoManagementClientScenarioTest(ScenarioTest):

    def current_subscription(self):
        subs = self.cmd('az account show').get_output_in_json()
        return subs['id']

    @ResourceGroupPreparer(name_prefix='cli_test_kusto_kustorptest'[:9], key='rg')
    def test_kusto(self, resource_group):

        self.kwargs.update({
            'subscription_id': self.current_subscription()
        })

        self.kwargs.update({
            'KustoClusterLeader': self.create_random_name(prefix='cli_test_clusters'[:9], length=24),
            'Clusters_3': self.create_random_name(prefix='cli_test_clusters'[:9], length=24),
            'Clusters_2': self.create_random_name(prefix='cli_test_clusters'[:9], length=24),
            'Clusters_4': self.create_random_name(prefix='cli_test_clusters'[:9], length=24),
            'KustoDatabase8': self.create_random_name(prefix='cli_test_databases'[:9], length=24),
            'Databases_2': self.create_random_name(prefix='cli_test_databases'[:9], length=24),
            'Databases_3': self.create_random_name(prefix='cli_test_databases'[:9], length=24),
            'Databases_4': self.create_random_name(prefix='cli_test_databases'[:9], length=24),
            'attachedDatabaseConfigurations1': self.create_random_name(prefix='cli_test_attached_database_configurations'[:9], length=24),
            'AttachedDatabaseConfigurations_2': self.create_random_name(prefix='cli_test_attached_database_configurations'[:9], length=24),
            'DataConnections8': self.create_random_name(prefix='cli_test_data_connections'[:9], length=24),
            'DataConnections_2': self.create_random_name(prefix='cli_test_data_connections'[:9], length=24),
        })

        self.cmd('az kusto cluster create '
                 '--cluster-name "{Clusters_2}" '
                 '--identity "{{\\"type\\":\\"SystemAssigned\\"}}" '
                 '--location "westus" '
                 '--properties-enable-purge true '
                 '--properties-enable-streaming-ingest true '
                 '--properties-key-vault-properties key-name=keyName key-vault-uri=https://dummy.keyvault.com key-version=keyVersion '
                 '--sku name=Standard_L8s capacity=2 tier=Standard '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto database create '
                 '--cluster-name "{Clusters_2}" '
                 '--database-name "{KustoDatabase8}" '
                 '--location "westus" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto data-connection create '
                 '--cluster-name "{Clusters_2}" '
                 '--data-connection-name "{DataConnections8}" '
                 '--database-name "{KustoDatabase8}" '
                 '--kind "EventHub" '
                 '--location "westus" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto attached-database-configuration create '
                 '--attached-database-configuration-name "{attachedDatabaseConfigurations1}" '
                 '--cluster-name "{Clusters_2}" '
                 '--location "westus" '
                 '--properties-cluster-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Kusto/Clusters/{KustoClusterLeader}" '
                 '--properties-database-name "{Databases_2}" '
                 '--properties-default-principals-modification-kind "Union" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto attached-database-configuration show '
                 '--attached-database-configuration-name "{attachedDatabaseConfigurations1}" '
                 '--cluster-name "{Clusters_2}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto data-connection show '
                 '--cluster-name "{Clusters_2}" '
                 '--data-connection-name "{DataConnections8}" '
                 '--database-name "{KustoDatabase8}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto database list '
                 '--cluster-name "{Clusters_2}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto data-connection list '
                 '--cluster-name "{Clusters_2}" '
                 '--database-name "{KustoDatabase8}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto attached-database-configuration list '
                 '--cluster-name "{Clusters_2}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto database show '
                 '--cluster-name "{Clusters_2}" '
                 '--database-name "{KustoDatabase8}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto database list '
                 '--cluster-name "{Clusters_2}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto data-connection list '
                 '--cluster-name "{Clusters_2}" '
                 '--database-name "{KustoDatabase8}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto cluster list '
                 '--cluster-name "{Clusters_2}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto cluster show '
                 '--cluster-name "{Clusters_2}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto cluster list '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto cluster list',
                 checks=[])

        self.cmd('az kusto cluster list',
                 checks=[])

        # EXAMPLE NOT FOUND: KustoOperationsList

        self.cmd('az kusto data-connection update '
                 '--cluster-name "{Clusters_2}" '
                 '--data-connection-name "{DataConnections8}" '
                 '--database-name "{KustoDatabase8}" '
                 '--kind "EventHub" '
                 '--location "westus" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto data-connection data-connection-validation '
                 '--cluster-name "{Clusters_2}" '
                 '--database-name "{KustoDatabase8}" '
                 '--data-connection-name "{DataConnections8}" '
                 '--properties "{{\\"consumerGroup\\":\\"testConsumerGroup1\\",\\"eventHubResourceId\\":\\"/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.EventHub/namespaces/eventhubTestns1/eventhubs/eventhubTest1\\",\\"kind\\":\\"EventHub\\"}}" '
                 '--resource-group "{rg}"',
                 checks=[])

        # EXAMPLE NOT FOUND: KustoDataConnectionsCheckNameAvailability

        self.cmd('az kusto database remove-principal '
                 '--cluster-name "{Clusters_2}" '
                 '--database-name "{Databases_3}" '
                 '--value name=Some User=undefined type=User app-id= email=user@microsoft.com fqn=aaduser role=Admin '
                 '--value name=Kusto type=Group app-id= email=kusto@microsoft.com fqn=aadgroup role=Viewer '
                 '--value name=SomeApp type=App app-id=some_guid_app_id email= fqn=aadapp role=Admin '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto database list-principal '
                 '--cluster-name "{Clusters_2}" '
                 '--database-name "{Databases_3}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto database add-principal '
                 '--cluster-name "{Clusters_2}" '
                 '--database-name "{Databases_3}" '
                 '--value name=Some User=undefined type=User app-id= email=user@microsoft.com fqn=aaduser role=Admin '
                 '--value name=Kusto type=Group app-id= email=kusto@microsoft.com fqn=aadgroup role=Viewer '
                 '--value name=SomeApp type=App app-id=some_guid_app_id email= fqn=aadapp role=Admin '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto database update '
                 '--cluster-name "{Clusters_2}" '
                 '--database-name "{KustoDatabase8}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto cluster detach-follower-database '
                 '--cluster-name "{Clusters_2}" '
                 '--attached-database-configuration-name "{AttachedDatabaseConfigurations_2}" '
                 '--cluster-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Kusto/clusters/{Clusters_3}" '
                 '--resource-group "{rg}"',
                 checks=[])

        # EXAMPLE NOT FOUND: KustoDatabaseCheckNameAvailability

        self.cmd('az kusto cluster list-follower-database '
                 '--cluster-name "{Clusters_2}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto cluster start '
                 '--cluster-name "{Clusters_2}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto cluster stop '
                 '--cluster-name "{Clusters_2}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto cluster update '
                 '--cluster-name "{Clusters_2}" '
                 '--identity "{{\\"type\\":\\"SystemAssigned\\"}}" '
                 '--location "westus" '
                 '--properties-enable-purge true '
                 '--properties-enable-streaming-ingest true '
                 '--properties-key-vault-properties key-name=keyName key-vault-uri=https://dummy.keyvault.com key-version=keyVersion '
                 '--resource-group "{rg}"',
                 checks=[])

        # EXAMPLE NOT FOUND: KustoClustersCheckNameAvailability

        self.cmd('az kusto attached-database-configuration delete '
                 '--attached-database-configuration-name "{attachedDatabaseConfigurations1}" '
                 '--cluster-name "{Clusters_2}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto data-connection delete '
                 '--cluster-name "{Clusters_2}" '
                 '--data-connection-name "{DataConnections_2}" '
                 '--database-name "{KustoDatabase8}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto database delete '
                 '--cluster-name "{Clusters_2}" '
                 '--database-name "{KustoDatabase8}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto cluster delete '
                 '--cluster-name "{Clusters_2}" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto database-principal-assignment create '
                 '--cluster-name "{Clusters_4}" '
                 '--database-name "{Databases_4}" '
                 '--properties-principal-id "87654321-1234-1234-1234-123456789123" '
                 '--properties-principal-type "App" '
                 '--properties-role "Admin" '
                 '--properties-tenant-id "12345678-1234-1234-1234-123456789123" '
                 '--principal-assignment-name "kustoprincipal1" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto database-principal-assignment show '
                 '--cluster-name "{Clusters_4}" '
                 '--database-name "{Databases_4}" '
                 '--principal-assignment-name "kustoprincipal1" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto database-principal-assignment delete '
                 '--cluster-name "{Clusters_4}" '
                 '--database-name "{Databases_4}" '
                 '--principal-assignment-name "kustoprincipal1" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto cluster-principal-assignment create '
                 '--cluster-name "{Clusters_4}" '
                 '--properties-principal-id "87654321-1234-1234-1234-123456789123" '
                 '--properties-principal-type "App" '
                 '--properties-role "Admin" '
                 '--properties-tenant-id "12345678-1234-1234-1234-123456789123" '
                 '--principal-assignment-name "kustoprincipal1" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto cluster-principal-assignment show '
                 '--cluster-name "{Clusters_4}" '
                 '--principal-assignment-name "kustoprincipal1" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az kusto cluster-principal-assignment delete '
                 '--cluster-name "{Clusters_4}" '
                 '--principal-assignment-name "kustoprincipal1" '
                 '--resource-group "{rg}"',
                 checks=[])
