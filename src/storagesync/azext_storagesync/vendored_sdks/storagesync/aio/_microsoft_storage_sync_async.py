# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration_async import MicrosoftStorageSyncConfiguration
from .operations_async import OperationOperations
from .operations_async import StorageSyncServiceOperations
from .operations_async import PrivateLinkResourceOperations
from .operations_async import PrivateEndpointConnectionOperations
from .operations_async import SyncGroupOperations
from .operations_async import CloudEndpointOperations
from .operations_async import ServerEndpointOperations
from .operations_async import RegisteredServerOperations
from .operations_async import WorkflowOperations
from .operations_async import OperationStatusOperations
from .. import models


class MicrosoftStorageSync(object):
    """Microsoft Storage Sync Service API.

    :ivar operation: OperationOperations operations
    :vartype operation: microsoft_storage_sync.aio.operations_async.OperationOperations
    :ivar storage_sync_service: StorageSyncServiceOperations operations
    :vartype storage_sync_service: microsoft_storage_sync.aio.operations_async.StorageSyncServiceOperations
    :ivar private_link_resource: PrivateLinkResourceOperations operations
    :vartype private_link_resource: microsoft_storage_sync.aio.operations_async.PrivateLinkResourceOperations
    :ivar private_endpoint_connection: PrivateEndpointConnectionOperations operations
    :vartype private_endpoint_connection: microsoft_storage_sync.aio.operations_async.PrivateEndpointConnectionOperations
    :ivar sync_group: SyncGroupOperations operations
    :vartype sync_group: microsoft_storage_sync.aio.operations_async.SyncGroupOperations
    :ivar cloud_endpoint: CloudEndpointOperations operations
    :vartype cloud_endpoint: microsoft_storage_sync.aio.operations_async.CloudEndpointOperations
    :ivar server_endpoint: ServerEndpointOperations operations
    :vartype server_endpoint: microsoft_storage_sync.aio.operations_async.ServerEndpointOperations
    :ivar registered_server: RegisteredServerOperations operations
    :vartype registered_server: microsoft_storage_sync.aio.operations_async.RegisteredServerOperations
    :ivar workflow: WorkflowOperations operations
    :vartype workflow: microsoft_storage_sync.aio.operations_async.WorkflowOperations
    :ivar operation_status: OperationStatusOperations operations
    :vartype operation_status: microsoft_storage_sync.aio.operations_async.OperationStatusOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = MicrosoftStorageSyncConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.storage_sync_service = StorageSyncServiceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resource = PrivateLinkResourceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connection = PrivateEndpointConnectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sync_group = SyncGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.cloud_endpoint = CloudEndpointOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.server_endpoint = ServerEndpointOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.registered_server = RegisteredServerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow = WorkflowOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation_status = OperationStatusOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "MicrosoftStorageSync":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
