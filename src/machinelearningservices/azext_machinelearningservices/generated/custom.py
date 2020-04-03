# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines

import json


def machinelearningservices_workspace_list(cmd, client,
                                           resource_group_name=None,
                                           skiptoken=None):
    if resource_group_name is not None:
        return client.list_by_resource_group(resource_group_name=resource_group_name, skiptoken=skiptoken)
    return client.list_by_subscription(skiptoken=skiptoken)


def machinelearningservices_workspace_show(cmd, client,
                                           resource_group_name,
                                           workspace_name):
    return client.get(resource_group_name=resource_group_name, workspace_name=workspace_name)


def machinelearningservices_workspace_create(cmd, client,
                                             resource_group_name,
                                             workspace_name,
                                             identity=None,
                                             location=None,
                                             tags=None,
                                             sku=None,
                                             properties_description=None,
                                             properties_friendly_name=None,
                                             properties_key_vault=None,
                                             properties_application_insights=None,
                                             properties_container_registry=None,
                                             properties_storage_account=None,
                                             properties_discovery_url=None,
                                             properties_encryption=None,
                                             properties_hbi_workspace=None,
                                             properties_image_build_compute=None,
                                             properties_allow_public_access_when_behind_vnet=None,
                                             properties_shared_private_link_resources=None,
                                             properties_linked_workspaces=None):
    identity = json.loads(identity) if isinstance(identity, str) else identity
    properties_encryption = json.loads(properties_encryption) if isinstance(properties_encryption, str) else properties_encryption
    properties_linked_workspaces = json.loads(properties_linked_workspaces) if isinstance(properties_linked_workspaces, str) else properties_linked_workspaces
    return client.begin_create_or_update(resource_group_name=resource_group_name, workspace_name=workspace_name, identity=identity, location=location, tags=tags, sku=sku, description=properties_description, friendly_name=properties_friendly_name, key_vault=properties_key_vault, application_insights=properties_application_insights, container_registry=properties_container_registry, storage_account=properties_storage_account, discovery_url=properties_discovery_url, encryption=properties_encryption, hbi_workspace=properties_hbi_workspace, image_build_compute=properties_image_build_compute, allow_public_access_when_behind_vnet=properties_allow_public_access_when_behind_vnet, shared_private_link_resources=properties_shared_private_link_resources, linked_workspaces=properties_linked_workspaces)


def machinelearningservices_workspace_update(cmd, client,
                                             resource_group_name,
                                             workspace_name,
                                             tags=None,
                                             sku=None,
                                             properties_description=None,
                                             properties_friendly_name=None):
    return client.update(resource_group_name=resource_group_name, workspace_name=workspace_name, tags=tags, sku=sku, description=properties_description, friendly_name=properties_friendly_name)


def machinelearningservices_workspace_delete(cmd, client,
                                             resource_group_name,
                                             workspace_name):
    return client.delete(resource_group_name=resource_group_name, workspace_name=workspace_name)


def machinelearningservices_workspace_list_key(cmd, client,
                                               resource_group_name,
                                               workspace_name):
    return client.list_key(resource_group_name=resource_group_name, workspace_name=workspace_name)


def machinelearningservices_workspace_resync_key(cmd, client,
                                                 resource_group_name,
                                                 workspace_name):
    return client.resync_key(resource_group_name=resource_group_name, workspace_name=workspace_name)


def machinelearningservices_workspace_feature_list(cmd, client,
                                                   resource_group_name,
                                                   workspace_name):
    return client.list(resource_group_name=resource_group_name, workspace_name=workspace_name)


def machinelearningservices_usage_list(cmd, client,
                                       location):
    return client.list(location=location)


def machinelearningservices_virtual_machine_size_list(cmd, client,
                                                      location):
    return client.list(location=location)


def machinelearningservices_quota_list(cmd, client,
                                       location):
    return client.list(location=location)


def machinelearningservices_quota_update(cmd, client,
                                         location,
                                         value=None):
    return client.update(location=location, value=value)


def machinelearningservices_machine_learning_compute_list(cmd, client,
                                                          resource_group_name,
                                                          workspace_name,
                                                          skiptoken=None):
    return client.list_by_workspace(resource_group_name=resource_group_name, workspace_name=workspace_name, skiptoken=skiptoken)


def machinelearningservices_machine_learning_compute_show(cmd, client,
                                                          resource_group_name,
                                                          workspace_name,
                                                          compute_name):
    return client.get(resource_group_name=resource_group_name, workspace_name=workspace_name, compute_name=compute_name)


def machinelearningservices_machine_learning_compute_create(cmd, client,
                                                            resource_group_name,
                                                            workspace_name,
                                                            compute_name,
                                                            identity=None,
                                                            location=None,
                                                            tags=None,
                                                            sku=None,
                                                            properties=None):
    identity = json.loads(identity) if isinstance(identity, str) else identity
    properties = json.loads(properties) if isinstance(properties, str) else properties
    return client.begin_create_or_update(resource_group_name=resource_group_name, workspace_name=workspace_name, compute_name=compute_name, identity=identity, location=location, tags=tags, sku=sku, properties=properties)


