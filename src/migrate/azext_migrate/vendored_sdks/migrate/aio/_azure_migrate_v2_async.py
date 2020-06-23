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

from ._configuration_async import AzureMigrateV2Configuration
from .operations_async import ProjectOperations
from .operations_async import ProjectOperations
from .operations_async import MachineOperations
from .operations_async import GroupOperations
from .operations_async import AssessmentOperations
from .operations_async import AssessedMachineOperations
from .operations_async import HyperVCollectorOperations
from .operations_async import VMwareCollectorOperations
from .operations_async import OperationOperations
from .. import models


class AzureMigrateV2(object):
    """Assess your workloads for Azure.

    :ivar project: ProjectOperations operations
    :vartype project: azure_migrate_v2.aio.operations_async.ProjectOperations
    :ivar project: ProjectOperations operations
    :vartype project: azure_migrate_v2.aio.operations_async.ProjectOperations
    :ivar machine: MachineOperations operations
    :vartype machine: azure_migrate_v2.aio.operations_async.MachineOperations
    :ivar group: GroupOperations operations
    :vartype group: azure_migrate_v2.aio.operations_async.GroupOperations
    :ivar assessment: AssessmentOperations operations
    :vartype assessment: azure_migrate_v2.aio.operations_async.AssessmentOperations
    :ivar assessed_machine: AssessedMachineOperations operations
    :vartype assessed_machine: azure_migrate_v2.aio.operations_async.AssessedMachineOperations
    :ivar hyper_vcollector: HyperVCollectorOperations operations
    :vartype hyper_vcollector: azure_migrate_v2.aio.operations_async.HyperVCollectorOperations
    :ivar vmware_collector: VMwareCollectorOperations operations
    :vartype vmware_collector: azure_migrate_v2.aio.operations_async.VMwareCollectorOperations
    :ivar operation: OperationOperations operations
    :vartype operation: azure_migrate_v2.aio.operations_async.OperationOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Azure Subscription Id in which project was created.
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
        self._config = AzureMigrateV2Configuration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.project = ProjectOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.project = ProjectOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.machine = MachineOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group = GroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.assessment = AssessmentOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.assessed_machine = AssessedMachineOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.hyper_vcollector = HyperVCollectorOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.vmware_collector = VMwareCollectorOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AzureMigrateV2":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
