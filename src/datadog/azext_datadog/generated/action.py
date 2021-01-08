# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=protected-access

import argparse
from collections import defaultdict
from knack.util import CLIError


class AddMarketplaceagreementsProperties(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.properties = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'publisher':
                d['publisher'] = v[0]
            elif kl == 'product':
                d['product'] = v[0]
            elif kl == 'plan':
                d['plan'] = v[0]
            elif kl == 'license-text-link':
                d['license_text_link'] = v[0]
            elif kl == 'privacy-policy-link':
                d['privacy_policy_link'] = v[0]
            elif kl == 'retrieve-datetime':
                d['retrieve_datetime'] = v[0]
            elif kl == 'signature':
                d['signature'] = v[0]
            elif kl == 'accepted':
                d['accepted'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter properties. All possible keys are: '
                               'publisher, product, plan, license-text-link, privacy-policy-link, retrieve-datetime, '
                               'signature, accepted'.format(k))
        return d


class AddDatadogOrganizationProperties(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.datadog_organization_properties = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'linking-auth-code':
                d['linking_auth_code'] = v[0]
            elif kl == 'linking-client-id':
                d['linking_client_id'] = v[0]
            elif kl == 'enterprise-app-id':
                d['enterprise_app_id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter datadog_organization_properties. All '
                               'possible keys are: linking-auth-code, linking-client-id, enterprise-app-id'.format(k))
        return d


class AddUserInfo(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.user_info = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'name':
                d['name'] = v[0]
            elif kl == 'email-address':
                d['email_address'] = v[0]
            elif kl == 'phone-number':
                d['phone_number'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter user_info. All possible keys are: name, '
                               'email-address, phone-number'.format(k))
        return d


class AddFilteringTags(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddFilteringTags, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'name':
                d['name'] = v[0]
            elif kl == 'value':
                d['value'] = v[0]
            elif kl == 'action':
                d['action'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter filtering_tags. All possible keys are: '
                               'name, value, action'.format(k))
        return d


class AddLogRulesFilteringTags(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddLogRulesFilteringTags, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'name':
                d['name'] = v[0]
            elif kl == 'value':
                d['value'] = v[0]
            elif kl == 'action':
                d['action'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter log_rules_filtering_tags. All possible '
                               'keys are: name, value, action'.format(k))
        return d


class AddSinglesignonconfigurationsProperties(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.properties = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'single-sign-on-state':
                d['single_sign_on_state'] = v[0]
            elif kl == 'enterprise-app-id':
                d['enterprise_app_id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter properties. All possible keys are: '
                               'single-sign-on-state, enterprise-app-id'.format(k))
        return d
