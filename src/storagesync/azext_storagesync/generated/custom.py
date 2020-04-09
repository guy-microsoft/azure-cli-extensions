# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines

import json


def storagesync_storage_sync_service_list(cmd, client,
                                          resource_group_name=None):
    if resource_group_name is not None:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list_by_subscription()


def storagesync_storage_sync_service_show(cmd, client,
                                          resource_group_name,
                                          storage_sync_service_name):
    return client.get(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name)


def storagesync_storage_sync_service_create(cmd, client,
                                            resource_group_name,
                                            storage_sync_service_name,
                                            location,
                                            tags=None,
                                            properties=None):
    return client.create(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, location=location, tags=tags, properties=properties)


def storagesync_storage_sync_service_update(cmd, client,
                                            resource_group_name,
                                            storage_sync_service_name,
                                            tags=None):
    return client.update(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, tags=tags)


def storagesync_storage_sync_service_delete(cmd, client,
                                            resource_group_name,
                                            storage_sync_service_name):
    return client.delete(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name)


def storagesync_sync_group_list(cmd, client,
                                resource_group_name,
                                storage_sync_service_name):
    return client.list_by_storage_sync_service(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name)


def storagesync_sync_group_show(cmd, client,
                                resource_group_name,
                                storage_sync_service_name,
                                sync_group_name):
    return client.get(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, sync_group_name=sync_group_name)


def storagesync_sync_group_create(cmd, client,
                                  resource_group_name,
                                  storage_sync_service_name,
                                  sync_group_name):
    return client.create(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, sync_group_name=sync_group_name)


def storagesync_sync_group_delete(cmd, client,
                                  resource_group_name,
                                  storage_sync_service_name,
                                  sync_group_name):
    return client.delete(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, sync_group_name=sync_group_name)


def storagesync_cloud_endpoint_list(cmd, client,
                                    resource_group_name,
                                    storage_sync_service_name,
                                    sync_group_name):
    return client.list_by_sync_group(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, sync_group_name=sync_group_name)


def storagesync_cloud_endpoint_show(cmd, client,
                                    resource_group_name,
                                    storage_sync_service_name,
                                    sync_group_name,
                                    cloud_endpoint_name):
    return client.get(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, sync_group_name=sync_group_name, cloud_endpoint_name=cloud_endpoint_name)


def storagesync_cloud_endpoint_create(cmd, client,
                                      resource_group_name,
                                      storage_sync_service_name,
                                      sync_group_name,
                                      cloud_endpoint_name,
                                      properties_storage_account_resource_id=None,
                                      properties_azure_file_share_name=None,
                                      properties_storage_account_tenant_id=None,
                                      properties_friendly_name=None):
    return client.begin_create(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, sync_group_name=sync_group_name, cloud_endpoint_name=cloud_endpoint_name, storage_account_resource_id=properties_storage_account_resource_id, azure_file_share_name=properties_azure_file_share_name, storage_account_tenant_id=properties_storage_account_tenant_id, friendly_name=properties_friendly_name)


def storagesync_cloud_endpoint_delete(cmd, client,
                                      resource_group_name,
                                      storage_sync_service_name,
                                      sync_group_name,
                                      cloud_endpoint_name):
    return client.begin_delete(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, sync_group_name=sync_group_name, cloud_endpoint_name=cloud_endpoint_name)


def storagesync_cloud_endpoint_pre_restore(cmd, client,
                                           resource_group_name,
                                           storage_sync_service_name,
                                           sync_group_name,
                                           cloud_endpoint_name,
                                           partition=None,
                                           replica_group=None,
                                           request_id=None,
                                           azure_file_share_uri=None,
                                           status=None,
                                           source_azure_file_share_uri=None,
                                           backup_metadata_property_bag=None,
                                           restore_file_spec=None,
                                           pause_wait_for_sync_drain_time_period_in_seconds=None):
    return client.begin_pre_restore(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, sync_group_name=sync_group_name, cloud_endpoint_name=cloud_endpoint_name, partition=partition, replica_group=replica_group, request_id=request_id, azure_file_share_uri=azure_file_share_uri, status=status, source_azure_file_share_uri=source_azure_file_share_uri, backup_metadata_property_bag=backup_metadata_property_bag, restore_file_spec=restore_file_spec, pause_wait_for_sync_drain_time_period_in_seconds=pause_wait_for_sync_drain_time_period_in_seconds)


