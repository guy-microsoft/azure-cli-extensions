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

from knack.util import CLIError


def datashare_account_list(cmd, client,
                           resource_group_name=None,
                           skip_token=None):
    if resource_group_name is not None:
        return client.list_by_resource_group(resource_group_name=resource_group_name,
                                             skip_token=skip_token)
    return client.list_by_subscription(skip_token=skip_token)


def datashare_account_show(cmd, client,
                           resource_group_name,
                           account_name):
    return client.get(resource_group_name=resource_group_name,
                      account_name=account_name)


def datashare_account_create(cmd, client,
                             resource_group_name,
                             account_name,
                             identity,
                             location=None,
                             tags=None):
    return client.begin_create(resource_group_name=resource_group_name,
                               account_name=account_name,
                               location=location,
                               tags=tags,
                               identity=identity)


def datashare_account_update(cmd, client,
                             resource_group_name,
                             account_name,
                             tags=None):
    return client.update(resource_group_name=resource_group_name,
                         account_name=account_name,
                         tags=tags)


def datashare_account_delete(cmd, client,
                             resource_group_name,
                             account_name):
    return client.begin_delete(resource_group_name=resource_group_name,
                               account_name=account_name)


def datashare_consumer_invitation_show(cmd, client,
                                       location,
                                       invitation_id):
    return client.get(location=location,
                      invitation_id=invitation_id)


def datashare_consumer_invitation_list_invitation(cmd, client,
                                                  skip_token=None):
    return client.list_invitation(skip_token=skip_token)


def datashare_consumer_invitation_reject_invitation(cmd, client,
                                                    location,
                                                    invitation_id):
    return client.reject_invitation(location=location,
                                    invitation_id=invitation_id)


def datashare_data_set_list(cmd, client,
                            resource_group_name,
                            account_name,
                            share_name,
                            skip_token=None):
    return client.list_by_share(resource_group_name=resource_group_name,
                                account_name=account_name,
                                share_name=share_name,
                                skip_token=skip_token)


def datashare_data_set_show(cmd, client,
                            resource_group_name,
                            account_name,
                            share_name,
                            data_set_name):
    return client.get(resource_group_name=resource_group_name,
                      account_name=account_name,
                      share_name=share_name,
                      data_set_name=data_set_name)


def datashare_data_set_create(cmd, client,
                              resource_group_name,
                              account_name,
                              share_name,
                              data_set_name,
                              blob_data_set=None,
                              blob_folder_data_set=None,
                              blob_container_data_set=None,
                              adls_gen2_file_data_set=None,
                              adls_gen2_folder_data_set=None,
                              adls_gen2_file_system_data_set=None,
                              adls_gen1_folder_data_set=None,
                              adls_gen1_file_data_set=None,
                              kusto_cluster_data_set=None,
                              kusto_database_data_set=None,
                              sql_dw_table_data_set=None,
                              sql_d_b_table_data_set=None):
    all_data_set = []
    if blob_data_set is not None:
        all_data_set.append(blob_data_set)
    if blob_folder_data_set is not None:
        all_data_set.append(blob_folder_data_set)
    if blob_container_data_set is not None:
        all_data_set.append(blob_container_data_set)
    if adls_gen2_file_data_set is not None:
        all_data_set.append(adls_gen2_file_data_set)
    if adls_gen2_folder_data_set is not None:
        all_data_set.append(adls_gen2_folder_data_set)
    if adls_gen2_file_system_data_set is not None:
        all_data_set.append(adls_gen2_file_system_data_set)
    if adls_gen1_folder_data_set is not None:
        all_data_set.append(adls_gen1_folder_data_set)
    if adls_gen1_file_data_set is not None:
        all_data_set.append(adls_gen1_file_data_set)
    if kusto_cluster_data_set is not None:
        all_data_set.append(kusto_cluster_data_set)
    if kusto_database_data_set is not None:
        all_data_set.append(kusto_database_data_set)
    if sql_dw_table_data_set is not None:
        all_data_set.append(sql_dw_table_data_set)
    if sql_d_b_table_data_set is not None:
        all_data_set.append(sql_d_b_table_data_set)
    if len(all_data_set) > 1:
        raise CLIError('at most one of  blob_data_set, blob_folder_data_set, blob_container_data_set, adls_gen2_file_da'
                       'ta_set, adls_gen2_folder_data_set, adls_gen2_file_system_data_set, adls_gen1_folder_data_set, a'
                       'dls_gen1_file_data_set, kusto_cluster_data_set, kusto_database_data_set, sql_dw_table_data_set,'
                       ' sql_d_b_table_data_set is needed for data_set!')
    if len(all_data_set) != 1:
        raise CLIError('data_set is required. but none of blob_data_set, blob_folder_data_set, blob_container_data_set,'
                       ' adls_gen2_file_data_set, adls_gen2_folder_data_set, adls_gen2_file_system_data_set, adls_gen1_'
                       'folder_data_set, adls_gen1_file_data_set, kusto_cluster_data_set, kusto_database_data_set, sql_'
                       'dw_table_data_set, sql_d_b_table_data_set is provided!')
    data_set = all_data_set[0] if len(all_data_set) == 1 else None
    return client.create(resource_group_name=resource_group_name,
                         account_name=account_name,
                         share_name=share_name,
                         data_set_name=data_set_name,
                         data_set=data_set)


