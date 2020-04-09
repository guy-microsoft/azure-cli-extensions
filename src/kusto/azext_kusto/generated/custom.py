# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines

import json


def kusto_cluster_list(cmd, client,
                       resource_group_name=None,
                       cluster_name=None):
    if resource_group_name is not None and cluster_name is not None:
        return client.list_sku_by_resource(resource_group_name=resource_group_name, cluster_name=cluster_name)
    elif resource_group_name is not None:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
        return client.list()
    return client.list_sku()


def kusto_cluster_show(cmd, client,
                       resource_group_name,
                       cluster_name):
    return client.get(resource_group_name=resource_group_name, cluster_name=cluster_name)


def kusto_cluster_create(cmd, client,
                         resource_group_name,
                         cluster_name,
                         location,
                         sku,
                         tags=None,
                         zones=None,
                         identity=None,
                         properties_trusted_external_tenants=None,
                         properties_optimized_autoscale=None,
                         properties_enable_disk_encryption=None,
                         properties_enable_streaming_ingest=None,
                         properties_virtual_network_configuration=None,
                         properties_key_vault_properties=None,
                         properties_enable_purge=None,
                         properties_language_extensions=None):
    zones = json.loads(zones) if isinstance(zones, str) else zones
    identity = json.loads(identity) if isinstance(identity, str) else identity
    return client.begin_create_or_update(resource_group_name=resource_group_name, cluster_name=cluster_name, tags=tags, location=location, sku=sku, zones=zones, identity=identity, trusted_external_tenants=properties_trusted_external_tenants, optimized_autoscale=properties_optimized_autoscale, enable_disk_encryption=properties_enable_disk_encryption, enable_streaming_ingest=properties_enable_streaming_ingest, virtual_network_configuration=properties_virtual_network_configuration, key_vault_properties=properties_key_vault_properties, enable_purge=properties_enable_purge, language_extensions=properties_language_extensions)


def kusto_cluster_update(cmd, client,
                         resource_group_name,
                         cluster_name,
                         tags=None,
                         location=None,
                         sku=None,
                         identity=None,
                         properties_trusted_external_tenants=None,
                         properties_optimized_autoscale=None,
                         properties_enable_disk_encryption=None,
                         properties_enable_streaming_ingest=None,
                         properties_virtual_network_configuration=None,
                         properties_key_vault_properties=None,
                         properties_enable_purge=None,
                         properties_language_extensions=None):
    identity = json.loads(identity) if isinstance(identity, str) else identity
    return client.begin_update(resource_group_name=resource_group_name, cluster_name=cluster_name, tags=tags, location=location, sku=sku, identity=identity, trusted_external_tenants=properties_trusted_external_tenants, optimized_autoscale=properties_optimized_autoscale, enable_disk_encryption=properties_enable_disk_encryption, enable_streaming_ingest=properties_enable_streaming_ingest, virtual_network_configuration=properties_virtual_network_configuration, key_vault_properties=properties_key_vault_properties, enable_purge=properties_enable_purge, language_extensions=properties_language_extensions)


def kusto_cluster_delete(cmd, client,
                         resource_group_name,
                         cluster_name):
    return client.begin_delete(resource_group_name=resource_group_name, cluster_name=cluster_name)


def kusto_cluster_detach_follower_database(cmd, client,
                                           resource_group_name,
                                           cluster_name,
                                           cluster_resource_id,
                                           attached_database_configuration_name):
    return client.begin_detach_follower_database(resource_group_name=resource_group_name, cluster_name=cluster_name, cluster_resource_id=cluster_resource_id, attached_database_configuration_name=attached_database_configuration_name)


def kusto_cluster_add_language_extension(cmd, client,
                                         resource_group_name,
                                         cluster_name,
                                         value=None):
    return client.begin_add_language_extension(resource_group_name=resource_group_name, cluster_name=cluster_name, value=value)


def kusto_cluster_remove_language_extension(cmd, client,
                                            resource_group_name,
                                            cluster_name,
                                            value=None):
    return client.begin_remove_language_extension(resource_group_name=resource_group_name, cluster_name=cluster_name, value=value)


def kusto_cluster_stop(cmd, client,
                       resource_group_name,
                       cluster_name):
    return client.begin_stop(resource_group_name=resource_group_name, cluster_name=cluster_name)


def kusto_cluster_start(cmd, client,
                        resource_group_name,
                        cluster_name):
    return client.begin_start(resource_group_name=resource_group_name, cluster_name=cluster_name)


def kusto_cluster_list_follower_database(cmd, client,
                                         resource_group_name,
                                         cluster_name):
    return client.list_follower_database(resource_group_name=resource_group_name, cluster_name=cluster_name)


def kusto_cluster_diagnose_virtual_network(cmd, client,
                                           resource_group_name,
                                           cluster_name):
    return client.begin_diagnose_virtual_network(resource_group_name=resource_group_name, cluster_name=cluster_name)


