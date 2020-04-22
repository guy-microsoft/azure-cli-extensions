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
from azure.cli.core.commands.parameters import (
    get_three_state_flag,
    get_enum_type
)
from azext_managementgroup.action import AddDetailsParent


def load_arguments(self, _):

    with self.argument_context('managementgroup management-group list') as c:
        c.argument('cache_control', help='Indicates that the request shouldn\'t utilize any caches.')

    with self.argument_context('managementgroup management-group show') as c:
        c.argument('group_id', help='Management Group ID.')
        c.argument('expand', arg_type=get_enum_type(['children', 'path']), help='The $expand=children query string para'
                   'meter allows clients to request inclusion of children in the response payload.  $expand=path includ'
                   'es the path from the root group to the current group.')
        c.argument('recurse', arg_type=get_three_state_flag(), help='The $recurse=true query string parameter allows cl'
                   'ients to request inclusion of entire hierarchy in the response payload. Note that  $expand=children'
                   ' must be passed up if $recurse is set to true.')
        c.argument('filter', help='A filter which allows the exclusion of subscriptions from results (i.e. \'$filter=ch'
                   'ildren.childType ne Subscription\')')
        c.argument('cache_control', help='Indicates that the request shouldn\'t utilize any caches.')

    with self.argument_context('managementgroup management-group create') as c:
        c.argument('group_id', help='Management Group ID.')
        c.argument('cache_control', help='Indicates that the request shouldn\'t utilize any caches.')
        c.argument('name', help='The name of the management group. For example, 00000000-0000-0000-0000-000000000000')
        c.argument('display_name', help='The friendly name of the management group. If no value is passed then this  fi'
                   'eld will be set to the groupId.')
        c.argument('details_parent', action=AddDetailsParent, nargs='+', help='(Optional) The ID of the parent manageme'
                   'nt group used during creation. Expect value: id=xx.')

    with self.argument_context('managementgroup management-group update') as c:
        c.argument('group_id', help='Management Group ID.')
        c.argument('cache_control', help='Indicates that the request shouldn\'t utilize any caches.')
        c.argument('display_name', help='The friendly name of the management group.')
        c.argument('parent_id', help='(Optional) The fully qualified ID for the parent management group.  For example, '
                   '/providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000')

    with self.argument_context('managementgroup management-group delete') as c:
        c.argument('group_id', help='Management Group ID.')
        c.argument('cache_control', help='Indicates that the request shouldn\'t utilize any caches.')

    with self.argument_context('managementgroup management-group-subscription create') as c:
        c.argument('group_id', help='Management Group ID.')
        c.argument('subscription_id', help='Subscription ID.')
        c.argument('cache_control', help='Indicates that the request shouldn\'t utilize any caches.')

    with self.argument_context('managementgroup management-group-subscription delete') as c:
        c.argument('group_id', help='Management Group ID.')
        c.argument('subscription_id', help='Subscription ID.')
        c.argument('cache_control', help='Indicates that the request shouldn\'t utilize any caches.')

    with self.argument_context('managementgroup hierarchy-setting list') as c:
        c.argument('group_id', help='Management Group ID.')

    with self.argument_context('managementgroup hierarchy-setting show') as c:
        c.argument('group_id', help='Management Group ID.')

    with self.argument_context('managementgroup hierarchy-setting create') as c:
        c.argument('group_id', help='Management Group ID.')
        c.argument('require_authorization_for_group_creation', arg_type=get_three_state_flag(), help='Indicates whether'
                   ' RBAC access is required upon group creation under the root Management Group. If set to true, user '
                   'will require Microsoft.Management/managementGroups/write action on the root Management Group scope '
                   'in order to create new Groups directly under the root. This will prevent new users from creating ne'
                   'w Management Groups, unless they are given access.')
        c.argument('default_management_group', help='Settings that sets the default Management Group under which new su'
                   'bscriptions get added in this tenant. For example, /providers/Microsoft.Management/managementGroups'
                   '/defaultGroup')

    with self.argument_context('managementgroup hierarchy-setting update') as c:
        c.argument('group_id', help='Management Group ID.')
        c.argument('require_authorization_for_group_creation', arg_type=get_three_state_flag(), help='Indicates whether'
                   ' RBAC access is required upon group creation under the root Management Group. If set to true, user '
                   'will require Microsoft.Management/managementGroups/write action on the root Management Group scope '
                   'in order to create new Groups directly under the root. This will prevent new users from creating ne'
                   'w Management Groups, unless they are given access.')
        c.argument('default_management_group', help='Settings that sets the default Management Group under which new su'
                   'bscriptions get added in this tenant. For example, /providers/Microsoft.Management/managementGroups'
                   '/defaultGroup')

    with self.argument_context('managementgroup hierarchy-setting delete') as c:
        c.argument('group_id', help='Management Group ID.')

    with self.argument_context('managementgroup  start-tenant-backfill') as c:
        pass

    with self.argument_context('managementgroup  tenant-backfill-status') as c:
        pass

    with self.argument_context('managementgroup entity list') as c:
        c.argument('select', help='This parameter specifies the fields to include in the response. Can include any comb'
                   'ination of Name,DisplayName,Type,ParentDisplayNameChain,ParentChain, e.g. \'$select=Name,DisplayNam'
                   'e,Type,ParentDisplayNameChain,ParentNameChain\'. When specified the $select parameter can override '
                   'select in $skipToken.')
        c.argument('search', arg_type=get_enum_type(['AllowedParents', 'AllowedChildren',
                   'ParentAndFirstLevelChildren', 'ParentOnly', 'ChildrenOnly']), help='The $search parameter is used i'
                   'n conjunction with the $filter parameter to return three different outputs depending on the paramet'
                   'er passed in.  With $search=AllowedParents the API will return the entity info of all groups that t'
                   'he requested entity will be able to reparent to as determined by the user\'s permissions. With $sea'
                   'rch=AllowedChildren the API will return the entity info of all entities that can be added as childr'
                   'en of the requested entity. With $search=ParentAndFirstLevelChildren the API will return the parent'
                   ' and  first level of children that the user has either direct access to or indirect access via one '
                   'of their descendants. With $search=ParentOnly the API will return only the group if the user has ac'
                   'cess to at least one of the descendants of the group. With $search=ChildrenOnly the API will return'
                   ' only the first level of children of the group entity info specified in $filter.  The user must hav'
                   'e direct access to the children entities or one of it\'s descendants for it to show up in the resul'
                   'ts.')
        c.argument('filter', help='The filter parameter allows you to filter on the the name or display name fields. Yo'
                   'u can check for equality on the name field (e.g. name eq \'{entityName}\')  and you can check for s'
                   'ubstrings on either the name or display name fields(e.g. contains(name, \'{substringToSearch}\'), c'
                   'ontains(displayName, \'{substringToSearch\')). Note that the \'{entityName}\' and \'{substringToSea'
                   'rch}\' fields are checked case insensitively.')
        c.argument('view', arg_type=get_enum_type(['FullHierarchy', 'GroupsOnly', 'SubscriptionsOnly', 'Audit']),
                   help='The view parameter allows clients to filter the type of data that is returned by the getEntiti'
                   'es call.')
        c.argument('group_name', help='A filter which allows the get entities call to focus on a particular group (i.e.'
                   ' "$filter=name eq \'groupName\'")')
        c.argument('cache_control', help='Indicates that the request shouldn\'t utilize any caches.')
