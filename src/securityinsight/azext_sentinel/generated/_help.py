# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['sentinel alert-rule'] = """
    type: group
    short-summary: Manage alert rule with sentinel
"""

helps['sentinel alert-rule list'] = """
    type: command
    short-summary: "Gets all alert rules."
    examples:
      - name: Get all alert rules.
        text: |-
               az sentinel alert-rule list --resource-group "myRg" --workspace-name "myWorkspace"
"""

helps['sentinel alert-rule show'] = """
    type: command
    short-summary: "Gets the alert rule."
    examples:
      - name: Get a Fusion alert rule.
        text: |-
               az sentinel alert-rule show --resource-group "myRg" --rule-id "myFirstFusionRule" --workspace-name \
"myWorkspace"
      - name: Get a MicrosoftSecurityIncidentCreation rule.
        text: |-
               az sentinel alert-rule show --resource-group "myRg" --rule-id "microsoftSecurityIncidentCreationRuleExam\
ple" --workspace-name "myWorkspace"
      - name: Get a Scheduled alert rule.
        text: |-
               az sentinel alert-rule show --resource-group "myRg" --rule-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" \
--workspace-name "myWorkspace"
"""

helps['sentinel alert-rule create'] = """
    type: command
    short-summary: "Creates or updates the action of alert rule. And Create the alert rule."
    parameters:
      - name: --fusion-alert-rule
        short-summary: "Represents Fusion alert rule."
        long-summary: |
            Usage: --fusion-alert-rule alert-rule-template-name=XX enabled=XX kind=XX etag=XX

            alert-rule-template-name: The Name of the alert rule template used to create this rule.
            enabled: Determines whether this alert rule is enabled or disabled.
            kind: Required. The alert rule kind
            etag: Etag of the azure resource
      - name: --microsoft-security-incident-creation-alert-rule
        short-summary: "Represents MicrosoftSecurityIncidentCreation rule."
        long-summary: |
            Usage: --microsoft-security-incident-creation-alert-rule display-names-filter=XX \
display-names-exclude-filter=XX product-filter=XX severities-filter=XX alert-rule-template-name=XX description=XX \
display-name=XX enabled=XX kind=XX etag=XX

            display-names-filter: the alerts' displayNames on which the cases will be generated
            display-names-exclude-filter: the alerts' displayNames on which the cases will not be generated
            product-filter: The alerts' productName on which the cases will be generated
            severities-filter: the alerts' severities on which the cases will be generated
            alert-rule-template-name: The Name of the alert rule template used to create this rule.
            description: The description of the alert rule.
            display-name: The display name for alerts created by this alert rule.
            enabled: Determines whether this alert rule is enabled or disabled.
            kind: Required. The alert rule kind
            etag: Etag of the azure resource
      - name: --scheduled-alert-rule
        short-summary: "Represents scheduled alert rule."
        long-summary: |
            Usage: --scheduled-alert-rule query=XX query-frequency=XX query-period=XX severity=XX trigger-operator=XX \
trigger-threshold=XX alert-rule-template-name=XX description=XX display-name=XX enabled=XX suppression-duration=XX \
suppression-enabled=XX tactics=XX kind=XX etag=XX

            query: The query that creates alerts for this rule.
            query-frequency: The frequency (in ISO 8601 duration format) for this alert rule to run.
            query-period: The period (in ISO 8601 duration format) that this alert rule looks at.
            severity: The severity for alerts created by this alert rule.
            trigger-operator: The operation against the threshold that triggers alert rule.
            trigger-threshold: The threshold triggers this alert rule.
            alert-rule-template-name: The Name of the alert rule template used to create this rule.
            description: The description of the alert rule.
            display-name: The display name for alerts created by this alert rule.
            enabled: Determines whether this alert rule is enabled or disabled.
            suppression-duration: The suppression (in ISO 8601 duration format) to wait since last time this alert \
rule been triggered.
            suppression-enabled: Determines whether the suppression for this alert rule is enabled or disabled.
            tactics: The tactics of the alert rule
            kind: Required. The alert rule kind
            etag: Etag of the azure resource
    examples:
      - name: Creates or updates an action of alert rule.
        text: |-
               az sentinel alert-rule create --etag "\\"0300bf09-0000-0000-0000-5c37296e0000\\"" \
