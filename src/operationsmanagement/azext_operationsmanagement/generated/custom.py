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


def operationsmanagement_solution_list(client,
                                       resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list_by_subscription()


def operationsmanagement_solution_show(client,
                                       resource_group_name,
                                       solution_name):
    return client.get(resource_group_name=resource_group_name,
                      solution_name=solution_name)


def operationsmanagement_solution_create(client,
                                         resource_group_name,
                                         solution_name,
                                         location=None,
                                         tags=None,
                                         plan=None,
                                         properties=None,
                                         no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       solution_name=solution_name,
                       location=location,
                       tags=tags,
                       plan=plan,
                       properties=properties)


def operationsmanagement_solution_update(client,
                                         resource_group_name,
                                         solution_name,
                                         tags=None,
                                         no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_update,
                       resource_group_name=resource_group_name,
                       solution_name=solution_name,
                       tags=tags)


def operationsmanagement_solution_delete(client,
                                         resource_group_name,
                                         solution_name,
                                         no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       solution_name=solution_name)


def operationsmanagement_management_association_list(client):
    return client.list_by_subscription()


def operationsmanagement_management_association_show(client,
                                                     resource_group_name,
                                                     provider_name,
                                                     resource_type,
                                                     resource_name,
                                                     management_association_name):
    return client.get(resource_group_name=resource_group_name,
                      provider_name=provider_name,
                      resource_type=resource_type,
                      resource_name=resource_name,
                      management_association_name=management_association_name)


def operationsmanagement_management_association_create(client,
                                                       resource_group_name,
                                                       provider_name,
                                                       resource_type,
                                                       resource_name,
                                                       management_association_name,
                                                       location=None,
                                                       application_id=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   provider_name=provider_name,
                                   resource_type=resource_type,
                                   resource_name=resource_name,
                                   management_association_name=management_association_name,
                                   location=location,
                                   application_id=application_id)


def operationsmanagement_management_association_update(client,
                                                       resource_group_name,
                                                       provider_name,
                                                       resource_type,
                                                       resource_name,
                                                       management_association_name,
                                                       location=None,
                                                       application_id=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   provider_name=provider_name,
                                   resource_type=resource_type,
                                   resource_name=resource_name,
                                   management_association_name=management_association_name,
                                   location=location,
                                   application_id=application_id)


def operationsmanagement_management_association_delete(client,
                                                       resource_group_name,
                                                       provider_name,
                                                       resource_type,
                                                       resource_name,
                                                       management_association_name):
    return client.delete(resource_group_name=resource_group_name,
                         provider_name=provider_name,
                         resource_type=resource_type,
                         resource_name=resource_name,
                         management_association_name=management_association_name)


def operationsmanagement_management_configuration_list(client):
    return client.list_by_subscription()


def operationsmanagement_management_configuration_show(client,
                                                       resource_group_name,
                                                       management_configuration_name):
    return client.get(resource_group_name=resource_group_name,
                      management_configuration_name=management_configuration_name)


def operationsmanagement_management_configuration_create(client,
                                                         resource_group_name,
                                                         management_configuration_name,
                                                         location=None,
                                                         application_id=None,
                                                         parent_resource_type=None,
                                                         parameters=None,
                                                         template=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   management_configuration_name=management_configuration_name,
                                   location=location,
                                   application_id=application_id,
                                   parent_resource_type=parent_resource_type,
                                   parameters=parameters,
                                   template=template)


def operationsmanagement_management_configuration_update(client,
                                                         resource_group_name,
                                                         management_configuration_name,
                                                         location=None,
                                                         application_id=None,
                                                         parent_resource_type=None,
                                                         parameters=None,
                                                         template=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   management_configuration_name=management_configuration_name,
                                   location=location,
                                   application_id=application_id,
                                   parent_resource_type=parent_resource_type,
                                   parameters=parameters,
                                   template=template)


def operationsmanagement_management_configuration_delete(client,
                                                         resource_group_name,
                                                         management_configuration_name):
    return client.delete(resource_group_name=resource_group_name,
                         management_configuration_name=management_configuration_name)
