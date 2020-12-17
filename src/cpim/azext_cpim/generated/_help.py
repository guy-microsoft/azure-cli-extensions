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


helps['cpim b2-c-tenant'] = """
    type: group
    short-summary: cpim b2-c-tenant
"""

helps['cpim b2-c-tenant list'] = """
    type: command
    short-summary: "Get all the Azure AD B2C tenant resources in a resource group. And Get all the Azure AD B2C tenant \
resources in a subscription."
    examples:
      - name: B2CTenants_ListByResourceGroup
        text: |-
               az cpim b2-c-tenant list --resource-group "contosoResourceGroup"
      - name: B2CTenants_ListBySubscription
        text: |-
               az cpim b2-c-tenant list
"""

helps['cpim b2-c-tenant show'] = """
    type: command
    short-summary: "Get the Azure AD B2C tenant resource."
    examples:
      - name: Get tenant
        text: |-
               az cpim b2-c-tenant show --resource-group "contosoResourceGroup" --resource-name \
"contoso.onmicrosoft.com"
"""

helps['cpim b2-c-tenant create'] = """
    type: command
    short-summary: "Initiates an async request to create both the Azure AD B2C tenant and the corresponding Azure \
resource linked to a subscription."
    parameters:
      - name: --properties
        long-summary: |
            Usage: --properties display-name=XX country-code=XX

            display-name: The display name of the B2C tenant.
            country-code: Country code of Azure tenant (e.g. 'US'). Refer to `aka.ms/B2CDataResidency \
<https://aka.ms/B2CDataResidency>`_ to see valid country codes and corresponding data residency locations. If you do \
not see a country code in an valid data residency location, choose one from the list.
    examples:
      - name: Create tenant
        text: |-
               az cpim b2-c-tenant create --location "United States" --properties display-name="Contoso" \
country-code="US" --sku-name "Standard" --resource-group "contosoResourceGroup" --resource-name \
"contoso.onmicrosoft.com"
"""

helps['cpim b2-c-tenant update'] = """
    type: command
    short-summary: "Update the Azure AD B2C tenant resource."
    examples:
      - name: Get tenant
        text: |-
               az cpim b2-c-tenant update --resource-group "contosoResourceGroup" --resource-name \
"contoso.onmicrosoft.com" --sku-name "PremiumP1" --tags key="value"
"""

helps['cpim b2-c-tenant delete'] = """
    type: command
    short-summary: "Initiates an async operation to delete the Azure AD B2C tenant and Azure resource. The resource \
deletion can only happen as the last step in `the tenant deletion process <https://aka.ms/deleteB2Ctenant>`_."
    examples:
      - name: Delete tenant
        text: |-
               az cpim b2-c-tenant delete --resource-group "rg1" --resource-name "contoso.onmicrosoft.com"
"""

helps['cpim b2-c-tenant wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the cpim b2-c-tenant is met.
    examples:
      - name: Pause executing next line of CLI script until the cpim b2-c-tenant is successfully created.
        text: |-
               az cpim b2-c-tenant wait --resource-group "contosoResourceGroup" --resource-name \
"contoso.onmicrosoft.com" --created
      - name: Pause executing next line of CLI script until the cpim b2-c-tenant is successfully deleted.
        text: |-
               az cpim b2-c-tenant wait --resource-group "contosoResourceGroup" --resource-name \
"contoso.onmicrosoft.com" --deleted
"""

helps['cpim operation'] = """
    type: group
    short-summary: cpim operation
"""

helps['cpim operation get-async-status'] = """
    type: command
    short-summary: "Gets the status of the async operation."
    examples:
      - name: Get Async Status
        text: |-
               az cpim operation get-async-status --operation-id "99999999-9999-9999-9999-999999999999"
"""
