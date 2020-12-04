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
# pylint: disable=unused-argument

from knack.util import CLIError
from azure.cli.core.util import sdk_no_wait


def databoxedge_device_list(client,
                            resource_group_name=None,
                            expand=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name,
                                             expand=expand)
    return client.list_by_subscription(expand=expand)


def databoxedge_device_show(client,
                            device_name,
                            resource_group_name):
    return client.get(device_name=device_name,
                      resource_group_name=resource_group_name)


def databoxedge_device_create(client,
                              device_name,
                              resource_group_name,
                              location,
                              tags=None,
                              sku=None,
                              etag=None,
                              data_box_edge_device_status=None,
                              description=None,
                              model_description=None,
                              friendly_name=None,
                              no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       device_name=device_name,
                       resource_group_name=resource_group_name,
                       location=location,
                       tags=tags,
                       sku=sku,
                       etag=etag,
                       data_box_edge_device_status=data_box_edge_device_status,
                       description=description,
                       model_description=model_description,
                       friendly_name=friendly_name)


def databoxedge_device_update(client,
                              device_name,
                              resource_group_name,
                              tags=None):
    return client.update(device_name=device_name,
                         resource_group_name=resource_group_name,
                         tags=tags)


def databoxedge_device_delete(client,
                              device_name,
                              resource_group_name,
                              no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       device_name=device_name,
                       resource_group_name=resource_group_name)


def databoxedge_device_create_or_update_security_setting(client,
                                                         device_name,
                                                         resource_group_name,
                                                         device_admin_password,
                                                         no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update_security_setting,
                       device_name=device_name,
                       resource_group_name=resource_group_name,
                       device_admin_password=device_admin_password)


def databoxedge_device_download_update(client,
                                       device_name,
                                       resource_group_name,
                                       no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_download_update,
                       device_name=device_name,
                       resource_group_name=resource_group_name)


def databoxedge_device_get_extended_information(client,
                                                device_name,
                                                resource_group_name):
    return client.get_extended_information(device_name=device_name,
                                           resource_group_name=resource_group_name)


def databoxedge_device_get_network_setting(client,
                                           device_name,
                                           resource_group_name):
    return client.get_network_setting(device_name=device_name,
                                      resource_group_name=resource_group_name)


def databoxedge_device_get_update_summary(client,
                                          device_name,
                                          resource_group_name):
    return client.get_update_summary(device_name=device_name,
                                     resource_group_name=resource_group_name)


def databoxedge_device_install_update(client,
                                      device_name,
                                      resource_group_name,
                                      no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_install_update,
                       device_name=device_name,
                       resource_group_name=resource_group_name)


def databoxedge_device_scan_for_update(client,
                                       device_name,
                                       resource_group_name,
                                       no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_scan_for_update,
                       device_name=device_name,
                       resource_group_name=resource_group_name)


def databoxedge_device_upload_certificate(client,
                                          device_name,
                                          resource_group_name,
                                          certificate,
                                          authentication_type=None):
    return client.upload_certificate(device_name=device_name,
                                     resource_group_name=resource_group_name,
                                     authentication_type=authentication_type,
                                     certificate=certificate)


def databoxedge_alert_list(client,
                           device_name,
                           resource_group_name):
    return client.list_by_data_box_edge_device(device_name=device_name,
                                               resource_group_name=resource_group_name)


def databoxedge_alert_show(client,
                           device_name,
                           name,
                           resource_group_name):
    return client.get(device_name=device_name,
                      name=name,
                      resource_group_name=resource_group_name)


def databoxedge_bandwidth_schedule_list(client,
                                        device_name,
                                        resource_group_name):
    return client.list_by_data_box_edge_device(device_name=device_name,
                                               resource_group_name=resource_group_name)


def databoxedge_bandwidth_schedule_show(client,
                                        device_name,
                                        name,
                                        resource_group_name):
    return client.get(device_name=device_name,
                      name=name,
                      resource_group_name=resource_group_name)


