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

from azure.cli.core.commands.parameters import (
    tags_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azext_customproviders.action import (
    AddActions,
    AddResourceTypes,
    AddValidations
)


def load_arguments(self, _):

    with self.argument_context('customproviders custom-resource-provider list') as c:
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('customproviders custom-resource-provider show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_provider_name', type=str, help='The name of the resource provider.', id_part='name')

    with self.argument_context('customproviders custom-resource-provider create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_provider_name', type=str, help='The name of the resource provider.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)
        c.argument('actions', action=AddActions, nargs='*', help='A list of actions that the custom resource provider '
                   'implements.')
        c.argument('resource_types', action=AddResourceTypes, nargs='*', help='A list of resource types that the '
                   'custom resource provider implements.')
        c.argument('validations', action=AddValidations, nargs='*', help='A list of validations to run on the custom '
                   'resource provider\'s requests.')

    with self.argument_context('customproviders custom-resource-provider update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_provider_name', type=str, help='The name of the resource provider.', id_part='name')
        c.argument('tags', tags_type)

    with self.argument_context('customproviders custom-resource-provider delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_provider_name', type=str, help='The name of the resource provider.', id_part='name')

    with self.argument_context('customproviders custom-resource-provider wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_provider_name', type=str, help='The name of the resource provider.', id_part='name')

    with self.argument_context('customproviders association show') as c:
        c.argument('scope', type=str, help='The scope of the association.')
        c.argument('association_name', options_list=['--name', '-n', '--association-name'], type=str, help='The name '
                   'of the association.')

    with self.argument_context('customproviders association create') as c:
        c.argument('scope', type=str, help='The scope of the association. The scope can be any valid REST resource '
                   'instance. For example, use \'/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/'
                   'providers/Microsoft.Compute/virtualMachines/{vm-name}\' for a virtual machine resource.')
        c.argument('association_name', options_list=['--name', '-n', '--association-name'], type=str, help='The name '
                   'of the association.')
        c.argument('target_resource_id', type=str, help='The REST resource instance of the target resource for this '
                   'association.')

    with self.argument_context('customproviders association update') as c:
        c.argument('scope', type=str, help='The scope of the association. The scope can be any valid REST resource '
                   'instance. For example, use \'/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/'
                   'providers/Microsoft.Compute/virtualMachines/{vm-name}\' for a virtual machine resource.')
        c.argument('association_name', options_list=['--name', '-n', '--association-name'], type=str, help='The name '
                   'of the association.')
        c.argument('target_resource_id', type=str, help='The REST resource instance of the target resource for this '
                   'association.')

    with self.argument_context('customproviders association delete') as c:
        c.argument('scope', type=str, help='The scope of the association.')
        c.argument('association_name', options_list=['--name', '-n', '--association-name'], type=str, help='The name '
                   'of the association.')

    with self.argument_context('customproviders association list-all') as c:
        c.argument('scope', type=str, help='The scope of the association.')

    with self.argument_context('customproviders association wait') as c:
        c.argument('scope', type=str, help='The scope of the association.')
        c.argument('association_name', options_list=['--name', '-n', '--association-name'], type=str, help='The name '
                   'of the association.')