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
from .operations import ViewsOperations
from .operations import AlertsOperations
from .operations import ForecastOperations
from .operations import DimensionsOperations
from .operations import QueryOperations
from .operations import Operations
from .operations import ExportsOperations
from . import models


class CostManagementClient(object):
    """CostManagementClient.

    :ivar views: ViewsOperations operations
    :vartype views: cost_management_client.operations.ViewsOperations
    :ivar alerts: AlertsOperations operations
    :vartype alerts: cost_management_client.operations.AlertsOperations
    :ivar forecast: ForecastOperations operations
    :vartype forecast: cost_management_client.operations.ForecastOperations
    :ivar dimensions: DimensionsOperations operations
    :vartype dimensions: cost_management_client.operations.DimensionsOperations
    :ivar query: QueryOperations operations
    :vartype query: cost_management_client.operations.QueryOperations
    :ivar operations: Operations operations
    :vartype operations: cost_management_client.operations.Operations
    :ivar exports: ExportsOperations operations
    :vartype exports: cost_management_client.operations.ExportsOperations
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

        self.views = ViewsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.alerts = AlertsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.forecast = ForecastOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.dimensions = DimensionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.query = QueryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.exports = ExportsOperations(
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
