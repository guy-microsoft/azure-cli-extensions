# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_customproviders.generated._client_factory import cf_custom_resource_provider
    customproviders_custom_resource_provider = CliCommandType(
        operations_tmpl='azext_customproviders.vendored_sdks.customproviders.operations._custom_resource_provider_operations#CustomResourceProviderOperations.{}',
        client_factory=cf_custom_resource_provider)
    with self.command_group('customproviders custom-resource-provider', customproviders_custom_resource_provider, client_factory=cf_custom_resource_provider) as g:
        g.custom_command('list', 'customproviders_custom_resource_provider_list')
        g.custom_show_command('show', 'customproviders_custom_resource_provider_show')
        g.custom_command('create', 'customproviders_custom_resource_provider_create', supports_no_wait=True)
        g.custom_command('update', 'customproviders_custom_resource_provider_update')
        g.custom_command('delete', 'customproviders_custom_resource_provider_delete', supports_no_wait=True)
        g.wait_command('wait')

    from azext_customproviders.generated._client_factory import cf_association
    customproviders_association = CliCommandType(
        operations_tmpl='azext_customproviders.vendored_sdks.customproviders.operations._association_operations#AssociationOperations.{}',
        client_factory=cf_association)
    with self.command_group('customproviders association', customproviders_association, client_factory=cf_association) as g:
        g.custom_command('list', 'customproviders_association_list')
        g.custom_show_command('show', 'customproviders_association_show')
        g.custom_command('create', 'customproviders_association_create', supports_no_wait=True)
        g.generic_update_command('update', supports_no_wait=True)
        g.custom_command('delete', 'customproviders_association_delete', supports_no_wait=True)
        g.wait_command('wait')
