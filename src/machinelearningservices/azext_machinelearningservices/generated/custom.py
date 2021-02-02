# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines

from azure.cli.core.util import sdk_no_wait


def machinelearningservices_workspace_list(client,
                                           resource_group_name=None,
                                           skiptoken=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name,
                                             skiptoken=skiptoken)
    return client.list_by_subscription(skiptoken=skiptoken)


def machinelearningservices_workspace_show(client,
                                           resource_group_name,
                                           workspace_name):
    return client.get(resource_group_name=resource_group_name,
                      workspace_name=workspace_name)


def machinelearningservices_workspace_create(client,
                                             resource_group_name,
                                             workspace_name,
                                             location=None,
                                             tags=None,
                                             sku=None,
                                             type_=None,
                                             user_assigned_identities=None,
                                             description=None,
                                             friendly_name=None,
                                             key_vault=None,
                                             application_insights=None,
                                             container_registry=None,
                                             storage_account=None,
                                             discovery_url=None,
                                             hbi_workspace=None,
                                             image_build_compute=None,
                                             allow_public_access_when_behind_vnet=None,
                                             shared_private_link_resources=None,
                                             status=None,
                                             key_vault_properties=None,
                                             no_wait=False):
    if hbi_workspace is None:
        hbi_workspace = False
    if allow_public_access_when_behind_vnet is None:
        allow_public_access_when_behind_vnet = False
    parameters = {}
    parameters['location'] = location
    parameters['tags'] = tags
    parameters['sku'] = sku
    parameters['identity'] = {}
    parameters['identity']['type'] = type_
    parameters['identity']['user_assigned_identities'] = user_assigned_identities
    parameters['friendly_name'] = friendly_name
    parameters['key_vault'] = key_vault
    parameters['application_insights'] = application_insights
    parameters['container_registry'] = container_registry
    parameters['storage_account'] = storage_account
    parameters['discovery_url'] = discovery_url
    parameters['hbi_workspace'] = False if hbi_workspace is None else hbi_workspace
    parameters['image_build_compute'] = image_build_compute
    parameters['allow_public_access_when_behind_vnet'] = False if allow_public_access_when_behind_vnet is None else allow_public_access_when_behind_vnet
    parameters['shared_private_link_resources'] = shared_private_link_resources
    parameters['encryption'] = {}
    parameters['encryption']['status'] = status
    parameters['encryption']['key_vault_properties'] = key_vault_properties
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       parameters=parameters)


def machinelearningservices_workspace_update(client,
                                             resource_group_name,
                                             workspace_name,
                                             tags=None,
                                             sku=None,
                                             description=None,
                                             friendly_name=None):
    parameters = {}
    parameters['tags'] = tags
    parameters['sku'] = sku
    parameters['description'] = description
    parameters['friendly_name'] = friendly_name
    return client.update(resource_group_name=resource_group_name,
                         workspace_name=workspace_name,
                         parameters=parameters)


def machinelearningservices_workspace_delete(client,
                                             resource_group_name,
                                             workspace_name,
                                             no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name)


def machinelearningservices_workspace_list_key(client,
                                               resource_group_name,
                                               workspace_name):
    return client.list_keys(resource_group_name=resource_group_name,
                            workspace_name=workspace_name)


def machinelearningservices_workspace_resync_key(client,
                                                 resource_group_name,
                                                 workspace_name):
    return client.resync_keys(resource_group_name=resource_group_name,
                              workspace_name=workspace_name)


def machinelearningservices_workspace_feature_list(client,
                                                   resource_group_name,
                                                   workspace_name):
    return client.list(resource_group_name=resource_group_name,
                       workspace_name=workspace_name)


def machinelearningservices_notebook_prepare(client,
                                             resource_group_name,
                                             workspace_name):
    return client.begin_prepare(resource_group_name=resource_group_name,
                                workspace_name=workspace_name)


def machinelearningservices_usage_list(client,
                                       location):
    return client.list(location=location)


