# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import BackupRequest
    from ._models_py3 import CheckNameAvailabilityParameters
    from ._models_py3 import CheckNameAvailabilityResult
    from ._models_py3 import CloudEndpoint
    from ._models_py3 import CloudEndpointArray
    from ._models_py3 import CloudEndpointCreateParameters
    from ._models_py3 import CloudTieringCachePerformance
    from ._models_py3 import CloudTieringDatePolicyStatus
    from ._models_py3 import CloudTieringFilesNotTiering
    from ._models_py3 import CloudTieringSpaceSavings
    from ._models_py3 import CloudTieringVolumeFreeSpacePolicyStatus
    from ._models_py3 import FilesNotTieringError
    from ._models_py3 import OperationDisplayInfo
    from ._models_py3 import OperationDisplayResource
    from ._models_py3 import OperationEntity
    from ._models_py3 import OperationEntityListResult
    from ._models_py3 import OperationProperties
    from ._models_py3 import OperationResourceMetricSpecification
    from ._models_py3 import OperationResourceMetricSpecificationDimension
    from ._models_py3 import OperationResourceServiceSpecification
    from ._models_py3 import OperationStatus
    from ._models_py3 import PostBackupResponse
    from ._models_py3 import PostRestoreRequest
    from ._models_py3 import PreRestoreRequest
    from ._models_py3 import PrivateEndpoint
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateEndpointConnectionListResult
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkResourceListResult
    from ._models_py3 import PrivateLinkServiceConnectionState
    from ._models_py3 import ProxyResource
    from ._models_py3 import RecallActionParameters
    from ._models_py3 import RegisteredServer
    from ._models_py3 import RegisteredServerArray
    from ._models_py3 import RegisteredServerCreateParameters
    from ._models_py3 import Resource
    from ._models_py3 import ResourcesMoveInfo
    from ._models_py3 import RestoreFileSpec
    from ._models_py3 import ServerEndpoint
    from ._models_py3 import ServerEndpointArray
    from ._models_py3 import ServerEndpointBackgroundDataDownloadActivity
    from ._models_py3 import ServerEndpointCloudTieringStatus
    from ._models_py3 import ServerEndpointCreateParameters
    from ._models_py3 import ServerEndpointFilesNotSyncingError
    from ._models_py3 import ServerEndpointRecallError
    from ._models_py3 import ServerEndpointRecallStatus
    from ._models_py3 import ServerEndpointSyncActivityStatus
    from ._models_py3 import ServerEndpointSyncSessionStatus
    from ._models_py3 import ServerEndpointSyncStatus
    from ._models_py3 import ServerEndpointUpdateParameters
    from ._models_py3 import StorageSyncApiError
    from ._models_py3 import StorageSyncError
    from ._models_py3 import StorageSyncErrorDetails
    from ._models_py3 import StorageSyncInnerErrorDetails
    from ._models_py3 import StorageSyncService
    from ._models_py3 import StorageSyncServiceArray
    from ._models_py3 import StorageSyncServiceCreateParameters
    from ._models_py3 import StorageSyncServiceUpdateParameters
    from ._models_py3 import SubscriptionState
    from ._models_py3 import SyncGroup
    from ._models_py3 import SyncGroupArray
    from ._models_py3 import SyncGroupCreateParameters
    from ._models_py3 import TrackedResource
    from ._models_py3 import TriggerChangeDetectionParameters
    from ._models_py3 import TriggerRolloverRequest
    from ._models_py3 import Workflow
    from ._models_py3 import WorkflowArray
except (SyntaxError, ImportError):
    from ._models import BackupRequest  # type: ignore
    from ._models import CheckNameAvailabilityParameters  # type: ignore
    from ._models import CheckNameAvailabilityResult  # type: ignore
    from ._models import CloudEndpoint  # type: ignore
    from ._models import CloudEndpointArray  # type: ignore
    from ._models import CloudEndpointCreateParameters  # type: ignore
    from ._models import CloudTieringCachePerformance  # type: ignore
    from ._models import CloudTieringDatePolicyStatus  # type: ignore
    from ._models import CloudTieringFilesNotTiering  # type: ignore
    from ._models import CloudTieringSpaceSavings  # type: ignore
    from ._models import CloudTieringVolumeFreeSpacePolicyStatus  # type: ignore
    from ._models import FilesNotTieringError  # type: ignore
    from ._models import OperationDisplayInfo  # type: ignore
    from ._models import OperationDisplayResource  # type: ignore
    from ._models import OperationEntity  # type: ignore
    from ._models import OperationEntityListResult  # type: ignore
    from ._models import OperationProperties  # type: ignore
    from ._models import OperationResourceMetricSpecification  # type: ignore
    from ._models import OperationResourceMetricSpecificationDimension  # type: ignore
    from ._models import OperationResourceServiceSpecification  # type: ignore
    from ._models import OperationStatus  # type: ignore
    from ._models import PostBackupResponse  # type: ignore
    from ._models import PostRestoreRequest  # type: ignore
    from ._models import PreRestoreRequest  # type: ignore
    from ._models import PrivateEndpoint  # type: ignore
    from ._models import PrivateEndpointConnection  # type: ignore
    from ._models import PrivateEndpointConnectionListResult  # type: ignore
    from ._models import PrivateLinkResource  # type: ignore
    from ._models import PrivateLinkResourceListResult  # type: ignore
    from ._models import PrivateLinkServiceConnectionState  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import RecallActionParameters  # type: ignore
    from ._models import RegisteredServer  # type: ignore
    from ._models import RegisteredServerArray  # type: ignore
    from ._models import RegisteredServerCreateParameters  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourcesMoveInfo  # type: ignore
    from ._models import RestoreFileSpec  # type: ignore
    from ._models import ServerEndpoint  # type: ignore
    from ._models import ServerEndpointArray  # type: ignore
    from ._models import ServerEndpointBackgroundDataDownloadActivity  # type: ignore
    from ._models import ServerEndpointCloudTieringStatus  # type: ignore
    from ._models import ServerEndpointCreateParameters  # type: ignore
    from ._models import ServerEndpointFilesNotSyncingError  # type: ignore
    from ._models import ServerEndpointRecallError  # type: ignore
    from ._models import ServerEndpointRecallStatus  # type: ignore
    from ._models import ServerEndpointSyncActivityStatus  # type: ignore
    from ._models import ServerEndpointSyncSessionStatus  # type: ignore
    from ._models import ServerEndpointSyncStatus  # type: ignore
    from ._models import ServerEndpointUpdateParameters  # type: ignore
    from ._models import StorageSyncApiError  # type: ignore
    from ._models import StorageSyncError  # type: ignore
    from ._models import StorageSyncErrorDetails  # type: ignore
    from ._models import StorageSyncInnerErrorDetails  # type: ignore
    from ._models import StorageSyncService  # type: ignore
    from ._models import StorageSyncServiceArray  # type: ignore
    from ._models import StorageSyncServiceCreateParameters  # type: ignore
    from ._models import StorageSyncServiceUpdateParameters  # type: ignore
    from ._models import SubscriptionState  # type: ignore
    from ._models import SyncGroup  # type: ignore
    from ._models import SyncGroupArray  # type: ignore
    from ._models import SyncGroupCreateParameters  # type: ignore
    from ._models import TrackedResource  # type: ignore
    from ._models import TriggerChangeDetectionParameters  # type: ignore
    from ._models import TriggerRolloverRequest  # type: ignore
    from ._models import Workflow  # type: ignore
    from ._models import WorkflowArray  # type: ignore

