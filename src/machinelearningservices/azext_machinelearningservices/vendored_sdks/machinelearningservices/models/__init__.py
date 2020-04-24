# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import Aks
    from ._models_py3 import AksComputeSecrets
    from ._models_py3 import AksNetworkingConfiguration
    from ._models_py3 import AksProperties
    from ._models_py3 import AmlCompute
    from ._models_py3 import AmlComputeNodeInformation
    from ._models_py3 import AmlComputeNodesInformation
    from ._models_py3 import AmlComputeProperties
    from ._models_py3 import AmlUserFeature
    from ._models_py3 import ClusterUpdateParameters
    from ._models_py3 import Compute
    from ._models_py3 import ComputeNodesInformation
    from ._models_py3 import ComputeResource
    from ._models_py3 import ComputeSecrets
    from ._models_py3 import DataFactory
    from ._models_py3 import DataLakeAnalytics
    from ._models_py3 import DataLakeAnalyticsProperties
    from ._models_py3 import Databricks
    from ._models_py3 import DatabricksComputeSecrets
    from ._models_py3 import DatabricksProperties
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse
    from ._models_py3 import HdInsight
    from ._models_py3 import Identity
    from ._models_py3 import KeyVaultProperties
    from ._models_py3 import ListAmlUserFeatureResult
    from ._models_py3 import ListUsagesResult
    from ._models_py3 import ListWorkspaceKeysResult
    from ._models_py3 import ListWorkspaceQuotas
    from ._models_py3 import MachineLearningServiceError
    from ._models_py3 import NodeStateCounts
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import PaginatedComputeResourcesList
    from ._models_py3 import Password
    from ._models_py3 import PrivateEndpoint
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkResourceListResult
    from ._models_py3 import PrivateLinkServiceConnectionState
    from ._models_py3 import QuotaBaseProperties
    from ._models_py3 import QuotaUpdateParameters
    from ._models_py3 import RegistryListCredentialsResult
    from ._models_py3 import Resource
    from ._models_py3 import ResourceId
    from ._models_py3 import ResourceName
    from ._models_py3 import ResourceQuota
    from ._models_py3 import ResourceSkuLocationInfo
    from ._models_py3 import ResourceSkuZoneDetails
    from ._models_py3 import Restriction
    from ._models_py3 import ScaleSettings
    from ._models_py3 import ServicePrincipalCredentials
    from ._models_py3 import SharedPrivateLinkResource
    from ._models_py3 import Sku
    from ._models_py3 import SkuCapability
    from ._models_py3 import SkuListResult
    from ._models_py3 import SslConfiguration
    from ._models_py3 import SystemService
    from ._models_py3 import UpdateWorkspaceQuotas
    from ._models_py3 import UpdateWorkspaceQuotasResult
    from ._models_py3 import Usage
    from ._models_py3 import UsageName
    from ._models_py3 import UserAccountCredentials
    from ._models_py3 import VirtualMachine
    from ._models_py3 import VirtualMachineSecrets
    from ._models_py3 import VirtualMachineSize
    from ._models_py3 import VirtualMachineSizeListResult
    from ._models_py3 import VirtualMachineSshCredentials
    from ._models_py3 import Workspace
    from ._models_py3 import WorkspaceListResult
    from ._models_py3 import WorkspaceSku
    from ._models_py3 import WorkspaceUpdateParameters
