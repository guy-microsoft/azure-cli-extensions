# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ServiceOperations:
    """ServiceOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~data_box_management_client.models
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

    def list_available_sku_by_resource_group(
        self,
        resource_group_name: str,
        location: str,
        transfer_type: Union[str, "models.TransferType"],
        country: str,
        available_sku_request_location: str,
        sku_names: Optional[List[Union[str, "models.SkuName"]]] = None,
        **kwargs
    ) -> AsyncIterable["models.AvailableSkusResult"]:
        """This method provides the list of available skus for the given subscription, resource group and
        location.

        :param resource_group_name: The Resource Group Name.
        :type resource_group_name: str
        :param location: The location of the resource.
        :type location: str
        :param transfer_type: Type of the transfer.
        :type transfer_type: str or ~data_box_management_client.models.TransferType
        :param country: ISO country code. Country for hardware shipment. For codes check:
         https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements.
        :type country: str
        :param available_sku_request_location: Location for data transfer. For locations check:
         https://management.azure.com/subscriptions/SUBSCRIPTIONID/locations?api-version=2018-01-01.
        :type available_sku_request_location: str
        :param sku_names: Sku Names to filter for available skus.
        :type sku_names: list[str or ~data_box_management_client.models.SkuName]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either AvailableSkusResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~data_box_management_client.models.AvailableSkusResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.AvailableSkusResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        available_sku_request = models.AvailableSkuRequest(transfer_type=transfer_type, country=country, location=available_sku_request_location, sku_names=sku_names)
        api_version = "2020-11-01"
        content_type = "application/json"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_available_sku_by_resource_group.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'location': self._serialize.url("location", location, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                body_content_kwargs = {}  # type: Dict[str, Any]
                body_content = self._serialize.body(available_sku_request, 'AvailableSkuRequest')
                body_content_kwargs['content'] = body_content
                request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                body_content_kwargs = {}  # type: Dict[str, Any]
                body_content = self._serialize.body(available_sku_request, 'AvailableSkuRequest')
                body_content_kwargs['content'] = body_content
                request = self._client.get(url, query_parameters, header_parameters, **body_content_kwargs)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('AvailableSkusResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.ApiError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_available_sku_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/locations/{location}/availableSkus'}  # type: ignore

    async def validate_address(
        self,
        location: str,
        validation_type: Union[str, "models.ValidationInputDiscriminator"],
        shipping_address: "models.ShippingAddress",
        device_type: Union[str, "models.SkuName"],
        preferred_shipment_type: Optional[Union[str, "models.TransportShipmentTypes"]] = None,
        **kwargs
    ) -> "models.AddressValidationOutput":
        """[DEPRECATED NOTICE: This operation will soon be removed]. This method validates the customer
        shipping address and provide alternate addresses if any.

        :param location: The location of the resource.
        :type location: str
        :param validation_type: Identifies the type of validation request.
        :type validation_type: str or ~data_box_management_client.models.ValidationInputDiscriminator
        :param shipping_address: Shipping address of the customer.
        :type shipping_address: ~data_box_management_client.models.ShippingAddress
        :param device_type: Device type to be used for the job.
        :type device_type: str or ~data_box_management_client.models.SkuName
        :param preferred_shipment_type: Indicates Shipment Logistics type that the customer preferred.
        :type preferred_shipment_type: str or ~data_box_management_client.models.TransportShipmentTypes
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AddressValidationOutput, or the result of cls(response)
        :rtype: ~data_box_management_client.models.AddressValidationOutput
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.AddressValidationOutput"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        validate_address = models.ValidateAddress(validation_type=validation_type, shipping_address=shipping_address, device_type=device_type, preferred_shipment_type=preferred_shipment_type)
        api_version = "2020-11-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.validate_address.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'location': self._serialize.url("location", location, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(validate_address, 'ValidateAddress')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ApiError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AddressValidationOutput', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    validate_address.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DataBox/locations/{location}/validateAddress'}  # type: ignore

    async def validate_input_by_resource_group(
        self,
        resource_group_name: str,
        location: str,
        validation_request: "models.ValidationRequest",
        **kwargs
    ) -> "models.ValidationResponse":
        """This method does all necessary pre-job creation validation under resource group.

        :param resource_group_name: The Resource Group Name.
        :type resource_group_name: str
        :param location: The location of the resource.
        :type location: str
        :param validation_request: Inputs of the customer.
        :type validation_request: ~data_box_management_client.models.ValidationRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ValidationResponse, or the result of cls(response)
        :rtype: ~data_box_management_client.models.ValidationResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ValidationResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-11-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.validate_input_by_resource_group.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'location': self._serialize.url("location", location, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(validation_request, 'ValidationRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ApiError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ValidationResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    validate_input_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/locations/{location}/validateInputs'}  # type: ignore

    async def validate_input(
        self,
        location: str,
        validation_request: "models.ValidationRequest",
        **kwargs
    ) -> "models.ValidationResponse":
        """This method does all necessary pre-job creation validation under subscription.

        :param location: The location of the resource.
        :type location: str
        :param validation_request: Inputs of the customer.
        :type validation_request: ~data_box_management_client.models.ValidationRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ValidationResponse, or the result of cls(response)
        :rtype: ~data_box_management_client.models.ValidationResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ValidationResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-11-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.validate_input.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'location': self._serialize.url("location", location, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(validation_request, 'ValidationRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ApiError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ValidationResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    validate_input.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DataBox/locations/{location}/validateInputs'}  # type: ignore

    async def region_configuration(
        self,
        location: str,
        schedule_availability_request: Optional["models.ScheduleAvailabilityRequest"] = None,
        sku_name: Optional[Union[str, "models.SkuName"]] = None,
        **kwargs
    ) -> "models.RegionConfigurationResponse":
        """This API provides configuration details specific to given region/location at Subscription
        level.

        :param location: The location of the resource.
        :type location: str
        :param schedule_availability_request: Request body to get the availability for scheduling
         orders.
        :type schedule_availability_request: ~data_box_management_client.models.ScheduleAvailabilityRequest
        :param sku_name: Type of the device.
        :type sku_name: str or ~data_box_management_client.models.SkuName
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RegionConfigurationResponse, or the result of cls(response)
        :rtype: ~data_box_management_client.models.RegionConfigurationResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.RegionConfigurationResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        region_configuration_request = models.RegionConfigurationRequest(schedule_availability_request=schedule_availability_request, sku_name=sku_name)
        api_version = "2020-11-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.region_configuration.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'location': self._serialize.url("location", location, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(region_configuration_request, 'RegionConfigurationRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ApiError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('RegionConfigurationResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    region_configuration.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DataBox/locations/{location}/regionConfiguration'}  # type: ignore

    async def region_configuration_by_resource_group(
        self,
        resource_group_name: str,
        location: str,
        schedule_availability_request: Optional["models.ScheduleAvailabilityRequest"] = None,
        sku_name: Optional[Union[str, "models.SkuName"]] = None,
        **kwargs
    ) -> "models.RegionConfigurationResponse":
        """This API provides configuration details specific to given region/location at Resource group
        level.

        :param resource_group_name: The Resource Group Name.
        :type resource_group_name: str
        :param location: The location of the resource.
        :type location: str
        :param schedule_availability_request: Request body to get the availability for scheduling
         orders.
        :type schedule_availability_request: ~data_box_management_client.models.ScheduleAvailabilityRequest
        :param sku_name: Type of the device.
        :type sku_name: str or ~data_box_management_client.models.SkuName
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RegionConfigurationResponse, or the result of cls(response)
        :rtype: ~data_box_management_client.models.RegionConfigurationResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.RegionConfigurationResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        region_configuration_request = models.RegionConfigurationRequest(schedule_availability_request=schedule_availability_request, sku_name=sku_name)
        api_version = "2020-11-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.region_configuration_by_resource_group.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'location': self._serialize.url("location", location, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(region_configuration_request, 'RegionConfigurationRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ApiError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('RegionConfigurationResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    region_configuration_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/locations/{location}/regionConfiguration'}  # type: ignore