def kusto_cluster_list_language_extension(cmd, client,
                                          resource_group_name,
                                          cluster_name):
    return client.list_language_extension(resource_group_name=resource_group_name, cluster_name=cluster_name)


def kusto_cluster_principal_assignment_list(cmd, client,
                                            resource_group_name,
                                            cluster_name):
    return client.list(resource_group_name=resource_group_name, cluster_name=cluster_name)


def kusto_cluster_principal_assignment_show(cmd, client,
                                            resource_group_name,
                                            cluster_name,
                                            principal_assignment_name):
    return client.get(resource_group_name=resource_group_name, cluster_name=cluster_name, principal_assignment_name=principal_assignment_name)


def kusto_cluster_principal_assignment_create(cmd, client,
                                              resource_group_name,
                                              cluster_name,
                                              principal_assignment_name,
                                              properties_principal_id=None,
                                              properties_role=None,
                                              properties_tenant_id=None,
                                              properties_principal_type=None):
    return client.begin_create_or_update(resource_group_name=resource_group_name, cluster_name=cluster_name, principal_assignment_name=principal_assignment_name, principal_id=properties_principal_id, role=properties_role, tenant_id=properties_tenant_id, principal_type=properties_principal_type)


def kusto_cluster_principal_assignment_update(cmd, client,
                                              resource_group_name,
                                              cluster_name,
                                              principal_assignment_name,
                                              properties_principal_id=None,
                                              properties_role=None,
                                              properties_tenant_id=None,
                                              properties_principal_type=None):
    return client.begin_create_or_update(resource_group_name=resource_group_name, cluster_name=cluster_name, principal_assignment_name=principal_assignment_name, principal_id=properties_principal_id, role=properties_role, tenant_id=properties_tenant_id, principal_type=properties_principal_type)


def kusto_cluster_principal_assignment_delete(cmd, client,
                                              resource_group_name,
                                              cluster_name,
                                              principal_assignment_name):
    return client.begin_delete(resource_group_name=resource_group_name, cluster_name=cluster_name, principal_assignment_name=principal_assignment_name)


def kusto_database_list(cmd, client,
                        resource_group_name,
                        cluster_name):
    return client.list_by_cluster(resource_group_name=resource_group_name, cluster_name=cluster_name)


def kusto_database_show(cmd, client,
                        resource_group_name,
                        cluster_name,
                        database_name):
    return client.get(resource_group_name=resource_group_name, cluster_name=cluster_name, database_name=database_name)


def kusto_database_create(cmd, client,
                          resource_group_name,
                          cluster_name,
                          database_name,
                          kind,
                          location=None):
    return client.begin_create_or_update(resource_group_name=resource_group_name, cluster_name=cluster_name, database_name=database_name, location=location, kind=kind)


def kusto_database_update(cmd, client,
                          resource_group_name,
                          cluster_name,
                          database_name,
                          kind,
                          location=None):
    return client.begin_update(resource_group_name=resource_group_name, cluster_name=cluster_name, database_name=database_name, location=location, kind=kind)


def kusto_database_delete(cmd, client,
                          resource_group_name,
                          cluster_name,
                          database_name):
    return client.begin_delete(resource_group_name=resource_group_name, cluster_name=cluster_name, database_name=database_name)


def kusto_database_add_principal(cmd, client,
                                 resource_group_name,
                                 cluster_name,
                                 database_name,
                                 value=None):
    return client.add_principal(resource_group_name=resource_group_name, cluster_name=cluster_name, database_name=database_name, value=value)


def kusto_database_remove_principal(cmd, client,
                                    resource_group_name,
                                    cluster_name,
                                    database_name,
                                    value=None):
    return client.remove_principal(resource_group_name=resource_group_name, cluster_name=cluster_name, database_name=database_name, value=value)


def kusto_database_list_principal(cmd, client,
                                  resource_group_name,
                                  cluster_name,
                                  database_name):
    return client.list_principal(resource_group_name=resource_group_name, cluster_name=cluster_name, database_name=database_name)


def kusto_database_principal_assignment_list(cmd, client,
                                             resource_group_name,
                                             cluster_name,
                                             database_name):
    return client.list(resource_group_name=resource_group_name, cluster_name=cluster_name, database_name=database_name)


def kusto_database_principal_assignment_show(cmd, client,
                                             resource_group_name,
                                             cluster_name,
                                             database_name,
                                             principal_assignment_name):
    return client.get(resource_group_name=resource_group_name, cluster_name=cluster_name, database_name=database_name, principal_assignment_name=principal_assignment_name)


def kusto_database_principal_assignment_create(cmd, client,
                                               resource_group_name,
                                               cluster_name,
                                               database_name,
                                               principal_assignment_name,
                                               properties_principal_id=None,
                                               properties_role=None,
                                               properties_tenant_id=None,
                                               properties_principal_type=None):
    return client.begin_create_or_update(resource_group_name=resource_group_name, cluster_name=cluster_name, database_name=database_name, principal_assignment_name=principal_assignment_name, principal_id=properties_principal_id, role=properties_role, tenant_id=properties_tenant_id, principal_type=properties_principal_type)