def machinelearningservices_virtual_machine_size_list(client,
                                                      location,
                                                      compute_type=None,
                                                      recommended=None):
    return client.list(location=location,
                       compute_type=compute_type,
                       recommended=recommended)


def machinelearningservices_quota_list(client,
                                       location):
    return client.list(location=location)


def machinelearningservices_quota_update(client,
                                         location,
                                         value=None):
    parameters = {}
    parameters['value'] = value
    return client.update(location=location,
                         parameters=parameters)


def machinelearningservices_workspace_connection_list(client,
                                                      resource_group_name,
                                                      workspace_name,
                                                      target=None,
                                                      category=None):
    return client.list(resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       target=target,
                       category=category)


def machinelearningservices_workspace_connection_show(client,
                                                      resource_group_name,
                                                      workspace_name,
                                                      connection_name):
    return client.get(resource_group_name=resource_group_name,
                      workspace_name=workspace_name,
                      connection_name=connection_name)


def machinelearningservices_workspace_connection_create(client,
                                                        resource_group_name,
                                                        workspace_name,
                                                        connection_name,
                                                        name=None,
                                                        category=None,
                                                        target=None,
                                                        auth_type=None,
                                                        value=None):
    parameters = {}
    parameters['name'] = name
    parameters['category'] = category
    parameters['target'] = target
    parameters['auth_type'] = auth_type
    parameters['value'] = value
    return client.create(resource_group_name=resource_group_name,
                         workspace_name=workspace_name,
                         connection_name=connection_name,
                         parameters=parameters)


def machinelearningservices_workspace_connection_delete(client,
                                                        resource_group_name,
                                                        workspace_name,
                                                        connection_name):
    return client.delete(resource_group_name=resource_group_name,
                         workspace_name=workspace_name,
                         connection_name=connection_name)


def machinelearningservices_machine_learning_compute_list(client,
                                                          resource_group_name,
                                                          workspace_name,
                                                          skiptoken=None):
    return client.list_by_workspace(resource_group_name=resource_group_name,
                                    workspace_name=workspace_name,
                                    skiptoken=skiptoken)


def machinelearningservices_machine_learning_compute_show(client,
                                                          resource_group_name,
                                                          workspace_name,
                                                          compute_name):
    return client.get(resource_group_name=resource_group_name,
                      workspace_name=workspace_name,
                      compute_name=compute_name)


def machinelearningservices_machine_learning_compute_aks_create(client,
                                                                resource_group_name,
                                                                workspace_name,
                                                                compute_name,
                                                                location=None,
                                                                tags=None,
                                                                sku=None,
                                                                type_=None,
                                                                user_assigned_identities=None,
                                                                ak_s_compute_location=None,
                                                                ak_s_description=None,
                                                                ak_s_resource_id=None,
                                                                ak_s_properties=None,
                                                                no_wait=False):
    parameters = {}
    parameters['location'] = location
    parameters['tags'] = tags
    parameters['sku'] = sku
    parameters['identity'] = {}
    parameters['identity']['type'] = type_
    parameters['identity']['user_assigned_identities'] = user_assigned_identities
    parameters['properties'] = {}
    parameters['properties']['compute_type'] = 'Aks'
    parameters['properties']['compute_location'] = ak_s_compute_location
    parameters['properties']['description'] = ak_s_description
    parameters['properties']['resource_id'] = ak_s_resource_id
    parameters['properties']['properties'] = ak_s_properties
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       compute_name=compute_name,
                       parameters=parameters)


