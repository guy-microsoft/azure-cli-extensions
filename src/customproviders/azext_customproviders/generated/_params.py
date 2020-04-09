# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from knack.arguments import CLIArgumentType
from azure.cli.core.commands.parameters import (
    tags_type,
    resource_group_name_type,
    get_location_type
)
from azext_customproviders.action import (
    AddActions,
    AddResourceTypes,
    AddValidations
)


def load_arguments(self, _):

    with self.argument_context('customproviders custom-resource-provider list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group.')

    with self.argument_context('customproviders custom-resource-provider show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group.')
        c.argument('resource_provider_name', help='The name of the resource provider.')

    with self.argument_context('customproviders custom-resource-provider create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group.')
        c.argument('resource_provider_name', help='The name of the resource provider.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='Resource location')
        c.argument('tags', tags_type, help='Resource tags')
        c.argument('properties_actions', action=AddActions, nargs='+', help='A list of actions that the custom resource provider implements.')
        c.argument('properties_resource_types', action=AddResourceTypes, nargs='+', help='A list of resource types that the custom resource provider implements.')
        c.argument('properties_validations', action=AddValidations, nargs='+', help='A list of validations to run on the custom resource provider\'s requests.')

    with self.argument_context('customproviders custom-resource-provider update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group.')
        c.argument('resource_provider_name', help='The name of the resource provider.')
        c.argument('tags', tags_type, help='Resource tags')

    with self.argument_context('customproviders custom-resource-provider delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group.')
        c.argument('resource_provider_name', help='The name of the resource provider.')

    with self.argument_context('customproviders association list') as c:
        c.argument('scope', help='The scope of the association. The scope can be any valid REST resource instance. For example, use \'/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.Compute/virtualMachines/{vm-name}\' for a virtual machine resource.')

    with self.argument_context('customproviders association show') as c:
        c.argument('scope', help='The scope of the association. The scope can be any valid REST resource instance. For example, use \'/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.Compute/virtualMachines/{vm-name}\' for a virtual machine resource.')
        c.argument('association_name', help='The name of the association.')

    with self.argument_context('customproviders association create') as c:
        c.argument('scope', help='The scope of the association. The scope can be any valid REST resource instance. For example, use \'/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.Compute/virtualMachines/{vm-name}\' for a virtual machine resource.')
        c.argument('association_name', help='The name of the association.')
        c.argument('properties_target_resource_id', help='The REST resource instance of the target resource for this association.')

    with self.argument_context('customproviders association update') as c:
        c.argument('scope', help='The scope of the association. The scope can be any valid REST resource instance. For example, use \'/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.Compute/virtualMachines/{vm-name}\' for a virtual machine resource.')
        c.argument('association_name', help='The name of the association.')
        c.argument('properties_target_resource_id', help='The REST resource instance of the target resource for this association.')

    with self.argument_context('customproviders association delete') as c:
        c.argument('scope', help='The scope of the association. The scope can be any valid REST resource instance. For example, use \'/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.Compute/virtualMachines/{vm-name}\' for a virtual machine resource.')
        c.argument('association_name', help='The name of the association.')
