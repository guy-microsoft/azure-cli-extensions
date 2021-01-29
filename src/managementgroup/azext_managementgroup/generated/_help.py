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


helps['managementgroup management-group'] = """
    type: group
    short-summary: Manage management group with managementgroup
"""

helps['managementgroup management-group list'] = """
    type: command
    short-summary: "List management groups for the authenticated user."
    examples:
      - name: ListManagementGroups
        text: |-
               az managementgroup management-group list --cache-control "no-cache"
"""

helps['managementgroup management-group show'] = """
    type: command
    short-summary: "Get the details of the management group."
    examples:
      - name: GetManagementGroup
        text: |-
               az managementgroup management-group show --cache-control "no-cache" --group-id \
"20000000-0001-0000-0000-000000000000"
      - name: GetManagementGroupWithExpand
        text: |-
               az managementgroup management-group show --expand "children" --cache-control "no-cache" --group-id \
"20000000-0001-0000-0000-000000000000"
      - name: GetManagementGroupsWithExpandAndRecurse
        text: |-
               az managementgroup management-group show --expand "children" --recurse true --cache-control "no-cache" \
--group-id "20000000-0001-0000-0000-000000000000"
"""

helps['managementgroup management-group create'] = """
    type: command
    short-summary: "Create a management group. If a management group is already created and a subsequent create \
request is issued with different properties, the management group properties will be updated."
    examples:
      - name: PutManagementGroup
        text: |-
               az managementgroup management-group create --cache-control "no-cache" --display-name "ChildGroup" --id \
"/providers/Microsoft.Management/managementGroups/RootGroup" --group-id "ChildGroup"
"""

helps['managementgroup management-group update'] = """
    type: command
    short-summary: "Update a management group."
    examples:
      - name: PatchManagementGroup
        text: |-
               az managementgroup management-group update --cache-control "no-cache" --group-id "ChildGroup" \
--display-name "AlternateDisplayName" --parent-group-id "/providers/Microsoft.Management/managementGroups/AlternateRoot\
Group"
"""

helps['managementgroup management-group delete'] = """
    type: command
    short-summary: "Delete management group. If a management group contains child resources, the request will fail."
    examples:
      - name: DeleteManagementGroup
        text: |-
               az managementgroup management-group delete --cache-control "no-cache" --group-id "GroupToDelete"
"""

helps['managementgroup management-group show-descendant'] = """
    type: command
    short-summary: "List all entities that descend from a management group."
    examples:
      - name: GetDescendants
        text: |-
               az managementgroup management-group show-descendant --group-id "20000000-0000-0000-0000-000000000000"
"""

helps['managementgroup management-group wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the managementgroup management-group is met.
    examples:
      - name: Pause executing next line of CLI script until the managementgroup management-group is successfully \
created.
        text: |-
               az managementgroup management-group wait --expand "children" --recurse true --cache-control "no-cache" \
--group-id "20000000-0001-0000-0000-000000000000" --created
      - name: Pause executing next line of CLI script until the managementgroup management-group is successfully \
deleted.
        text: |-
               az managementgroup management-group wait --expand "children" --recurse true --cache-control "no-cache" \
--group-id "20000000-0001-0000-0000-000000000000" --deleted
"""

helps['managementgroup management-group-subscription'] = """
    type: group
    short-summary: Manage management group subscription with managementgroup
"""

helps['managementgroup management-group-subscription create'] = """
    type: command
    short-summary: "Associates existing subscription with the management group."
    examples:
      - name: AddSubscriptionToManagementGroup
        text: |-
               az managementgroup management-group-subscription create --cache-control "no-cache" --group-id "Group" \
--subscription-id "728bcbe4-8d56-4510-86c2-4921b8beefbc"
"""

helps['managementgroup management-group-subscription delete'] = """
    type: command
    short-summary: "De-associates subscription from the management group."
    examples:
      - name: DeleteSubscriptionFromManagementGroup
        text: |-
               az managementgroup management-group-subscription delete --cache-control "no-cache" --group-id "Group" \
--subscription-id "728bcbe4-8d56-4510-86c2-4921b8beefbc"
"""

helps['managementgroup management-group-subscription show-subscription'] = """
    type: command
    short-summary: "Retrieves details about given subscription which is associated with the management group."
    examples:
      - name: GetSubscriptionFromManagementGroup
        text: |-
               az managementgroup management-group-subscription show-subscription --cache-control "no-cache" \
--group-id "Group" --subscription-id "728bcbe4-8d56-4510-86c2-4921b8beefbc"
"""

helps['managementgroup management-group-subscription show-subscription-under-management-group'] = """
    type: command
    short-summary: "Retrieves details about all subscriptions which are associated with the management group."
    examples:
      - name: GetAllSubscriptionsFromManagementGroup
        text: |-
               az managementgroup management-group-subscription show-subscription-under-management-group --group-id \
"Group"
"""

helps['managementgroup hierarchy-setting'] = """
    type: group
    short-summary: Manage hierarchy setting with managementgroup
"""

helps['managementgroup hierarchy-setting list'] = """
    type: command
    short-summary: "Gets all the hierarchy settings defined at the Management Group level. Settings can only be set on \
the root Management Group of the hierarchy."
    examples:
      - name: ListGroupSettings
        text: |-
               az managementgroup hierarchy-setting list --group-id "root"
"""

helps['managementgroup hierarchy-setting show'] = """
    type: command
    short-summary: "Gets the hierarchy settings defined at the Management Group level. Settings can only be set on the \
root Management Group of the hierarchy."
    examples:
      - name: GetGroupSettings
        text: |-
               az managementgroup hierarchy-setting show --group-id "root"
"""

helps['managementgroup hierarchy-setting create'] = """
    type: command
    short-summary: "Create the hierarchy settings defined at the Management Group level."
    examples:
      - name: GetGroupSettings
        text: |-
               az managementgroup hierarchy-setting create --default-management-group "/providers/Microsoft.Management/\
managementGroups/DefaultGroup" --require-authorization-for-group-creation true --group-id "root"
"""

helps['managementgroup hierarchy-setting update'] = """
    type: command
    short-summary: "Updates the hierarchy settings defined at the Management Group level."
    examples:
      - name: GetGroupSettings
        text: |-
               az managementgroup hierarchy-setting update --default-management-group "/providers/Microsoft.Management/\
managementGroups/DefaultGroup" --require-authorization-for-group-creation true --group-id "root"
"""

helps['managementgroup hierarchy-setting delete'] = """
    type: command
    short-summary: "Deletes the hierarchy settings defined at the Management Group level."
    examples:
      - name: GetGroupSettings
        text: |-
               az managementgroup hierarchy-setting delete --group-id "root"
"""

helps['managementgroup'] = """
    type: group
    short-summary: Manage  with managementgroup
"""

helps['managementgroup start-tenant-backfill'] = """
    type: command
    short-summary: "Starts backfilling subscriptions for the Tenant."
    examples:
      - name: StartTenantBackfill
        text: |-
               az managementgroup start-tenant-backfill
"""

helps['managementgroup tenant-backfill-status'] = """
    type: command
    short-summary: "Gets tenant backfill status."
    examples:
      - name: TenantBackfillStatus
        text: |-
               az managementgroup tenant-backfill-status
"""

helps['managementgroup entity'] = """
    type: group
    short-summary: Manage entity with managementgroup
"""

helps['managementgroup entity list'] = """
    type: command
    short-summary: "List all entities (Management Groups, Subscriptions, etc.) for the authenticated user."
    examples:
      - name: GetEntities
        text: |-
               az managementgroup entity list
"""