def machinelearningservices_machine_learning_compute_aml_compute_create(client,
                                                                        resource_group_name,
                                                                        workspace_name,
                                                                        compute_name,
                                                                        location=None,
                                                                        tags=None,
                                                                        sku=None,
                                                                        type_=None,
                                                                        user_assigned_identities=None,
                                                                        compute_location=None,
                                                                        description=None,
                                                                        resource_id=None,
                                                                        aml_compute_properties=None,
                                                                        no_wait=False):
    parameters = {}
    parameters['location'] = location
    parameters['tags'] = tags
    parameters['sku'] = sku
    parameters['identity'] = {}
    parameters['identity']['type'] = type_
    parameters['identity']['user_assigned_identities'] = user_assigned_identities
    parameters['properties'] = {}
    parameters['properties']['compute_type'] = 'AmlCompute'
    parameters['properties']['compute_location'] = compute_location
    parameters['properties']['description'] = description
    parameters['properties']['resource_id'] = resource_id
    parameters['properties']['properties'] = aml_compute_properties
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       compute_name=compute_name,
                       parameters=parameters)


def machinelearningservices_machine_learning_compute_compute_instance_create(client,
                                                                             resource_group_name,
                                                                             workspace_name,
                                                                             compute_name,
                                                                             location=None,
                                                                             tags=None,
                                                                             sku=None,
                                                                             type_=None,
                                                                             user_assigned_identities=None,
                                                                             compute_location=None,
                                                                             description=None,
                                                                             resource_id=None,
                                                                             vm_size=None,
                                                                             application_sharing_policy=None,
                                                                             ssh_settings=None,
                                                                             id_=None,
                                                                             no_wait=False):
    if application_sharing_policy is None:
        application_sharing_policy = "Shared"
    parameters = {}
    parameters['location'] = location
    parameters['tags'] = tags
    parameters['sku'] = sku
    parameters['identity'] = {}
    parameters['identity']['type'] = type_
    parameters['identity']['user_assigned_identities'] = user_assigned_identities
    parameters['properties'] = {}
    parameters['properties']['compute_type'] = 'ComputeInstance'
    parameters['properties']['compute_location'] = compute_location
    parameters['properties']['description'] = description
    parameters['properties']['resource_id'] = resource_id
    parameters['properties']['properties'] = {}
    parameters['properties']['properties']['vm_size'] = vm_size
    parameters['properties']['properties']['application_sharing_policy'] = "Shared" if application_sharing_policy is None else application_sharing_policy
    parameters['properties']['properties']['ssh_settings'] = ssh_settings
    parameters['properties']['properties']['subnet'] = {}
    parameters['properties']['properties']['subnet']['id'] = id_
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       compute_name=compute_name,
                       parameters=parameters)


def machinelearningservices_machine_learning_compute_data_factory_create(client,
                                                                         resource_group_name,
                                                                         workspace_name,
                                                                         compute_name,
                                                                         location=None,
                                                                         tags=None,
                                                                         sku=None,
                                                                         type_=None,
                                                                         user_assigned_identities=None,
                                                                         compute_location=None,
                                                                         description=None,
                                                                         resource_id=None,
                                                                         no_wait=False):
    parameters = {}
    parameters['location'] = location
    parameters['tags'] = tags
    parameters['sku'] = sku
    parameters['identity'] = {}
    parameters['identity']['type'] = type_
    parameters['identity']['user_assigned_identities'] = user_assigned_identities
    parameters['properties'] = {}
    parameters['properties']['compute_type'] = 'DataFactory'
    parameters['properties']['compute_location'] = compute_location
    parameters['properties']['description'] = description
    parameters['properties']['resource_id'] = resource_id
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       compute_name=compute_name,
                       parameters=parameters)


