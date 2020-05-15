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


helps['windowsiotservices service'] = """
    type: group
    short-summary: windowsiotservices service
"""

helps['windowsiotservices service list'] = """
    type: command
    short-summary: Get all the IoT hubs in a subscription.
    examples:
      - name: Service_ListByResourceGroup
        text: |-
               az windowsiotservices service list --resource-group "res6117"
"""

helps['windowsiotservices service show'] = """
    type: command
    short-summary: Get the non-security related metadata of a Windows IoT Device Service.
    examples:
      - name: Services_GetProperties
        text: |-
               az windowsiotservices service show --device-name "service8596" --resource-group "res9407"
"""

helps['windowsiotservices service create'] = """
    type: command
    short-summary: Create or update the metadata of a Windows IoT Device Service. The usual pattern to modify a propert\
y is to retrieve the Windows IoT Device Service metadata and security metadata, and then combine them with the modified\
 values in a new body to update the Windows IoT Device Service.
    examples:
      - name: Service_Create
        text: |-
               az windowsiotservices service create --device-name "service4445" --admin-domain-name "d.e.f" --billing-d\
omain-name "a.b.c" --notes "blah" --quantity 1000000 --resource-group "res9101"
"""

helps['windowsiotservices service update'] = """
    type: command
    short-summary: Updates the metadata of a Windows IoT Device Service. The usual pattern to modify a property is to r\
etrieve the Windows IoT Device Service metadata and security metadata, and then combine them with the modified values i\
n a new body to update the Windows IoT Device Service.
    examples:
      - name: Service_Update
        text: |-
               az windowsiotservices service update --device-name "service8596" --admin-domain-name "d.e.f" --billing-d\
omain-name "a.b.c" --notes "blah" --quantity 1000000 --resource-group "res9407"
"""

helps['windowsiotservices service delete'] = """
    type: command
    short-summary: Delete a Windows IoT Device Service.
    examples:
      - name: Service_Delete
        text: |-
               az windowsiotservices service delete --device-name "service2434" --resource-group "res4228"
"""

helps['windowsiotservices service check-device-service-name-availability'] = """
    type: command
    short-summary: Check if a Windows IoT Device Service name is available.
    examples:
      - name: Service_CheckNameAvailability
        text: |-
               az windowsiotservices service check-device-service-name-availability --name "service3363"
"""