def datashare_data_set_delete(cmd, client,
                              resource_group_name,
                              account_name,
                              share_name,
                              data_set_name):
    return client.begin_delete(resource_group_name=resource_group_name,
                               account_name=account_name,
                               share_name=share_name,
                               data_set_name=data_set_name)


def datashare_data_set_mapping_list(cmd, client,
                                    resource_group_name,
                                    account_name,
                                    share_subscription_name,
                                    skip_token=None):
    return client.list_by_share_subscription(resource_group_name=resource_group_name,
                                             account_name=account_name,
                                             share_subscription_name=share_subscription_name,
                                             skip_token=skip_token)


def datashare_data_set_mapping_show(cmd, client,
                                    resource_group_name,
                                    account_name,
                                    share_subscription_name,
                                    data_set_mapping_name):
    return client.get(resource_group_name=resource_group_name,
                      account_name=account_name,
                      share_subscription_name=share_subscription_name,
                      data_set_mapping_name=data_set_mapping_name)


def datashare_data_set_mapping_create(cmd, client,
                                      resource_group_name,
                                      account_name,
                                      share_subscription_name,
                                      data_set_mapping_name,
                                      blob_data_set_mapping=None,
                                      blob_folder_data_set_mapping=None,
                                      blob_container_data_set_mapping=None,
                                      adls_gen2_file_data_set_mapping=None,
                                      adls_gen2_folder_data_set_mapping=None,
                                      adls_gen2_file_system_data_set_mapping=None,
                                      kusto_cluster_data_set_mapping=None,
                                      kusto_database_data_set_mapping=None,
                                      sql_dw_table_data_set_mapping=None,
                                      sql_d_b_table_data_set_mapping=None):
    all_data_set_mapping = []
    if blob_data_set_mapping is not None:
        all_data_set_mapping.append(blob_data_set_mapping)
    if blob_folder_data_set_mapping is not None:
        all_data_set_mapping.append(blob_folder_data_set_mapping)
    if blob_container_data_set_mapping is not None:
        all_data_set_mapping.append(blob_container_data_set_mapping)
    if adls_gen2_file_data_set_mapping is not None:
        all_data_set_mapping.append(adls_gen2_file_data_set_mapping)
    if adls_gen2_folder_data_set_mapping is not None:
        all_data_set_mapping.append(adls_gen2_folder_data_set_mapping)
    if adls_gen2_file_system_data_set_mapping is not None:
        all_data_set_mapping.append(adls_gen2_file_system_data_set_mapping)
    if kusto_cluster_data_set_mapping is not None:
        all_data_set_mapping.append(kusto_cluster_data_set_mapping)
    if kusto_database_data_set_mapping is not None:
        all_data_set_mapping.append(kusto_database_data_set_mapping)
    if sql_dw_table_data_set_mapping is not None:
        all_data_set_mapping.append(sql_dw_table_data_set_mapping)
    if sql_d_b_table_data_set_mapping is not None:
        all_data_set_mapping.append(sql_d_b_table_data_set_mapping)
    if len(all_data_set_mapping) > 1:
        raise CLIError('at most one of  blob_data_set_mapping, blob_folder_data_set_mapping, blob_container_data_set_ma'
                       'pping, adls_gen2_file_data_set_mapping, adls_gen2_folder_data_set_mapping, adls_gen2_file_syste'
                       'm_data_set_mapping, kusto_cluster_data_set_mapping, kusto_database_data_set_mapping, sql_dw_tab'
                       'le_data_set_mapping, sql_d_b_table_data_set_mapping is needed for data_set_mapping!')
    if len(all_data_set_mapping) != 1:
        raise CLIError('data_set_mapping is required. but none of blob_data_set_mapping, blob_folder_data_set_mapping, '
                       'blob_container_data_set_mapping, adls_gen2_file_data_set_mapping, adls_gen2_folder_data_set_map'
                       'ping, adls_gen2_file_system_data_set_mapping, kusto_cluster_data_set_mapping, kusto_database_da'
                       'ta_set_mapping, sql_dw_table_data_set_mapping, sql_d_b_table_data_set_mapping is provided!')
    data_set_mapping = all_data_set_mapping[0] if len(all_data_set_mapping) == 1 else None
    return client.create(resource_group_name=resource_group_name,
                         account_name=account_name,
                         share_subscription_name=share_subscription_name,
                         data_set_mapping_name=data_set_mapping_name,
                         data_set_mapping=data_set_mapping)


