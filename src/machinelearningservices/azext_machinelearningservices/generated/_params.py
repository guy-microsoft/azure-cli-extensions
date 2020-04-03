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
from azext_machinelearningservices.action import (
    AddSku,
    AddSharedPrivateLinkResources,
    AddValue,
    AddScaleSettings,
    AddPrivateEndpoint,
    AddPrivateLinkServiceConnectionState
)


def load_arguments(self, _):

    with self.argument_context('machinelearningservices workspace list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('skiptoken', help='Continuation token for pagination.')

    with self.argument_context('machinelearningservices workspace show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')

    with self.argument_context('machinelearningservices workspace create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')
        c.argument('identity', arg_type=CLIArgumentType(options_list=['--identity'], help='Identity for the resource.'))
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='Specifies the location of the resource.')
        c.argument('tags', tags_type, help='Contains resource tags defined as key/value pairs.')
        c.argument('sku', action=AddSku, nargs='+', help='Sku of the resource')
        c.argument('properties_description', help='The description of this workspace.')
        c.argument('properties_friendly_name', help='The friendly name for this workspace. This name in mutable')
        c.argument('properties_key_vault', help='ARM id of the key vault associated with this workspace. This cannot be changed once the workspace has been created')
        c.argument('properties_application_insights', help='ARM id of the application insights associated with this workspace. This cannot be changed once the workspace has been created')
        c.argument('properties_container_registry', help='ARM id of the container registry associated with this workspace. This cannot be changed once the workspace has been created')
        c.argument('properties_storage_account', help='ARM id of the storage account associated with this workspace. This cannot be changed once the workspace has been created')
        c.argument('properties_discovery_url', help='Url for the discovery service to identify regional endpoints for machine learning experimentation services')
        c.argument('properties_encryption', arg_type=CLIArgumentType(options_list=['--properties-encryption'], help=''))
        c.argument('properties_hbi_workspace', arg_type=get_three_state_flag(), help='The flag to signal HBI data in the workspace and reduce diagnostic data collected by the service')
        c.argument('properties_image_build_compute', help='The compute name for image build')
        c.argument('properties_allow_public_access_when_behind_vnet', arg_type=get_three_state_flag(), help='The flag to indicate whether to allow public access when behind VNet.')
        c.argument('properties_shared_private_link_resources', action=AddSharedPrivateLinkResources, nargs='+', help='The list of shared private link resources in this workspace.')
        c.argument('properties_linked_workspaces', arg_type=CLIArgumentType(options_list=['--properties-linked-workspaces'], help='Dictionary that contains all linked workspaces in the AML workspace, with resourceId of the linked workspace as key.'))

    with self.argument_context('machinelearningservices workspace update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')
        c.argument('tags', tags_type, help='The resource tags for the machine learning workspace.')
        c.argument('sku', action=AddSku, nargs='+', help='Sku of the resource')
        c.argument('properties_description', help='The description of this workspace.')
        c.argument('properties_friendly_name', help='The friendly name for this workspace.')

    with self.argument_context('machinelearningservices workspace delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')

    with self.argument_context('machinelearningservices workspace list-key') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')

    with self.argument_context('machinelearningservices workspace resync-key') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')

    with self.argument_context('machinelearningservices workspace-feature list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')

    with self.argument_context('machinelearningservices usage list') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The location for which resource usage is queried.')

    with self.argument_context('machinelearningservices virtual-machine-size list') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The location for which resource usage is queried.')

    with self.argument_context('machinelearningservices quota list') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The location for which resource usage is queried.')

    with self.argument_context('machinelearningservices quota update') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The location for which resource usage is queried.')
        c.argument('value', action=AddValue, nargs='+', help='The list for update quota.')

    with self.argument_context('machinelearningservices machine-learning-compute list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')
        c.argument('skiptoken', help='Continuation token for pagination.')

    with self.argument_context('machinelearningservices machine-learning-compute show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')
        c.argument('compute_name', help='Name of the Azure Machine Learning compute.')

    with self.argument_context('machinelearningservices machine-learning-compute create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')
        c.argument('compute_name', help='Name of the Azure Machine Learning compute.')
        c.argument('identity', arg_type=CLIArgumentType(options_list=['--identity'], help='Identity for the resource.'))
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='Specifies the location of the resource.')
        c.argument('tags', tags_type, help='Contains resource tags defined as key/value pairs.')
        c.argument('sku', action=AddSku, nargs='+', help='Sku of the resource')
        c.argument('properties', arg_type=CLIArgumentType(options_list=['--properties'], help='Machine Learning compute object.'))

    with self.argument_context('machinelearningservices machine-learning-compute update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')
        c.argument('compute_name', help='Name of the Azure Machine Learning compute.')
        c.argument('properties_scale_settings', action=AddScaleSettings, nargs='+', help='scale settings for AML Compute')

    with self.argument_context('machinelearningservices machine-learning-compute delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')
        c.argument('compute_name', help='Name of the Azure Machine Learning compute.')
        c.argument('underlying_resource_action', arg_type=get_enum_type(['Delete', 'Detach']), help='Delete the underlying compute if \'Delete\', or detach the underlying compute from workspace if \'Detach\'.')

    with self.argument_context('machinelearningservices machine-learning-compute list-node') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')
        c.argument('compute_name', help='Name of the Azure Machine Learning compute.')

    with self.argument_context('machinelearningservices machine-learning-compute list-key') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')
        c.argument('compute_name', help='Name of the Azure Machine Learning compute.')

    with self.argument_context('machinelearningservices  list') as c:
        pass

    with self.argument_context('machinelearningservices private-endpoint-connection show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')
        c.argument('private_endpoint_connection_name', help='The name of the private endpoint connection associated with the workspace')

    with self.argument_context('machinelearningservices private-endpoint-connection delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')
        c.argument('private_endpoint_connection_name', help='The name of the private endpoint connection associated with the workspace')

    with self.argument_context('machinelearningservices private-endpoint-connection put') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')
        c.argument('private_endpoint_connection_name', help='The name of the private endpoint connection associated with the workspace')
        c.argument('identity', arg_type=CLIArgumentType(options_list=['--identity'], help='Identity for the resource.'))
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='Specifies the location of the resource.')
        c.argument('tags', tags_type, help='Contains resource tags defined as key/value pairs.')
        c.argument('sku', action=AddSku, nargs='+', help='Sku of the resource')
        c.argument('properties_private_endpoint', action=AddPrivateEndpoint, nargs='+', help='The Private Endpoint resource.')
        c.argument('properties_private_link_service_connection_state', action=AddPrivateLinkServiceConnectionState, nargs='+', help='A collection of information about the state of the connection between service consumer and provider.')
        c.argument('properties_provisioning_state', arg_type=get_enum_type(['Succeeded', 'Creating', 'Deleting', 'Failed']), help='The current provisioning state.')

    with self.argument_context('machinelearningservices private-link-resource list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')

    with self.argument_context('machinelearningservices linked-workspace list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')
        c.argument('link_subscription_id', help='The subscriptionid of the linked workspace.')
        c.argument('link_resource_group', help='The resource group name of the linked workspace.')
        c.argument('link_resource_name', help='The resource name of the linked workspace.')
        c.argument('link_resource_id', help='The resourceId of the linked workspace.')
        c.argument('uai_resource_id', help='The resourceId of the user assigned identity for the linked workspace.')

    with self.argument_context('machinelearningservices linked-workspace show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')
        c.argument('link_name', help='Friendly name of the linked workspace')

    with self.argument_context('machinelearningservices linked-workspace create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')
        c.argument('link_name', help='Friendly name of the linked workspace')
        c.argument('resource_id', help='ResourceId of the linked workspace')
        c.argument('user_assigned_identity_resource_id', help='ResourceId of the user assigned identity for the linked workspace')

    with self.argument_context('machinelearningservices linked-workspace update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')
        c.argument('link_name', help='Friendly name of the linked workspace')
        c.argument('user_assigned_identity_resource_id', help='ResourceId of the user assigned identity for the linked workspace')

    with self.argument_context('machinelearningservices linked-workspace delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='Name of the resource group in which workspace is located.')
        c.argument('workspace_name', help='Name of Azure Machine Learning workspace.')
        c.argument('link_name', help='Friendly name of the linked workspace')
