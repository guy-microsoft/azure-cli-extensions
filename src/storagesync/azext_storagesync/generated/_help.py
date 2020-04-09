# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['storagesync storage-sync-service'] = """
    type: group
    short-summary: storagesync storage-sync-service
"""

helps['storagesync storage-sync-service list'] = """
    type: command
    short-summary: Get a StorageSyncService list by subscription.
    examples:
      - name: StorageSyncServices_ListByResourceGroup
        text: |-
               az storagesync storage-sync-service list --resource-group "SampleResourceGroup_1"
"""

helps['storagesync storage-sync-service show'] = """
    type: command
    short-summary: Get a given StorageSyncService.
    examples:
      - name: StorageSyncServices_Get
        text: |-
               az storagesync storage-sync-service show --resource-group "SampleResourceGroup_1"
               --storage-sync-service-name "SampleStorageSyncService_1"
"""

helps['storagesync storage-sync-service create'] = """
    type: command
    short-summary: Create a new StorageSyncService.
    examples:
      - name: StorageSyncServices_Create
        text: |-
               az storagesync storage-sync-service create --location "WestUS" --resource-group
               "SampleResourceGroup_1" --storage-sync-service-name "SampleStorageSyncService_1"
"""

helps['storagesync storage-sync-service update'] = """
    type: command
    short-summary: Patch a given StorageSyncService.
    examples:
      - name: StorageSyncServices_Update
        text: |-
               az storagesync storage-sync-service update --tags Dept=IT Environment=Test
               --resource-group "SampleResourceGroup_1" --storage-sync-service-name
               "SampleStorageSyncService_1"
"""

helps['storagesync storage-sync-service delete'] = """
    type: command
    short-summary: Delete a given StorageSyncService.
    examples:
      - name: StorageSyncServices_Delete
        text: |-
               az storagesync storage-sync-service delete --resource-group "SampleResourceGroup_1"
               --storage-sync-service-name "SampleStorageSyncService_1"
"""

helps['storagesync sync-group'] = """
    type: group
    short-summary: storagesync sync-group
"""

helps['storagesync sync-group list'] = """
    type: command
    short-summary: Get a SyncGroup List.
    examples:
      - name: SyncGroups_ListByStorageSyncService
        text: |-
               az storagesync sync-group list --resource-group "SampleResourceGroup_1"
               --storage-sync-service-name "SampleStorageSyncService_1"
"""

helps['storagesync sync-group show'] = """
    type: command
    short-summary: Get a given SyncGroup.
    examples:
      - name: SyncGroups_Get
        text: |-
               az storagesync sync-group show --resource-group "SampleResourceGroup_1"
               --storage-sync-service-name "SampleStorageSyncService_1" --sync-group-name
               "SampleSyncGroup_1"
"""

helps['storagesync sync-group create'] = """
    type: command
    short-summary: Create a new SyncGroup.
    examples:
      - name: SyncGroups_Create
        text: |-
               az storagesync sync-group create --resource-group "SampleResourceGroup_1"
               --storage-sync-service-name "SampleStorageSyncService_1" --sync-group-name
               "SampleSyncGroup_1"
"""

helps['storagesync sync-group delete'] = """
    type: command
    short-summary: Delete a given SyncGroup.
    examples:
      - name: SyncGroups_Delete
        text: |-
               az storagesync sync-group delete --resource-group "SampleResourceGroup_1"
               --storage-sync-service-name "SampleStorageSyncService_1" --sync-group-name
               "SampleSyncGroup_1"
"""

helps['storagesync cloud-endpoint'] = """
    type: group
    short-summary: storagesync cloud-endpoint
"""

helps['storagesync cloud-endpoint list'] = """
    type: command
    short-summary: Get a CloudEndpoint List.
    examples:
      - name: CloudEndpoints_ListBySyncGroup
        text: |-
               az storagesync cloud-endpoint list --resource-group "SampleResourceGroup_1"
               --storage-sync-service-name "SampleStorageSyncService_1" --sync-group-name
               "SampleSyncGroup_1"
"""

helps['storagesync cloud-endpoint show'] = """
    type: command
    short-summary: Get a given CloudEndpoint.
    examples:
      - name: CloudEndpoints_Get
        text: |-
               az storagesync cloud-endpoint show --cloud-endpoint-name "SampleCloudEndpoint_1"
               --resource-group "SampleResourceGroup_1" --storage-sync-service-name
               "SampleStorageSyncService_1" --sync-group-name "SampleSyncGroup_1"
