# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ReferenceDataSetOperations:
    """ReferenceDataSetOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~time_series_insights_client.models
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

    async def create_or_update(
        self,
        resource_group_name: str,
        environment_name: str,
        reference_data_set_name: str,
        location: str,
        key_properties: List["models.ReferenceDataSetKeyProperty"],
        tags: Optional[Dict[str, str]] = None,
        data_string_comparison_behavior: Optional[Union[str, "models.DataStringComparisonBehavior"]] = None,
        **kwargs
    ) -> "models.ReferenceDataSetResource":
        """Create or update a reference data set in the specified environment.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param environment_name: The name of the Time Series Insights environment associated with the
         specified resource group.
        :type environment_name: str
        :param reference_data_set_name: Name of the reference data set.
        :type reference_data_set_name: str
        :param location: The location of the resource.
        :type location: str
        :param key_properties: The list of key properties for the reference data set.
        :type key_properties: list[~time_series_insights_client.models.ReferenceDataSetKeyProperty]
        :param tags: Key-value pairs of additional properties for the resource.
        :type tags: dict[str, str]
        :param data_string_comparison_behavior: The reference data set key comparison behavior can be
         set using this property. By default, the value is 'Ordinal' - which means case sensitive key
         comparison will be performed while joining reference data with events or while adding new
         reference data. When 'OrdinalIgnoreCase' is set, case insensitive comparison will be used.
        :type data_string_comparison_behavior: str or ~time_series_insights_client.models.DataStringComparisonBehavior
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ReferenceDataSetResource, or the result of cls(response)
        :rtype: ~time_series_insights_client.models.ReferenceDataSetResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ReferenceDataSetResource"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        parameters = models.ReferenceDataSetCreateOrUpdateParameters(location=location, tags=tags, key_properties=key_properties, data_string_comparison_behavior=data_string_comparison_behavior)
        api_version = "2020-05-15"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'environmentName': self._serialize.url("environment_name", environment_name, 'str'),
            'referenceDataSetName': self._serialize.url("reference_data_set_name", reference_data_set_name, 'str', max_length=63, min_length=3, pattern=r'^[A-Za-z0-9]'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(parameters, 'ReferenceDataSetCreateOrUpdateParameters')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('ReferenceDataSetResource', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('ReferenceDataSetResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/referenceDataSets/{referenceDataSetName}'}  # type: ignore

    async def get(
        self,
        resource_group_name: str,
        environment_name: str,
        reference_data_set_name: str,
        **kwargs
    ) -> "models.ReferenceDataSetResource":
        """Gets the reference data set with the specified name in the specified environment.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param environment_name: The name of the Time Series Insights environment associated with the
         specified resource group.
        :type environment_name: str
        :param reference_data_set_name: The name of the Time Series Insights reference data set
         associated with the specified environment.
        :type reference_data_set_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ReferenceDataSetResource, or the result of cls(response)
        :rtype: ~time_series_insights_client.models.ReferenceDataSetResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ReferenceDataSetResource"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-05-15"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'environmentName': self._serialize.url("environment_name", environment_name, 'str'),
            'referenceDataSetName': self._serialize.url("reference_data_set_name", reference_data_set_name, 'str'),
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ReferenceDataSetResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/referenceDataSets/{referenceDataSetName}'}  # type: ignore

    async def update(
        self,
        resource_group_name: str,
        environment_name: str,
        reference_data_set_name: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> "models.ReferenceDataSetResource":
        """Updates the reference data set with the specified name in the specified subscription, resource
        group, and environment.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param environment_name: The name of the Time Series Insights environment associated with the
         specified resource group.
        :type environment_name: str
        :param reference_data_set_name: The name of the Time Series Insights reference data set
         associated with the specified environment.
        :type reference_data_set_name: str
        :param tags: Key-value pairs of additional properties for the reference data set.
        :type tags: dict[str, str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ReferenceDataSetResource, or the result of cls(response)
        :rtype: ~time_series_insights_client.models.ReferenceDataSetResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ReferenceDataSetResource"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        reference_data_set_update_parameters = models.ReferenceDataSetUpdateParameters(tags=tags)
        api_version = "2020-05-15"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'environmentName': self._serialize.url("environment_name", environment_name, 'str'),
            'referenceDataSetName': self._serialize.url("reference_data_set_name", reference_data_set_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(reference_data_set_update_parameters, 'ReferenceDataSetUpdateParameters')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ReferenceDataSetResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/referenceDataSets/{referenceDataSetName}'}  # type: ignore

    async def delete(
        self,
        resource_group_name: str,
        environment_name: str,
        reference_data_set_name: str,
        **kwargs
    ) -> None:
        """Deletes the reference data set with the specified name in the specified subscription, resource
        group, and environment.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param environment_name: The name of the Time Series Insights environment associated with the
         specified resource group.
        :type environment_name: str
        :param reference_data_set_name: The name of the Time Series Insights reference data set
         associated with the specified environment.
        :type reference_data_set_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-05-15"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'environmentName': self._serialize.url("environment_name", environment_name, 'str'),
            'referenceDataSetName': self._serialize.url("reference_data_set_name", reference_data_set_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/referenceDataSets/{referenceDataSetName}'}  # type: ignore

    async def list_by_environment(
        self,
        resource_group_name: str,
        environment_name: str,
        **kwargs
    ) -> "models.ReferenceDataSetListResponse":
        """Lists all the available reference data sets associated with the subscription and within the
        specified resource group and environment.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param environment_name: The name of the Time Series Insights environment associated with the
         specified resource group.
        :type environment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ReferenceDataSetListResponse, or the result of cls(response)
        :rtype: ~time_series_insights_client.models.ReferenceDataSetListResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ReferenceDataSetListResponse"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-05-15"

        # Construct URL
        url = self.list_by_environment.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'environmentName': self._serialize.url("environment_name", environment_name, 'str'),
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ReferenceDataSetListResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    list_by_environment.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/referenceDataSets'}  # type: ignore