def databoxedge_bandwidth_schedule_create(client,
                                          device_name,
                                          name,
                                          resource_group_name,
                                          start,
                                          stop,
                                          rate_in_mbps,
                                          days,
                                          no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       device_name=device_name,
                       name=name,
                       resource_group_name=resource_group_name,
                       start=start,
                       stop=stop,
                       rate_in_mbps=rate_in_mbps,
                       days=days)


def databoxedge_bandwidth_schedule_update(client,
                                          device_name,
                                          name,
                                          resource_group_name,
                                          start,
                                          stop,
                                          rate_in_mbps,
                                          days,
                                          no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       device_name=device_name,
                       name=name,
                       resource_group_name=resource_group_name,
                       start=start,
                       stop=stop,
                       rate_in_mbps=rate_in_mbps,
                       days=days)


def databoxedge_bandwidth_schedule_delete(client,
                                          device_name,
                                          name,
                                          resource_group_name,
                                          no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       device_name=device_name,
                       name=name,
                       resource_group_name=resource_group_name)


def databoxedge_job_show(client,
                         device_name,
                         name,
                         resource_group_name):
    return client.get(device_name=device_name,
                      name=name,
                      resource_group_name=resource_group_name)


def databoxedge_node_list(client,
                          device_name,
                          resource_group_name):
    return client.list_by_data_box_edge_device(device_name=device_name,
                                               resource_group_name=resource_group_name)


def databoxedge_operation_status_show(client,
                                      device_name,
                                      name,
                                      resource_group_name):
    return client.get(device_name=device_name,
                      name=name,
                      resource_group_name=resource_group_name)


def databoxedge_order_list(client,
                           device_name,
                           resource_group_name):
    return client.list_by_data_box_edge_device(device_name=device_name,
                                               resource_group_name=resource_group_name)


def databoxedge_order_show(client,
                           device_name,
                           resource_group_name):
    return client.get(device_name=device_name,
                      resource_group_name=resource_group_name)


def databoxedge_order_create(client,
                             device_name,
                             resource_group_name,
                             contact_information=None,
                             shipping_address=None,
                             current_status_status=None,
                             current_status_comments=None,
                             no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       device_name=device_name,
                       resource_group_name=resource_group_name,
                       contact_information=contact_information,
                       shipping_address=shipping_address,
                       status=current_status_status,
                       comments=current_status_comments)


def databoxedge_order_update(client,
                             device_name,
                             resource_group_name,
                             contact_information=None,
                             shipping_address=None,
                             current_status_status=None,
                             current_status_comments=None,
                             no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       device_name=device_name,
                       resource_group_name=resource_group_name,
                       contact_information=contact_information,
                       shipping_address=shipping_address,
                       status=current_status_status,
                       comments=current_status_comments)


def databoxedge_order_delete(client,
                             device_name,
                             resource_group_name,
                             no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       device_name=device_name,
                       resource_group_name=resource_group_name)


def databoxedge_role_list(client,
                          device_name,
                          resource_group_name):
    return client.list_by_data_box_edge_device(device_name=device_name,
                                               resource_group_name=resource_group_name)


def databoxedge_role_show(client,
                          device_name,
                          name,
                          resource_group_name):
    return client.get(device_name=device_name,
                      name=name,
                      resource_group_name=resource_group_name)


def databoxedge_role_create(client,
                            device_name,
                            name,
                            resource_group_name,
                            role,
                            no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       device_name=device_name,
                       name=name,
                       resource_group_name=resource_group_name,
                       role=role)


def databoxedge_role_update(instance,
                            device_name,
                            name,
                            resource_group_name,
                            no_wait=False):
    return instance


def databoxedge_role_delete(client,
                            device_name,
                            name,
                            resource_group_name,
                            no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       device_name=device_name,
                       name=name,
                       resource_group_name=resource_group_name)


def databoxedge_share_list(client,
                           device_name,
                           resource_group_name):
    return client.list_by_data_box_edge_device(device_name=device_name,
                                               resource_group_name=resource_group_name)


def databoxedge_share_show(client,
                           device_name,
                           name,
                           resource_group_name):
    return client.get(device_name=device_name,
                      name=name,
                      resource_group_name=resource_group_name)