except (SyntaxError, ImportError):
    from ._models import Aks  # type: ignore
    from ._models import AksComputeSecrets  # type: ignore
    from ._models import AksNetworkingConfiguration  # type: ignore
    from ._models import AksProperties  # type: ignore
    from ._models import AmlCompute  # type: ignore
    from ._models import AmlComputeNodeInformation  # type: ignore
    from ._models import AmlComputeNodesInformation  # type: ignore
    from ._models import AmlComputeProperties  # type: ignore
    from ._models import AmlUserFeature  # type: ignore
    from ._models import ClusterUpdateParameters  # type: ignore
    from ._models import Compute  # type: ignore
    from ._models import ComputeNodesInformation  # type: ignore
    from ._models import ComputeResource  # type: ignore
    from ._models import ComputeSecrets  # type: ignore
    from ._models import DataFactory  # type: ignore
    from ._models import DataLakeAnalytics  # type: ignore
    from ._models import DataLakeAnalyticsProperties  # type: ignore
    from ._models import Databricks  # type: ignore
    from ._models import DatabricksComputeSecrets  # type: ignore
    from ._models import DatabricksProperties  # type: ignore
    from ._models import ErrorDetail  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import HdInsight  # type: ignore
    from ._models import Identity  # type: ignore
    from ._models import KeyVaultProperties  # type: ignore
    from ._models import ListAmlUserFeatureResult  # type: ignore
    from ._models import ListUsagesResult  # type: ignore
    from ._models import ListWorkspaceKeysResult  # type: ignore
    from ._models import ListWorkspaceQuotas  # type: ignore
    from ._models import MachineLearningServiceError  # type: ignore
    from ._models import NodeStateCounts  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import PaginatedComputeResourcesList  # type: ignore
    from ._models import Password  # type: ignore
    from ._models import PrivateEndpoint  # type: ignore
    from ._models import PrivateEndpointConnection  # type: ignore
    from ._models import PrivateLinkResource  # type: ignore
    from ._models import PrivateLinkResourceListResult  # type: ignore
    from ._models import PrivateLinkServiceConnectionState  # type: ignore
    from ._models import QuotaBaseProperties  # type: ignore
    from ._models import QuotaUpdateParameters  # type: ignore
    from ._models import RegistryListCredentialsResult  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourceId  # type: ignore
    from ._models import ResourceName  # type: ignore
    from ._models import ResourceQuota  # type: ignore
    from ._models import ResourceSkuLocationInfo  # type: ignore
    from ._models import ResourceSkuZoneDetails  # type: ignore
    from ._models import Restriction  # type: ignore
    from ._models import ScaleSettings  # type: ignore
    from ._models import ServicePrincipalCredentials  # type: ignore
    from ._models import SharedPrivateLinkResource  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import SkuCapability  # type: ignore
    from ._models import SkuListResult  # type: ignore
    from ._models import SslConfiguration  # type: ignore
    from ._models import SystemService  # type: ignore
    from ._models import UpdateWorkspaceQuotas  # type: ignore
    from ._models import UpdateWorkspaceQuotasResult  # type: ignore
    from ._models import Usage  # type: ignore
    from ._models import UsageName  # type: ignore
    from ._models import UserAccountCredentials  # type: ignore
    from ._models import VirtualMachine  # type: ignore
    from ._models import VirtualMachineSecrets  # type: ignore
    from ._models import VirtualMachineSize  # type: ignore
    from ._models import VirtualMachineSizeListResult  # type: ignore
    from ._models import VirtualMachineSshCredentials  # type: ignore
    from ._models import Workspace  # type: ignore
    from ._models import WorkspaceListResult  # type: ignore
    from ._models import WorkspaceSku  # type: ignore
    from ._models import WorkspaceUpdateParameters  # type: ignore

from ._azure_machine_learning_workspaces_enums import (
    AllocationState,
    ComputeType,
    EncryptionStatus,
    NodeState,
    PrivateEndpointConnectionProvisioningState,
    PrivateEndpointServiceConnectionStatus,
    ProvisioningState,
    ReasonCode,
    RemoteLoginPortPublicAccess,
    SslConfigurationStatus,
    Status,
    UnderlyingResourceAction,
    VmPriority,
)

__all__ = [
    'Aks',
    'AksComputeSecrets',
    'AksNetworkingConfiguration',
    'AksProperties',
    'AmlCompute',
    'AmlComputeNodeInformation',
    'AmlComputeNodesInformation',
    'AmlComputeProperties',
    'AmlUserFeature',
    'ClusterUpdateParameters',
    'Compute',
    'ComputeNodesInformation',
    'ComputeResource',
    'ComputeSecrets',
    'DataFactory',
    'DataLakeAnalytics',
    'DataLakeAnalyticsProperties',
    'Databricks',
    'DatabricksComputeSecrets',
    'DatabricksProperties',
    'ErrorDetail',
    'ErrorResponse',
    'HdInsight',
    'Identity',
    'KeyVaultProperties',
    'ListAmlUserFeatureResult',
    'ListUsagesResult',
    'ListWorkspaceKeysResult',
    'ListWorkspaceQuotas',
    'MachineLearningServiceError',
    'NodeStateCounts',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'PaginatedComputeResourcesList',
    'Password',
    'PrivateEndpoint',
    'PrivateEndpointConnection',
    'PrivateLinkResource',
    'PrivateLinkResourceListResult',
    'PrivateLinkServiceConnectionState',
    'QuotaBaseProperties',
    'QuotaUpdateParameters',
    'RegistryListCredentialsResult',
    'Resource',
    'ResourceId',
    'ResourceName',
    'ResourceQuota',
    'ResourceSkuLocationInfo',
    'ResourceSkuZoneDetails',
    'Restriction',
    'ScaleSettings',
    'ServicePrincipalCredentials',
    'SharedPrivateLinkResource',
    'Sku',
    'SkuCapability',
    'SkuListResult',
    'SslConfiguration',
    'SystemService',
    'UpdateWorkspaceQuotas',
    'UpdateWorkspaceQuotasResult',
    'Usage',
    'UsageName',
    'UserAccountCredentials',
    'VirtualMachine',
    'VirtualMachineSecrets',
    'VirtualMachineSize',
    'VirtualMachineSizeListResult',
    'VirtualMachineSshCredentials',
    'Workspace',
    'WorkspaceListResult',
    'WorkspaceSku',
    'WorkspaceUpdateParameters',
    'AllocationState',
    'ComputeType',
    'EncryptionStatus',
    'NodeState',
    'PrivateEndpointConnectionProvisioningState',
    'PrivateEndpointServiceConnectionStatus',
    'ProvisioningState',
    'ReasonCode',
    'RemoteLoginPortPublicAccess',
    'SslConfigurationStatus',
    'Status',
    'UnderlyingResourceAction',
    'VmPriority',
]
