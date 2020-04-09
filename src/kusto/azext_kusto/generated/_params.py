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
    get_three_state_flag,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azext_kusto.action import (
    AddSku,
    AddTrustedExternalTenants,
    AddOptimizedAutoscale,
    AddVirtualNetworkConfiguration,
    AddKeyVaultProperties,
    AddLanguageExtensions,
    AddValue
)


def load_arguments(self, _):

    with self.argument_context('kusto cluster list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')

    with self.argument_context('kusto cluster show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')

    with self.argument_context('kusto cluster create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('tags', tags_type, help='Resource tags.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The geo-location where the resource lives')
        c.argument('sku', action=AddSku, nargs='+', help='Azure SKU definition.')
        c.argument('zones', nargs='+', help='An array represents the availability zones of the cluster.')
        c.argument('identity', arg_type=CLIArgumentType(options_list=['--identity'], help='Identity for the resource.'))
        c.argument('properties_trusted_external_tenants', action=AddTrustedExternalTenants, nargs='+', help='The cluster\'s external tenants.')
        c.argument('properties_optimized_autoscale', action=AddOptimizedAutoscale, nargs='+', help='A class that contains the optimized auto scale definition.')
        c.argument('properties_enable_disk_encryption', arg_type=get_three_state_flag(), help='A boolean value that indicates if the cluster\'s disks are encrypted.')
        c.argument('properties_enable_streaming_ingest', arg_type=get_three_state_flag(), help='A boolean value that indicates if the streaming ingest is enabled.')
        c.argument('properties_virtual_network_configuration', action=AddVirtualNetworkConfiguration, nargs='+', help='A class that contains virtual network definition.')
        c.argument('properties_key_vault_properties', action=AddKeyVaultProperties, nargs='+', help='Properties of the key vault.')
        c.argument('properties_enable_purge', arg_type=get_three_state_flag(), help='A boolean value that indicates if the purge operations are enabled.')
        c.argument('properties_language_extensions', action=AddLanguageExtensions, nargs='+', help='The list of language extension objects.')

    with self.argument_context('kusto cluster update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('tags', tags_type, help='Resource tags.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='Resource location.')
        c.argument('sku', action=AddSku, nargs='+', help='Azure SKU definition.')
        c.argument('identity', arg_type=CLIArgumentType(options_list=['--identity'], help='Identity for the resource.'))
        c.argument('properties_trusted_external_tenants', action=AddTrustedExternalTenants, nargs='+', help='The cluster\'s external tenants.')
        c.argument('properties_optimized_autoscale', action=AddOptimizedAutoscale, nargs='+', help='A class that contains the optimized auto scale definition.')
        c.argument('properties_enable_disk_encryption', arg_type=get_three_state_flag(), help='A boolean value that indicates if the cluster\'s disks are encrypted.')
        c.argument('properties_enable_streaming_ingest', arg_type=get_three_state_flag(), help='A boolean value that indicates if the streaming ingest is enabled.')
        c.argument('properties_virtual_network_configuration', action=AddVirtualNetworkConfiguration, nargs='+', help='A class that contains virtual network definition.')
        c.argument('properties_key_vault_properties', action=AddKeyVaultProperties, nargs='+', help='Properties of the key vault.')
        c.argument('properties_enable_purge', arg_type=get_three_state_flag(), help='A boolean value that indicates if the purge operations are enabled.')
        c.argument('properties_language_extensions', action=AddLanguageExtensions, nargs='+', help='The list of language extension objects.')

    with self.argument_context('kusto cluster delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')

    with self.argument_context('kusto cluster detach-follower-database') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('cluster_resource_id', help='Resource id of the cluster that follows a database owned by this cluster.')
        c.argument('attached_database_configuration_name', help='Resource name of the attached database configuration in the follower cluster.')

    with self.argument_context('kusto cluster add-language-extension') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('value', action=AddValue, nargs='+', help='The list of language extensions.')

    with self.argument_context('kusto cluster remove-language-extension') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('value', action=AddValue, nargs='+', help='The list of language extensions.')

    with self.argument_context('kusto cluster stop') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')

    with self.argument_context('kusto cluster start') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')

    with self.argument_context('kusto cluster list-follower-database') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')

    with self.argument_context('kusto cluster diagnose-virtual-network') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')

    with self.argument_context('kusto cluster list-language-extension') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')

    with self.argument_context('kusto cluster-principal-assignment list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')

    with self.argument_context('kusto cluster-principal-assignment show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('principal_assignment_name', help='The name of the Kusto principalAssignment.')

    with self.argument_context('kusto cluster-principal-assignment create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('principal_assignment_name', help='The name of the Kusto principalAssignment.')
        c.argument('properties_principal_id', help='The principal ID assigned to the cluster principal. It can be a user email, application ID, or security group name.')
        c.argument('properties_role', arg_type=get_enum_type(['AllDatabasesAdmin', 'AllDatabasesViewer']), help='Cluster principal role.')
        c.argument('properties_tenant_id', help='The tenant id of the principal')
        c.argument('properties_principal_type', arg_type=get_enum_type(['App', 'Group', 'User']), help='Principal type.')

    with self.argument_context('kusto cluster-principal-assignment update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('principal_assignment_name', help='The name of the Kusto principalAssignment.')
        c.argument('properties_principal_id', help='The principal ID assigned to the cluster principal. It can be a user email, application ID, or security group name.')
        c.argument('properties_role', arg_type=get_enum_type(['AllDatabasesAdmin', 'AllDatabasesViewer']), help='Cluster principal role.')
        c.argument('properties_tenant_id', help='The tenant id of the principal')
        c.argument('properties_principal_type', arg_type=get_enum_type(['App', 'Group', 'User']), help='Principal type.')

    with self.argument_context('kusto cluster-principal-assignment delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('principal_assignment_name', help='The name of the Kusto principalAssignment.')

    with self.argument_context('kusto database list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')

    with self.argument_context('kusto database show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('database_name', help='The name of the database in the Kusto cluster.')

    with self.argument_context('kusto database create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('database_name', help='The name of the database in the Kusto cluster.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='Resource location.')
        c.argument('kind', arg_type=get_enum_type(['ReadWrite', 'ReadOnlyFollowing', 'EventHub', 'EventGrid', 'IotHub']), help='Kind of the database')

    with self.argument_context('kusto database update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('database_name', help='The name of the database in the Kusto cluster.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='Resource location.')
        c.argument('kind', arg_type=get_enum_type(['ReadWrite', 'ReadOnlyFollowing', 'EventHub', 'EventGrid', 'IotHub']), help='Kind of the database')

    with self.argument_context('kusto database delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('database_name', help='The name of the database in the Kusto cluster.')

    with self.argument_context('kusto database add-principal') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('database_name', help='The name of the database in the Kusto cluster.')
        c.argument('value', action=AddValue, nargs='+', help='The list of Kusto database principals.')

    with self.argument_context('kusto database remove-principal') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('database_name', help='The name of the database in the Kusto cluster.')
        c.argument('value', action=AddValue, nargs='+', help='The list of Kusto database principals.')

    with self.argument_context('kusto database list-principal') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('database_name', help='The name of the database in the Kusto cluster.')

    with self.argument_context('kusto database-principal-assignment list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('database_name', help='The name of the database in the Kusto cluster.')

    with self.argument_context('kusto database-principal-assignment show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('database_name', help='The name of the database in the Kusto cluster.')
        c.argument('principal_assignment_name', help='The name of the Kusto principalAssignment.')

    with self.argument_context('kusto database-principal-assignment create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('database_name', help='The name of the database in the Kusto cluster.')
        c.argument('principal_assignment_name', help='The name of the Kusto principalAssignment.')
        c.argument('properties_principal_id', help='The principal ID assigned to the database principal. It can be a user email, application ID, or security group name.')
        c.argument('properties_role', arg_type=get_enum_type(['Admin', 'Ingestor', 'Monitor', 'User', 'UnrestrictedViewers', 'Viewer']), help='Database principal role.')
        c.argument('properties_tenant_id', help='The tenant id of the principal')
        c.argument('properties_principal_type', arg_type=get_enum_type(['App', 'Group', 'User']), help='Principal type.')

    with self.argument_context('kusto database-principal-assignment update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('database_name', help='The name of the database in the Kusto cluster.')
        c.argument('principal_assignment_name', help='The name of the Kusto principalAssignment.')
        c.argument('properties_principal_id', help='The principal ID assigned to the database principal. It can be a user email, application ID, or security group name.')
        c.argument('properties_role', arg_type=get_enum_type(['Admin', 'Ingestor', 'Monitor', 'User', 'UnrestrictedViewers', 'Viewer']), help='Database principal role.')
        c.argument('properties_tenant_id', help='The tenant id of the principal')
        c.argument('properties_principal_type', arg_type=get_enum_type(['App', 'Group', 'User']), help='Principal type.')

    with self.argument_context('kusto database-principal-assignment delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('database_name', help='The name of the database in the Kusto cluster.')
        c.argument('principal_assignment_name', help='The name of the Kusto principalAssignment.')

    with self.argument_context('kusto attached-database-configuration list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')

    with self.argument_context('kusto attached-database-configuration show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('attached_database_configuration_name', help='The name of the attached database configuration.')

    with self.argument_context('kusto attached-database-configuration create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('attached_database_configuration_name', help='The name of the attached database configuration.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='Resource location.')
        c.argument('properties_database_name', help='The name of the database which you would like to attach, use * if you want to follow all current and future databases.')
        c.argument('properties_cluster_resource_id', help='The resource id of the cluster where the databases you would like to attach reside.')
        c.argument('properties_default_principals_modification_kind', arg_type=get_enum_type(['Union', 'Replace', 'None']), help='The default principals modification kind')

    with self.argument_context('kusto attached-database-configuration update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('attached_database_configuration_name', help='The name of the attached database configuration.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='Resource location.')
        c.argument('properties_database_name', help='The name of the database which you would like to attach, use * if you want to follow all current and future databases.')
        c.argument('properties_cluster_resource_id', help='The resource id of the cluster where the databases you would like to attach reside.')
        c.argument('properties_default_principals_modification_kind', arg_type=get_enum_type(['Union', 'Replace', 'None']), help='The default principals modification kind')

    with self.argument_context('kusto attached-database-configuration delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('attached_database_configuration_name', help='The name of the attached database configuration.')

    with self.argument_context('kusto data-connection list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('database_name', help='The name of the database in the Kusto cluster.')

    with self.argument_context('kusto data-connection show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('database_name', help='The name of the database in the Kusto cluster.')
        c.argument('data_connection_name', help='The name of the data connection.')

    with self.argument_context('kusto data-connection create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('database_name', help='The name of the database in the Kusto cluster.')
        c.argument('data_connection_name', help='The name of the data connection.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='Resource location.')
        c.argument('kind', arg_type=get_enum_type(['ReadWrite', 'ReadOnlyFollowing', 'EventHub', 'EventGrid', 'IotHub']), help='Kind of the database')

    with self.argument_context('kusto data-connection update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('database_name', help='The name of the database in the Kusto cluster.')
        c.argument('data_connection_name', help='The name of the data connection.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='Resource location.')
        c.argument('kind', arg_type=get_enum_type(['ReadWrite', 'ReadOnlyFollowing', 'EventHub', 'EventGrid', 'IotHub']), help='Kind of the database')

    with self.argument_context('kusto data-connection delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('database_name', help='The name of the database in the Kusto cluster.')
        c.argument('data_connection_name', help='The name of the data connection.')

    with self.argument_context('kusto data-connection data-connection-validation') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The name of the resource group containing the Kusto cluster.')
        c.argument('cluster_name', help='The name of the Kusto cluster.')
        c.argument('database_name', help='The name of the database in the Kusto cluster.')
        c.argument('data_connection_name', help='The name of the data connection.')
        c.argument('properties', arg_type=CLIArgumentType(options_list=['--properties'], help='Class representing an data connection.'))
