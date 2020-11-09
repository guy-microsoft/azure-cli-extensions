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


def storagecache_sku_list(client):
    return client.list()


def storagecache_usage_model_list(client):
    return client.list()


def storagecache_asc_operation_show(client,
                                    location,
                                    operation_id):
    return client.get(location=location,
                      operation_id=operation_id)


def storagecache_cache_list(client,
                            resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list()


def storagecache_cache_show(client,
                            resource_group_name,
                            cache_name):
    return client.get(resource_group_name=resource_group_name,
                      cache_name=cache_name)


def storagecache_cache_create(client,
                              resource_group_name,
                              cache_name,
                              tags=None,
                              location=None,
                              cache_size_gb=None,
                              provisioning_state=None,
                              subnet=None,
                              security_settings_root_squash=None,
                              encryption_settings_key_encryption_key=None,
                              network_settings_mtu=None,
                              sku_name=None,
                              identity_type=None,
                              no_wait=False):
    if network_settings_mtu is None:
        network_settings_mtu = 1500
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       cache_name=cache_name,
                       tags=tags,
                       location=location,
                       cache_size_gb=cache_size_gb,
                       provisioning_state=provisioning_state,
                       subnet=subnet,
                       upgrade_status=None,
                       root_squash=security_settings_root_squash,
                       key_encryption_key=encryption_settings_key_encryption_key,
                       mtu=network_settings_mtu,
                       name=sku_name,
                       type=identity_type)


def storagecache_cache_update(client,
                              resource_group_name,
                              cache_name,
                              tags=None,
                              location=None,
                              cache_size_gb=None,
                              provisioning_state=None,
                              subnet=None,
                              security_settings_root_squash=None,
                              encryption_settings_key_encryption_key=None,
                              network_settings_mtu=None,
                              sku_name=None,
                              identity_type=None):
    if network_settings_mtu is None:
        network_settings_mtu = 1500
    return client.update(resource_group_name=resource_group_name,
                         cache_name=cache_name,
                         tags=tags,
                         location=location,
                         cache_size_gb=cache_size_gb,
                         provisioning_state=provisioning_state,
                         subnet=subnet,
                         upgrade_status=None,
                         root_squash=security_settings_root_squash,
                         key_encryption_key=encryption_settings_key_encryption_key,
                         mtu=network_settings_mtu,
                         name=sku_name,
                         type=identity_type)


def storagecache_cache_delete(client,
                              resource_group_name,
                              cache_name,
                              no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       cache_name=cache_name)


def storagecache_cache_flush(client,
                             resource_group_name,
                             cache_name,
                             no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_flush,
                       resource_group_name=resource_group_name,
                       cache_name=cache_name)


def storagecache_cache_start(client,
                             resource_group_name,
                             cache_name,
                             no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_start,
                       resource_group_name=resource_group_name,
                       cache_name=cache_name)


def storagecache_cache_stop(client,
                            resource_group_name,
                            cache_name,
                            no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_stop,
                       resource_group_name=resource_group_name,
                       cache_name=cache_name)


def storagecache_cache_upgrade_firmware(client,
                                        resource_group_name,
                                        cache_name,
                                        no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_upgrade_firmware,
                       resource_group_name=resource_group_name,
                       cache_name=cache_name)


def storagecache_storage_target_list(client,
                                     resource_group_name,
                                     cache_name):
    return client.list_by_cache(resource_group_name=resource_group_name,
                                cache_name=cache_name)


def storagecache_storage_target_show(client,
                                     resource_group_name,
                                     cache_name,
                                     storage_target_name):
    return client.get(resource_group_name=resource_group_name,
                      cache_name=cache_name,
                      storage_target_name=storage_target_name)


def storagecache_storage_target_create(client,
                                       resource_group_name,
                                       cache_name,
                                       storage_target_name,
                                       junctions=None,
                                       provisioning_state=None,
                                       nfs3=None,
                                       unknown_unknown_map=None,
                                       clfs_target=None,
                                       no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       cache_name=cache_name,
                       storage_target_name=storage_target_name,
                       junctions=junctions,
                       target_type=target_type,
                       provisioning_state=provisioning_state,
                       nfs3=nfs3,
                       unknown_map=unknown_unknown_map,
                       target=clfs_target)


def storagecache_storage_target_update(client,
                                       resource_group_name,
                                       cache_name,
                                       storage_target_name,
                                       junctions=None,
                                       provisioning_state=None,
                                       nfs3=None,
                                       unknown_unknown_map=None,
                                       clfs_target=None,
                                       no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       cache_name=cache_name,
                       storage_target_name=storage_target_name,
                       junctions=junctions,
                       target_type=target_type,
                       provisioning_state=provisioning_state,
                       nfs3=nfs3,
                       unknown_map=unknown_unknown_map,
                       target=clfs_target)


def storagecache_storage_target_delete(client,
                                       resource_group_name,
                                       cache_name,
                                       storage_target_name,
                                       no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       cache_name=cache_name,
                       storage_target_name=storage_target_name)