"""

helps['storagesync cloud-endpoint create'] = """
    type: command
    short-summary: Create a new CloudEndpoint.
    examples:
      - name: CloudEndpoints_Create
        text: |-
               az storagesync cloud-endpoint create --cloud-endpoint-name "SampleCloudEndpoint_1"
               --properties-azure-file-share-name
               "cvcloud-afscv-0719-058-a94a1354-a1fd-4e9a-9a50-919fad8c4ba4" --properties-friendly-name
               "ankushbsubscriptionmgmtmab" --properties-storage-account-resource-id "/subscriptions/744f
               4d70-6d17-4921-8970-a765d14f763f/resourceGroups/tminienv59svc/providers/Microsoft.Storage/
               storageAccounts/tminienv59storage" --properties-storage-account-tenant-id
               "\\"72f988bf-86f1-41af-91ab-2d7cd011db47\\"" --resource-group "SampleResourceGroup_1"
               --storage-sync-service-name "SampleStorageSyncService_1" --sync-group-name
               "SampleSyncGroup_1"
"""

helps['storagesync cloud-endpoint delete'] = """
    type: command
    short-summary: Delete a given CloudEndpoint.
    examples:
      - name: CloudEndpoints_Delete
        text: |-
               az storagesync cloud-endpoint delete --cloud-endpoint-name "SampleCloudEndpoint_1"
               --resource-group "SampleResourceGroup_1" --storage-sync-service-name
               "SampleStorageSyncService_1" --sync-group-name "SampleSyncGroup_1"
"""

helps['storagesync cloud-endpoint pre-restore'] = """
    type: command
    short-summary: Pre Restore a given CloudEndpoint.
    examples:
      - name: CloudEndpoints_PreRestore
        text: |-
               az storagesync cloud-endpoint pre-restore --cloud-endpoint-name "SampleCloudEndpoint_1"
               --azure-file-share-uri
               "https://hfsazbackupdevintncus2.file.core.test-cint.azure-test.net/sampleFileShare"
               --restore-file-spec path=text1.txt isdir=false --restore-file-spec path=MyDir isdir=true
               --restore-file-spec path=MyDir/SubDir isdir=false --restore-file-spec
               path=MyDir/SubDir/File1.pdf isdir=false --resource-group "SampleResourceGroup_1"
               --storage-sync-service-name "SampleStorageSyncService_1" --sync-group-name
               "SampleSyncGroup_1"
"""

helps['storagesync cloud-endpoint post-restore'] = """
    type: command
    short-summary: Post Restore a given CloudEndpoint.
    examples:
      - name: CloudEndpoints_PostRestore
        text: |-
               az storagesync cloud-endpoint post-restore --cloud-endpoint-name "SampleCloudEndpoint_1"
               --azure-file-share-uri
               "https://hfsazbackupdevintncus2.file.core.test-cint.azure-test.net/sampleFileShare"
               --restore-file-spec path=text1.txt isdir=false --restore-file-spec path=MyDir isdir=true
               --restore-file-spec path=MyDir/SubDir isdir=false --restore-file-spec
               path=MyDir/SubDir/File1.pdf isdir=false --source-azure-file-share-uri
               "https://hfsazbackupdevintncus2.file.core.test-cint.azure-test.net/sampleFileShare"
               --status "Succeeded" --resource-group "SampleResourceGroup_1" --storage-sync-service-name
               "SampleStorageSyncService_1" --sync-group-name "SampleSyncGroup_1"
"""

helps['storagesync cloud-endpoint trigger-change-detection'] = """
    type: command
    short-summary: Triggers detection of changes performed on Azure File share connected to the specified Azure File Sync Cloud Endpoint.
    examples:
      - name: CloudEndpoints_TriggerChangeDetection
        text: |-
               az storagesync cloud-endpoint trigger-change-detection --cloud-endpoint-name
               "SampleCloudEndpoint_1" --change-detection-mode "Recursive" --directory-path
               "NewDirectory" --resource-group "SampleResourceGroup_1" --storage-sync-service-name
               "SampleStorageSyncService_1" --sync-group-name "SampleSyncGroup_1"
"""

helps['storagesync cloud-endpoint pre-backup'] = """
    type: command
    short-summary: Pre Backup a given CloudEndpoint.
    examples:
      - name: CloudEndpoints_PreBackup
        text: |-
               az storagesync cloud-endpoint pre-backup --cloud-endpoint-name "SampleCloudEndpoint_1"
               --azure-file-share
               "https://sampleserver.file.core.test-cint.azure-test.net/sampleFileShare"
               --resource-group "SampleResourceGroup_1" --storage-sync-service-name
               "SampleStorageSyncService_1" --sync-group-name "SampleSyncGroup_1"