def storagesync_cloud_endpoint_post_restore(cmd, client,
                                            resource_group_name,
                                            storage_sync_service_name,
                                            sync_group_name,
                                            cloud_endpoint_name,
                                            partition=None,
                                            replica_group=None,
                                            request_id=None,
                                            azure_file_share_uri=None,
                                            status=None,
                                            source_azure_file_share_uri=None,
                                            failed_file_list=None,
                                            restore_file_spec=None):
    return client.begin_post_restore(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, sync_group_name=sync_group_name, cloud_endpoint_name=cloud_endpoint_name, partition=partition, replica_group=replica_group, request_id=request_id, azure_file_share_uri=azure_file_share_uri, status=status, source_azure_file_share_uri=source_azure_file_share_uri, failed_file_list=failed_file_list, restore_file_spec=restore_file_spec)


def storagesync_cloud_endpoint_trigger_change_detection(cmd, client,
                                                        resource_group_name,
                                                        storage_sync_service_name,
                                                        sync_group_name,
                                                        cloud_endpoint_name,
                                                        directory_path=None,
                                                        change_detection_mode=None,
                                                        paths=None):
    paths = json.loads(paths) if isinstance(paths, str) else paths
    return client.begin_trigger_change_detection(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, sync_group_name=sync_group_name, cloud_endpoint_name=cloud_endpoint_name, directory_path=directory_path, change_detection_mode=change_detection_mode, paths=paths)


def storagesync_cloud_endpoint_pre_backup(cmd, client,
                                          resource_group_name,
                                          storage_sync_service_name,
                                          sync_group_name,
                                          cloud_endpoint_name,
                                          azure_file_share=None):
    return client.begin_pre_backup(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, sync_group_name=sync_group_name, cloud_endpoint_name=cloud_endpoint_name, azure_file_share=azure_file_share)


def storagesync_cloud_endpoint_post_backup(cmd, client,
                                           resource_group_name,
                                           storage_sync_service_name,
                                           sync_group_name,
                                           cloud_endpoint_name,
                                           azure_file_share=None):
    return client.begin_post_backup(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, sync_group_name=sync_group_name, cloud_endpoint_name=cloud_endpoint_name, azure_file_share=azure_file_share)


def storagesync_cloud_endpoint_restoreheartbeat(cmd, client,
                                                resource_group_name,
                                                storage_sync_service_name,
                                                sync_group_name,
                                                cloud_endpoint_name):
    return client.restoreheartbeat(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, sync_group_name=sync_group_name, cloud_endpoint_name=cloud_endpoint_name)


def storagesync_server_endpoint_list(cmd, client,
                                     resource_group_name,
                                     storage_sync_service_name,
                                     sync_group_name):
    return client.list_by_sync_group(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, sync_group_name=sync_group_name)


def storagesync_server_endpoint_show(cmd, client,
                                     resource_group_name,
                                     storage_sync_service_name,
                                     sync_group_name,
                                     server_endpoint_name):
    return client.get(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, sync_group_name=sync_group_name, server_endpoint_name=server_endpoint_name)


def storagesync_server_endpoint_create(cmd, client,
                                       resource_group_name,
                                       storage_sync_service_name,
                                       sync_group_name,
                                       server_endpoint_name,
                                       properties_server_local_path=None,
                                       properties_cloud_tiering=None,
                                       properties_volume_free_space_percent=None,
                                       properties_tier_files_older_than_days=None,
                                       properties_friendly_name=None,
                                       properties_server_resource_id=None,
                                       properties_offline_data_transfer=None,
                                       properties_offline_data_transfer_share_name=None):
    return client.begin_create(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, sync_group_name=sync_group_name, server_endpoint_name=server_endpoint_name, server_local_path=properties_server_local_path, cloud_tiering=properties_cloud_tiering, volume_free_space_percent=properties_volume_free_space_percent, tier_files_older_than_days=properties_tier_files_older_than_days, friendly_name=properties_friendly_name, server_resource_id=properties_server_resource_id, offline_data_transfer=properties_offline_data_transfer, offline_data_transfer_share_name=properties_offline_data_transfer_share_name)