from ._microsoft_storage_sync_enums import (
    ChangeDetectionMode,
    FeatureStatus,
    IncomingTrafficPolicy,
    InitialDownloadPolicy,
    InitialUploadPolicy,
    LocalCacheMode,
    NameAvailabilityReason,
    OperationDirection,
    PrivateEndpointConnectionProvisioningState,
    PrivateEndpointServiceConnectionStatus,
    ProgressType,
    Reason,
    RegisteredServerAgentVersionStatus,
    ServerEndpointHealthState,
    ServerEndpointOfflineDataTransferState,
    ServerEndpointSyncActivityState,
    ServerEndpointSyncMode,
    WorkflowStatus,
)

__all__ = [
    'BackupRequest',
    'CheckNameAvailabilityParameters',
    'CheckNameAvailabilityResult',
    'CloudEndpoint',
    'CloudEndpointArray',
    'CloudEndpointCreateParameters',
    'CloudTieringCachePerformance',
    'CloudTieringDatePolicyStatus',
    'CloudTieringFilesNotTiering',
    'CloudTieringSpaceSavings',
    'CloudTieringVolumeFreeSpacePolicyStatus',
    'FilesNotTieringError',
    'OperationDisplayInfo',
    'OperationDisplayResource',
    'OperationEntity',
    'OperationEntityListResult',
    'OperationProperties',
    'OperationResourceMetricSpecification',
    'OperationResourceMetricSpecificationDimension',
    'OperationResourceServiceSpecification',
    'OperationStatus',
    'PostBackupResponse',
    'PostRestoreRequest',
    'PreRestoreRequest',
    'PrivateEndpoint',
    'PrivateEndpointConnection',
    'PrivateEndpointConnectionListResult',
    'PrivateLinkResource',
    'PrivateLinkResourceListResult',
    'PrivateLinkServiceConnectionState',
    'ProxyResource',
    'RecallActionParameters',
    'RegisteredServer',
    'RegisteredServerArray',
    'RegisteredServerCreateParameters',
    'Resource',
    'ResourcesMoveInfo',
    'RestoreFileSpec',
    'ServerEndpoint',
    'ServerEndpointArray',
    'ServerEndpointBackgroundDataDownloadActivity',
    'ServerEndpointCloudTieringStatus',
    'ServerEndpointCreateParameters',
    'ServerEndpointFilesNotSyncingError',
    'ServerEndpointRecallError',
    'ServerEndpointRecallStatus',
    'ServerEndpointSyncActivityStatus',
    'ServerEndpointSyncSessionStatus',
    'ServerEndpointSyncStatus',
    'ServerEndpointUpdateParameters',
    'StorageSyncApiError',
    'StorageSyncError',
    'StorageSyncErrorDetails',
    'StorageSyncInnerErrorDetails',
    'StorageSyncService',
    'StorageSyncServiceArray',
    'StorageSyncServiceCreateParameters',
    'StorageSyncServiceUpdateParameters',
    'SubscriptionState',
    'SyncGroup',
    'SyncGroupArray',
    'SyncGroupCreateParameters',
    'TrackedResource',
    'TriggerChangeDetectionParameters',
    'TriggerRolloverRequest',
    'Workflow',
    'WorkflowArray',
    'ChangeDetectionMode',
    'FeatureStatus',
    'IncomingTrafficPolicy',
    'InitialDownloadPolicy',
    'InitialUploadPolicy',
    'LocalCacheMode',
    'NameAvailabilityReason',
    'OperationDirection',
    'PrivateEndpointConnectionProvisioningState',
    'PrivateEndpointServiceConnectionStatus',
    'ProgressType',
    'Reason',
    'RegisteredServerAgentVersionStatus',
    'ServerEndpointHealthState',
    'ServerEndpointOfflineDataTransferState',
    'ServerEndpointSyncActivityState',
    'ServerEndpointSyncMode',
    'WorkflowStatus',
]
