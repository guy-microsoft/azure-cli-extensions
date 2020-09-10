# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import DataBoxEdgeManagementClientConfiguration
from .operations import OperationOperations
from .operations import DeviceOperations
from .operations import AlertOperations
from .operations import BandwidthScheduleOperations
from .operations import JobOperations
from .operations import NodeOperations
from .operations import OperationStatusOperations
from .operations import OrderOperations
from .operations import RoleOperations
from .operations import ShareOperations
from .operations import StorageAccountCredentialsOperations
from .operations import StorageAccountOperations
from .operations import ContainerOperations
from .operations import TriggerOperations
from .operations import UserOperations
from .operations import SkuOperations
from . import models


class DataBoxEdgeManagementClient(object):
    """DataBoxEdgeManagementClient.

    :ivar operation: OperationOperations operations
    :vartype operation: data_box_edge_management_client.operations.OperationOperations
    :ivar device: DeviceOperations operations
    :vartype device: data_box_edge_management_client.operations.DeviceOperations
    :ivar alert: AlertOperations operations
    :vartype alert: data_box_edge_management_client.operations.AlertOperations
    :ivar bandwidth_schedule: BandwidthScheduleOperations operations
    :vartype bandwidth_schedule: data_box_edge_management_client.operations.BandwidthScheduleOperations
    :ivar job: JobOperations operations
    :vartype job: data_box_edge_management_client.operations.JobOperations
    :ivar node: NodeOperations operations
    :vartype node: data_box_edge_management_client.operations.NodeOperations
    :ivar operation_status: OperationStatusOperations operations
    :vartype operation_status: data_box_edge_management_client.operations.OperationStatusOperations
    :ivar order: OrderOperations operations
    :vartype order: data_box_edge_management_client.operations.OrderOperations
    :ivar role: RoleOperations operations
    :vartype role: data_box_edge_management_client.operations.RoleOperations
    :ivar share: ShareOperations operations
    :vartype share: data_box_edge_management_client.operations.ShareOperations
    :ivar storage_account_credentials: StorageAccountCredentialsOperations operations
    :vartype storage_account_credentials: data_box_edge_management_client.operations.StorageAccountCredentialsOperations
    :ivar storage_account: StorageAccountOperations operations
    :vartype storage_account: data_box_edge_management_client.operations.StorageAccountOperations
    :ivar container: ContainerOperations operations
    :vartype container: data_box_edge_management_client.operations.ContainerOperations
    :ivar trigger: TriggerOperations operations
    :vartype trigger: data_box_edge_management_client.operations.TriggerOperations
    :ivar user: UserOperations operations
    :vartype user: data_box_edge_management_client.operations.UserOperations
    :ivar sku: SkuOperations operations
    :vartype sku: data_box_edge_management_client.operations.SkuOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
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
        self._config = DataBoxEdgeManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device = DeviceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.alert = AlertOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.bandwidth_schedule = BandwidthScheduleOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.job = JobOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.node = NodeOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation_status = OperationStatusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.order = OrderOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.role = RoleOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.share = ShareOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.storage_account_credentials = StorageAccountCredentialsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.storage_account = StorageAccountOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.container = ContainerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.trigger = TriggerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user = UserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sku = SkuOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> DataBoxEdgeManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
