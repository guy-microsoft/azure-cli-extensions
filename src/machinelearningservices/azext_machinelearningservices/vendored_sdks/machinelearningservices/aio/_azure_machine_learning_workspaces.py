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

from ._configuration import AzureMachineLearningWorkspacesConfiguration
from .operations import Operations
from .operations import WorkspacesOperations
from .operations import WorkspaceFeaturesOperations
from .operations import UsagesOperations
from .operations import VirtualMachineSizesOperations
from .operations import QuotasOperations
from .operations import MachineLearningComputeOperations
from .operations import AzureMachineLearningWorkspacesOperationsMixin
from .operations import PrivateEndpointConnectionsOperations
from .operations import PrivateLinkResourcesOperations
from .operations import LinkedServicesOperations
from .operations import MachineLearningServiceOperations
from .operations import NotebooksOperations
from .operations import WorkspaceConnectionsOperations
from .operations import CodeContainersOperations
from .operations import CodeVersionsOperations
from .operations import DataContainersOperations
from .operations import DatastoresOperations
from .operations import DataVersionsOperations
from .operations import EnvironmentContainersOperations
from .operations import EnvironmentSpecificationVersionsOperations
from .operations import JobsOperations
from .operations import LabelingJobsOperations
from .operations import ModelContainersOperations
from .operations import ModelVersionsOperations
from .. import models


class AzureMachineLearningWorkspaces(AzureMachineLearningWorkspacesOperationsMixin):
    """These APIs allow end users to operate on Azure Machine Learning Workspace resources.

    :ivar operations: Operations operations
    :vartype operations: azure_machine_learning_workspaces.aio.operations.Operations
    :ivar workspaces: WorkspacesOperations operations
    :vartype workspaces: azure_machine_learning_workspaces.aio.operations.WorkspacesOperations
    :ivar workspace_features: WorkspaceFeaturesOperations operations
    :vartype workspace_features: azure_machine_learning_workspaces.aio.operations.WorkspaceFeaturesOperations
    :ivar usages: UsagesOperations operations
    :vartype usages: azure_machine_learning_workspaces.aio.operations.UsagesOperations
    :ivar virtual_machine_sizes: VirtualMachineSizesOperations operations
    :vartype virtual_machine_sizes: azure_machine_learning_workspaces.aio.operations.VirtualMachineSizesOperations
    :ivar quotas: QuotasOperations operations
    :vartype quotas: azure_machine_learning_workspaces.aio.operations.QuotasOperations
    :ivar machine_learning_compute: MachineLearningComputeOperations operations
    :vartype machine_learning_compute: azure_machine_learning_workspaces.aio.operations.MachineLearningComputeOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections: azure_machine_learning_workspaces.aio.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: azure_machine_learning_workspaces.aio.operations.PrivateLinkResourcesOperations
    :ivar linked_services: LinkedServicesOperations operations
    :vartype linked_services: azure_machine_learning_workspaces.aio.operations.LinkedServicesOperations
    :ivar machine_learning_service: MachineLearningServiceOperations operations
    :vartype machine_learning_service: azure_machine_learning_workspaces.aio.operations.MachineLearningServiceOperations
    :ivar notebooks: NotebooksOperations operations
    :vartype notebooks: azure_machine_learning_workspaces.aio.operations.NotebooksOperations
    :ivar workspace_connections: WorkspaceConnectionsOperations operations
    :vartype workspace_connections: azure_machine_learning_workspaces.aio.operations.WorkspaceConnectionsOperations
    :ivar code_containers: CodeContainersOperations operations
    :vartype code_containers: azure_machine_learning_workspaces.aio.operations.CodeContainersOperations
    :ivar code_versions: CodeVersionsOperations operations
    :vartype code_versions: azure_machine_learning_workspaces.aio.operations.CodeVersionsOperations
    :ivar data_containers: DataContainersOperations operations
    :vartype data_containers: azure_machine_learning_workspaces.aio.operations.DataContainersOperations
    :ivar datastores: DatastoresOperations operations
    :vartype datastores: azure_machine_learning_workspaces.aio.operations.DatastoresOperations
    :ivar data_versions: DataVersionsOperations operations
    :vartype data_versions: azure_machine_learning_workspaces.aio.operations.DataVersionsOperations
    :ivar environment_containers: EnvironmentContainersOperations operations
    :vartype environment_containers: azure_machine_learning_workspaces.aio.operations.EnvironmentContainersOperations
    :ivar environment_specification_versions: EnvironmentSpecificationVersionsOperations operations
    :vartype environment_specification_versions: azure_machine_learning_workspaces.aio.operations.EnvironmentSpecificationVersionsOperations
    :ivar jobs: JobsOperations operations
    :vartype jobs: azure_machine_learning_workspaces.aio.operations.JobsOperations
    :ivar labeling_jobs: LabelingJobsOperations operations
    :vartype labeling_jobs: azure_machine_learning_workspaces.aio.operations.LabelingJobsOperations
    :ivar model_containers: ModelContainersOperations operations
    :vartype model_containers: azure_machine_learning_workspaces.aio.operations.ModelContainersOperations
    :ivar model_versions: ModelVersionsOperations operations
    :vartype model_versions: azure_machine_learning_workspaces.aio.operations.ModelVersionsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Azure subscription identifier.
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
        self._config = AzureMachineLearningWorkspacesConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspaces = WorkspacesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_features = WorkspaceFeaturesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_sizes = VirtualMachineSizesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.quotas = QuotasOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.machine_learning_compute = MachineLearningComputeOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.linked_services = LinkedServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.machine_learning_service = MachineLearningServiceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.notebooks = NotebooksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_connections = WorkspaceConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.code_containers = CodeContainersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.code_versions = CodeVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_containers = DataContainersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.datastores = DatastoresOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_versions = DataVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.environment_containers = EnvironmentContainersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.environment_specification_versions = EnvironmentSpecificationVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.jobs = JobsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.labeling_jobs = LabelingJobsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.model_containers = ModelContainersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.model_versions = ModelVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AzureMachineLearningWorkspaces":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