def kusto_database_principal_assignment_update(cmd, client,
                                               resource_group_name,
                                               cluster_name,
                                               database_name,
                                               principal_assignment_name,
                                               properties_principal_id=None,
                                               properties_role=None,
                                               properties_tenant_id=None,
                                               properties_principal_type=None):
    return client.begin_create_or_update(resource_group_name=resource_group_name, cluster_name=cluster_name, database_name=database_name, principal_assignment_name=principal_assignment_name, principal_id=properties_principal_id, role=properties_role, tenant_id=properties_tenant_id, principal_type=properties_principal_type)


def kusto_database_principal_assignment_delete(cmd, client,
                                               resource_group_name,
                                               cluster_name,
                                               database_name,
                                               principal_assignment_name):
    return client.begin_delete(resource_group_name=resource_group_name, cluster_name=cluster_name, database_name=database_name, principal_assignment_name=principal_assignment_name)


def kusto_attached_database_configuration_list(cmd, client,
                                               resource_group_name,
                                               cluster_name):
    return client.list_by_cluster(resource_group_name=resource_group_name, cluster_name=cluster_name)


def kusto_attached_database_configuration_show(cmd, client,
                                               resource_group_name,
                                               cluster_name,
                                               attached_database_configuration_name):
    return client.get(resource_group_name=resource_group_name, cluster_name=cluster_name, attached_database_configuration_name=attached_database_configuration_name)


def kusto_attached_database_configuration_create(cmd, client,
                                                 resource_group_name,
                                                 cluster_name,
                                                 attached_database_configuration_name,
                                                 location=None,
                                                 properties_database_name=None,
                                                 properties_cluster_resource_id=None,
                                                 properties_default_principals_modification_kind=None):
    return client.begin_create_or_update(resource_group_name=resource_group_name, cluster_name=cluster_name, attached_database_configuration_name=attached_database_configuration_name, location=location, database_name=properties_database_name, cluster_resource_id=properties_cluster_resource_id, default_principals_modification_kind=properties_default_principals_modification_kind)


def kusto_attached_database_configuration_update(cmd, client,
                                                 resource_group_name,
                                                 cluster_name,
                                                 attached_database_configuration_name,
                                                 location=None,
                                                 properties_database_name=None,
                                                 properties_cluster_resource_id=None,
                                                 properties_default_principals_modification_kind=None):
    return client.begin_create_or_update(resource_group_name=resource_group_name, cluster_name=cluster_name, attached_database_configuration_name=attached_database_configuration_name, location=location, database_name=properties_database_name, cluster_resource_id=properties_cluster_resource_id, default_principals_modification_kind=properties_default_principals_modification_kind)


def kusto_attached_database_configuration_delete(cmd, client,
                                                 resource_group_name,
                                                 cluster_name,
                                                 attached_database_configuration_name):
    return client.begin_delete(resource_group_name=resource_group_name, cluster_name=cluster_name, attached_database_configuration_name=attached_database_configuration_name)


def kusto_data_connection_list(cmd, client,
                               resource_group_name,
                               cluster_name,
                               database_name):
    return client.list_by_database(resource_group_name=resource_group_name, cluster_name=cluster_name, database_name=database_name)


def kusto_data_connection_show(cmd, client,
                               resource_group_name,
                               cluster_name,
                               database_name,
                               data_connection_name):
    return client.get(resource_group_name=resource_group_name, cluster_name=cluster_name, database_name=database_name, data_connection_name=data_connection_name)


def kusto_data_connection_create(cmd, client,
                                 resource_group_name,
                                 cluster_name,
                                 database_name,
                                 data_connection_name,
                                 kind,
                                 location=None):
    return client.begin_create_or_update(resource_group_name=resource_group_name, cluster_name=cluster_name, database_name=database_name, data_connection_name=data_connection_name, location=location, kind=kind)


def kusto_data_connection_update(cmd, client,
                                 resource_group_name,
                                 cluster_name,
                                 database_name,
                                 data_connection_name,
                                 kind,
                                 location=None):
    return client.begin_update(resource_group_name=resource_group_name, cluster_name=cluster_name, database_name=database_name, data_connection_name=data_connection_name, location=location, kind=kind)


def kusto_data_connection_delete(cmd, client,
                                 resource_group_name,
                                 cluster_name,
                                 database_name,
                                 data_connection_name):
    return client.begin_delete(resource_group_name=resource_group_name, cluster_name=cluster_name, database_name=database_name, data_connection_name=data_connection_name)


def kusto_data_connection_data_connection_validation(cmd, client,
                                                     resource_group_name,
                                                     cluster_name,
                                                     database_name,
                                                     data_connection_name=None,
                                                     properties=None):
    properties = json.loads(properties) if isinstance(properties, str) else properties
    return client.data_connection_validation(resource_group_name=resource_group_name, cluster_name=cluster_name, database_name=database_name, data_connection_name=data_connection_name, properties=properties)
