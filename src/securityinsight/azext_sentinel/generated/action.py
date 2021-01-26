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


class AddFusionAlertRule(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.fusion_alert_rule = action

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
            if kl == 'alert-rule-template-name':
                d['alert_rule_template_name'] = v[0]
            elif kl == 'enabled':
                d['enabled'] = v[0]
            elif kl == 'etag':
                d['etag'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter fusion_alert_rule. All possible keys are: '
                               'alert-rule-template-name, enabled, etag'.format(k))
        d['kind'] = 'Fusion'
        return d


class AddMicrosoftSecurityIncidentCreationAlertRule(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.microsoft_security_incident_creation_alert_rule = action

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
            if kl == 'display-names-filter':
                d['display_names_filter'] = v
            elif kl == 'display-names-exclude-filter':
                d['display_names_exclude_filter'] = v
            elif kl == 'product-filter':
                d['product_filter'] = v[0]
            elif kl == 'severities-filter':
                d['severities_filter'] = v
            elif kl == 'alert-rule-template-name':
                d['alert_rule_template_name'] = v[0]
            elif kl == 'description':
                d['description'] = v[0]
            elif kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'enabled':
                d['enabled'] = v[0]
            elif kl == 'etag':
                d['etag'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter microsoft_security_incident_creation_alert'
                               '_rule. All possible keys are: display-names-filter, display-names-exclude-filter, '
                               'product-filter, severities-filter, alert-rule-template-name, description, '
                               'display-name, enabled, etag'.format(k))
        d['kind'] = 'MicrosoftSecurityIncidentCreation'
        return d


class AddScheduledAlertRule(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.scheduled_alert_rule = action

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
            if kl == 'query':
                d['query'] = v[0]
            elif kl == 'query-frequency':
                d['query_frequency'] = v[0]
            elif kl == 'query-period':
                d['query_period'] = v[0]
            elif kl == 'severity':
                d['severity'] = v[0]
            elif kl == 'trigger-operator':
                d['trigger_operator'] = v[0]
            elif kl == 'trigger-threshold':
                d['trigger_threshold'] = v[0]
            elif kl == 'alert-rule-template-name':
                d['alert_rule_template_name'] = v[0]
            elif kl == 'description':
                d['description'] = v[0]
            elif kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'enabled':
                d['enabled'] = v[0]
            elif kl == 'suppression-duration':
                d['suppression_duration'] = v[0]
            elif kl == 'suppression-enabled':
                d['suppression_enabled'] = v[0]
            elif kl == 'tactics':
                d['tactics'] = v
            elif kl == 'etag':
                d['etag'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter scheduled_alert_rule. All possible keys '
                               'are: query, query-frequency, query-period, severity, trigger-operator, '
                               'trigger-threshold, alert-rule-template-name, description, display-name, enabled, '
                               'suppression-duration, suppression-enabled, tactics, etag'.format(k))
        d['kind'] = 'Scheduled'
        return d


class AddIncidentInfo(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.incident_info = action

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
            if kl == 'incident-id':
                d['incident_id'] = v[0]
            elif kl == 'severity':
                d['severity'] = v[0]
            elif kl == 'title':
                d['title'] = v[0]
            elif kl == 'relation-name':
                d['relation_name'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter incident_info. All possible keys are: '
                               'incident-id, severity, title, relation-name'.format(k))
        return d


class AddAadDataConnector(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.aad_data_connector = action

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
            if kl == 'tenant-id':
                d['tenant_id'] = v[0]
            elif kl == 'state':
                d['state'] = v[0]
            elif kl == 'etag':
                d['etag'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter aad_data_connector. All possible keys '
                               'are: tenant-id, state, etag'.format(k))
        d['kind'] = 'AzureActiveDirectory'
        return d


class AddAatpDataConnector(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.aatp_data_connector = action

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
            if kl == 'tenant-id':
                d['tenant_id'] = v[0]
            elif kl == 'state':
                d['state'] = v[0]
            elif kl == 'etag':
                d['etag'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter aatp_data_connector. All possible keys '
                               'are: tenant-id, state, etag'.format(k))
        d['kind'] = 'AzureAdvancedThreatProtection'
        return d


class AddAscDataConnector(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.asc_data_connector = action

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
            if kl == 'subscription-id':
                d['subscription_id'] = v[0]
            elif kl == 'state':
                d['state'] = v[0]
            elif kl == 'etag':
                d['etag'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter asc_data_connector. All possible keys '
                               'are: subscription-id, state, etag'.format(k))
        d['kind'] = 'AzureSecurityCenter'
        return d


class AddAwsCloudTrailDataConnector(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.aws_cloud_trail_data_connector = action

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
            if kl == 'aws-role-arn':
                d['aws_role_arn'] = v[0]
            elif kl == 'state':
                d['state'] = v[0]
            elif kl == 'etag':
                d['etag'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter aws_cloud_trail_data_connector. All '
                               'possible keys are: aws-role-arn, state, etag'.format(k))
        d['kind'] = 'AmazonWebServicesCloudTrail'
        return d


class AddMcasDataConnector(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.mcas_data_connector = action

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
            if kl == 'tenant-id':
                d['tenant_id'] = v[0]
            elif kl == 'state-properties-data-types-alerts-state':
                d['undefined'] = v[0]
            elif kl == 'state-properties-data-types-discovery-logs-state':
                d['state'] = v[0]
            elif kl == 'etag':
                d['etag'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter mcas_data_connector. All possible keys '
                               'are: tenant-id, state-properties-data-types-alerts-state, '
                               'state-properties-data-types-discovery-logs-state, etag'.format(k))
        d['kind'] = 'MicrosoftCloudAppSecurity'
        return d


class AddMdatpDataConnector(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.mdatp_data_connector = action

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
            if kl == 'tenant-id':
                d['tenant_id'] = v[0]
            elif kl == 'state':
                d['state'] = v[0]
            elif kl == 'etag':
                d['etag'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter mdatp_data_connector. All possible keys '
                               'are: tenant-id, state, etag'.format(k))
        d['kind'] = 'MicrosoftDefenderAdvancedThreatProtection'
        return d


class AddOfficeDataConnector(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.office_data_connector = action

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
            if kl == 'tenant-id':
                d['tenant_id'] = v[0]
            elif kl == 'state-properties-data-types-teams-state':
                d['state'] = v[0]
            elif kl == 'state-properties-data-types-share-point-state':
                d['state'] = v[0]
            elif kl == 'state-properties-data-types-exchange-state':
                d['state'] = v[0]
            elif kl == 'etag':
                d['etag'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter office_data_connector. All possible keys '
                               'are: tenant-id, state-properties-data-types-teams-state, '
                               'state-properties-data-types-share-point-state, state-properties-data-types-exchange-sta'
                               'te, etag'.format(k))
        d['kind'] = 'Office365'
        return d


class AddTiDataConnector(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.ti_data_connector = action

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
            if kl == 'tenant-id':
                d['tenant_id'] = v[0]
            elif kl == 'state':
                d['state'] = v[0]
            elif kl == 'etag':
                d['etag'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter ti_data_connector. All possible keys are: '
                               'tenant-id, state, etag'.format(k))
        d['kind'] = 'ThreatIntelligence'
        return d


class AddLabels(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddLabels, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'label-name':
                d['label_name'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter labels. All possible keys are: label-name'
                .format(k))
        return d


class AddOwner(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.owner = action

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
            if kl == 'email':
                d['email'] = v[0]
            elif kl == 'assigned-to':
                d['assigned_to'] = v[0]
            elif kl == 'object-id':
                d['object_id'] = v[0]
            elif kl == 'user-principal-name':
                d['user_principal_name'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter owner. All possible keys are: email, '
                               'assigned-to, object-id, user-principal-name'.format(k))
        return d