"""

helps['storagesync cloud-endpoint post-backup'] = """
    type: command
    short-summary: Post Backup a given CloudEndpoint.
    examples:
      - name: CloudEndpoints_PostBackup
        text: |-
               az storagesync cloud-endpoint post-backup --cloud-endpoint-name "SampleCloudEndpoint_1"
               --azure-file-share
               "https://sampleserver.file.core.test-cint.azure-test.net/sampleFileShare"
               --resource-group "SampleResourceGroup_1" --storage-sync-service-name
               "SampleStorageSyncService_1" --sync-group-name "SampleSyncGroup_1"
"""

helps['storagesync cloud-endpoint restoreheartbeat'] = """
    type: command
    short-summary: Restore Heartbeat a given CloudEndpoint.
    examples:
      - name: CloudEndpoints_restoreheartbeat
        text: |-
               az storagesync cloud-endpoint restoreheartbeat --cloud-endpoint-name
               "SampleCloudEndpoint_1" --resource-group "SampleResourceGroup_1"
               --storage-sync-service-name "SampleStorageSyncService_1" --sync-group-name
               "SampleSyncGroup_1"
"""

helps['storagesync server-endpoint'] = """
    type: group
    short-summary: storagesync server-endpoint
"""

helps['storagesync server-endpoint list'] = """
    type: command
    short-summary: Get a ServerEndpoint list.
    examples:
      - name: ServerEndpoints_ListBySyncGroup
        text: |-
               az storagesync server-endpoint list --resource-group "SampleResourceGroup_1"
               --storage-sync-service-name "SampleStorageSyncService_1" --sync-group-name
               "SampleSyncGroup_1"
"""

helps['storagesync server-endpoint show'] = """
    type: command
    short-summary: Get a ServerEndpoint.
    examples:
      - name: ServerEndpoints_Get
        text: |-
               az storagesync server-endpoint show --resource-group "SampleResourceGroup_1"
               --server-endpoint-name "SampleServerEndpoint_1" --storage-sync-service-name
               "SampleStorageSyncService_1" --sync-group-name "SampleSyncGroup_1"
"""

helps['storagesync server-endpoint create'] = """
    type: command
    short-summary: Create a new ServerEndpoint.
    examples:
      - name: ServerEndpoints_Create
        text: |-
               az storagesync server-endpoint create --properties-cloud-tiering "off"
               --properties-offline-data-transfer "on" --properties-offline-data-transfer-share-name
               "myfileshare" --properties-server-local-path "D:\\\\SampleServerEndpoint_1"
               --properties-server-resource-id "/subscriptions/52b8da2f-61e0-4a1f-8dde-336911f367fb/resou
               rceGroups/SampleResourceGroup_1/providers/Microsoft.StorageSync/storageSyncServices/Sample
               StorageSyncService_1/registeredServers/080d4133-bdb5-40a0-96a0-71a6057bfe9a"
               --properties-tier-files-older-than-days 0 --properties-volume-free-space-percent 100
               --resource-group "SampleResourceGroup_1" --server-endpoint-name "SampleServerEndpoint_1"
               --storage-sync-service-name "SampleStorageSyncService_1" --sync-group-name
               "SampleSyncGroup_1"
"""

helps['storagesync server-endpoint update'] = """
    type: command
    short-summary: Patch a given ServerEndpoint.
    examples:
      - name: ServerEndpoints_Update
        text: |-
               az storagesync server-endpoint update --properties-cloud-tiering "off"
               --properties-offline-data-transfer "off" --properties-tier-files-older-than-days 0
               --properties-volume-free-space-percent 100 --resource-group "SampleResourceGroup_1"
               --server-endpoint-name "SampleServerEndpoint_1" --storage-sync-service-name
               "SampleStorageSyncService_1" --sync-group-name "SampleSyncGroup_1"
"""

helps['storagesync server-endpoint delete'] = """
    type: command
    short-summary: Delete a given ServerEndpoint.
    examples:
      - name: ServerEndpoints_Delete
        text: |-
               az storagesync server-endpoint delete --resource-group "SampleResourceGroup_1"
               --server-endpoint-name "SampleServerEndpoint_1" --storage-sync-service-name
               "SampleStorageSyncService_1" --sync-group-name "SampleSyncGroup_1"
"""

helps['storagesync server-endpoint recall-action'] = """
    type: command
    short-summary: Recall a server endpoint.
    examples:
      - name: ServerEndpoints_recallAction
        text: |-
               az storagesync server-endpoint recall-action --pattern "" --recall-path ""
               --resource-group "SampleResourceGroup_1" --server-endpoint-name "SampleServerEndpoint_1"
               --storage-sync-service-name "SampleStorageSyncService_1" --sync-group-name
               "SampleSyncGroup_1"
