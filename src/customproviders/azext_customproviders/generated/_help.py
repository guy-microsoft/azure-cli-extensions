# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['customproviders custom-resource-provider'] = """
    type: group
    short-summary: customproviders custom-resource-provider
"""

helps['customproviders custom-resource-provider list'] = """
    type: command
    short-summary: Gets all the custom resource providers within a subscription.
    examples:
      - name: List all custom resource providers on the resourceGroup
        text: |-
               az customproviders custom-resource-provider list --resource-group "testRG"
"""

helps['customproviders custom-resource-provider show'] = """
    type: command
    short-summary: Gets the custom resource provider manifest.
    examples:
      - name: Get a custom resource provider
        text: |-
               az customproviders custom-resource-provider show --resource-group "testRG"
               --resource-provider-name "newrp"
"""

helps['customproviders custom-resource-provider create'] = """
    type: command
    short-summary: Creates or updates the custom resource provider.
    examples:
      - name: Create or update the custom resource provider
        text: |-
               az customproviders custom-resource-provider create --resource-group "testRG" --location
               "eastus" --properties-actions
               name=TestAction endpoint=https://mytestendpoint/ routing-type=Proxy
               --properties-resource-types
               name=TestResource endpoint=https://mytestendpoint2/ routing-type=Proxy,Cache
               --resource-provider-name "newrp"
"""

helps['customproviders custom-resource-provider update'] = """
    type: command
    short-summary: Updates an existing custom resource provider. The only value that can be updated via PATCH currently is the tags.
    examples:
      - name: Update a custom resource provider
        text: |-
               az customproviders custom-resource-provider update --resource-group "testRG"
               --resource-provider-name "newrp"
"""

helps['customproviders custom-resource-provider delete'] = """
    type: command
    short-summary: Deletes the custom resource provider.
    examples:
      - name: Delete a custom resource provider
        text: |-
               az customproviders custom-resource-provider delete --resource-group "testRG"
               --resource-provider-name "newrp"
"""

helps['customproviders association'] = """
    type: group
    short-summary: customproviders association
"""

helps['customproviders association list'] = """
    type: command
    short-summary: Gets all association for the given scope.
    examples:
      - name: Get all associations
        text: |-
               az customproviders association list --scope "scope"
"""

helps['customproviders association show'] = """
    type: command
    short-summary: Get an association.
    examples:
      - name: Get an association
        text: |-
               az customproviders association show --association-name "associationName" --scope "scope"
"""

helps['customproviders association create'] = """
    type: command
    short-summary: Create or update an association.
    examples:
      - name: Create or update an association
        text: |-
               az customproviders association create --properties-target-resource-id "/subscriptions/0000
               0000-0000-0000-0000-000000000000/resourceGroups/appRG/providers/Microsoft.Solutions/applic
               ations/applicationName" --association-name "associationName" --scope "scope"
"""

helps['customproviders association update'] = """
    type: command
    short-summary: Create or update an association.
    examples:
      - name: Create or update an association
        text: |-
               az customproviders association create --properties-target-resource-id "/subscriptions/0000
               0000-0000-0000-0000-000000000000/resourceGroups/appRG/providers/Microsoft.Solutions/applic
               ations/applicationName" --association-name "associationName" --scope "scope"
"""

helps['customproviders association delete'] = """
    type: command
    short-summary: Delete an association.
    examples:
      - name: Delete an association
        text: |-
               az customproviders association delete --association-name "associationName" --scope
               "scope"
"""
