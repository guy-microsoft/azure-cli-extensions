# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_sentinel.generated._client_factory import cf_alert_rule
    sentinel_alert_rule = CliCommandType(
        operations_tmpl='azext_sentinel.vendored_sdks.securityinsight.operations._alert_rules_operations#AlertRulesOper'
        'ations.{}',
        client_factory=cf_alert_rule)
    with self.command_group('sentinel alert-rule', sentinel_alert_rule, client_factory=cf_alert_rule) as g:
        g.custom_command('list', 'sentinel_alert_rule_list')
        g.custom_show_command('show', 'sentinel_alert_rule_show')
        g.custom_command('create', 'sentinel_alert_rule_create')
        g.custom_command('update', 'sentinel_alert_rule_update')
        g.custom_command('delete', 'sentinel_alert_rule_delete', confirmation=True)
        g.custom_command('show-action', 'sentinel_alert_rule_show_action')

    from azext_sentinel.generated._client_factory import cf_action
    sentinel_action = CliCommandType(
        operations_tmpl='azext_sentinel.vendored_sdks.securityinsight.operations._actions_operations#ActionsOperations.'
        '{}',
        client_factory=cf_action)
    with self.command_group('sentinel action', sentinel_action, client_factory=cf_action) as g:
        g.custom_command('list', 'sentinel_action_list')

    from azext_sentinel.generated._client_factory import cf_alert_rule_template
    sentinel_alert_rule_template = CliCommandType(
        operations_tmpl='azext_sentinel.vendored_sdks.securityinsight.operations._alert_rule_templates_operations#Alert'
        'RuleTemplatesOperations.{}',
        client_factory=cf_alert_rule_template)
    with self.command_group('sentinel alert-rule-template', sentinel_alert_rule_template,
                            client_factory=cf_alert_rule_template) as g:
        g.custom_command('list', 'sentinel_alert_rule_template_list')
        g.custom_show_command('show', 'sentinel_alert_rule_template_show')

    from azext_sentinel.generated._client_factory import cf_bookmark
    sentinel_bookmark = CliCommandType(
        operations_tmpl='azext_sentinel.vendored_sdks.securityinsight.operations._bookmarks_operations#BookmarksOperati'
        'ons.{}',
        client_factory=cf_bookmark)
    with self.command_group('sentinel bookmark', sentinel_bookmark, client_factory=cf_bookmark) as g:
        g.custom_command('list', 'sentinel_bookmark_list')
        g.custom_show_command('show', 'sentinel_bookmark_show')
        g.custom_command('create', 'sentinel_bookmark_create')
        g.generic_update_command('update', setter_arg_name='bookmark', custom_func_name='sentinel_bookmark_update')
        g.custom_command('delete', 'sentinel_bookmark_delete', confirmation=True)

    from azext_sentinel.generated._client_factory import cf_data_connector
    sentinel_data_connector = CliCommandType(
        operations_tmpl='azext_sentinel.vendored_sdks.securityinsight.operations._data_connectors_operations#DataConnec'
        'torsOperations.{}',
        client_factory=cf_data_connector)
    with self.command_group('sentinel data-connector', sentinel_data_connector,
                            client_factory=cf_data_connector) as g:
        g.custom_command('list', 'sentinel_data_connector_list')
        g.custom_show_command('show', 'sentinel_data_connector_show')
        g.custom_command('create', 'sentinel_data_connector_create')
        g.custom_command('update', 'sentinel_data_connector_update')
        g.custom_command('delete', 'sentinel_data_connector_delete', confirmation=True)

    from azext_sentinel.generated._client_factory import cf_incident
    sentinel_incident = CliCommandType(
        operations_tmpl='azext_sentinel.vendored_sdks.securityinsight.operations._incidents_operations#IncidentsOperati'
        'ons.{}',
        client_factory=cf_incident)
    with self.command_group('sentinel incident', sentinel_incident, client_factory=cf_incident) as g:
        g.custom_command('list', 'sentinel_incident_list')
        g.custom_show_command('show', 'sentinel_incident_show')
        g.custom_command('create', 'sentinel_incident_create')
        g.generic_update_command('update', setter_arg_name='incident', custom_func_name='sentinel_incident_update')
        g.custom_command('delete', 'sentinel_incident_delete', confirmation=True)

    from azext_sentinel.generated._client_factory import cf_incident_comment
    sentinel_incident_comment = CliCommandType(
        operations_tmpl='azext_sentinel.vendored_sdks.securityinsight.operations._incident_comments_operations#Incident'
        'CommentsOperations.{}',
        client_factory=cf_incident_comment)
    with self.command_group('sentinel incident-comment', sentinel_incident_comment,
                            client_factory=cf_incident_comment) as g:
        g.custom_command('list', 'sentinel_incident_comment_list')
        g.custom_show_command('show', 'sentinel_incident_comment_show')
        g.custom_command('create', 'sentinel_incident_comment_create')
        g.custom_command('delete', 'sentinel_incident_comment_delete', confirmation=True)

    with self.command_group('sentinel', is_experimental=True):
        pass