def machinelearningservices_machine_learning_compute_update(cmd, client,
                                                            resource_group_name,
                                                            workspace_name,
                                                            compute_name,
                                                            properties_scale_settings=None):
    return client.begin_update(resource_group_name=resource_group_name, workspace_name=workspace_name, compute_name=compute_name, scale_settings=properties_scale_settings)


def machinelearningservices_machine_learning_compute_delete(cmd, client,
                                                            resource_group_name,
                                                            workspace_name,
                                                            compute_name,
                                                            underlying_resource_action):
    return client.begin_delete(resource_group_name=resource_group_name, workspace_name=workspace_name, compute_name=compute_name, underlying_resource_action=underlying_resource_action)


def machinelearningservices_machine_learning_compute_list_node(cmd, client,
                                                               resource_group_name,
                                                               workspace_name,
                                                               compute_name):
    return client.list_node(resource_group_name=resource_group_name, workspace_name=workspace_name, compute_name=compute_name)


def machinelearningservices_machine_learning_compute_list_key(cmd, client,
                                                              resource_group_name,
                                                              workspace_name,
                                                              compute_name):
    return client.list_key(resource_group_name=resource_group_name, workspace_name=workspace_name, compute_name=compute_name)


def machinelearningservices__list(cmd, client):
    return client.list_sku()


def machinelearningservices_private_endpoint_connection_show(cmd, client,
                                                             resource_group_name,
                                                             workspace_name,
                                                             private_endpoint_connection_name):
    return client.get(resource_group_name=resource_group_name, workspace_name=workspace_name, private_endpoint_connection_name=private_endpoint_connection_name)


def machinelearningservices_private_endpoint_connection_delete(cmd, client,
                                                               resource_group_name,
                                                               workspace_name,
                                                               private_endpoint_connection_name):
    return client.delete(resource_group_name=resource_group_name, workspace_name=workspace_name, private_endpoint_connection_name=private_endpoint_connection_name)


def machinelearningservices_private_endpoint_connection_put(cmd, client,
                                                            resource_group_name,
                                                            workspace_name,
                                                            private_endpoint_connection_name,
                                                            identity=None,
                                                            location=None,
                                                            tags=None,
                                                            sku=None,
                                                            properties_private_endpoint=None,
                                                            properties_private_link_service_connection_state=None,
                                                            properties_provisioning_state=None):
    identity = json.loads(identity) if isinstance(identity, str) else identity
    return client.put(resource_group_name=resource_group_name, workspace_name=workspace_name, private_endpoint_connection_name=private_endpoint_connection_name, identity=identity, location=location, tags=tags, sku=sku, private_endpoint=properties_private_endpoint, private_link_service_connection_state=properties_private_link_service_connection_state, provisioning_state=properties_provisioning_state)


def machinelearningservices_private_link_resource_list(cmd, client,
                                                       resource_group_name,
                                                       workspace_name):
    return client.list_by_workspace(resource_group_name=resource_group_name, workspace_name=workspace_name)


def machinelearningservices_linked_workspace_list(cmd, client,
                                                  resource_group_name,
                                                  workspace_name,
                                                  link_subscription_id=None,
                                                  link_resource_group=None,
                                                  link_resource_name=None,
                                                  link_resource_id=None,
                                                  uai_resource_id=None):
    return client.list(resource_group_name=resource_group_name, workspace_name=workspace_name, link_subscription_id=link_subscription_id, link_resource_group=link_resource_group, link_resource_name=link_resource_name, link_resource_id=link_resource_id, uai_resource_id=uai_resource_id)


def machinelearningservices_linked_workspace_show(cmd, client,
                                                  resource_group_name,
                                                  workspace_name,
                                                  link_name):
    return client.get(resource_group_name=resource_group_name, workspace_name=workspace_name, link_name=link_name)


def machinelearningservices_linked_workspace_create(cmd, client,
                                                    resource_group_name,
                                                    workspace_name,
                                                    link_name=None,
                                                    resource_id=None,
                                                    user_assigned_identity_resource_id=None):
    return client.create(resource_group_name=resource_group_name, workspace_name=workspace_name, link_name=link_name, resource_id=resource_id, user_assigned_identity_resource_id=user_assigned_identity_resource_id)


def machinelearningservices_linked_workspace_update(cmd, client,
                                                    resource_group_name,
                                                    workspace_name,
                                                    link_name,
                                                    user_assigned_identity_resource_id=None):
    return client.update(resource_group_name=resource_group_name, workspace_name=workspace_name, link_name=link_name, user_assigned_identity_resource_id=user_assigned_identity_resource_id)


def machinelearningservices_linked_workspace_delete(cmd, client,
                                                    resource_group_name,
                                                    workspace_name,
                                                    link_name):
    return client.delete(resource_group_name=resource_group_name, workspace_name=workspace_name, link_name=link_name)
