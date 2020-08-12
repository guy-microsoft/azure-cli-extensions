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
from azure.cli.core.commands.parameters import get_enum_type
from azext_account.action import (
    AddProperties,
    AddOwners
)


def load_arguments(self, _):

    with self.argument_context('account subscription list') as c:
        pass

    with self.argument_context('account subscription show') as c:
        c.argument('subscription_id', help='The ID of the target subscription.', id_part='subscription')

    with self.argument_context('account subscription list-location') as c:
        c.argument('subscription_id', help='The ID of the target subscription.')

    with self.argument_context('account tenant list') as c:
        pass

    with self.argument_context('account subscription create') as c:
        c.argument('alias_name', help='Alias Name')
        c.argument('properties', action=AddProperties, nargs='+', help='Put alias request properties.')

    with self.argument_context('account subscription delete') as c:
        c.argument('alias_name', help='Alias Name')

    with self.argument_context('account subscription cancel') as c:
        c.argument('subscription_id', help='Subscription Id.', id_part='subscription')

    with self.argument_context('account subscription create-csp-subscription') as c:
        c.argument('billing_account_name', help='The name of the Microsoft Customer Agreement billing account for which'
                   ' you want to create the subscription.')
        c.argument('customer_name', help='The name of the customer.')
        c.argument('display_name', help='The friendly name of the subscription.')
        c.argument('sku_id', help='The SKU ID of the Azure plan. Azure plan determines the pricing and service-level ag'
                   'reement of the subscription.  Use 001 for Microsoft Azure Plan and 002 for Microsoft Azure Plan for'
                   ' DevTest.')
        c.argument('reseller_id', help='Reseller ID, basically MPN Id.')

    with self.argument_context('account subscription create-subscription') as c:
        c.argument('billing_account_name', help='The name of the Microsoft Customer Agreement billing account for which'
                   ' you want to create the subscription.')
        c.argument('billing_profile_name', help='The name of the billing profile in the billing account for which you w'
                   'ant to create the subscription.')
        c.argument('invoice_section_name', help='The name of the invoice section in the billing account for which you w'
                   'ant to create the subscription.')
        c.argument('display_name', help='The friendly name of the subscription.')
        c.argument('sku_id', help='The SKU ID of the Azure plan. Azure plan determines the pricing and service-level ag'
                   'reement of the subscription.  Use 001 for Microsoft Azure Plan and 002 for Microsoft Azure Plan for'
                   ' DevTest.')
        c.argument('cost_center', help='If set, the cost center will show up on the Azure usage and charges file.')
        c.argument('management_group_id', help='The identifier of the management group to which this subscription will '
                   'be associated.')
        c.argument('additional_parameters', arg_type=CLIArgumentType(options_list=['--additional-parameters'], help='Ad'
                   'ditional, untyped parameters to support custom subscription creation scenarios. Expected value: jso'
                   'n-string/@json-file.'))
        c.argument('owner_object_id', help='Object id of the Principal')

    with self.argument_context('account subscription create-subscription-in-enrollment-account') as c:
        c.argument('enrollment_account_name', help='The name of the enrollment account to which the subscription will b'
                   'e billed.')
        c.argument('display_name', help='The display name of the subscription.')
        c.argument('management_group_id', help='The Management Group Id.')
        c.argument('owners', action=AddOwners, nargs='+', help='The list of principals that should be granted Owner acc'
                   'ess on the subscription. Principals should be of type User, Service Principal or Security Group.')
        c.argument('offer_type', arg_type=get_enum_type(['MS-AZR-0017P', 'MS-AZR-0148P']), help='The offer type of the '
                   'subscription. For example, MS-AZR-0017P (EnterpriseAgreement) and MS-AZR-0148P (EnterpriseAgreement'
                   ' devTest) are available. Only valid when creating a subscription in a enrollment account scope.')
        c.argument('additional_parameters', arg_type=CLIArgumentType(options_list=['--additional-parameters'], help='Ad'
                   'ditional, untyped parameters to support custom subscription creation scenarios. Expected value: jso'
                   'n-string/@json-file.'))

    with self.argument_context('account subscription enable') as c:
        c.argument('subscription_id', help='Subscription Id.', id_part='subscription')

    with self.argument_context('account subscription get-alias') as c:
        c.argument('alias_name', help='Alias Name')

    with self.argument_context('account subscription list-alias') as c:
        pass

    with self.argument_context('account subscription rename') as c:
        c.argument('subscription_id', help='Subscription Id.', id_part='subscription')
        c.argument('subscription_name', options_list=['--name', '-n'], help='New subscription name')

    with self.argument_context('account subscription-operation show') as c:
        c.argument('operation_id', help='The operation ID, which can be found from the Location field in the generate r'
                   'ecommendation response header.')