--logic-app-resource-id "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.Lo\
gic/workflows/MyAlerts" --trigger-uri "https://prod-31.northcentralus.logic.azure.com:443/workflows/cd3765391efd48549fd\
7681ded1d48d7/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=signature" \
--action-id "912bec42-cb66-4c03-ac63-1761b6898c3e" --resource-group "myRg" --rule-id "73e01a99-5cd7-4139-a149-9f2736ff2\
ab5" --workspace-name "myWorkspace"
      - name: Creates or updates a Fusion alert rule.
        text: |-
               az sentinel alert-rule create --fusion-alert-rule etag="3d00c3ca-0000-0100-0000-5d42d5010000" \
alert-rule-template-name="f71aba3d-28fb-450b-b192-4e76a83015c8" enabled=true --resource-group "myRg" --rule-id \
"myFirstFusionRule" --workspace-name "myWorkspace"
      - name: Creates or updates a MicrosoftSecurityIncidentCreation rule.
        text: |-
               az sentinel alert-rule create --microsoft-security-incident-creation-alert-rule \
etag="\\"260097e0-0000-0d00-0000-5d6fa88f0000\\"" product-filter="Microsoft Cloud App Security" display-name="testing \
displayname" enabled=true --resource-group "myRg" --rule-id "microsoftSecurityIncidentCreationRuleExample" \
--workspace-name "myWorkspace"
      - name: Creates or updates a Scheduled alert rule.
        text: |-
               az sentinel alert-rule create --scheduled-alert-rule etag="\\"0300bf09-0000-0000-0000-5c37296e0000\\"" \
query="ProtectionStatus | extend HostCustomEntity = Computer | extend IPCustomEntity = ComputerIP_Hidden" \
query-frequency="PT1H" query-period="P2DT1H30M" severity="High" trigger-operator="GreaterThan" trigger-threshold=0 \
description="" display-name="Rule2" enabled=true suppression-duration="PT1H" suppression-enabled=false \
tactics="Persistence" tactics="LateralMovement" --resource-group "myRg" --rule-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5\
" --workspace-name "myWorkspace"
"""

helps['sentinel alert-rule update'] = """
    type: command
    short-summary: "Update the alert rule."
    parameters:
      - name: --fusion-alert-rule
        short-summary: "Represents Fusion alert rule."
        long-summary: |
            Usage: --fusion-alert-rule alert-rule-template-name=XX enabled=XX kind=XX etag=XX

            alert-rule-template-name: The Name of the alert rule template used to create this rule.
            enabled: Determines whether this alert rule is enabled or disabled.
            kind: Required. The alert rule kind
            etag: Etag of the azure resource
      - name: --microsoft-security-incident-creation-alert-rule
        short-summary: "Represents MicrosoftSecurityIncidentCreation rule."
        long-summary: |
            Usage: --microsoft-security-incident-creation-alert-rule display-names-filter=XX \
display-names-exclude-filter=XX product-filter=XX severities-filter=XX alert-rule-template-name=XX description=XX \
display-name=XX enabled=XX kind=XX etag=XX

            display-names-filter: the alerts' displayNames on which the cases will be generated
            display-names-exclude-filter: the alerts' displayNames on which the cases will not be generated
            product-filter: The alerts' productName on which the cases will be generated
            severities-filter: the alerts' severities on which the cases will be generated
            alert-rule-template-name: The Name of the alert rule template used to create this rule.
            description: The description of the alert rule.
            display-name: The display name for alerts created by this alert rule.
            enabled: Determines whether this alert rule is enabled or disabled.
            kind: Required. The alert rule kind
            etag: Etag of the azure resource
      - name: --scheduled-alert-rule
        short-summary: "Represents scheduled alert rule."
        long-summary: |
            Usage: --scheduled-alert-rule query=XX query-frequency=XX query-period=XX severity=XX trigger-operator=XX \
