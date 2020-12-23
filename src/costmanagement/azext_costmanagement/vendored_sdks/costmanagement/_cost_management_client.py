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

from ._configuration import CostManagementClientConfiguration
from .operations import ViewOperations
from .operations import AlertOperations
from .operations import ForecastOperations
from .operations import DimensionOperations
from .operations import QueryOperations
from .operations import OperationOperations
from .operations import ExportOperations
from . import models


class CostManagementClient(object):
    """CostManagementClient.

    :ivar view: ViewOperations operations
    :vartype view: cost_management_client.operations.ViewOperations
    :ivar alert: AlertOperations operations
    :vartype alert: cost_management_client.operations.AlertOperations
    :ivar forecast: ForecastOperations operations
    :vartype forecast: cost_management_client.operations.ForecastOperations
    :ivar dimension: DimensionOperations operations
    :vartype dimension: cost_management_client.operations.DimensionOperations
    :ivar query: QueryOperations operations
    :vartype query: cost_management_client.operations.QueryOperations
    :ivar operation: OperationOperations operations
    :vartype operation: cost_management_client.operations.OperationOperations
    :ivar export: ExportOperations operations
    :vartype export: cost_management_client.operations.ExportOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = CostManagementClientConfiguration(credential, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.view = ViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.alert = AlertOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.forecast = ForecastOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.dimension = DimensionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.query = QueryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.export = ExportOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> CostManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
