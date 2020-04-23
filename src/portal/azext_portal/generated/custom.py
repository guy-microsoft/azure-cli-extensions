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

import json


def portal_dashboard_list(cmd, client,
                          resource_group_name=None):
    if resource_group_name is not None:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list_by_subscription()


def portal_dashboard_show(cmd, client,
                          resource_group_name,
                          dashboard_name):
    return client.get(resource_group_name=resource_group_name,
                      dashboard_name=dashboard_name)


def portal_dashboard_create(cmd, client,
                            resource_group_name,
                            dashboard_name,
                            location,
                            tags=None,
                            lenses=None,
                            metadata=None):
    if isinstance(lenses, str):
        lenses = json.loads(lenses)
    if isinstance(metadata, str):
        metadata = json.loads(metadata)
    return client.create_or_update(resource_group_name=resource_group_name,
                                   dashboard_name=dashboard_name,
                                   location=location,
                                   tags=tags,
                                   lenses=lenses,
                                   metadata=metadata)


def portal_dashboard_update(cmd, client,
                            resource_group_name,
                            dashboard_name,
                            tags=None,
                            lenses=None,
                            metadata=None):
    if isinstance(lenses, str):
        lenses = json.loads(lenses)
    if isinstance(metadata, str):
        metadata = json.loads(metadata)
    return client.update(resource_group_name=resource_group_name,
                         dashboard_name=dashboard_name,
                         tags=tags,
                         lenses=lenses,
                         metadata=metadata)


def portal_dashboard_delete(cmd, client,
                            resource_group_name,
                            dashboard_name):
    return client.delete(resource_group_name=resource_group_name,
                         dashboard_name=dashboard_name)