def datashare_data_set_mapping_delete(cmd, client,
                                      resource_group_name,
                                      account_name,
                                      share_subscription_name,
                                      data_set_mapping_name):
    return client.delete(resource_group_name=resource_group_name,
                         account_name=account_name,
                         share_subscription_name=share_subscription_name,
                         data_set_mapping_name=data_set_mapping_name)


def datashare_invitation_list(cmd, client,
                              resource_group_name,
                              account_name,
                              share_name,
                              skip_token=None):
    return client.list_by_share(resource_group_name=resource_group_name,
                                account_name=account_name,
                                share_name=share_name,
                                skip_token=skip_token)


def datashare_invitation_show(cmd, client,
                              resource_group_name,
                              account_name,
                              share_name,
                              invitation_name):
    return client.get(resource_group_name=resource_group_name,
                      account_name=account_name,
                      share_name=share_name,
                      invitation_name=invitation_name)


def datashare_invitation_create(cmd, client,
                                resource_group_name,
                                account_name,
                                share_name,
                                invitation_name,
                                target_active_directory_id=None,
                                target_email=None,
                                target_object_id=None):
    return client.create(resource_group_name=resource_group_name,
                         account_name=account_name,
                         share_name=share_name,
                         invitation_name=invitation_name,
                         target_active_directory_id=target_active_directory_id,
                         target_email=target_email,
                         target_object_id=target_object_id)


def datashare_invitation_delete(cmd, client,
                                resource_group_name,
                                account_name,
                                share_name,
                                invitation_name):
    return client.delete(resource_group_name=resource_group_name,
                         account_name=account_name,
                         share_name=share_name,
                         invitation_name=invitation_name)


def datashare_share_list(cmd, client,
                         resource_group_name,
                         account_name,
                         skip_token=None):
    return client.list_by_account(resource_group_name=resource_group_name,
                                  account_name=account_name,
                                  skip_token=skip_token)


def datashare_share_show(cmd, client,
                         resource_group_name,
                         account_name,
                         share_name):
    return client.get(resource_group_name=resource_group_name,
                      account_name=account_name,
                      share_name=share_name)


def datashare_share_create(cmd, client,
                           resource_group_name,
                           account_name,
                           share_name,
                           description=None,
                           share_kind=None,
                           terms=None):
    return client.create(resource_group_name=resource_group_name,
                         account_name=account_name,
                         share_name=share_name,
                         description=description,
                         share_kind=share_kind,
                         terms=terms)


def datashare_share_delete(cmd, client,
                           resource_group_name,
                           account_name,
                           share_name):
    return client.begin_delete(resource_group_name=resource_group_name,
                               account_name=account_name,
                               share_name=share_name)


def datashare_share_list_synchronization(cmd, client,
                                         resource_group_name,
                                         account_name,
                                         share_name,
                                         skip_token=None):
    return client.list_synchronization(resource_group_name=resource_group_name,
                                       account_name=account_name,
                                       share_name=share_name,
                                       skip_token=skip_token)


def datashare_share_list_synchronization_detail(cmd, client,
                                                resource_group_name,
                                                account_name,
                                                share_name,
                                                skip_token=None,
                                                consumer_email=None,
                                                consumer_name=None,
                                                consumer_tenant_name=None,
                                                duration_ms=None,
                                                end_time=None,
                                                message=None,
                                                start_time=None,
                                                status=None,
                                                synchronization_id=None):
    return client.list_synchronization_detail(resource_group_name=resource_group_name,
                                              account_name=account_name,
                                              share_name=share_name,
                                              skip_token=skip_token,
                                              consumer_email=consumer_email,
                                              consumer_name=consumer_name,
                                              consumer_tenant_name=consumer_tenant_name,
                                              duration_ms=duration_ms,
                                              end_time=end_time,
                                              message=message,
                                              start_time=start_time,
                                              status=status,
                                              synchronization_id=synchronization_id)