trigger-threshold=XX alert-rule-template-name=XX description=XX display-name=XX enabled=XX suppression-duration=XX \
suppression-enabled=XX tactics=XX kind=XX etag=XX

            query: The query that creates alerts for this rule.
            query-frequency: The frequency (in ISO 8601 duration format) for this alert rule to run.
            query-period: The period (in ISO 8601 duration format) that this alert rule looks at.
            severity: The severity for alerts created by this alert rule.
            trigger-operator: The operation against the threshold that triggers alert rule.
            trigger-threshold: The threshold triggers this alert rule.
            alert-rule-template-name: The Name of the alert rule template used to create this rule.
            description: The description of the alert rule.
            display-name: The display name for alerts created by this alert rule.
            enabled: Determines whether this alert rule is enabled or disabled.
            suppression-duration: The suppression (in ISO 8601 duration format) to wait since last time this alert \
rule been triggered.
            suppression-enabled: Determines whether the suppression for this alert rule is enabled or disabled.
            tactics: The tactics of the alert rule
            kind: Required. The alert rule kind
            etag: Etag of the azure resource
"""

helps['sentinel alert-rule delete'] = """
    type: command
    short-summary: "Delete the action of alert rule. And Delete the alert rule."
    examples:
      - name: Delete an action of alert rule.
        text: |-
               az sentinel alert-rule delete --action-id "912bec42-cb66-4c03-ac63-1761b6898c3e" --resource-group \
"myRg" --rule-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --workspace-name "myWorkspace"
      - name: Delete an alert rule.
        text: |-
               az sentinel alert-rule delete --resource-group "myRg" --rule-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" \
--workspace-name "myWorkspace"
"""

helps['sentinel alert-rule show-action'] = """
    type: command
    short-summary: "Gets the action of alert rule."
    examples:
      - name: Get an action of alert rule.
        text: |-
               az sentinel alert-rule show-action --action-id "912bec42-cb66-4c03-ac63-1761b6898c3e" --resource-group \
"myRg" --rule-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --workspace-name "myWorkspace"
"""

helps['sentinel action'] = """
    type: group
    short-summary: Manage action with sentinel
"""

helps['sentinel action list'] = """
    type: command
    short-summary: "Gets all actions of alert rule."
    examples:
      - name: Get all actions of alert rule.
        text: |-
               az sentinel action list --resource-group "myRg" --rule-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" \
--workspace-name "myWorkspace"
"""

helps['sentinel alert-rule-template'] = """
    type: group
    short-summary: Manage alert rule template with sentinel
"""

helps['sentinel alert-rule-template list'] = """
    type: command
    short-summary: "Gets all alert rule templates."
    examples:
      - name: Get all alert rule templates.
        text: |-
               az sentinel alert-rule-template list --resource-group "myRg" --workspace-name "myWorkspace"
"""

helps['sentinel alert-rule-template show'] = """
    type: command
    short-summary: "Gets the alert rule template."
    examples:
      - name: Get alert rule template by Id.
        text: |-
               az sentinel alert-rule-template show --alert-rule-template-id "65360bb0-8986-4ade-a89d-af3cf44d28aa" \
--resource-group "myRg" --workspace-name "myWorkspace"
"""

helps['sentinel bookmark'] = """
    type: group
    short-summary: Manage bookmark with sentinel
"""

helps['sentinel bookmark list'] = """
    type: command
    short-summary: "Gets all bookmarks."
    examples:
      - name: Get all bookmarks.
        text: |-
               az sentinel bookmark list --resource-group "myRg" --workspace-name "myWorkspace"
"""

helps['sentinel bookmark show'] = """
    type: command
    short-summary: "Gets a bookmark."
    examples:
      - name: Get a bookmark.
        text: |-
               az sentinel bookmark show --bookmark-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" \
--workspace-name "myWorkspace"
"""

helps['sentinel bookmark create'] = """
    type: command
    short-summary: "Create the bookmark."
    parameters:
      - name: --incident-info
        short-summary: "Describes an incident that relates to bookmark"
        long-summary: |
            Usage: --incident-info incident-id=XX severity=XX title=XX relation-name=XX

            incident-id: Required. Incident Id
            severity: Required. The severity of the incident
            title: Required. The title of the incident
            relation-name: Required. Relation Name
    examples:
      - name: Creates or updates a bookmark.
        text: |-
               az sentinel bookmark create --etag "\\"0300bf09-0000-0000-0000-5c37296e0000\\"" --created \