"""

helps['storagesync registered-server'] = """
    type: group
    short-summary: storagesync registered-server
"""

helps['storagesync registered-server list'] = """
    type: command
    short-summary: Get a given registered server list.
    examples:
      - name: RegisteredServers_ListByStorageSyncService
        text: |-
               az storagesync registered-server list --resource-group "SampleResourceGroup_1"
               --storage-sync-service-name "SampleStorageSyncService_1"
"""

helps['storagesync registered-server show'] = """
    type: command
    short-summary: Get a given registered server.
    examples:
      - name: RegisteredServers_Get
        text: |-
               az storagesync registered-server show --resource-group "SampleResourceGroup_1"
               --server-id "080d4133-bdb5-40a0-96a0-71a6057bfe9a" --storage-sync-service-name
               "SampleStorageSyncService_1"
"""

helps['storagesync registered-server create'] = """
    type: command
    short-summary: Add a new registered server.
    examples:
      - name: RegisteredServers_Create
        text: |-
               az storagesync registered-server create --properties-agent-version "1.0.277.0"
               --properties-last-heart-beat "\\"2017-08-08T18:29:06.470652Z\\""
               --properties-server-certificate "\\"MIIDFjCCAf6gAwIBAgIQQS+DS8uhc4VNzUkTw7wbRjANBgkqhkiG9w0
               BAQ0FADAzMTEwLwYDVQQDEyhhbmt1c2hiLXByb2QzLnJlZG1vbmQuY29ycC5taWNyb3NvZnQuY29tMB4XDTE3MDgwM
               zE3MDQyNFoXDTE4MDgwNDE3MDQyNFowMzExMC8GA1UEAxMoYW5rdXNoYi1wcm9kMy5yZWRtb25kLmNvcnAubWljcm9
               zb2Z0LmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALDRvV4gmsIy6jGDPiHsXmvgVP749NNP7Dopd
               lbHaNhjFmYINHl0uWylyaZmgJrROt2mnxN/zEyJtGnqYHlzUr4xvGq/qV5pqgdB9tag/sw9i22gfe9PRZ0FmSOZnXM
               bLYgLiDFqLtut5gHcOuWMj03YnkfoBEKlFBxWbagvW2yxz/Sxi9OVSJOKCaXra0RpcIHrO/KFl6ho2eE1/7Ykmfa8h
               ZvSdoPd5gHdLiQcMB/pxq+mWp1fI6c8vFZoDu7Atn+NXTzYPKUxKzaisF12TsaKpohUsJpbB3Wocb0F5frn614D2pg
               14ERB5otjAMWw1m65csQWPI6dP8KIYe0+QPkCAwEAAaMmMCQwIgYDVR0lAQH/BBgwFgYIKwYBBQUHAwIGCisGAQQBg
               jcKAwwwDQYJKoZIhvcNAQENBQADggEBAA4RhVIBkw34M1RwakJgHvtjsOFxF1tVQA941NtLokx1l2Z8+GFQkcG4xpZ
               St+UN6wLerdCbnNhtkCErWUDeaT0jxk4g71Ofex7iM04crT4iHJr8mi96/XnhnkTUs+GDk12VgdeeNEczMZz+8Mxw9
               dJ5NCnYgTwO0SzGlclRsDvjzkLo8rh2ZG6n/jKrEyNXXo+hOqhupij0QbRP2Tvexdfw201kgN1jdZify8XzJ8Oi0bT
               S0KpJf2pNPOlooK2bjMUei9ANtEdXwwfVZGWvVh6tJjdv6k14wWWJ1L7zhA1IIVb1J+sQUzJji5iX0DrezjTz1Fg+g
               AzITaA/WsuujlM=\\"" --properties-server-role "Standalone" --resource-group
               "SampleResourceGroup_1" --properties-server-id "\\"080d4133-bdb5-40a0-96a0-71a6057bfe9a\\""
               --storage-sync-service-name "SampleStorageSyncService_1"
"""

helps['storagesync registered-server delete'] = """
    type: command
    short-summary: Delete the given registered server.
    examples:
      - name: RegisteredServers_Delete
        text: |-
               az storagesync registered-server delete --resource-group "SampleResourceGroup_1"
               --server-id "41166691-ab03-43e9-ab3e-0330eda162ac" --storage-sync-service-name
               "SampleStorageSyncService_1"