def datashare_provider_share_subscription_list(cmd, client,
                                               resource_group_name,
                                               account_name,
                                               share_name,
                                               skip_token=None):
    return client.list_by_share(resource_group_name=resource_group_name,
                                account_name=account_name,
                                share_name=share_name,
                                skip_token=skip_token)


def datashare_provider_share_subscription_show(cmd, client,
                                               resource_group_name,
                                               account_name,
                                               share_name,
                                               provider_share_subscription_id):
    return client.get_by_share(resource_group_name=resource_group_name,
                               account_name=account_name,
                               share_name=share_name,
                               provider_share_subscription_id=provider_share_subscription_id)


def datashare_provider_share_subscription_reinstate(cmd, client,
                                                    resource_group_name,
                                                    account_name,
                                                    share_name,
                                                    provider_share_subscription_id):
    return client.reinstate(resource_group_name=resource_group_name,
                            account_name=account_name,
                            share_name=share_name,
                            provider_share_subscription_id=provider_share_subscription_id)


def datashare_provider_share_subscription_revoke(cmd, client,
                                                 resource_group_name,
                                                 account_name,
                                                 share_name,
                                                 provider_share_subscription_id):
    return client.begin_revoke(resource_group_name=resource_group_name,
                               account_name=account_name,
                               share_name=share_name,
                               provider_share_subscription_id=provider_share_subscription_id)


def datashare_share_subscription_list(cmd, client,
                                      resource_group_name,
                                      account_name,
                                      skip_token=None):
    return client.list_by_account(resource_group_name=resource_group_name,
                                  account_name=account_name,
                                  skip_token=skip_token)


def datashare_share_subscription_show(cmd, client,
                                      resource_group_name,
                                      account_name,
                                      share_subscription_name):
    return client.get(resource_group_name=resource_group_name,
                      account_name=account_name,
                      share_subscription_name=share_subscription_name)


def datashare_share_subscription_create(cmd, client,
                                        resource_group_name,
                                        account_name,
                                        share_subscription_name,
                                        invitation_id,
                                        source_share_location):
    return client.create(resource_group_name=resource_group_name,
                         account_name=account_name,
                         share_subscription_name=share_subscription_name,
                         invitation_id=invitation_id,
                         source_share_location=source_share_location)


def datashare_share_subscription_delete(cmd, client,
                                        resource_group_name,
                                        account_name,
                                        share_subscription_name):
    return client.begin_delete(resource_group_name=resource_group_name,
                               account_name=account_name,
                               share_subscription_name=share_subscription_name)


def datashare_share_subscription_cancel_synchronization(cmd, client,
                                                        resource_group_name,
                                                        account_name,
                                                        share_subscription_name,
                                                        synchronization_id):
    return client.begin_cancel_synchronization(resource_group_name=resource_group_name,
                                               account_name=account_name,
                                               share_subscription_name=share_subscription_name,
                                               synchronization_id=synchronization_id)


def datashare_share_subscription_list_source_share_synchronization_setting(cmd, client,
                                                                           resource_group_name,
                                                                           account_name,
                                                                           share_subscription_name,
                                                                           skip_token=None):
    return client.list_source_share_synchronization_setting(resource_group_name=resource_group_name,
                                                            account_name=account_name,
                                                            share_subscription_name=share_subscription_name,
                                                            skip_token=skip_token)


def datashare_share_subscription_list_synchronization(cmd, client,
                                                      resource_group_name,
                                                      account_name,
                                                      share_subscription_name,
                                                      skip_token=None):
    return client.list_synchronization(resource_group_name=resource_group_name,
                                       account_name=account_name,
                                       share_subscription_name=share_subscription_name,
                                       skip_token=skip_token)


def datashare_share_subscription_list_synchronization_detail(cmd, client,
                                                             resource_group_name,
                                                             account_name,
                                                             share_subscription_name,
                                                             synchronization_id,
                                                             skip_token=None):
    return client.list_synchronization_detail(resource_group_name=resource_group_name,
                                              account_name=account_name,
                                              share_subscription_name=share_subscription_name,
                                              skip_token=skip_token,
                                              synchronization_id=synchronization_id)


