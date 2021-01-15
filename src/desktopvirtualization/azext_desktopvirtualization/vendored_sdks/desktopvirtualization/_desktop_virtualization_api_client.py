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

from ._configuration import DesktopVirtualizationAPIClientConfiguration
from .operations import Operations
from .operations import WorkspacesOperations
from .operations import ScalingPlansOperations
from .operations import ApplicationGroupsOperations
from .operations import StartMenuItemsOperations
from .operations import ApplicationsOperations
from .operations import DesktopsOperations
from .operations import HostPoolsOperations
from .operations import UserSessionsOperations
from .operations import SessionHostsOperations
from .operations import MsixPackagesOperations
from .operations import MsixImagesOperations
from . import models


class DesktopVirtualizationAPIClient(object):
    """DesktopVirtualizationAPIClient.

    :ivar operations: Operations operations
    :vartype operations: desktop_virtualization_api_client.operations.Operations
    :ivar workspaces: WorkspacesOperations operations
    :vartype workspaces: desktop_virtualization_api_client.operations.WorkspacesOperations
    :ivar scaling_plans: ScalingPlansOperations operations
    :vartype scaling_plans: desktop_virtualization_api_client.operations.ScalingPlansOperations
    :ivar application_groups: ApplicationGroupsOperations operations
    :vartype application_groups: desktop_virtualization_api_client.operations.ApplicationGroupsOperations
    :ivar start_menu_items: StartMenuItemsOperations operations
    :vartype start_menu_items: desktop_virtualization_api_client.operations.StartMenuItemsOperations
    :ivar applications: ApplicationsOperations operations
    :vartype applications: desktop_virtualization_api_client.operations.ApplicationsOperations
    :ivar desktops: DesktopsOperations operations
    :vartype desktops: desktop_virtualization_api_client.operations.DesktopsOperations
    :ivar host_pools: HostPoolsOperations operations
    :vartype host_pools: desktop_virtualization_api_client.operations.HostPoolsOperations
    :ivar user_sessions: UserSessionsOperations operations
    :vartype user_sessions: desktop_virtualization_api_client.operations.UserSessionsOperations
    :ivar session_hosts: SessionHostsOperations operations
    :vartype session_hosts: desktop_virtualization_api_client.operations.SessionHostsOperations
    :ivar msix_packages: MsixPackagesOperations operations
    :vartype msix_packages: desktop_virtualization_api_client.operations.MsixPackagesOperations
    :ivar msix_images: MsixImagesOperations operations
    :vartype msix_images: desktop_virtualization_api_client.operations.MsixImagesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription.
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
        self._config = DesktopVirtualizationAPIClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspaces = WorkspacesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.scaling_plans = ScalingPlansOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.application_groups = ApplicationGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.start_menu_items = StartMenuItemsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.applications = ApplicationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.desktops = DesktopsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.host_pools = HostPoolsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_sessions = UserSessionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.session_hosts = SessionHostsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.msix_packages = MsixPackagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.msix_images = MsixImagesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> DesktopVirtualizationAPIClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
