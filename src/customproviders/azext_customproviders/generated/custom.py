# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines


def customproviders_custom_resource_provider_list(cmd, client,
                                                  resource_group_name=None):
    if resource_group_name is not None:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list_by_subscription()


def customproviders_custom_resource_provider_show(cmd, client,
                                                  resource_group_name,
                                                  resource_provider_name):
    return client.get(resource_group_name=resource_group_name, resource_provider_name=resource_provider_name)


def customproviders_custom_resource_provider_create(cmd, client,
                                                    resource_group_name,
                                                    resource_provider_name,
                                                    location,
                                                    tags=None,
                                                    properties_actions=None,
                                                    properties_resource_types=None,
                                                    properties_validations=None):
    return client.begin_create_or_update(resource_group_name=resource_group_name, resource_provider_name=resource_provider_name, location=location, tags=tags, actions=properties_actions, resource_types=properties_resource_types, validations=properties_validations)


def customproviders_custom_resource_provider_update(cmd, client,
                                                    resource_group_name,
                                                    resource_provider_name,
                                                    tags=None):
    return client.update(resource_group_name=resource_group_name, resource_provider_name=resource_provider_name, tags=tags)


def customproviders_custom_resource_provider_delete(cmd, client,
                                                    resource_group_name,
                                                    resource_provider_name):
    return client.begin_delete(resource_group_name=resource_group_name, resource_provider_name=resource_provider_name)


def customproviders_association_list(cmd, client,
                                     scope):
    return client.list_all(scope=scope)


def customproviders_association_show(cmd, client,
                                     scope,
                                     association_name):
    return client.get(scope=scope, association_name=association_name)


def customproviders_association_create(cmd, client,
                                       scope,
                                       association_name,
                                       properties_target_resource_id=None):
    return client.begin_create_or_update(scope=scope, association_name=association_name, target_resource_id=properties_target_resource_id)


def customproviders_association_update(cmd, client,
                                       scope,
                                       association_name,
                                       properties_target_resource_id=None):
    return client.begin_create_or_update(scope=scope, association_name=association_name, target_resource_id=properties_target_resource_id)


def customproviders_association_delete(cmd, client,
                                       scope,
                                       association_name):
    return client.begin_delete(scope=scope, association_name=association_name)