"2019-01-01T13:15:30Z" --user-info-object-id "2046feea-040d-4a46-9e2b-91c2941bfa70" --display-name "My bookmark" \
--labels "Tag1" "Tag2" --notes "Found a suspicious activity" --query "SecurityEvent | where TimeGenerated > ago(1d) \
and TimeGenerated < ago(2d)" --query-result "Security Event query result" --updated "2019-01-01T13:15:30Z" --object-id \
"2046feea-040d-4a46-9e2b-91c2941bfa70" --bookmark-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" \
--workspace-name "myWorkspace"
"""

helps['sentinel bookmark update'] = """
    type: command
    short-summary: "Update the bookmark."
    parameters:
      - name: --incident-info
        short-summary: "Describes an incident that relates to bookmark"
        long-summary: |
            Usage: --incident-info incident-id=XX severity=XX title=XX relation-name=XX

            incident-id: Required. Incident Id
            severity: Required. The severity of the incident
            title: Required. The title of the incident
            relation-name: Required. Relation Name
"""

helps['sentinel bookmark delete'] = """
    type: command
    short-summary: "Delete the bookmark."
    examples:
      - name: Delete a bookmark.
        text: |-
               az sentinel bookmark delete --bookmark-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group \
"myRg" --workspace-name "myWorkspace"
"""

helps['sentinel data-connector'] = """
    type: group
    short-summary: Manage data connector with sentinel
"""

helps['sentinel data-connector list'] = """
    type: command
    short-summary: "Gets all data connectors."
    examples:
      - name: Get all data connectors.
        text: |-
               az sentinel data-connector list --resource-group "myRg" --workspace-name "myWorkspace"
"""

helps['sentinel data-connector show'] = """
    type: command
    short-summary: "Gets a data connector."
    examples:
      - name: Get a ASC data connector.
        text: |-
               az sentinel data-connector show --data-connector-id "763f9fa1-c2d3-4fa2-93e9-bccd4899aa12" \
--resource-group "myRg" --workspace-name "myWorkspace"
      - name: Get a MCAS data connector.
        text: |-
               az sentinel data-connector show --data-connector-id "b96d014d-b5c2-4a01-9aba-a8058f629d42" \
--resource-group "myRg" --workspace-name "myWorkspace"
      - name: Get a MDATP data connector
        text: |-
               az sentinel data-connector show --data-connector-id "06b3ccb8-1384-4bcc-aec7-852f6d57161b" \
--resource-group "myRg" --workspace-name "myWorkspace"
      - name: Get a TI data connector.
        text: |-
               az sentinel data-connector show --data-connector-id "c345bf40-8509-4ed2-b947-50cb773aaf04" \
--resource-group "myRg" --workspace-name "myWorkspace"
      - name: Get an AAD data connector.
        text: |-
               az sentinel data-connector show --data-connector-id "f0cd27d2-5f03-4c06-ba31-d2dc82dcb51d" \
--resource-group "myRg" --workspace-name "myWorkspace"
      - name: Get an AATP data connector.
        text: |-
               az sentinel data-connector show --data-connector-id "07e42cb3-e658-4e90-801c-efa0f29d3d44" \
--resource-group "myRg" --workspace-name "myWorkspace"
      - name: Get an AwsCloudTrail data connector.
        text: |-
               az sentinel data-connector show --data-connector-id "c345bf40-8509-4ed2-b947-50cb773aaf04" \
