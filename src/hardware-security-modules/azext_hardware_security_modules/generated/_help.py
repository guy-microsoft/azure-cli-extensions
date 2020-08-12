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


helps['hardware-security-modules dedicated-hsm'] = """
    type: group
    short-summary: hardware-security-modules dedicated-hsm
"""

helps['hardware-security-modules dedicated-hsm list'] = """
    type: command
    short-summary: The List operation gets information about the dedicated HSMs associated with the subscription.
    examples:
      - name: List dedicated HSM devices in a resource group
        text: |-
               az hardware-security-modules dedicated-hsm list --resource-group "hsm-group"
"""

helps['hardware-security-modules dedicated-hsm show'] = """
    type: command
    short-summary: Gets the specified Azure dedicated HSM.
    examples:
      - name: Get a dedicated HSM
        text: |-
               az hardware-security-modules dedicated-hsm show --name "hsm1" --resource-group "hsm-group"
"""

helps['hardware-security-modules dedicated-hsm create'] = """
    type: command
    short-summary: Create or Update a dedicated HSM in the specified subscription.
    parameters:
      - name: --network-profile-subnet
        short-summary: Specifies the identifier of the subnet.
        long-summary: |
            Usage: --network-profile-subnet id=XX

            id: The ARM resource id in the form of /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/.\
..
      - name: --network-profile-network-interfaces
        short-summary: Specifies the list of resource Ids for the network interfaces associated with the dedicated HSM.
        long-summary: |
            Usage: --network-profile-network-interfaces private-ip-address=XX

            private-ip-address: Private Ip address of the interface

            Multiple actions can be specified by using more than one --network-profile-network-interfaces argument.
    examples:
      - name: Create a new or update an existing dedicated HSM
        text: |-
               az hardware-security-modules dedicated-hsm create --name "hsm1" --location "westus" --network-profile-ne\
twork-interfaces private-ip-address="1.0.0.1" --network-profile-subnet id="/subscriptions/00000000-0000-0000-0000-00000\
0000000/resourceGroups/hsm-group/providers/Microsoft.Network/virtualNetworks/stamp01/subnets/stamp01" --stamp-id "stamp\
01" --tags Dept="hsm" Environment="dogfood" --resource-group "hsm-group"
"""

helps['hardware-security-modules dedicated-hsm update'] = """
    type: command
    short-summary: Update a dedicated HSM in the specified subscription.
    examples:
      - name: Update an existing dedicated HSM
        text: |-
               az hardware-security-modules dedicated-hsm update --name "hsm1" --tags Dept="hsm" Environment="dogfood" \
Slice="A" --resource-group "hsm-group"
"""

helps['hardware-security-modules dedicated-hsm delete'] = """
    type: command
    short-summary: Deletes the specified Azure Dedicated HSM.
    examples:
      - name: Delete a dedicated HSM
        text: |-
               az hardware-security-modules dedicated-hsm delete --name "hsm1" --resource-group "hsm-group"
"""

helps['hardware-security-modules dedicated-hsm wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the hardware-security-modules dedicated-hsm is\
 met.
    examples:
      - name: Pause executing next line of CLI script until the hardware-security-modules dedicated-hsm is successfully\
 created.
        text: |-
               az hardware-security-modules dedicated-hsm wait --name "hsm1" --resource-group "hsm-group" --created
      - name: Pause executing next line of CLI script until the hardware-security-modules dedicated-hsm is successfully\
 updated.
        text: |-
               az hardware-security-modules dedicated-hsm wait --name "hsm1" --resource-group "hsm-group" --updated
      - name: Pause executing next line of CLI script until the hardware-security-modules dedicated-hsm is successfully\
 deleted.
        text: |-
               az hardware-security-modules dedicated-hsm wait --name "hsm1" --resource-group "hsm-group" --deleted
"""
