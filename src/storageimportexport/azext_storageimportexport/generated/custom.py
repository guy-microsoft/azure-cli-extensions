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


def storageimportexport_location_list(client):
    return client.list()


def storageimportexport_location_show(client,
                                      location_name):
    return client.get(location_name=location_name)


def storageimportexport_job_list(client,
                                 top=None,
                                 filter=None,
                                 resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(top=top,
                                             filter=filter,
                                             resource_group_name=resource_group_name)
    return client.list_by_subscription(top=top,
                                       filter=filter)


def storageimportexport_job_show(client,
                                 job_name,
                                 resource_group_name):
    return client.get(job_name=job_name,
                      resource_group_name=resource_group_name)


def storageimportexport_job_create(client,
                                   job_name,
                                   resource_group_name,
                                   client_tenant_id=None,
                                   location=None,
                                   tags=None,
                                   storage_account_id=None,
                                   job_type=None,
                                   return_address=None,
                                   return_shipping=None,
                                   shipping_information=None,
                                   delivery_package=None,
                                   return_package=None,
                                   diagnostics_path=None,
                                   log_level=None,
                                   backup_drive_manifest=None,
                                   state=None,
                                   cancel_requested=None,
                                   percent_complete=None,
                                   incomplete_blob_list_uri=None,
                                   drive_list=None,
                                   provisioning_state=None,
                                   export_blob_listblob_path=None,
                                   export_blob_list_blob_path=None,
                                   export_blob_list_blob_path_prefix=None):
    if isinstance(tags, str):
        tags = json.loads(tags)
    return client.create(job_name=job_name,
                         resource_group_name=resource_group_name,
                         client_tenant_id=client_tenant_id,
                         location=location,
                         tags=tags,
                         storage_account_id=storage_account_id,
                         job_type=job_type,
                         return_address=return_address,
                         return_shipping=return_shipping,
                         shipping_information=shipping_information,
                         delivery_package=delivery_package,
                         return_package=return_package,
                         diagnostics_path=diagnostics_path,
                         log_level=log_level,
                         backup_drive_manifest=backup_drive_manifest,
                         state=state,
                         cancel_requested=cancel_requested,
                         percent_complete=percent_complete,
                         incomplete_blob_list_uri=incomplete_blob_list_uri,
                         drive_list=drive_list,
                         provisioning_state=provisioning_state,
                         blob_listblob_path=export_blob_listblob_path,
                         blob_path=export_blob_list_blob_path,
                         blob_path_prefix=export_blob_list_blob_path_prefix)


def storageimportexport_job_update(client,
                                   job_name,
                                   resource_group_name,
                                   tags=None,
                                   cancel_requested=None,
                                   state=None,
                                   return_address=None,
                                   return_shipping=None,
                                   delivery_package=None,
                                   log_level=None,
                                   backup_drive_manifest=None,
                                   drive_list=None):
    if isinstance(tags, str):
        tags = json.loads(tags)
    return client.update(job_name=job_name,
                         resource_group_name=resource_group_name,
                         tags=tags,
                         cancel_requested=cancel_requested,
                         state=state,
                         return_address=return_address,
                         return_shipping=return_shipping,
                         delivery_package=delivery_package,
                         log_level=log_level,
                         backup_drive_manifest=backup_drive_manifest,
                         drive_list=drive_list)


def storageimportexport_job_delete(client,
                                   job_name,
                                   resource_group_name):
    return client.delete(job_name=job_name,
                         resource_group_name=resource_group_name)


def storageimportexport_bit_locker_key_list(client,
                                            job_name,
                                            resource_group_name):
    return client.list(job_name=job_name,
                       resource_group_name=resource_group_name)
