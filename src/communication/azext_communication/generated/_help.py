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


helps['communication'] = """
    type: group
    short-summary: communication
"""

helps['communication list'] = """
    type: command
    short-summary: "Handles requests to list all resources in a resource group. And Handles requests to list all \
resources in a subscription."
    examples:
      - name: List by resource group
        text: |-
               az communication list --resource-group "MyResourceGroup"
      - name: List by subscription
        text: |-
               az communication list
"""

helps['communication show'] = """
    type: command
    short-summary: "Get the CommunicationService and its properties."
    examples:
      - name: Get resource
        text: |-
               az communication show --name "MyCommunicationResource" --resource-group "MyResourceGroup"
"""

helps['communication create'] = """
    type: command
    short-summary: "Create a new CommunicationService or update an existing CommunicationService."
    examples:
      - name: Create or update resource
        text: |-
               az communication create --name "MyCommunicationResource" --location "Global" --data-location "United \
States" --resource-group "MyResourceGroup"
"""

helps['communication update'] = """
    type: command
    short-summary: "Operation to update an existing CommunicationService."
    examples:
      - name: Update resource
        text: |-
               az communication update --name "MyCommunicationResource" --tags newTag="newVal" --resource-group \
"MyResourceGroup"
"""

helps['communication delete'] = """
    type: command
    short-summary: "Operation to delete a CommunicationService."
    examples:
      - name: Delete resource
        text: |-
               az communication delete --name "MyCommunicationResource" --resource-group "MyResourceGroup"
"""

helps['communication link-notification-hub'] = """
    type: command
    short-summary: "Links an Azure Notification Hub to this communication service."
    examples:
      - name: Link notification hub
        text: |-
               az communication link-notification-hub --name "MyCommunicationResource" --connection-string \
"Endpoint=sb://MyNamespace.servicebus.windows.net/;SharedAccessKey=abcd1234" --resource-id \
"/subscriptions/12345/resourceGroups/MyOtherResourceGroup/providers/Microsoft.NotificationHubs/namespaces/MyNamespace/n\
otificationHubs/MyHub" --resource-group "MyResourceGroup"
"""

helps['communication list-key'] = """
    type: command
    short-summary: "Get the access keys of the CommunicationService resource."
    examples:
      - name: List keys
        text: |-
               az communication list-key --name "MyCommunicationResource" --resource-group "MyResourceGroup"
"""

helps['communication regenerate-key'] = """
    type: command
    short-summary: "Regenerate CommunicationService access key. PrimaryKey and SecondaryKey cannot be regenerated at \
the same time."
    examples:
      - name: Regenerate key
        text: |-
               az communication regenerate-key --name "MyCommunicationResource" --key-type "Primary" --resource-group \
"MyResourceGroup"
"""

helps['communication wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the communication is met.
    examples:
      - name: Pause executing next line of CLI script until the communication is successfully created.
        text: |-
               az communication wait --name "MyCommunicationResource" --resource-group "MyResourceGroup" --created
      - name: Pause executing next line of CLI script until the communication is successfully deleted.
        text: |-
               az communication wait --name "MyCommunicationResource" --resource-group "MyResourceGroup" --deleted
"""

helps['communication'] = """
    type: group
    short-summary: communication
"""

helps['communication show-status'] = """
    type: command
    short-summary: "Gets the current status of an async operation."
    examples:
      - name: Get OperationStatus
        text: |-
               az communication show-status --operation-id "db5f291f-284d-46e9-9152-d5c83f7c14b8" --location "westus2"
"""