"""

helps['storagesync registered-server trigger-rollover'] = """
    type: command
    short-summary: Triggers Server certificate rollover.
    examples:
      - name: RegisteredServers_triggerRollover
        text: |-
               az storagesync registered-server trigger-rollover --server-certificate "\\"MIIDFjCCAf6gAwIB
               AgIQQS+DS8uhc4VNzUkTw7wbRjANBgkqhkiG9w0BAQ0FADAzMTEwLwYDVQQDEyhhbmt1c2hiLXByb2QzLnJlZG1vbm
               QuY29ycC5taWNyb3NvZnQuY29tMB4XDTE3MDgwMzE3MDQyNFoXDTE4MDgwNDE3MDQyNFowMzExMC8GA1UEAxMoYW5r
               dXNoYi1wcm9kMy5yZWRtb25kLmNvcnAubWljcm9zb2Z0LmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCgg
               EBALDRvV4gmsIy6jGDPiHsXmvgVP749NNP7DopdlbHaNhjFmYINHl0uWylyaZmgJrROt2mnxN/zEyJtGnqYHlzUr4x
               vGq/qV5pqgdB9tag/sw9i22gfe9PRZ0FmSOZnXMbLYgLiDFqLtut5gHcOuWMj03YnkfoBEKlFBxWbagvW2yxz/Sxi9
               OVSJOKCaXra0RpcIHrO/KFl6ho2eE1/7Ykmfa8hZvSdoPd5gHdLiQcMB/pxq+mWp1fI6c8vFZoDu7Atn+NXTzYPKUx
               KzaisF12TsaKpohUsJpbB3Wocb0F5frn614D2pg14ERB5otjAMWw1m65csQWPI6dP8KIYe0+QPkCAwEAAaMmMCQwIg
               YDVR0lAQH/BBgwFgYIKwYBBQUHAwIGCisGAQQBgjcKAwwwDQYJKoZIhvcNAQENBQADggEBAA4RhVIBkw34M1RwakJg
               HvtjsOFxF1tVQA941NtLokx1l2Z8+GFQkcG4xpZSt+UN6wLerdCbnNhtkCErWUDeaT0jxk4g71Ofex7iM04crT4iHJ
               r8mi96/XnhnkTUs+GDk12VgdeeNEczMZz+8Mxw9dJ5NCnYgTwO0SzGlclRsDvjzkLo8rh2ZG6n/jKrEyNXXo+hOqhu
               pij0QbRP2Tvexdfw201kgN1jdZify8XzJ8Oi0bTS0KpJf2pNPOlooK2bjMUei9ANtEdXwwfVZGWvVh6tJjdv6k14wW
               WJ1L7zhA1IIVb1J+sQUzJji5iX0DrezjTz1Fg+gAzITaA/WsuujlM=\\"" --resource-group
               "SampleResourceGroup_1" --server-id "d166ca76-dad2-49df-b409-12345642d730"
               --storage-sync-service-name "SampleStorageSyncService_1"
"""

helps['storagesync workflow'] = """
    type: group
    short-summary: storagesync workflow
"""

helps['storagesync workflow list'] = """
    type: command
    short-summary: Get a Workflow List
    examples:
      - name: Workflows_ListByStorageSyncService
        text: |-
               az storagesync workflow list --resource-group "SampleResourceGroup_1"
               --storage-sync-service-name "SampleStorageSyncService_1"
"""

helps['storagesync workflow show'] = """
    type: command
    short-summary: Get Workflows resource
    examples:
      - name: Workflows_Get
        text: |-
               az storagesync workflow show --resource-group "SampleResourceGroup_1"
               --storage-sync-service-name "SampleStorageSyncService_1" --workflow-id
               "828219ea-083e-48b5-89ea-8fd9991b2e75"
"""

helps['storagesync workflow abort'] = """
    type: command
    short-summary: Abort the given workflow.
    examples:
      - name: Workflows_Abort
        text: |-
               az storagesync workflow abort --resource-group "SampleResourceGroup_1"
               --storage-sync-service-name "SampleStorageSyncService_1" --workflow-id
               "7ffd50b3-5574-478d-9ff2-9371bc42ce68"
"""

helps['storagesync operation-status'] = """
    type: group
    short-summary: storagesync operation-status
"""

helps['storagesync operation-status show'] = """
    type: command
    short-summary: Get Operation status
    examples:
      - name: Workflows_Get
        text: |-
               az storagesync operation-status show --operation-id
               "14b50e24-f68d-4b29-a882-38be9dfb8bd1" --location-name "westus" --resource-group
               "SampleResourceGroup_1" --workflow-id "828219ea-083e-48b5-89ea-8fd9991b2e75"
"""
