# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class GuestConfigurationHcrpAssignmentReportOperations:
    """GuestConfigurationHcrpAssignmentReportOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~guest_configuration_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def list(
        self,
        resource_group_name: str,
        guest_configuration_assignment_name: str,
        machine_name: str,
        **kwargs
    ) -> "models.GuestConfigurationAssignmentReportList":
        """List all reports for the guest configuration assignment, latest report first.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param guest_configuration_assignment_name: The guest configuration assignment name.
        :type guest_configuration_assignment_name: str
        :param machine_name: The name of the ARC machine.
        :type machine_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GuestConfigurationAssignmentReportList, or the result of cls(response)
        :rtype: ~guest_configuration_client.models.GuestConfigurationAssignmentReportList
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.GuestConfigurationAssignmentReportList"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-06-25"

        # Construct URL
        url = self.list.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', pattern=r'^[-\w\._]+$'),
            'guestConfigurationAssignmentName': self._serialize.url("guest_configuration_assignment_name", guest_configuration_assignment_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'machineName': self._serialize.url("machine_name", machine_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('GuestConfigurationAssignmentReportList', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/machines/{machineName}/providers/Microsoft.GuestConfiguration/guestConfigurationAssignments/{guestConfigurationAssignmentName}/reports'}  # type: ignore

    async def get(
        self,
        resource_group_name: str,
        guest_configuration_assignment_name: str,
        report_id: str,
        machine_name: str,
        **kwargs
    ) -> "models.GuestConfigurationAssignmentReport":
        """Get a report for the guest configuration assignment, by reportId.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param guest_configuration_assignment_name: The guest configuration assignment name.
        :type guest_configuration_assignment_name: str
        :param report_id: The GUID for the guest configuration assignment report.
        :type report_id: str
        :param machine_name: The name of the ARC machine.
        :type machine_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GuestConfigurationAssignmentReport, or the result of cls(response)
        :rtype: ~guest_configuration_client.models.GuestConfigurationAssignmentReport
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.GuestConfigurationAssignmentReport"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-06-25"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', pattern=r'^[-\w\._]+$'),
            'guestConfigurationAssignmentName': self._serialize.url("guest_configuration_assignment_name", guest_configuration_assignment_name, 'str'),
            'reportId': self._serialize.url("report_id", report_id, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'machineName': self._serialize.url("machine_name", machine_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('GuestConfigurationAssignmentReport', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/machines/{machineName}/providers/Microsoft.GuestConfiguration/guestConfigurationAssignments/{guestConfigurationAssignmentName}/reports/{reportId}'}  # type: ignore
