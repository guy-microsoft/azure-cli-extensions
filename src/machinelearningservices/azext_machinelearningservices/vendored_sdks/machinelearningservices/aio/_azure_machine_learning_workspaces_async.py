# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import AzureMachineLearningWorkspacesConfiguration
from .operations_async import OperationOperations
from .operations_async import WorkspaceOperations
from .operations_async import WorkspaceFeatureOperations
from .operations_async import UsageOperations
from .operations_async import VirtualMachineSizeOperations
from .operations_async import QuotaOperations
from .operations_async import MachineLearningComputeOperations
from .operations_async import AzureMachineLearningWorkspacesOperationsMixin
from .operations_async import PrivateEndpointConnectionOperations
from .operations_async import PrivateLinkResourceOperations
from .. import models


class AzureMachineLearningWorkspaces(AzureMachineLearningWorkspacesOperationsMixin):
    """These APIs allow end users to operate on Azure Machine Learning Workspace resources.

    :ivar operation: OperationOperations operations
    :vartype operation: azure.mgmt.machinelearningservices.aio.operations_async.OperationOperations
    :ivar workspace: WorkspaceOperations operations
    :vartype workspace: azure.mgmt.machinelearningservices.aio.operations_async.WorkspaceOperations
    :ivar workspace_feature: WorkspaceFeatureOperations operations
    :vartype workspace_feature: azure.mgmt.machinelearningservices.aio.operations_async.WorkspaceFeatureOperations
    :ivar usage: UsageOperations operations
    :vartype usage: azure.mgmt.machinelearningservices.aio.operations_async.UsageOperations
    :ivar virtual_machine_size: VirtualMachineSizeOperations operations
    :vartype virtual_machine_size: azure.mgmt.machinelearningservices.aio.operations_async.VirtualMachineSizeOperations
    :ivar quota: QuotaOperations operations
    :vartype quota: azure.mgmt.machinelearningservices.aio.operations_async.QuotaOperations
    :ivar machine_learning_compute: MachineLearningComputeOperations operations
    :vartype machine_learning_compute: azure.mgmt.machinelearningservices.aio.operations_async.MachineLearningComputeOperations
    :ivar private_endpoint_connection: PrivateEndpointConnectionOperations operations
    :vartype private_endpoint_connection: azure.mgmt.machinelearningservices.aio.operations_async.PrivateEndpointConnectionOperations
    :ivar private_link_resource: PrivateLinkResourceOperations operations
    :vartype private_link_resource: azure.mgmt.machinelearningservices.aio.operations_async.PrivateLinkResourceOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param str base_url: Service URL
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
        self._config = AzureMachineLearningWorkspacesConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace = WorkspaceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_feature = WorkspaceFeatureOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usage = UsageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_size = VirtualMachineSizeOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.quota = QuotaOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.machine_learning_compute = MachineLearningComputeOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connection = PrivateEndpointConnectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resource = PrivateLinkResourceOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AzureMachineLearningWorkspaces":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
