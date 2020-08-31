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

from azure.cli.core.util import sdk_no_wait


def customproviders_custom_resource_provider_list(client,
                                                  resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list_by_subscription()


def customproviders_custom_resource_provider_show(client,
                                                  resource_group_name,
                                                  resource_provider_name):
    return client.get(resource_group_name=resource_group_name,
                      resource_provider_name=resource_provider_name)


def customproviders_custom_resource_provider_create(client,
                                                    resource_group_name,
                                                    resource_provider_name,
                                                    location,
                                                    tags=None,
                                                    actions=None,
                                                    resource_types=None,
                                                    validations=None,
                                                    no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       resource_provider_name=resource_provider_name,
                       location=location,
                       tags=tags,
                       actions=actions,
                       resource_types=resource_types,
                       validations=validations)


def customproviders_custom_resource_provider_update(client,
                                                    resource_group_name,
                                                    resource_provider_name,
                                                    tags=None):
    return client.update(resource_group_name=resource_group_name,
                         resource_provider_name=resource_provider_name,
                         tags=tags)


def customproviders_custom_resource_provider_delete(client,
                                                    resource_group_name,
                                                    resource_provider_name,
                                                    no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       resource_provider_name=resource_provider_name)


def customproviders_association_show(client,
                                     scope,
                                     association_name):
    return client.get(scope=scope,
                      association_name=association_name)


def customproviders_association_create(client,
                                       scope,
                                       association_name,
                                       target_resource_id=None,
                                       no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       scope=scope,
                       association_name=association_name,
                       target_resource_id=target_resource_id)


def customproviders_association_update(client,
                                       scope,
                                       association_name,
                                       target_resource_id=None,
                                       no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       scope=scope,
                       association_name=association_name,
                       target_resource_id=target_resource_id)


def customproviders_association_delete(client,
                                       scope,
                                       association_name,
                                       no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       scope=scope,
                       association_name=association_name)


def customproviders_association_list_all(client,
                                         scope):
    return client.list_all(scope=scope)
