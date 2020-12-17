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


def cpim_b2_c_tenant_list(client,
                          resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list_by_subscription()


def cpim_b2_c_tenant_show(client,
                          resource_group_name,
                          resource_name):
    return client.get(resource_group_name=resource_group_name,
                      resource_name=resource_name)


def cpim_b2_c_tenant_create(client,
                            resource_group_name,
                            resource_name,
                            location=None,
                            properties=None,
                            tags=None,
                            sku_name=None,
                            no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create,
                       resource_group_name=resource_group_name,
                       resource_name=resource_name,
                       location=location,
                       properties=properties,
                       tags=tags,
                       name=sku_name)


def cpim_b2_c_tenant_update(client,
                            resource_group_name,
                            resource_name,
                            tags=None,
                            tenant_id=None,
                            billing_config_billing_type=None,
                            sku_name=None):
    return client.update(resource_group_name=resource_group_name,
                         resource_name=resource_name,
                         tags=tags,
                         tenant_id=tenant_id,
                         billing_type=billing_config_billing_type,
                         name=sku_name)


def cpim_b2_c_tenant_delete(client,
                            resource_group_name,
                            resource_name,
                            no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       resource_name=resource_name)


def cpim_operation_get_async_status(client,
                                    operation_id):
    return client.get_async_status(operation_id=operation_id)