def machinelearningservices_machine_learning_compute_data_lake_analytics_create(client,
                                                                                resource_group_name,
                                                                                workspace_name,
                                                                                compute_name,
                                                                                location=None,
                                                                                tags=None,
                                                                                sku=None,
                                                                                type_=None,
                                                                                user_assigned_identities=None,
                                                                                compute_location=None,
                                                                                description=None,
                                                                                resource_id=None,
                                                                                data_lake_store_account_name=None,
                                                                                no_wait=False):
    parameters = {}
    parameters['location'] = location
    parameters['tags'] = tags
    parameters['sku'] = sku
    parameters['identity'] = {}
    parameters['identity']['type'] = type_
    parameters['identity']['user_assigned_identities'] = user_assigned_identities
    parameters['properties'] = {}
    parameters['properties']['compute_type'] = 'DataLakeAnalytics'
    parameters['properties']['compute_location'] = compute_location
    parameters['properties']['description'] = description
    parameters['properties']['resource_id'] = resource_id
    parameters['properties']['properties'] = {}
    parameters['properties']['properties']['data_lake_store_account_name'] = data_lake_store_account_name
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       compute_name=compute_name,
                       parameters=parameters)


def machinelearningservices_machine_learning_compute_databricks_create(client,
                                                                       resource_group_name,
                                                                       workspace_name,
                                                                       compute_name,
                                                                       location=None,
                                                                       tags=None,
                                                                       sku=None,
                                                                       type_=None,
                                                                       user_assigned_identities=None,
                                                                       compute_location=None,
                                                                       description=None,
                                                                       resource_id=None,
                                                                       databricks_access_token=None,
                                                                       no_wait=False):
    parameters = {}
    parameters['location'] = location
    parameters['tags'] = tags
    parameters['sku'] = sku
    parameters['identity'] = {}
    parameters['identity']['type'] = type_
    parameters['identity']['user_assigned_identities'] = user_assigned_identities
    parameters['properties'] = {}
    parameters['properties']['compute_type'] = 'Databricks'
    parameters['properties']['compute_location'] = compute_location
    parameters['properties']['description'] = description
    parameters['properties']['resource_id'] = resource_id
    parameters['properties']['properties'] = {}
    parameters['properties']['properties']['databricks_access_token'] = databricks_access_token
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       compute_name=compute_name,
                       parameters=parameters)


def machinelearningservices_machine_learning_compute_hd_insight_create(client,
                                                                       resource_group_name,
                                                                       workspace_name,
                                                                       compute_name,
                                                                       location=None,
                                                                       tags=None,
                                                                       sku=None,
                                                                       type_=None,
                                                                       user_assigned_identities=None,
                                                                       compute_location=None,
                                                                       description=None,
                                                                       resource_id=None,
                                                                       ssh_port=None,
                                                                       address=None,
                                                                       administrator_account=None,
                                                                       no_wait=False):
    parameters = {}
    parameters['location'] = location
    parameters['tags'] = tags
    parameters['sku'] = sku
    parameters['identity'] = {}
    parameters['identity']['type'] = type_
    parameters['identity']['user_assigned_identities'] = user_assigned_identities
    parameters['properties'] = {}
    parameters['properties']['compute_type'] = 'HdInsight'
    parameters['properties']['compute_location'] = compute_location
    parameters['properties']['description'] = description
    parameters['properties']['resource_id'] = resource_id
    parameters['properties']['properties'] = {}
    parameters['properties']['properties']['ssh_port'] = ssh_port
    parameters['properties']['properties']['address'] = address
    parameters['properties']['properties']['administrator_account'] = administrator_account
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       compute_name=compute_name,
                       parameters=parameters)


def machinelearningservices_machine_learning_compute_virtual_machine_create(client,
                                                                            resource_group_name,
                                                                            workspace_name,
                                                                            compute_name,
                                                                            location=None,
                                                                            tags=None,
                                                                            sku=None,
                                                                            type_=None,
                                                                            user_assigned_identities=None,
                                                                            compute_location=None,
                                                                            description=None,
                                                                            resource_id=None,
                                                                            virtual_machine_size=None,
                                                                            ssh_port=None,
                                                                            address=None,
                                                                            administrator_account=None,
                                                                            no_wait=False):
    parameters = {}
    parameters['location'] = location
    parameters['tags'] = tags
    parameters['sku'] = sku
    parameters['identity'] = {}
    parameters['identity']['type'] = type_
    parameters['identity']['user_assigned_identities'] = user_assigned_identities
    parameters['properties'] = {}
    parameters['properties']['compute_type'] = 'VirtualMachine'
    parameters['properties']['compute_location'] = compute_location
    parameters['properties']['description'] = description
    parameters['properties']['resource_id'] = resource_id
    parameters['properties']['properties'] = {}
    parameters['properties']['properties']['virtual_machine_size'] = virtual_machine_size
    parameters['properties']['properties']['ssh_port'] = ssh_port
    parameters['properties']['properties']['address'] = address
    parameters['properties']['properties']['administrator_account'] = administrator_account
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       compute_name=compute_name,
                       parameters=parameters)


