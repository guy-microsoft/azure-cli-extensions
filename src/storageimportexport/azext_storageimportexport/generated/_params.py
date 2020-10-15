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

from azure.cli.core.commands.parameters import (
    tags_type,
    get_three_state_flag,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azext_storageimportexport.action import (
    AddReturnAddress,
    AddReturnShipping,
    AddShippingInformation,
    AddDeliveryPackage,
    AddStorageimportexportJobCreateDriveList,
    AddExport,
    AddEncryptionKey,
    AddStorageimportexportJobUpdateDriveList
)


def load_arguments(self, _):

    with self.argument_context('storageimportexport location show') as c:
        c.argument('location_name', options_list=['--name', '-n', '--location-name'], type=str, help='The name of the '
                   'location. For example, West US or westus.')

    with self.argument_context('storageimportexport job list') as c:
        c.argument('top', type=int, help='An integer value that specifies how many jobs at most should be returned. '
                   'The value cannot exceed 100.')
        c.argument('filter_', options_list=['--filter'], type=str, help='Can be used to restrict the results to '
                   'certain conditions.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('storageimportexport job show') as c:
        c.argument('job_name', options_list=['--name', '-n', '--job-name'], type=str, help='The name of the '
                   'import/export job.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('storageimportexport job create') as c:
        c.argument('job_name', options_list=['--name', '-n', '--job-name'], type=str, help='The name of the '
                   'import/export job.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('client_tenant_id', type=str, help='The tenant ID of the client making the request.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)
        c.argument('storage_account_id', type=str, help='The resource identifier of the storage account where data '
                   'will be imported to or exported from.')
        c.argument('job_type', type=str, help='The type of job')
        c.argument('return_address', action=AddReturnAddress, nargs='*', help='Specifies the return address '
                   'information for the job.')
        c.argument('return_shipping', action=AddReturnShipping, nargs='*', help='Specifies the return carrier and '
                   'customer\'s account with the carrier.')
        c.argument('shipping_information', action=AddShippingInformation, nargs='*', help='Contains information about '
                   'the Microsoft datacenter to which the drives should be shipped.')
        c.argument('delivery_package', action=AddDeliveryPackage, nargs='*', help='Contains information about the '
                   'package being shipped by the customer to the Microsoft data center.')
        c.argument('return_package', action=AddDeliveryPackage, nargs='*', help='Contains information about the '
                   'package being shipped from the Microsoft data center to the customer to return the drives. The '
                   'format is the same as the deliveryPackage property above. This property is not included if the '
                   'drives have not yet been returned.')
        c.argument('diagnostics_path', type=str, help='The virtual blob directory to which the copy logs and backups '
                   'of drive manifest files (if enabled) will be stored.')
        c.argument('log_level', type=str, help='Default value is Error. Indicates whether error logging or verbose '
                   'logging will be enabled.')
        c.argument('backup_drive_manifest', arg_type=get_three_state_flag(), help='Default value is false. Indicates '
                   'whether the manifest files on the drives should be copied to block blobs.')
        c.argument('state', type=str, help='Current state of the job.')
        c.argument('cancel_requested', arg_type=get_three_state_flag(), help='Indicates whether a request has been '
                   'submitted to cancel the job.')
        c.argument('percent_complete', type=int, help='Overall percentage completed for the job.')
        c.argument('incomplete_blob_list_uri', type=str, help='A blob path that points to a block blob containing a '
                   'list of blob names that were not exported due to insufficient drive space. If all blobs were '
                   'exported successfully, then this element is not included in the response.')
        c.argument('drive_list', action=AddStorageimportexportJobCreateDriveList, nargs='*', help='List of up to ten '
                   'drives that comprise the job. The drive list is a required element for an import job; it is not '
                   'specified for export jobs.')
        c.argument('export', action=AddExport, nargs='*', help='A property containing information about the blobs to '
                   'be exported for an export job. This property is included for export jobs only.')
        c.argument('provisioning_state', type=str, help='Specifies the provisioning state of the job.')
        c.argument('encryption_key', action=AddEncryptionKey, nargs='*', help='Contains information about the '
                   'encryption key.')
        c.argument('affinity_id', type=str, help='Specifies the provisioning state of the job.')

    with self.argument_context('storageimportexport job update') as c:
        c.argument('job_name', options_list=['--name', '-n', '--job-name'], type=str, help='The name of the '
                   'import/export job.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('tags', tags_type)
        c.argument('cancel_requested', arg_type=get_three_state_flag(), help='If specified, the value must be true. '
                   'The service will attempt to cancel the job.')
        c.argument('state', type=str, help='If specified, the value must be Shipping, which tells the Import/Export '
                   'service that the package for the job has been shipped. The ReturnAddress and DeliveryPackage '
                   'properties must have been set either in this request or in a previous request, otherwise the '
                   'request will fail.')
        c.argument('return_address', action=AddReturnAddress, nargs='*', help='Specifies the return address '
                   'information for the job.')
        c.argument('return_shipping', action=AddReturnShipping, nargs='*', help='Specifies the return carrier and '
                   'customer\'s account with the carrier.')
        c.argument('delivery_package', action=AddDeliveryPackage, nargs='*', help='Contains information about the '
                   'package being shipped by the customer to the Microsoft data center.')
        c.argument('log_level', type=str, help='Indicates whether error logging or verbose logging is enabled.')
        c.argument('backup_drive_manifest', arg_type=get_three_state_flag(), help='Indicates whether the manifest '
                   'files on the drives should be copied to block blobs.')
        c.argument('drive_list', action=AddStorageimportexportJobUpdateDriveList, nargs='*', help='List of drives that '
                   'comprise the job.')

    with self.argument_context('storageimportexport job delete') as c:
        c.argument('job_name', options_list=['--name', '-n', '--job-name'], type=str, help='The name of the '
                   'import/export job.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('storageimportexport bit-locker-key list') as c:
        c.argument('job_name', type=str, help='The name of the import/export job.')
        c.argument('resource_group_name', resource_group_name_type)