--resource-group "myRg" --workspace-name "myWorkspace"
      - name: Get an Office365 data connector.
        text: |-
               az sentinel data-connector show --data-connector-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" \
--resource-group "myRg" --workspace-name "myWorkspace"
"""

helps['sentinel data-connector create'] = """
    type: command
    short-summary: "Create the data connector."
    parameters:
      - name: --aad-data-connector
        short-summary: "Represents AAD (Azure Active Directory) data connector."
        long-summary: |
            Usage: --aad-data-connector tenant-id=XX state=XX kind=XX etag=XX

            tenant-id: The tenant id to connect to, and get the data from.
            state: Describe whether this data type connection is enabled or not.
            kind: Required. The data connector kind
            etag: Etag of the azure resource
      - name: --aatp-data-connector
        short-summary: "Represents AATP (Azure Advanced Threat Protection) data connector."
        long-summary: |
            Usage: --aatp-data-connector tenant-id=XX state=XX kind=XX etag=XX

            tenant-id: The tenant id to connect to, and get the data from.
            state: Describe whether this data type connection is enabled or not.
            kind: Required. The data connector kind
            etag: Etag of the azure resource
      - name: --asc-data-connector
        short-summary: "Represents ASC (Azure Security Center) data connector."
        long-summary: |
            Usage: --asc-data-connector subscription-id=XX state=XX kind=XX etag=XX

            subscription-id: The subscription id to connect to, and get the data from.
            state: Describe whether this data type connection is enabled or not.
            kind: Required. The data connector kind
            etag: Etag of the azure resource
      - name: --aws-cloud-trail-data-connector
        short-summary: "Represents Amazon Web Services CloudTrail data connector."
        long-summary: |
            Usage: --aws-cloud-trail-data-connector aws-role-arn=XX state=XX kind=XX etag=XX

            aws-role-arn: The Aws Role Arn (with CloudTrailReadOnly policy) that is used to access the Aws account.
            state: Describe whether this data type connection is enabled or not.
            kind: Required. The data connector kind
            etag: Etag of the azure resource
      - name: --mcas-data-connector
        short-summary: "Represents MCAS (Microsoft Cloud App Security) data connector."
        long-summary: |
            Usage: --mcas-data-connector tenant-id=XX state-properties-data-types-alerts-state=XX \
state-properties-data-types-discovery-logs-state=XX kind=XX etag=XX

            tenant-id: The tenant id to connect to, and get the data from.
            state-properties-data-types-alerts-state: Describe whether this data type connection is enabled or not.
            state-properties-data-types-discovery-logs-state: Describe whether this data type connection is enabled or \
not.
            kind: Required. The data connector kind
            etag: Etag of the azure resource
      - name: --mdatp-data-connector
        short-summary: "Represents MDATP (Microsoft Defender Advanced Threat Protection) data connector."
        long-summary: |
            Usage: --mdatp-data-connector tenant-id=XX state=XX kind=XX etag=XX

            tenant-id: The tenant id to connect to, and get the data from.
            state: Describe whether this data type connection is enabled or not.
            kind: Required. The data connector kind
            etag: Etag of the azure resource
      - name: --office-data-connector
        short-summary: "Represents office data connector."
        long-summary: |
            Usage: --office-data-connector tenant-id=XX state-properties-data-types-teams-state=XX \
state-properties-data-types-share-point-state=XX state-properties-data-types-exchange-state=XX kind=XX etag=XX

            tenant-id: The tenant id to connect to, and get the data from.
            state-properties-data-types-teams-state: Describe whether this data type connection is enabled or not.
            state-properties-data-types-share-point-state: Describe whether this data type connection is enabled or \
not.
            state-properties-data-types-exchange-state: Describe whether this data type connection is enabled or not.
            kind: Required. The data connector kind
            etag: Etag of the azure resource
      - name: --ti-data-connector
        short-summary: "Represents threat intelligence data connector."
        long-summary: |
            Usage: --ti-data-connector tenant-id=XX state=XX kind=XX etag=XX

            tenant-id: The tenant id to connect to, and get the data from.
            state: Describe whether this data type connection is enabled or not.
            kind: Required. The data connector kind
            etag: Etag of the azure resource
    examples:
      - name: Creates or updates an Office365 data connector.
        text: |-
               az sentinel data-connector create --office-data-connector etag="\\"0300bf09-0000-0000-0000-5c37296e0000\