def storagesync_server_endpoint_update(cmd, client,
                                       resource_group_name,
                                       storage_sync_service_name,
                                       sync_group_name,
                                       server_endpoint_name,
                                       properties_cloud_tiering=None,
                                       properties_volume_free_space_percent=None,
                                       properties_tier_files_older_than_days=None,
                                       properties_offline_data_transfer=None,
                                       properties_offline_data_transfer_share_name=None):
    return client.begin_update(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, sync_group_name=sync_group_name, server_endpoint_name=server_endpoint_name, cloud_tiering=properties_cloud_tiering, volume_free_space_percent=properties_volume_free_space_percent, tier_files_older_than_days=properties_tier_files_older_than_days, offline_data_transfer=properties_offline_data_transfer, offline_data_transfer_share_name=properties_offline_data_transfer_share_name)


def storagesync_server_endpoint_delete(cmd, client,
                                       resource_group_name,
                                       storage_sync_service_name,
                                       sync_group_name,
                                       server_endpoint_name):
    return client.begin_delete(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, sync_group_name=sync_group_name, server_endpoint_name=server_endpoint_name)


def storagesync_server_endpoint_recall_action(cmd, client,
                                              resource_group_name,
                                              storage_sync_service_name,
                                              sync_group_name,
                                              server_endpoint_name,
                                              pattern=None,
                                              recall_path=None):
    return client.begin_recall_action(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, sync_group_name=sync_group_name, server_endpoint_name=server_endpoint_name, pattern=pattern, recall_path=recall_path)


def storagesync_registered_server_list(cmd, client,
                                       resource_group_name,
                                       storage_sync_service_name):
    return client.list_by_storage_sync_service(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name)


def storagesync_registered_server_show(cmd, client,
                                       resource_group_name,
                                       storage_sync_service_name,
                                       server_id):
    return client.get(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, server_id=server_id)


def storagesync_registered_server_create(cmd, client,
                                         resource_group_name,
                                         storage_sync_service_name,
                                         server_id=None,
                                         properties_server_certificate=None,
                                         properties_agent_version=None,
                                         properties_server_osversion=None,
                                         properties_last_heart_beat=None,
                                         properties_server_role=None,
                                         properties_cluster_id=None,
                                         properties_cluster_name=None,
                                         properties_server_id=None,
                                         properties_friendly_name=None):
    return client.begin_create(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, server_id=server_id, server_certificate=properties_server_certificate, agent_version=properties_agent_version, server_os_version=properties_server_osversion, last_heart_beat=properties_last_heart_beat, server_role=properties_server_role, cluster_id=properties_cluster_id, cluster_name=properties_cluster_name, server_id=properties_server_id, friendly_name=properties_friendly_name)


def storagesync_registered_server_delete(cmd, client,
                                         resource_group_name,
                                         storage_sync_service_name,
                                         server_id):
    return client.begin_delete(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, server_id=server_id)


def storagesync_registered_server_trigger_rollover(cmd, client,
                                                   resource_group_name,
                                                   storage_sync_service_name,
                                                   server_id,
                                                   server_certificate=None):
    return client.begin_trigger_rollover(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, server_id=server_id, server_certificate=server_certificate)


def storagesync_workflow_list(cmd, client,
                              resource_group_name,
                              storage_sync_service_name):
    return client.list_by_storage_sync_service(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name)


def storagesync_workflow_show(cmd, client,
                              resource_group_name,
                              storage_sync_service_name,
                              workflow_id):
    return client.get(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, workflow_id=workflow_id)


def storagesync_workflow_abort(cmd, client,
                               resource_group_name,
                               storage_sync_service_name,
                               workflow_id):
    return client.abort(resource_group_name=resource_group_name, storage_sync_service_name=storage_sync_service_name, workflow_id=workflow_id)


def storagesync_operation_status_show(cmd, client,
                                      resource_group_name,
                                      location_name,
                                      workflow_id,
                                      operation_id):
    return client.get(resource_group_name=resource_group_name, location_name=location_name, workflow_id=workflow_id, operation_id=operation_id)