def databoxedge_share_create(client,
                             device_name,
                             name,
                             resource_group_name,
                             share_status,
                             monitoring_status,
                             access_protocol,
                             description=None,
                             azure_container_info=None,
                             user_access_rights=None,
                             client_access_rights=None,
                             refresh_details=None,
                             data_policy=None,
                             no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       device_name=device_name,
                       name=name,
                       resource_group_name=resource_group_name,
                       description=description,
                       share_status=share_status,
                       monitoring_status=monitoring_status,
                       azure_container_info=azure_container_info,
                       access_protocol=access_protocol,
                       user_access_rights=user_access_rights,
                       client_access_rights=client_access_rights,
                       refresh_details=refresh_details,
                       data_policy=data_policy)


def databoxedge_share_update(client,
                             device_name,
                             name,
                             resource_group_name,
                             share_status,
                             monitoring_status,
                             access_protocol,
                             description=None,
                             azure_container_info=None,
                             user_access_rights=None,
                             client_access_rights=None,
                             refresh_details=None,
                             data_policy=None,
                             no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       device_name=device_name,
                       name=name,
                       resource_group_name=resource_group_name,
                       description=description,
                       share_status=share_status,
                       monitoring_status=monitoring_status,
                       azure_container_info=azure_container_info,
                       access_protocol=access_protocol,
                       user_access_rights=user_access_rights,
                       client_access_rights=client_access_rights,
                       refresh_details=refresh_details,
                       data_policy=data_policy)


def databoxedge_share_delete(client,
                             device_name,
                             name,
                             resource_group_name,
                             no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       device_name=device_name,
                       name=name,
                       resource_group_name=resource_group_name)


def databoxedge_share_refresh(client,
                              device_name,
                              name,
                              resource_group_name,
                              no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_refresh,
                       device_name=device_name,
                       name=name,
                       resource_group_name=resource_group_name)


def databoxedge_storage_account_credentials_list(client,
                                                 device_name,
                                                 resource_group_name):
    return client.list_by_data_box_edge_device(device_name=device_name,
                                               resource_group_name=resource_group_name)


def databoxedge_storage_account_credentials_show(client,
                                                 device_name,
                                                 name,
                                                 resource_group_name):
    return client.get(device_name=device_name,
                      name=name,
                      resource_group_name=resource_group_name)


def databoxedge_storage_account_credentials_delete(client,
                                                   device_name,
                                                   name,
                                                   resource_group_name,
                                                   no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       device_name=device_name,
                       name=name,
                       resource_group_name=resource_group_name)


def databoxedge_storage_account_list(client,
                                     device_name,
                                     resource_group_name):
    return client.list_by_data_box_edge_device(device_name=device_name,
                                               resource_group_name=resource_group_name)


def databoxedge_storage_account_show(client,
                                     device_name,
                                     storage_account_name,
                                     resource_group_name):
    return client.get(device_name=device_name,
                      storage_account_name=storage_account_name,
                      resource_group_name=resource_group_name)


def databoxedge_storage_account_delete(client,
                                       device_name,
                                       storage_account_name,
                                       resource_group_name,
                                       no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       device_name=device_name,
                       storage_account_name=storage_account_name,
                       resource_group_name=resource_group_name)


def databoxedge_container_list(client,
                               device_name,
                               storage_account_name,
                               resource_group_name):
    return client.list_by_storage_account(device_name=device_name,
                                          storage_account_name=storage_account_name,
                                          resource_group_name=resource_group_name)


def databoxedge_container_show(client,
                               device_name,
                               storage_account_name,
                               container_name,
                               resource_group_name):
    return client.get(device_name=device_name,
                      storage_account_name=storage_account_name,
                      container_name=container_name,
                      resource_group_name=resource_group_name)


def databoxedge_container_create(client,
                                 device_name,
                                 storage_account_name,
                                 container_name,
                                 resource_group_name,
                                 data_format,
                                 no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       device_name=device_name,
                       storage_account_name=storage_account_name,
                       container_name=container_name,
                       resource_group_name=resource_group_name,
                       data_format=data_format)


