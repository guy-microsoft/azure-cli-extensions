# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from knack.arguments import CLIArgumentType
from azure.cli.core.commands.parameters import (
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azext_storagecache.action import (
    AddSku,
    AddUpgradeStatus,
    AddJunctions,
    AddNfs3,
    AddClfs
)


def load_arguments(self, _):

    with self.argument_context('storagecache sku list') as c:
        pass

    with self.argument_context('storagecache usage-model list') as c:
        pass

    with self.argument_context('storagecache cache list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Target resource group.')

    with self.argument_context('storagecache cache show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Target resource group.')
        c.argument('cache_name', help='Name of Cache.')

    with self.argument_context('storagecache cache create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Target resource group.')
        c.argument('cache_name', help='Name of Cache.')
        c.argument('tags', tags_type, help='ARM tags as name/value pairs.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='Region name string.')
        c.argument('sku', action=AddSku, nargs='+', help='SKU for the Cache.')
        c.argument('properties_cache_size_gb', help='The size of this Cache, in GB.')
        c.argument('properties_provisioning_state', arg_type=get_enum_type(['Succeeded', 'Failed', 'Cancelled', 'Creating', 'Deleting', 'Updating']), help='ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property')
        c.argument('properties_subnet', help='A fully qualified URL.')
        c.argument('properties_upgrade_status', action=AddUpgradeStatus, nargs='+', help='Properties describing the software upgrade state of the Cache.')

    with self.argument_context('storagecache cache update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Target resource group.')
        c.argument('cache_name', help='Name of Cache.')
        c.argument('tags', tags_type, help='ARM tags as name/value pairs.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='Region name string.')
        c.argument('sku', action=AddSku, nargs='+', help='SKU for the Cache.')
        c.argument('properties_cache_size_gb', help='The size of this Cache, in GB.')
        c.argument('properties_provisioning_state', arg_type=get_enum_type(['Succeeded', 'Failed', 'Cancelled', 'Creating', 'Deleting', 'Updating']), help='ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property')
        c.argument('properties_subnet', help='A fully qualified URL.')
        c.argument('properties_upgrade_status', action=AddUpgradeStatus, nargs='+', help='Properties describing the software upgrade state of the Cache.')

    with self.argument_context('storagecache cache delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Target resource group.')
        c.argument('cache_name', help='Name of Cache.')

    with self.argument_context('storagecache cache flush') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Target resource group.')
        c.argument('cache_name', help='Name of Cache.')

    with self.argument_context('storagecache cache start') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Target resource group.')
        c.argument('cache_name', help='Name of Cache.')

    with self.argument_context('storagecache cache stop') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Target resource group.')
        c.argument('cache_name', help='Name of Cache.')

    with self.argument_context('storagecache cache upgrade-firmware') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Target resource group.')
        c.argument('cache_name', help='Name of Cache.')

    with self.argument_context('storagecache storage-target list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Target resource group.')
        c.argument('cache_name', help='Name of Cache.')

    with self.argument_context('storagecache storage-target show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Target resource group.')
        c.argument('cache_name', help='Name of Cache.')
        c.argument('storage_target_name', help='Name of Storage Target.')

    with self.argument_context('storagecache storage-target create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Target resource group.')
        c.argument('cache_name', help='Name of Cache.')
        c.argument('storage_target_name', help='Name of Storage Target.')
        c.argument('properties_junctions', action=AddJunctions, nargs='+', help='List of Cache namespace junctions to target for namespace associations.')
        c.argument('properties_target_type', arg_type=get_enum_type(['nfs3', 'clfs', 'unknown']), help='Type of the Storage Target.')
        c.argument('properties_provisioning_state', arg_type=get_enum_type(['Succeeded', 'Failed', 'Cancelled', 'Creating', 'Deleting', 'Updating']), help='ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property')
        c.argument('properties_nfs3', action=AddNfs3, nargs='+', help='An NFSv3 mount point for use as a Storage Target.')
        c.argument('properties_clfs', action=AddClfs, nargs='+', help='Storage container for use as a CLFS Storage Target.')
        c.argument('properties_unknown', arg_type=CLIArgumentType(options_list=['--properties-unknown'], help='Storage container for use as an Unknown Storage Target.'))

    with self.argument_context('storagecache storage-target update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Target resource group.')
        c.argument('cache_name', help='Name of Cache.')
        c.argument('storage_target_name', help='Name of Storage Target.')
        c.argument('properties_junctions', action=AddJunctions, nargs='+', help='List of Cache namespace junctions to target for namespace associations.')
        c.argument('properties_target_type', arg_type=get_enum_type(['nfs3', 'clfs', 'unknown']), help='Type of the Storage Target.')
        c.argument('properties_provisioning_state', arg_type=get_enum_type(['Succeeded', 'Failed', 'Cancelled', 'Creating', 'Deleting', 'Updating']), help='ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property')
        c.argument('properties_nfs3', action=AddNfs3, nargs='+', help='An NFSv3 mount point for use as a Storage Target.')
        c.argument('properties_clfs', action=AddClfs, nargs='+', help='Storage container for use as a CLFS Storage Target.')
        c.argument('properties_unknown', arg_type=CLIArgumentType(options_list=['--properties-unknown'], help='Storage container for use as an Unknown Storage Target.'))

    with self.argument_context('storagecache storage-target delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Target resource group.')
        c.argument('cache_name', help='Name of Cache.')
        c.argument('storage_target_name', help='Name of Storage Target.')