\\"" tenant-id="2070ecc9-b4d5-4ae4-adaa-936fa1954fa8" state-properties-data-types-exchange-state="Enabled" \
--data-connector-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" --workspace-name "myWorkspace"
"""

helps['sentinel data-connector update'] = """
    type: command
    short-summary: "Update the data connector."
    parameters:
      - name: --aad-data-connector
        short-summary: "Represents AAD (Azure Active Directory) data connector."
        long-summary: |
            Usage: --aad-data-connector tenant-id=XX state=XX kind=XX etag=XX

            tenant-id: The tenant id to connect to, and get the data from.
            state: Describe whether this data type connection is enabled or not.
            kind: Required. The data connector kind
            etag: Etag of the azure resource
      - name: --aatp-data-connector
        short-summary: "Represents AATP (Azure Advanced Threat Protection) data connector."
        long-summary: |
            Usage: --aatp-data-connector tenant-id=XX state=XX kind=XX etag=XX

            tenant-id: The tenant id to connect to, and get the data from.
            state: Describe whether this data type connection is enabled or not.
            kind: Required. The data connector kind
            etag: Etag of the azure resource
      - name: --asc-data-connector
        short-summary: "Represents ASC (Azure Security Center) data connector."
        long-summary: |
            Usage: --asc-data-connector subscription-id=XX state=XX kind=XX etag=XX

            subscription-id: The subscription id to connect to, and get the data from.
            state: Describe whether this data type connection is enabled or not.
            kind: Required. The data connector kind
            etag: Etag of the azure resource
      - name: --aws-cloud-trail-data-connector
        short-summary: "Represents Amazon Web Services CloudTrail data connector."
        long-summary: |
            Usage: --aws-cloud-trail-data-connector aws-role-arn=XX state=XX kind=XX etag=XX

            aws-role-arn: The Aws Role Arn (with CloudTrailReadOnly policy) that is used to access the Aws account.
            state: Describe whether this data type connection is enabled or not.
            kind: Required. The data connector kind
            etag: Etag of the azure resource
      - name: --mcas-data-connector
        short-summary: "Represents MCAS (Microsoft Cloud App Security) data connector."
        long-summary: |
            Usage: --mcas-data-connector tenant-id=XX state-properties-data-types-alerts-state=XX \
state-properties-data-types-discovery-logs-state=XX kind=XX etag=XX

            tenant-id: The tenant id to connect to, and get the data from.
            state-properties-data-types-alerts-state: Describe whether this data type connection is enabled or not.
            state-properties-data-types-discovery-logs-state: Describe whether this data type connection is enabled or \
not.
            kind: Required. The data connector kind
            etag: Etag of the azure resource
      - name: --mdatp-data-connector
        short-summary: "Represents MDATP (Microsoft Defender Advanced Threat Protection) data connector."
        long-summary: |
            Usage: --mdatp-data-connector tenant-id=XX state=XX kind=XX etag=XX

            tenant-id: The tenant id to connect to, and get the data from.
            state: Describe whether this data type connection is enabled or not.
            kind: Required. The data connector kind
            etag: Etag of the azure resource
      - name: --office-data-connector
        short-summary: "Represents office data connector."
        long-summary: |
            Usage: --office-data-connector tenant-id=XX state-properties-data-types-teams-state=XX \
state-properties-data-types-share-point-state=XX state-properties-data-types-exchange-state=XX kind=XX etag=XX

            tenant-id: The tenant id to connect to, and get the data from.
            state-properties-data-types-teams-state: Describe whether this data type connection is enabled or not.
            state-properties-data-types-share-point-state: Describe whether this data type connection is enabled or \
not.
            state-properties-data-types-exchange-state: Describe whether this data type connection is enabled or not.
            kind: Required. The data connector kind
            etag: Etag of the azure resource
      - name: --ti-data-connector
        short-summary: "Represents threat intelligence data connector."
        long-summary: |
            Usage: --ti-data-connector tenant-id=XX state=XX kind=XX etag=XX

            tenant-id: The tenant id to connect to, and get the data from.
            state: Describe whether this data type connection is enabled or not.
            kind: Required. The data connector kind
            etag: Etag of the azure resource
"""

helps['sentinel data-connector delete'] = """
    type: command
    short-summary: "Delete the data connector."
    examples:
      - name: Delete an Office365 data connector.
        text: |-
               az sentinel data-connector delete --data-connector-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" \
--resource-group "myRg" --workspace-name "myWorkspace"
"""

helps['sentinel incident'] = """
    type: group
    short-summary: Manage incident with sentinel
