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
# pylint: disable=too-many-statements

from knack.arguments import CLIArgumentType
from azure.cli.core.commands.parameters import resource_group_name_type


def load_arguments(self, _):

    with self.argument_context('windowsiotservices service list') as c:
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('windowsiotservices service show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('device_name', help='The name of the Windows IoT Device Service.')

    with self.argument_context('windowsiotservices service create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('device_name', help='The name of the Windows IoT Device Service.')
        c.argument('if_match', help='ETag of the Windows IoT Device Service. Do not specify for creating a new Windows '
                   'IoT Device Service. Required to update an existing Windows IoT Device Service.')
        c.argument('notes', help='Windows IoT Device Service notes.')
        c.argument('quantity', help='Windows IoT Device Service device allocation,')
        c.argument('billing_domain_name', help='Windows IoT Device Service ODM AAD domain')
        c.argument('admin_domain_name', help='Windows IoT Device Service OEM AAD domain')

    with self.argument_context('windowsiotservices service update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('device_name', help='The name of the Windows IoT Device Service.')
        c.argument('if_match', help='ETag of the Windows IoT Device Service. Do not specify for creating a brand new Wi'
                   'ndows IoT Device Service. Required to update an existing Windows IoT Device Service.')
        c.argument('notes', help='Windows IoT Device Service notes.')
        c.argument('quantity', help='Windows IoT Device Service device allocation,')
        c.argument('billing_domain_name', help='Windows IoT Device Service ODM AAD domain')
        c.argument('admin_domain_name', help='Windows IoT Device Service OEM AAD domain')

    with self.argument_context('windowsiotservices service delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('device_name', help='The name of the Windows IoT Device Service.')

    with self.argument_context('windowsiotservices service check-device-service-name-availability') as c:
        c.argument('name', help='The name of the Windows IoT Device Service to check.')