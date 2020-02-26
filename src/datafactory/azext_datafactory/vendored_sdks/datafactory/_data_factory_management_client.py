# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6237, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.core import PipelineClient
from msrest import Deserializer, Serializer

from ._configuration import DataFactoryManagementClientConfiguration
from .operations import Operations
from .operations import FactoriesOperations
from .operations import ExposureControlOperations
from .operations import IntegrationRuntimesOperations
from .operations import IntegrationRuntimeObjectMetadataOperations
from .operations import IntegrationRuntimeNodesOperations
from .operations import LinkedServicesOperations
from .operations import DatasetsOperations
from .operations import PipelinesOperations
from .operations import PipelineRunsOperations
from .operations import ActivityRunsOperations
from .operations import TriggersOperations
from .operations import TriggerRunsOperations
from .operations import DataFlowsOperations
from .operations import DataFlowDebugSessionOperations
from . import models


class DataFactoryManagementClient(object):
    """The Azure Data Factory V2 management API provides a RESTful set of web services that interact with Azure Data Factory V2 services.

    :ivar operations: Operations operations
    :vartype operations: data_factory_management_client.operations.Operations
    :ivar factories: FactoriesOperations operations
    :vartype factories: data_factory_management_client.operations.FactoriesOperations
    :ivar exposure_control: ExposureControlOperations operations
    :vartype exposure_control: data_factory_management_client.operations.ExposureControlOperations
    :ivar integration_runtimes: IntegrationRuntimesOperations operations
    :vartype integration_runtimes: data_factory_management_client.operations.IntegrationRuntimesOperations
    :ivar integration_runtime_object_metadata: IntegrationRuntimeObjectMetadataOperations operations
    :vartype integration_runtime_object_metadata: data_factory_management_client.operations.IntegrationRuntimeObjectMetadataOperations
    :ivar integration_runtime_nodes: IntegrationRuntimeNodesOperations operations
    :vartype integration_runtime_nodes: data_factory_management_client.operations.IntegrationRuntimeNodesOperations
    :ivar linked_services: LinkedServicesOperations operations
    :vartype linked_services: data_factory_management_client.operations.LinkedServicesOperations
    :ivar datasets: DatasetsOperations operations
    :vartype datasets: data_factory_management_client.operations.DatasetsOperations
    :ivar pipelines: PipelinesOperations operations
    :vartype pipelines: data_factory_management_client.operations.PipelinesOperations
    :ivar pipeline_runs: PipelineRunsOperations operations
    :vartype pipeline_runs: data_factory_management_client.operations.PipelineRunsOperations
    :ivar activity_runs: ActivityRunsOperations operations
    :vartype activity_runs: data_factory_management_client.operations.ActivityRunsOperations
    :ivar triggers: TriggersOperations operations
    :vartype triggers: data_factory_management_client.operations.TriggersOperations
    :ivar trigger_runs: TriggerRunsOperations operations
    :vartype trigger_runs: data_factory_management_client.operations.TriggerRunsOperations
    :ivar data_flows: DataFlowsOperations operations
    :vartype data_flows: data_factory_management_client.operations.DataFlowsOperations
    :ivar data_flow_debug_session: DataFlowDebugSessionOperations operations
    :vartype data_flow_debug_session: data_factory_management_client.operations.DataFlowDebugSessionOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.TokenCredential
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = DataFactoryManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.factories = FactoriesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.exposure_control = ExposureControlOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtimes = IntegrationRuntimesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_object_metadata = IntegrationRuntimeObjectMetadataOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_nodes = IntegrationRuntimeNodesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.linked_services = LinkedServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.datasets = DatasetsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.pipelines = PipelinesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.pipeline_runs = PipelineRunsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.activity_runs = ActivityRunsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.triggers = TriggersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.trigger_runs = TriggerRunsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_flows = DataFlowsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_flow_debug_session = DataFlowDebugSessionOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> DataFactoryManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)