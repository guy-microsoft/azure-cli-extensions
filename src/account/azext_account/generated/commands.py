# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_account.generated._client_factory import cf_subscription
    account_subscription = CliCommandType(
        operations_tmpl='azext_account.vendored_sdks.subscription.operations._subscription_operations#SubscriptionOpera'
        'tions.{}',
        client_factory=cf_subscription)
    with self.command_group('account subscription', account_subscription, client_factory=cf_subscription,
                            is_experimental=True) as g:
        g.custom_command('list', 'account_subscription_list')
        g.custom_show_command('show', 'account_subscription_show')
        g.custom_command('list-location', 'account_subscription_list_location')

    from azext_account.generated._client_factory import cf_tenant
    account_tenant = CliCommandType(
        operations_tmpl='azext_account.vendored_sdks.subscription.operations._tenant_operations#TenantOperations.{}',
        client_factory=cf_tenant)
    with self.command_group('account tenant', account_tenant, client_factory=cf_tenant, is_experimental=True) as g:
        g.custom_command('list', 'account_tenant_list')

    from azext_account.generated._client_factory import cf_subscription
    account_subscription = CliCommandType(
        operations_tmpl='azext_account.vendored_sdks.subscription.operations._subscription_operations#SubscriptionOpera'
        'tions.{}',
        client_factory=cf_subscription)
    with self.command_group('account subscription', account_subscription, client_factory=cf_subscription,
                            is_experimental=True) as g:
        g.custom_command('create', 'account_subscription_create')
        g.custom_command('delete', 'account_subscription_delete')
        g.custom_command('cancel', 'account_subscription_cancel')
        g.custom_command('create-csp-subscription', 'account_subscription_create_csp_subscription')
        g.custom_command('create-subscription', 'account_subscription_create_subscription')
        g.custom_command('create-subscription-in-enrollment-account', 'account_subscription_create_subscription_in_enro'
                         'llment_account')
        g.custom_command('enable', 'account_subscription_enable')
        g.custom_command('get-alias', 'account_subscription_get_alias')
        g.custom_command('list-alias', 'account_subscription_list_alias')
        g.custom_command('rename', 'account_subscription_rename')

    from azext_account.generated._client_factory import cf_subscription_operation
    account_subscription_operation = CliCommandType(
        operations_tmpl='azext_account.vendored_sdks.subscription.operations._subscription_operation_operations#Subscri'
        'ptionOperationOperations.{}',
        client_factory=cf_subscription_operation)
    with self.command_group('account subscription-operation', account_subscription_operation,
                            client_factory=cf_subscription_operation, is_experimental=True) as g:
        g.custom_show_command('show', 'account_subscription_operation_show')
