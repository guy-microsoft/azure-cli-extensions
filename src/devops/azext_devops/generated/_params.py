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
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azext_devops.action import (
    AddBootstrapConfigurationTemplateParameters,
    AddBootstrapConfigurationRepositoryProperties,
    AddBootstrapConfigurationRepositoryAuthorizationParameters
)


def load_arguments(self, _):

    with self.argument_context('devops pipeline list') as c:
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('devops pipeline show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('pipeline_name', options_list=['--name', '-n', '--pipeline-name'], type=str, help='The name of the '
                   'Azure Pipeline resource in ARM.', id_part='name')

    with self.argument_context('devops pipeline create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('pipeline_name', options_list=['--name', '-n', '--pipeline-name'], type=str, help='The name of the '
                   'Azure Pipeline resource in ARM.')
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('bootstrap_configuration_template_id', type=str,
                   help='Unique identifier of the pipeline template.')
        c.argument('bootstrap_configuration_template_parameters', action=AddBootstrapConfigurationTemplateParameters,
                   nargs='*', help='Dictionary of input parameters used in the pipeline template. Expect value: '
                   'KEY1=VALUE1 KEY2=VALUE2 ...')
        c.argument('bootstrap_configuration_repository_repository_type', arg_type=get_enum_type(['gitHub', 'vstsGit']),
                   help='Type of code repository.')
        c.argument('bootstrap_configuration_repository_id', type=str, help='Unique immutable identifier of the code '
                   'repository.')
        c.argument('bootstrap_configuration_repository_default_branch', type=str, help='Default branch used to '
                   'configure Continuous Integration (CI) in the pipeline.')
        c.argument('bootstrap_configuration_repository_properties',
                   action=AddBootstrapConfigurationRepositoryProperties, nargs='*', help='Repository-specific '
                   'properties. Expect value: KEY1=VALUE1 KEY2=VALUE2 ...')
        c.argument('bootstrap_configuration_repository_authorization_parameters',
                   action=AddBootstrapConfigurationRepositoryAuthorizationParameters, nargs='*', help='Authorization '
                   'parameters corresponding to the authorization type. Expect value: KEY1=VALUE1 KEY2=VALUE2 ...')
        c.argument('project_name', type=str, help='Name of the Azure DevOps Project.')
        c.argument('organization_name', type=str, help='Name of the Azure DevOps Organization.')

    with self.argument_context('devops pipeline update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('pipeline_name', options_list=['--name', '-n', '--pipeline-name'], type=str, help='The name of the '
                   'Azure Pipeline resource.', id_part='name')
        c.argument('tags', tags_type)

    with self.argument_context('devops pipeline delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('pipeline_name', options_list=['--name', '-n', '--pipeline-name'], type=str, help='The name of the '
                   'Azure Pipeline resource.', id_part='name')

    with self.argument_context('devops pipeline wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('pipeline_name', options_list=['--name', '-n', '--pipeline-name'], type=str, help='The name of the '
                   'Azure Pipeline resource in ARM.', id_part='name')