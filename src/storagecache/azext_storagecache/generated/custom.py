# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines

import json


def storagecache_sku_list(cmd, client):
    return client.list()


def storagecache_usage_model_list(cmd, client):
    return client.list()


def storagecache_cache_list(cmd, client,
                            resource_group_name=None):
    if resource_group_name is not None:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list()


def storagecache_cache_show(cmd, client,
                            resource_group_name,
                            cache_name):
    return client.get(resource_group_name=resource_group_name, cache_name=cache_name)


def storagecache_cache_create(cmd, client,
                              resource_group_name,
                              cache_name,
                              tags=None,
                              location=None,
                              sku=None,
                              properties_cache_size_gb=None,
                              properties_provisioning_state=None,
                              properties_subnet=None,
                              properties_upgrade_status=None):
    return client.begin_create_or_update(resource_group_name=resource_group_name, cache_name=cache_name, tags=tags, location=location, sku=sku, cache_size_gb=properties_cache_size_gb, provisioning_state=properties_provisioning_state, subnet=properties_subnet, upgrade_status=properties_upgrade_status)


def storagecache_cache_update(cmd, client,
                              resource_group_name,
                              cache_name,
                              tags=None,
                              location=None,
                              sku=None,
                              properties_cache_size_gb=None,
                              properties_provisioning_state=None,
                              properties_subnet=None,
                              properties_upgrade_status=None):
    return client.update(resource_group_name=resource_group_name, cache_name=cache_name, tags=tags, location=location, sku=sku, cache_size_gb=properties_cache_size_gb, provisioning_state=properties_provisioning_state, subnet=properties_subnet, upgrade_status=properties_upgrade_status)


def storagecache_cache_delete(cmd, client,
                              resource_group_name,
                              cache_name):
    return client.begin_delete(resource_group_name=resource_group_name, cache_name=cache_name)


def storagecache_cache_flush(cmd, client,
                             resource_group_name,
                             cache_name):
    return client.begin_flush(resource_group_name=resource_group_name, cache_name=cache_name)


def storagecache_cache_start(cmd, client,
                             resource_group_name,
                             cache_name):
    return client.begin_start(resource_group_name=resource_group_name, cache_name=cache_name)


def storagecache_cache_stop(cmd, client,
                            resource_group_name,
                            cache_name):
    return client.begin_stop(resource_group_name=resource_group_name, cache_name=cache_name)


def storagecache_cache_upgrade_firmware(cmd, client,
                                        resource_group_name,
                                        cache_name):
    return client.begin_upgrade_firmware(resource_group_name=resource_group_name, cache_name=cache_name)


def storagecache_storage_target_list(cmd, client,
                                     resource_group_name,
                                     cache_name):
    return client.list_by_cache(resource_group_name=resource_group_name, cache_name=cache_name)


def storagecache_storage_target_show(cmd, client,
                                     resource_group_name,
                                     cache_name,
                                     storage_target_name):
    return client.get(resource_group_name=resource_group_name, cache_name=cache_name, storage_target_name=storage_target_name)


def storagecache_storage_target_create(cmd, client,
                                       resource_group_name,
                                       cache_name,
                                       storage_target_name,
                                       properties_junctions=None,
                                       properties_target_type=None,
                                       properties_provisioning_state=None,
                                       properties_nfs3=None,
                                       properties_clfs=None,
                                       properties_unknown=None):
    properties_unknown = json.loads(properties_unknown) if isinstance(properties_unknown, str) else properties_unknown
    return client.begin_create_or_update(resource_group_name=resource_group_name, cache_name=cache_name, storage_target_name=storage_target_name, junctions=properties_junctions, target_type=properties_target_type, provisioning_state=properties_provisioning_state, nfs3=properties_nfs3, clfs=properties_clfs, unknown=properties_unknown)


def storagecache_storage_target_update(cmd, client,
                                       resource_group_name,
                                       cache_name,
                                       storage_target_name,
                                       properties_junctions=None,
                                       properties_target_type=None,
                                       properties_provisioning_state=None,
                                       properties_nfs3=None,
                                       properties_clfs=None,
                                       properties_unknown=None):
    properties_unknown = json.loads(properties_unknown) if isinstance(properties_unknown, str) else properties_unknown
    return client.begin_create_or_update(resource_group_name=resource_group_name, cache_name=cache_name, storage_target_name=storage_target_name, junctions=properties_junctions, target_type=properties_target_type, provisioning_state=properties_provisioning_state, nfs3=properties_nfs3, clfs=properties_clfs, unknown=properties_unknown)


def storagecache_storage_target_delete(cmd, client,
                                       resource_group_name,
                                       cache_name,
                                       storage_target_name):
    return client.begin_delete(resource_group_name=resource_group_name, cache_name=cache_name, storage_target_name=storage_target_name)