def datashare_share_subscription_synchronize(cmd, client,
                                             resource_group_name,
                                             account_name,
                                             share_subscription_name,
                                             synchronization_mode=None):
    return client.begin_synchronize(resource_group_name=resource_group_name,
                                    account_name=account_name,
                                    share_subscription_name=share_subscription_name,
                                    synchronization_mode=synchronization_mode)


def datashare_consumer_source_data_set_list(cmd, client,
                                            resource_group_name,
                                            account_name,
                                            share_subscription_name,
                                            skip_token=None):
    return client.list_by_share_subscription(resource_group_name=resource_group_name,
                                             account_name=account_name,
                                             share_subscription_name=share_subscription_name,
                                             skip_token=skip_token)


def datashare_synchronization_setting_list(cmd, client,
                                           resource_group_name,
                                           account_name,
                                           share_name,
                                           skip_token=None):
    return client.list_by_share(resource_group_name=resource_group_name,
                                account_name=account_name,
                                share_name=share_name,
                                skip_token=skip_token)


def datashare_synchronization_setting_show(cmd, client,
                                           resource_group_name,
                                           account_name,
                                           share_name,
                                           synchronization_setting_name):
    return client.get(resource_group_name=resource_group_name,
                      account_name=account_name,
                      share_name=share_name,
                      synchronization_setting_name=synchronization_setting_name)


def datashare_synchronization_setting_create(cmd, client,
                                             resource_group_name,
                                             account_name,
                                             share_name,
                                             synchronization_setting_name,
                                             scheduled_synchronization_setting=None):
    all_synchronization_setting = []
    if scheduled_synchronization_setting is not None:
        all_synchronization_setting.append(scheduled_synchronization_setting)
    if len(all_synchronization_setting) > 1:
        raise CLIError('at most one of  scheduled_synchronization_setting is needed for synchronization_setting!')
    if len(all_synchronization_setting) != 1:
        raise CLIError('synchronization_setting is required. but none of scheduled_synchronization_setting is provided!'
                       '')
    synchronization_setting = all_synchronization_setting[0] if len(all_synchronization_setting) == 1 else None
    return client.create(resource_group_name=resource_group_name,
                         account_name=account_name,
                         share_name=share_name,
                         synchronization_setting_name=synchronization_setting_name,
                         synchronization_setting=synchronization_setting)


def datashare_synchronization_setting_delete(cmd, client,
                                             resource_group_name,
                                             account_name,
                                             share_name,
                                             synchronization_setting_name):
    return client.begin_delete(resource_group_name=resource_group_name,
                               account_name=account_name,
                               share_name=share_name,
                               synchronization_setting_name=synchronization_setting_name)


def datashare_trigger_list(cmd, client,
                           resource_group_name,
                           account_name,
                           share_subscription_name,
                           skip_token=None):
    return client.list_by_share_subscription(resource_group_name=resource_group_name,
                                             account_name=account_name,
                                             share_subscription_name=share_subscription_name,
                                             skip_token=skip_token)


def datashare_trigger_show(cmd, client,
                           resource_group_name,
                           account_name,
                           share_subscription_name,
                           trigger_name):
    return client.get(resource_group_name=resource_group_name,
                      account_name=account_name,
                      share_subscription_name=share_subscription_name,
                      trigger_name=trigger_name)


def datashare_trigger_create(cmd, client,
                             resource_group_name,
                             account_name,
                             share_subscription_name,
                             trigger_name,
                             scheduled_trigger=None):
    all_trigger = []
    if scheduled_trigger is not None:
        all_trigger.append(scheduled_trigger)
    if len(all_trigger) > 1:
        raise CLIError('at most one of  scheduled_trigger is needed for trigger!')
    if len(all_trigger) != 1:
        raise CLIError('trigger is required. but none of scheduled_trigger is provided!')
    trigger = all_trigger[0] if len(all_trigger) == 1 else None
    return client.begin_create(resource_group_name=resource_group_name,
                               account_name=account_name,
                               share_subscription_name=share_subscription_name,
                               trigger_name=trigger_name,
                               trigger=trigger)


def datashare_trigger_delete(cmd, client,
                             resource_group_name,
                             account_name,
                             share_subscription_name,
                             trigger_name):
    return client.begin_delete(resource_group_name=resource_group_name,
                               account_name=account_name,
                               share_subscription_name=share_subscription_name,
                               trigger_name=trigger_name)