def machinelearningservices_machine_learning_compute_update(client,
                                                            resource_group_name,
                                                            workspace_name,
                                                            compute_name,
                                                            scale_settings=None,
                                                            no_wait=False):
    parameters = {}
    parameters['scale_settings'] = scale_settings
    return sdk_no_wait(no_wait,
                       client.begin_update,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       compute_name=compute_name,
                       parameters=parameters)


def machinelearningservices_machine_learning_compute_delete(client,
                                                            resource_group_name,
                                                            workspace_name,
                                                            compute_name,
                                                            underlying_resource_action,
                                                            no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       compute_name=compute_name,
                       underlying_resource_action=underlying_resource_action)


def machinelearningservices_machine_learning_compute_list_key(client,
                                                              resource_group_name,
                                                              workspace_name,
                                                              compute_name):
    return client.list_keys(resource_group_name=resource_group_name,
                            workspace_name=workspace_name,
                            compute_name=compute_name)


def machinelearningservices_machine_learning_compute_list_node(client,
                                                               resource_group_name,
                                                               workspace_name,
                                                               compute_name):
    return client.list_nodes(resource_group_name=resource_group_name,
                             workspace_name=workspace_name,
                             compute_name=compute_name)


def machinelearningservices_machine_learning_compute_restart(client,
                                                             resource_group_name,
                                                             workspace_name,
                                                             compute_name):
    return client.restart(resource_group_name=resource_group_name,
                          workspace_name=workspace_name,
                          compute_name=compute_name)


def machinelearningservices_machine_learning_compute_start(client,
                                                           resource_group_name,
                                                           workspace_name,
                                                           compute_name):
    return client.start(resource_group_name=resource_group_name,
                        workspace_name=workspace_name,
                        compute_name=compute_name)


def machinelearningservices_machine_learning_compute_stop(client,
                                                          resource_group_name,
                                                          workspace_name,
                                                          compute_name):
    return client.stop(resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       compute_name=compute_name)


def machinelearningservices_list_sku(client):
    return client.list_skus()


def machinelearningservices_private_endpoint_connection_show(client,
                                                             resource_group_name,
                                                             workspace_name,
                                                             private_endpoint_connection_name):
    return client.get(resource_group_name=resource_group_name,
                      workspace_name=workspace_name,
                      private_endpoint_connection_name=private_endpoint_connection_name)


def machinelearningservices_private_endpoint_connection_delete(client,
                                                               resource_group_name,
                                                               workspace_name,
                                                               private_endpoint_connection_name,
                                                               no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       private_endpoint_connection_name=private_endpoint_connection_name)


def machinelearningservices_private_endpoint_connection_put(client,
                                                            resource_group_name,
                                                            workspace_name,
                                                            private_endpoint_connection_name,
                                                            private_link_service_connection_state=None):
    properties = {}
    properties['private_link_service_connection_state'] = private_link_service_connection_state
    return client.put(resource_group_name=resource_group_name,
                      workspace_name=workspace_name,
                      private_endpoint_connection_name=private_endpoint_connection_name,
                      properties=properties)


def machinelearningservices_private_link_resource_list(client,
                                                       resource_group_name,
                                                       workspace_name):
    return client.list_by_workspace(resource_group_name=resource_group_name,
                                    workspace_name=workspace_name)
