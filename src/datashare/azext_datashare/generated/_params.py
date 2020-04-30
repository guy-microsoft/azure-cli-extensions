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
# pylint: disable=too-many-statements

from knack.arguments import CLIArgumentType
from azure.cli.core.commands.parameters import (
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azext_datashare.action import (
    AddIdentity,
    AddBlobDataSet,
    AddBlobFolderDataSet,
    AddBlobContainerDataSet,
    AddAdlsGen2FileDataSet,
    AddAdlsGen2FolderDataSet,
    AddAdlsGen2FileSystemDataSet,
    AddAdlsGen1FolderDataSet,
    AddAdlsGen1FileDataSet,
    AddKustoClusterDataSet,
    AddKustoDatabaseDataSet,
    AddSqlDwTableDataSet,
    AddSqlDBTableDataSet,
    AddStorageAccountDataSet,
    AddBlobDataSetMapping,
    AddBlobFolderDataSetMapping,
    AddBlobContainerDataSetMapping,
    AddAdlsGen2FileDataSetMapping,
    AddAdlsGen2FolderDataSetMapping,
    AddAdlsGen2FileSystemDataSetMapping,
    AddKustoClusterDataSetMapping,
    AddKustoDatabaseDataSetMapping,
    AddSqlDwTableDataSetMapping,
    AddSqlDBTableDataSetMapping,
    AddStorageAccountDataSetMapping,
    AddScheduledSynchronizationSetting,
    AddScheduledTrigger
)


def load_arguments(self, _):

    with self.argument_context('datashare account list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('skip_token', help='Continuation token')

    with self.argument_context('datashare account show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')

    with self.argument_context('datashare account create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)
        c.argument('identity', action=AddIdentity, nargs='+', help='Identity Info on the Account Expect value: KEY1=VAL'
                   'UE1 KEY2=VALUE2 ...')

    with self.argument_context('datashare account update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('tags', tags_type)

    with self.argument_context('datashare account delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')

    with self.argument_context('datashare consumer-invitation show') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('invitation_id', help='An invitation id')

    with self.argument_context('datashare consumer-invitation list-invitation') as c:
        c.argument('skip_token', help='The continuation token')

    with self.argument_context('datashare consumer-invitation reject-invitation') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('invitation_id', help='Unique id of the invitation.')

    with self.argument_context('datashare data-set list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share.')
        c.argument('skip_token', help='continuation token')

    with self.argument_context('datashare data-set show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share.')
        c.argument('data_set_name', help='The name of the dataSet.')

    with self.argument_context('datashare data-set create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share to add the data set to.')
        c.argument('data_set_name', help='The name of the dataSet.')
        c.argument('blob_data_set', action=AddBlobDataSet, nargs='+', help='An Azure storage blob data set. Expect valu'
                   'e: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: container-name, file-path, resource-group, sto'
                   'rage-account-name, subscription-id.', arg_group='DataSet')
        c.argument('blob_folder_data_set', action=AddBlobFolderDataSet, nargs='+', help='An Azure storage blob folder d'
                   'ata set. Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: container-name, prefix, re'
                   'source-group, storage-account-name, subscription-id.', arg_group='DataSet')
        c.argument('blob_container_data_set', action=AddBlobContainerDataSet, nargs='+', help='An Azure storage blob co'
                   'ntainer data set. Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: container-name, r'
                   'esource-group, storage-account-name, subscription-id.', arg_group='DataSet')
        c.argument('adls_gen2_file_data_set', action=AddAdlsGen2FileDataSet, nargs='+', help='An ADLS Gen 2 file data s'
                   'et. Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: file-path, file-system, resourc'
                   'e-group, storage-account-name, subscription-id.', arg_group='DataSet')
        c.argument('adls_gen2_folder_data_set', action=AddAdlsGen2FolderDataSet, nargs='+', help='An ADLS Gen 2 folder '
                   'data set. Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: file-system, folder-path,'
                   ' resource-group, storage-account-name, subscription-id.', arg_group='DataSet')
        c.argument('adls_gen2_file_system_data_set', action=AddAdlsGen2FileSystemDataSet, nargs='+', help='An ADLS Gen '
                   '2 file system data set. Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: file-system'
                   ', resource-group, storage-account-name, subscription-id.', arg_group='DataSet')
        c.argument('adls_gen1_folder_data_set', action=AddAdlsGen1FolderDataSet, nargs='+', help='An ADLS Gen 1 folder '
                   'data set. Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: account-name, folder-path'
                   ', resource-group, subscription-id.', arg_group='DataSet')
        c.argument('adls_gen1_file_data_set', action=AddAdlsGen1FileDataSet, nargs='+', help='An ADLS Gen 1 file data s'
                   'et. Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: account-name, file-name, folder'
                   '-path, resource-group, subscription-id.', arg_group='DataSet')
        c.argument('kusto_cluster_data_set', action=AddKustoClusterDataSet, nargs='+', help='A kusto cluster data set. '
                   'Expect value: kusto-cluster-resource-id=xx.', arg_group='DataSet')
        c.argument('kusto_database_data_set', action=AddKustoDatabaseDataSet, nargs='+', help='A kusto database data se'
                   't. Expect value: kusto-database-resource-id=xx.', arg_group='DataSet')
        c.argument('sql_dw_table_data_set', action=AddSqlDwTableDataSet, nargs='+', help='A SQL DW table data set. Expe'
                   'ct value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: data-warehouse-name, schema-name, sql-s'
                   'erver-resource-id, table-name.', arg_group='DataSet')
        c.argument('sql_d_b_table_data_set', action=AddSqlDBTableDataSet, nargs='+', help='A SQL DB table data set. Exp'
                   'ect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: database-name, schema-name, sql-server'
                   '-resource-id, table-name.', arg_group='DataSet')
        c.argument('storage_account_data_set', action=AddStorageAccountDataSet, nargs='+', help='An Azure storage accou'
                   'nt data set. Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: paths, storage-account'
                   '-resource-id.', arg_group='DataSet')

    with self.argument_context('datashare data-set delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share.')
        c.argument('data_set_name', help='The name of the dataSet.')

    with self.argument_context('datashare data-set-mapping list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', help='The name of the share subscription.')
        c.argument('skip_token', help='Continuation token')

    with self.argument_context('datashare data-set-mapping show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', help='The name of the shareSubscription.')
        c.argument('data_set_mapping_name', help='The name of the dataSetMapping.')

    with self.argument_context('datashare data-set-mapping create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', help='The name of the share subscription which will hold the data set sin'
                   'k.')
        c.argument('data_set_mapping_name', help='The name of the data set mapping to be created.')
        c.argument('blob_data_set_mapping', action=AddBlobDataSetMapping, nargs='+', help='A Blob data set mapping. Exp'
                   'ect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: container-name, data-set-id, file-path'
                   ', output-type, resource-group, storage-account-name, subscription-id.',
                   arg_group='DataSetMapping')
        c.argument('blob_folder_data_set_mapping', action=AddBlobFolderDataSetMapping, nargs='+', help='A Blob folder d'
                   'ata set mapping. Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: container-name, da'
                   'ta-set-id, prefix, resource-group, storage-account-name, subscription-id.', arg_group='DataSetMappi'
                   'ng')
        c.argument('blob_container_data_set_mapping', action=AddBlobContainerDataSetMapping, nargs='+', help='A Blob co'
                   'ntainer data set mapping. Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: container'
                   '-name, data-set-id, resource-group, storage-account-name, subscription-id.', arg_group='DataSetMapp'
                   'ing')
        c.argument('adls_gen2_file_data_set_mapping', action=AddAdlsGen2FileDataSetMapping, nargs='+', help='An ADLS Ge'
                   'n2 file data set mapping. Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: data-set-'
                   'id, file-path, file-system, output-type, resource-group, storage-account-name, subscription-id.',
                   arg_group='DataSetMapping')
        c.argument('adls_gen2_folder_data_set_mapping', action=AddAdlsGen2FolderDataSetMapping, nargs='+', help='An ADL'
                   'S Gen2 folder data set mapping. Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: dat'
                   'a-set-id, file-system, folder-path, resource-group, storage-account-name, subscription-id.',
                   arg_group='DataSetMapping')
        c.argument('adls_gen2_file_system_data_set_mapping', action=AddAdlsGen2FileSystemDataSetMapping, nargs='+',
                   help='An ADLS Gen2 file system data set mapping. Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , availab'
                   'le KEYs are: data-set-id, file-system, resource-group, storage-account-name, subscription-id.',
                   arg_group='DataSetMapping')
        c.argument('kusto_cluster_data_set_mapping', action=AddKustoClusterDataSetMapping, nargs='+', help='A Kusto clu'
                   'ster data set mapping Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: data-set-id, '
                   'kusto-cluster-resource-id.', arg_group='DataSetMapping')
        c.argument('kusto_database_data_set_mapping', action=AddKustoDatabaseDataSetMapping, nargs='+', help='A Kusto d'
                   'atabase data set mapping Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: data-set-i'
                   'd, kusto-cluster-resource-id.', arg_group='DataSetMapping')
        c.argument('sql_dw_table_data_set_mapping', action=AddSqlDwTableDataSetMapping, nargs='+', help='A SQL DW Table'
                   ' data set mapping. Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: data-set-id, dat'
                   'a-warehouse-name, schema-name, sql-server-resource-id, table-name.', arg_group='DataSetMapping')
        c.argument('sql_d_b_table_data_set_mapping', action=AddSqlDBTableDataSetMapping, nargs='+', help='A SQL DB Tabl'
                   'e data set mapping. Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: database-name, '
                   'data-set-id, schema-name, sql-server-resource-id, table-name.', arg_group='DataSetMapping')
        c.argument('storage_account_data_set_mapping', action=AddStorageAccountDataSetMapping, nargs='+', help='A stora'
                   'ge account data set mapping. Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: contai'
                   'ner-name, data-set-id, storage-account-resource-id.', arg_group='DataSetMapping')

    with self.argument_context('datashare data-set-mapping delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', help='The name of the shareSubscription.')
        c.argument('data_set_mapping_name', help='The name of the dataSetMapping.')

    with self.argument_context('datashare invitation list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share.')
        c.argument('skip_token', help='The continuation token')

    with self.argument_context('datashare invitation show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share.')
        c.argument('invitation_name', help='The name of the invitation.')

    with self.argument_context('datashare invitation create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share to send the invitation for.')
        c.argument('invitation_name', help='The name of the invitation.')
        c.argument('target_active_directory_id', help='The target Azure AD Id. Can\'t be combined with email.')
        c.argument('target_email', help='The email the invitation is directed to.')
        c.argument('target_object_id', help='The target user or application Id that invitation is being sent to. Must b'
                   'e specified along TargetActiveDirectoryId. This enables sending invitations to specific users or ap'
                   'plications in an AD tenant.')

    with self.argument_context('datashare invitation delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share.')
        c.argument('invitation_name', help='The name of the invitation.')

    with self.argument_context('datashare share list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('skip_token', help='Continuation Token')

    with self.argument_context('datashare share show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share to retrieve.')

    with self.argument_context('datashare share create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share.')
        c.argument('description', help='Share description.')
        c.argument('share_kind', arg_type=get_enum_type(['CopyBased', 'InPlace']), help='Share kind.')
        c.argument('terms', help='Share terms.')

    with self.argument_context('datashare share delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share.')

    with self.argument_context('datashare share list-synchronization') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share.')
        c.argument('skip_token', help='Continuation token')

    with self.argument_context('datashare share list-synchronization-detail') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share.')
        c.argument('skip_token', help='Continuation token')
        c.argument('consumer_email', help='Email of the user who created the synchronization')
        c.argument('consumer_name', help='Name of the user who created the synchronization')
        c.argument('consumer_tenant_name', help='Tenant name of the consumer who created the synchronization')
        c.argument('duration_ms', help='synchronization duration')
        c.argument('end_time', help='End time of synchronization')
        c.argument('message', help='message of synchronization')
        c.argument('start_time', help='start time of synchronization')
        c.argument('status', help='Raw Status')
        c.argument('synchronization_id', help='Synchronization id')

    with self.argument_context('datashare provider-share-subscription list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share.')
        c.argument('skip_token', help='Continuation Token')

    with self.argument_context('datashare provider-share-subscription show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share.')
        c.argument('provider_share_subscription_id', help='To locate shareSubscription')

    with self.argument_context('datashare provider-share-subscription reinstate') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share.')
        c.argument('provider_share_subscription_id', help='To locate shareSubscription')

    with self.argument_context('datashare provider-share-subscription revoke') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share.')
        c.argument('provider_share_subscription_id', help='To locate shareSubscription')

    with self.argument_context('datashare share-subscription list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('skip_token', help='Continuation Token')

    with self.argument_context('datashare share-subscription show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', help='The name of the shareSubscription.')

    with self.argument_context('datashare share-subscription create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', help='The name of the shareSubscription.')
        c.argument('invitation_id', help='The invitation id.')
        c.argument('source_share_location', help='Source share location.')

    with self.argument_context('datashare share-subscription delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', help='The name of the shareSubscription.')

    with self.argument_context('datashare share-subscription cancel-synchronization') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', help='The name of the shareSubscription.')
        c.argument('synchronization_id', help='Synchronization id')

    with self.argument_context('datashare share-subscription list-source-share-synchronization-setting') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', help='The name of the shareSubscription.')
        c.argument('skip_token', help='Continuation token')

    with self.argument_context('datashare share-subscription list-synchronization') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', help='The name of the share subscription.')
        c.argument('skip_token', help='Continuation token')

    with self.argument_context('datashare share-subscription list-synchronization-detail') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', help='The name of the share subscription.')
        c.argument('skip_token', help='Continuation token')
        c.argument('synchronization_id', help='Synchronization id')

    with self.argument_context('datashare share-subscription synchronize') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', help='The name of share subscription')
        c.argument('synchronization_mode', arg_type=get_enum_type(['Incremental', 'FullSync']), help='Mode of synchroni'
                   'zation used in triggers and snapshot sync. Incremental by default')

    with self.argument_context('datashare consumer-source-data-set list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', help='The name of the shareSubscription.')
        c.argument('skip_token', help='Continuation token')

    with self.argument_context('datashare synchronization-setting list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share.')
        c.argument('skip_token', help='continuation token')

    with self.argument_context('datashare synchronization-setting show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share.')
        c.argument('synchronization_setting_name', help='The name of the synchronizationSetting.')

    with self.argument_context('datashare synchronization-setting create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share to add the synchronization setting to.')
        c.argument('synchronization_setting_name', help='The name of the synchronizationSetting.')
        c.argument('scheduled_synchronization_setting', action=AddScheduledSynchronizationSetting, nargs='+', help='A t'
                   'ype of synchronization setting based on schedule Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , availa'
                   'ble KEYs are: recurrence-interval, synchronization-time.', arg_group='SynchronizationSetting')

    with self.argument_context('datashare synchronization-setting delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share.')
        c.argument('synchronization_setting_name', help='The name of the synchronizationSetting .')

    with self.argument_context('datashare trigger list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', help='The name of the share subscription.')
        c.argument('skip_token', help='Continuation token')

    with self.argument_context('datashare trigger show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', help='The name of the shareSubscription.')
        c.argument('trigger_name', help='The name of the trigger.')

    with self.argument_context('datashare trigger create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', help='The name of the share subscription which will hold the data set sin'
                   'k.')
        c.argument('trigger_name', help='The name of the trigger.')
        c.argument('scheduled_trigger', action=AddScheduledTrigger, nargs='+', help='A type of trigger based on schedul'
                   'e Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: recurrence-interval, synchronizat'
                   'ion-mode, synchronization-time.', arg_group='Trigger')

    with self.argument_context('datashare trigger delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', help='The name of the shareSubscription.')
        c.argument('trigger_name', help='The name of the trigger.')
