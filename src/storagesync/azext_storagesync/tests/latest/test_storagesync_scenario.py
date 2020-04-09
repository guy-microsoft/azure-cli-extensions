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


class MicrosoftStorageSyncScenarioTest(ScenarioTest):

    def current_subscription(self):
        subs = self.cmd('az account show').get_output_in_json()
        return subs['id']

    @ResourceGroupPreparer(name_prefix='cli_test_storagesync_tminienv59svc'[:9], key='rg')
    @ResourceGroupPreparer(name_prefix='cli_test_storagesync_SampleResourceGroup_1'[:9], key='rg_2')
    def test_storagesync(self, resource_group):

        self.kwargs.update({
            'subscription_id': self.current_subscription()
        })

        self.kwargs.update({
            'SampleStorageSyncService_1': self.create_random_name(prefix='cli_test_storage_sync_services'[:9], length=24),
            'SampleSyncGroup_1': self.create_random_name(prefix='cli_test_sync_groups'[:9], length=24),
            'SampleCloudEndpoint_1': self.create_random_name(prefix='cli_test_cloud_endpoints'[:9], length=24),
            '080d4133-bdb5-40a0-96a0-71a6057bfe9a': self.create_random_name(prefix='cli_test_registered_servers'[:9], length=24),
            'SampleServerEndpoint_1': self.create_random_name(prefix='cli_test_server_endpoints'[:9], length=24),
        })

        self.cmd('az storagesync storage-sync-service create '
                 '--location "WestUS" '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}"',
                 checks=[])

        self.cmd('az storagesync sync-group create '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}" '
                 '--sync-group-name "{SampleSyncGroup_1}"',
                 checks=[])

        self.cmd('az storagesync registered-server create '
                 '--properties-agent-version "1.0.277.0" '
                 '--properties-last-heart-beat "\\"2017-08-08T18:29:06.470652Z\\"" '
                 '--properties-server-certificate "\\"MIIDFjCCAf6gAwIBAgIQQS+DS8uhc4VNzUkTw7wbRjANBgkqhkiG9w0BAQ0FADAzMTEwLwYDVQQDEyhhbmt1c2hiLXByb2QzLnJlZG1vbmQuY29ycC5taWNyb3NvZnQuY29tMB4XDTE3MDgwMzE3MDQyNFoXDTE4MDgwNDE3MDQyNFowMzExMC8GA1UEAxMoYW5rdXNoYi1wcm9kMy5yZWRtb25kLmNvcnAubWljcm9zb2Z0LmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALDRvV4gmsIy6jGDPiHsXmvgVP749NNP7DopdlbHaNhjFmYINHl0uWylyaZmgJrROt2mnxN/zEyJtGnqYHlzUr4xvGq/qV5pqgdB9tag/sw9i22gfe9PRZ0FmSOZnXMbLYgLiDFqLtut5gHcOuWMj03YnkfoBEKlFBxWbagvW2yxz/Sxi9OVSJOKCaXra0RpcIHrO/KFl6ho2eE1/7Ykmfa8hZvSdoPd5gHdLiQcMB/pxq+mWp1fI6c8vFZoDu7Atn+NXTzYPKUxKzaisF12TsaKpohUsJpbB3Wocb0F5frn614D2pg14ERB5otjAMWw1m65csQWPI6dP8KIYe0+QPkCAwEAAaMmMCQwIgYDVR0lAQH/BBgwFgYIKwYBBQUHAwIGCisGAQQBgjcKAwwwDQYJKoZIhvcNAQENBQADggEBAA4RhVIBkw34M1RwakJgHvtjsOFxF1tVQA941NtLokx1l2Z8+GFQkcG4xpZSt+UN6wLerdCbnNhtkCErWUDeaT0jxk4g71Ofex7iM04crT4iHJr8mi96/XnhnkTUs+GDk12VgdeeNEczMZz+8Mxw9dJ5NCnYgTwO0SzGlclRsDvjzkLo8rh2ZG6n/jKrEyNXXo+hOqhupij0QbRP2Tvexdfw201kgN1jdZify8XzJ8Oi0bTS0KpJf2pNPOlooK2bjMUei9ANtEdXwwfVZGWvVh6tJjdv6k14wWWJ1L7zhA1IIVb1J+sQUzJji5iX0DrezjTz1Fg+gAzITaA/WsuujlM=\\"" '
                 '--properties-server-role "Standalone" '
                 '--resource-group "{rg_2}" '
                 '--properties-server-id "\\"080d4133-bdb5-40a0-96a0-71a6057bfe9a\\"" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}"',
                 checks=[])

        self.cmd('az storagesync cloud-endpoint create '
                 '--cloud-endpoint-name "{SampleCloudEndpoint_1}" '
                 '--properties-azure-file-share-name "cvcloud-afscv-0719-058-a94a1354-a1fd-4e9a-9a50-919fad8c4ba4" '
                 '--properties-friendly-name "ankushbsubscriptionmgmtmab" '
                 '--properties-storage-account-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Storage/storageAccounts/tminienv59storage" '
                 '--properties-storage-account-tenant-id "\\"72f988bf-86f1-41af-91ab-2d7cd011db47\\"" '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}" '
                 '--sync-group-name "{SampleSyncGroup_1}"',
                 checks=[])

        self.cmd('az storagesync server-endpoint create '
                 '--properties-cloud-tiering "off" '
                 '--properties-offline-data-transfer "on" '
                 '--properties-offline-data-transfer-share-name "myfileshare" '
                 '--properties-server-local-path "D:\\\\SampleServerEndpoint_1" '
                 '--properties-server-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg_2}/providers/Microsoft.StorageSync/storageSyncServices/{SampleStorageSyncService_1}/registeredServers/{080d4133-bdb5-40a0-96a0-71a6057bfe9a}" '
                 '--properties-tier-files-older-than-days 0 '
                 '--properties-volume-free-space-percent 100 '
                 '--resource-group "{rg_2}" '
                 '--server-endpoint-name "{SampleServerEndpoint_1}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}" '
                 '--sync-group-name "{SampleSyncGroup_1}"',
                 checks=[])

        self.cmd('az storagesync server-endpoint show '
                 '--resource-group "{rg_2}" '
                 '--server-endpoint-name "{SampleServerEndpoint_1}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}" '
                 '--sync-group-name "{SampleSyncGroup_1}"',
                 checks=[])

        self.cmd('az storagesync cloud-endpoint show '
                 '--cloud-endpoint-name "{SampleCloudEndpoint_1}" '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}" '
                 '--sync-group-name "{SampleSyncGroup_1}"',
                 checks=[])

        self.cmd('az storagesync server-endpoint list '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}" '
                 '--sync-group-name "{SampleSyncGroup_1}"',
                 checks=[])

        self.cmd('az storagesync cloud-endpoint list '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}" '
                 '--sync-group-name "{SampleSyncGroup_1}"',
                 checks=[])

        self.cmd('az storagesync registered-server show '
                 '--resource-group "{rg_2}" '
                 '--server-id "080d4133-bdb5-40a0-96a0-71a6057bfe9a" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}"',
                 checks=[])

        self.cmd('az storagesync workflow show '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}" '
                 '--workflow-id "828219ea-083e-48b5-89ea-8fd9991b2e75"',
                 checks=[])

        self.cmd('az storagesync operation-status show '
                 '--operation-id "14b50e24-f68d-4b29-a882-38be9dfb8bd1" '
                 '--location-name "westus" '
                 '--resource-group "{rg_2}" '
                 '--workflow-id "828219ea-083e-48b5-89ea-8fd9991b2e75"',
                 checks=[])

        self.cmd('az storagesync sync-group show '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}" '
                 '--sync-group-name "{SampleSyncGroup_1}"',
                 checks=[])

        self.cmd('az storagesync workflow show '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}" '
                 '--workflow-id "828219ea-083e-48b5-89ea-8fd9991b2e75"',
                 checks=[])

        self.cmd('az storagesync operation-status show '
                 '--operation-id "14b50e24-f68d-4b29-a882-38be9dfb8bd1" '
                 '--location-name "westus" '
                 '--resource-group "{rg_2}" '
                 '--workflow-id "828219ea-083e-48b5-89ea-8fd9991b2e75"',
                 checks=[])

        self.cmd('az storagesync registered-server list '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}"',
                 checks=[])

        self.cmd('az storagesync sync-group list '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}"',
                 checks=[])

        self.cmd('az storagesync workflow list '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}"',
                 checks=[])

        self.cmd('az storagesync storage-sync-service show '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}"',
                 checks=[])

        self.cmd('az storagesync storage-sync-service list '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az storagesync storage-sync-service list',
                 checks=[])

        # EXAMPLE NOT FOUND: Operations_List

        self.cmd('az storagesync cloud-endpoint trigger-change-detection '
                 '--cloud-endpoint-name "{SampleCloudEndpoint_1}" '
                 '--change-detection-mode "Recursive" '
                 '--directory-path "NewDirectory" '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}" '
                 '--sync-group-name "{SampleSyncGroup_1}"',
                 checks=[])

        self.cmd('az storagesync cloud-endpoint restoreheartbeat '
                 '--cloud-endpoint-name "{SampleCloudEndpoint_1}" '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}" '
                 '--sync-group-name "{SampleSyncGroup_1}"',
                 checks=[])

        self.cmd('az storagesync server-endpoint recall-action '
                 '--pattern "" '
                 '--recall-path "" '
                 '--resource-group "{rg_2}" '
                 '--server-endpoint-name "{SampleServerEndpoint_1}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}" '
                 '--sync-group-name "{SampleSyncGroup_1}"',
                 checks=[])

        self.cmd('az storagesync cloud-endpoint post-restore '
                 '--cloud-endpoint-name "{SampleCloudEndpoint_1}" '
                 '--azure-file-share-uri "https://hfsazbackupdevintncus2.file.core.test-cint.azure-test.net/sampleFileShare" '
                 '--restore-file-spec path=text1.txt isdir=false '
                 '--restore-file-spec path=MyDir isdir=true '
                 '--restore-file-spec path=MyDir/SubDir isdir=false '
                 '--restore-file-spec path=MyDir/SubDir/File1.pdf isdir=false '
                 '--source-azure-file-share-uri "https://hfsazbackupdevintncus2.file.core.test-cint.azure-test.net/sampleFileShare" '
                 '--status "Succeeded" '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}" '
                 '--sync-group-name "{SampleSyncGroup_1}"',
                 checks=[])

        self.cmd('az storagesync cloud-endpoint pre-restore '
                 '--cloud-endpoint-name "{SampleCloudEndpoint_1}" '
                 '--azure-file-share-uri "https://hfsazbackupdevintncus2.file.core.test-cint.azure-test.net/sampleFileShare" '
                 '--restore-file-spec path=text1.txt isdir=false '
                 '--restore-file-spec path=MyDir isdir=true '
                 '--restore-file-spec path=MyDir/SubDir isdir=false '
                 '--restore-file-spec path=MyDir/SubDir/File1.pdf isdir=false '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}" '
                 '--sync-group-name "{SampleSyncGroup_1}"',
                 checks=[])

        self.cmd('az storagesync cloud-endpoint post-backup '
                 '--cloud-endpoint-name "{SampleCloudEndpoint_1}" '
                 '--azure-file-share "https://sampleserver.file.core.test-cint.azure-test.net/sampleFileShare" '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}" '
                 '--sync-group-name "{SampleSyncGroup_1}"',
                 checks=[])

        self.cmd('az storagesync cloud-endpoint pre-backup '
                 '--cloud-endpoint-name "{SampleCloudEndpoint_1}" '
                 '--azure-file-share "https://sampleserver.file.core.test-cint.azure-test.net/sampleFileShare" '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}" '
                 '--sync-group-name "{SampleSyncGroup_1}"',
                 checks=[])

        self.cmd('az storagesync server-endpoint update '
                 '--properties-cloud-tiering "off" '
                 '--properties-offline-data-transfer "off" '
                 '--properties-tier-files-older-than-days 0 '
                 '--properties-volume-free-space-percent 100 '
                 '--resource-group "{rg_2}" '
                 '--server-endpoint-name "{SampleServerEndpoint_1}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}" '
                 '--sync-group-name "{SampleSyncGroup_1}"',
                 checks=[])

        self.cmd('az storagesync registered-server trigger-rollover '
                 '--server-certificate "\\"MIIDFjCCAf6gAwIBAgIQQS+DS8uhc4VNzUkTw7wbRjANBgkqhkiG9w0BAQ0FADAzMTEwLwYDVQQDEyhhbmt1c2hiLXByb2QzLnJlZG1vbmQuY29ycC5taWNyb3NvZnQuY29tMB4XDTE3MDgwMzE3MDQyNFoXDTE4MDgwNDE3MDQyNFowMzExMC8GA1UEAxMoYW5rdXNoYi1wcm9kMy5yZWRtb25kLmNvcnAubWljcm9zb2Z0LmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALDRvV4gmsIy6jGDPiHsXmvgVP749NNP7DopdlbHaNhjFmYINHl0uWylyaZmgJrROt2mnxN/zEyJtGnqYHlzUr4xvGq/qV5pqgdB9tag/sw9i22gfe9PRZ0FmSOZnXMbLYgLiDFqLtut5gHcOuWMj03YnkfoBEKlFBxWbagvW2yxz/Sxi9OVSJOKCaXra0RpcIHrO/KFl6ho2eE1/7Ykmfa8hZvSdoPd5gHdLiQcMB/pxq+mWp1fI6c8vFZoDu7Atn+NXTzYPKUxKzaisF12TsaKpohUsJpbB3Wocb0F5frn614D2pg14ERB5otjAMWw1m65csQWPI6dP8KIYe0+QPkCAwEAAaMmMCQwIgYDVR0lAQH/BBgwFgYIKwYBBQUHAwIGCisGAQQBgjcKAwwwDQYJKoZIhvcNAQENBQADggEBAA4RhVIBkw34M1RwakJgHvtjsOFxF1tVQA941NtLokx1l2Z8+GFQkcG4xpZSt+UN6wLerdCbnNhtkCErWUDeaT0jxk4g71Ofex7iM04crT4iHJr8mi96/XnhnkTUs+GDk12VgdeeNEczMZz+8Mxw9dJ5NCnYgTwO0SzGlclRsDvjzkLo8rh2ZG6n/jKrEyNXXo+hOqhupij0QbRP2Tvexdfw201kgN1jdZify8XzJ8Oi0bTS0KpJf2pNPOlooK2bjMUei9ANtEdXwwfVZGWvVh6tJjdv6k14wWWJ1L7zhA1IIVb1J+sQUzJji5iX0DrezjTz1Fg+gAzITaA/WsuujlM=\\"" '
                 '--resource-group "{rg_2}" '
                 '--server-id "d166ca76-dad2-49df-b409-12345642d730" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}"',
                 checks=[])

        self.cmd('az storagesync workflow abort '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}" '
                 '--workflow-id "7ffd50b3-5574-478d-9ff2-9371bc42ce68"',
                 checks=[])

        self.cmd('az storagesync storage-sync-service update '
                 '--tags Dept=IT Environment=Test '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}"',
                 checks=[])

        # EXAMPLE NOT FOUND: StorageSyncServiceCheckNameAvailability_AlreadyExists

        # EXAMPLE NOT FOUND: StorageSyncServiceCheckNameAvailability_Available

        self.cmd('az storagesync server-endpoint delete '
                 '--resource-group "{rg_2}" '
                 '--server-endpoint-name "{SampleServerEndpoint_1}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}" '
                 '--sync-group-name "{SampleSyncGroup_1}"',
                 checks=[])

        self.cmd('az storagesync cloud-endpoint delete '
                 '--cloud-endpoint-name "{SampleCloudEndpoint_1}" '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}" '
                 '--sync-group-name "{SampleSyncGroup_1}"',
                 checks=[])

        self.cmd('az storagesync registered-server delete '
                 '--resource-group "{rg_2}" '
                 '--server-id "41166691-ab03-43e9-ab3e-0330eda162ac" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}"',
                 checks=[])

        self.cmd('az storagesync sync-group delete '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}" '
                 '--sync-group-name "{SampleSyncGroup_1}"',
                 checks=[])

        self.cmd('az storagesync storage-sync-service delete '
                 '--resource-group "{rg_2}" '
                 '--storage-sync-service-name "{SampleStorageSyncService_1}"',
                 checks=[])