"""

helps['sentinel incident list'] = """
    type: command
    short-summary: "Gets all incidents."
    examples:
      - name: Get all incidents.
        text: |-
               az sentinel incident list --orderby "properties/createdTimeUtc desc" --top 1 --resource-group "myRg" \
--workspace-name "myWorkspace"
"""

helps['sentinel incident show'] = """
    type: command
    short-summary: "Gets an incident."
    examples:
      - name: Get an incident.
        text: |-
               az sentinel incident show --incident-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" \
--workspace-name "myWorkspace"
"""

helps['sentinel incident create'] = """
    type: command
    short-summary: "Create the incident."
    parameters:
      - name: --labels
        short-summary: "List of labels relevant to this incident"
        long-summary: |
            Usage: --labels label-name=XX

            label-name: Required. The name of the label

            Multiple actions can be specified by using more than one --labels argument.
      - name: --owner
        short-summary: "Describes a user that the incident is assigned to"
        long-summary: |
            Usage: --owner email=XX assigned-to=XX object-id=XX user-principal-name=XX

            email: The email of the user the incident is assigned to.
            assigned-to: The name of the user the incident is assigned to.
            object-id: The object id of the user the incident is assigned to.
            user-principal-name: The user principal name of the user the incident is assigned to.
    examples:
      - name: Creates or updates an incident.
        text: |-
               az sentinel incident create --etag "\\"0300bf09-0000-0000-0000-5c37296e0000\\"" --description "This is \
a demo incident" --classification "FalsePositive" --classification-comment "Not a malicious activity" \
--classification-reason "IncorrectAlertLogic" --first-activity-time-utc "2019-01-01T13:00:30Z" \
--last-activity-time-utc "2019-01-01T13:05:30Z" --owner object-id="2046feea-040d-4a46-9e2b-91c2941bfa70" --severity \
"High" --status "Closed" --title "My incident" --incident-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group \
"myRg" --workspace-name "myWorkspace"
"""

helps['sentinel incident update'] = """
    type: command
    short-summary: "Update the incident."
    parameters:
      - name: --labels
        short-summary: "List of labels relevant to this incident"
        long-summary: |
            Usage: --labels label-name=XX

            label-name: Required. The name of the label

            Multiple actions can be specified by using more than one --labels argument.
      - name: --owner
        short-summary: "Describes a user that the incident is assigned to"
        long-summary: |
            Usage: --owner email=XX assigned-to=XX object-id=XX user-principal-name=XX

            email: The email of the user the incident is assigned to.
            assigned-to: The name of the user the incident is assigned to.
            object-id: The object id of the user the incident is assigned to.
            user-principal-name: The user principal name of the user the incident is assigned to.
"""

helps['sentinel incident delete'] = """
    type: command
    short-summary: "Delete the incident."
    examples:
      - name: Delete an incident.
        text: |-
               az sentinel incident delete --incident-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group \
"myRg" --workspace-name "myWorkspace"
"""

helps['sentinel incident-comment'] = """
    type: group
    short-summary: Manage incident comment with sentinel
"""

helps['sentinel incident-comment list'] = """
    type: command
    short-summary: "Gets all incident comments."
    examples:
      - name: Get all incident comments.
        text: |-
               az sentinel incident-comment list --incident-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group \
"myRg" --workspace-name "myWorkspace"
"""

helps['sentinel incident-comment show'] = """
    type: command
    short-summary: "Gets an incident comment."
    examples:
      - name: Get an incident comment.
        text: |-
               az sentinel incident-comment show --incident-comment-id "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014" \
--incident-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" --workspace-name "myWorkspace"
"""

helps['sentinel incident-comment create'] = """
    type: command
    short-summary: "Creates or updates the incident comment."
    examples:
      - name: Creates or updates an incident comment.
        text: |-
               az sentinel incident-comment create --message "Some message" --incident-comment-id \
"4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014" --incident-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" \
--workspace-name "myWorkspace"
"""

helps['sentinel incident-comment delete'] = """
    type: command
    short-summary: "Delete the incident comment."
    examples:
      - name: Delete the incident comment.
        text: |-
               az sentinel incident-comment delete --incident-comment-id "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014" \
--incident-id "73e01a98-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" --workspace-name "myWorkspace"
"""