def databoxedge_container_update(client,
                                 device_name,
                                 storage_account_name,
                                 container_name,
                                 resource_group_name,
                                 data_format,
                                 no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       device_name=device_name,
                       storage_account_name=storage_account_name,
                       container_name=container_name,
                       resource_group_name=resource_group_name,
                       data_format=data_format)


def databoxedge_container_delete(client,
                                 device_name,
                                 storage_account_name,
                                 container_name,
                                 resource_group_name,
                                 no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       device_name=device_name,
                       storage_account_name=storage_account_name,
                       container_name=container_name,
                       resource_group_name=resource_group_name)


def databoxedge_container_refresh(client,
                                  device_name,
                                  storage_account_name,
                                  container_name,
                                  resource_group_name,
                                  no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_refresh,
                       device_name=device_name,
                       storage_account_name=storage_account_name,
                       container_name=container_name,
                       resource_group_name=resource_group_name)


def databoxedge_trigger_list(client,
                             device_name,
                             resource_group_name,
                             filter_=None):
    return client.list_by_data_box_edge_device(device_name=device_name,
                                               resource_group_name=resource_group_name,
                                               filter=filter_)


def databoxedge_trigger_show(client,
                             device_name,
                             name,
                             resource_group_name):
    return client.get(device_name=device_name,
                      name=name,
                      resource_group_name=resource_group_name)


def databoxedge_trigger_create(client,
                               device_name,
                               name,
                               resource_group_name,
                               file_event_trigger=None,
                               periodic_timer_event_trigger=None,
                               no_wait=False):
    all_trigger = []
    if file_event_trigger is not None:
        all_trigger.append(file_event_trigger)
    if periodic_timer_event_trigger is not None:
        all_trigger.append(periodic_timer_event_trigger)
    if len(all_trigger) > 1:
        raise CLIError('at most one of  file_event_trigger, periodic_timer_event_trigger is needed for trigger!')
    if len(all_trigger) != 1:
        raise CLIError('trigger is required. but none of file_event_trigger, periodic_timer_event_trigger is provided!')
    trigger = all_trigger[0] if len(all_trigger) == 1 else None
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       device_name=device_name,
                       name=name,
                       resource_group_name=resource_group_name,
                       trigger=trigger)


def databoxedge_trigger_update(instance,
                               device_name,
                               name,
                               resource_group_name,
                               file_event_trigger=None,
                               periodic_timer_event_trigger=None,
                               no_wait=False):
    return instance


def databoxedge_trigger_delete(client,
                               device_name,
                               name,
                               resource_group_name,
                               no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       device_name=device_name,
                       name=name,
                       resource_group_name=resource_group_name)


def databoxedge_user_list(client,
                          device_name,
                          resource_group_name,
                          filter_=None):
    return client.list_by_data_box_edge_device(device_name=device_name,
                                               resource_group_name=resource_group_name,
                                               filter=filter_)


def databoxedge_user_show(client,
                          device_name,
                          name,
                          resource_group_name):
    return client.get(device_name=device_name,
                      name=name,
                      resource_group_name=resource_group_name)


def databoxedge_user_create(client,
                            device_name,
                            name,
                            resource_group_name,
                            user_type,
                            encrypted_password=None,
                            share_access_rights=None,
                            no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       device_name=device_name,
                       name=name,
                       resource_group_name=resource_group_name,
                       encrypted_password=encrypted_password,
                       share_access_rights=share_access_rights,
                       user_type=user_type)


def databoxedge_user_update(client,
                            device_name,
                            name,
                            resource_group_name,
                            user_type,
                            encrypted_password=None,
                            share_access_rights=None,
                            no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       device_name=device_name,
                       name=name,
                       resource_group_name=resource_group_name,
                       encrypted_password=encrypted_password,
                       share_access_rights=share_access_rights,
                       user_type=user_type)


def databoxedge_user_delete(client,
                            device_name,
                            name,
                            resource_group_name,
                            no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       device_name=device_name,
                       name=name,
                       resource_group_name=resource_group_name)


def databoxedge_sku_list(client,
                         filter_=None):
    return client.list(filter=filter_)
