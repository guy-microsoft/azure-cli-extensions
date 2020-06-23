# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.polling import AsyncNoPolling, AsyncPollingMethod, async_poller
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class JobOperations:
    """JobOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.databox.models
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

    def list(
        self,
        skip_token: Optional[str] = None,
        **kwargs
    ) -> "models.JobResourceList":
        """Lists all the jobs available under the subscription.

        :param skip_token: $skipToken is supported on Get list of jobs, which provides the next page in
     the list of jobs.
        :type skip_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JobResourceList or the result of cls(response)
        :rtype: ~azure.mgmt.databox.models.JobResourceList
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.JobResourceList"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-09-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}  # type: Dict[str, Any]
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
            if skip_token is not None:
                query_parameters['$skipToken'] = self._serialize.query("skip_token", skip_token, 'str')

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('JobResourceList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DataBox/jobs'}

    def list_by_resource_group(
        self,
        resource_group_name: str,
        skip_token: Optional[str] = None,
        **kwargs
    ) -> "models.JobResourceList":
        """Lists all the jobs available under the given resource group.

        :param resource_group_name: The Resource Group Name.
        :type resource_group_name: str
        :param skip_token: $skipToken is supported on Get list of jobs, which provides the next page in
     the list of jobs.
        :type skip_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JobResourceList or the result of cls(response)
        :rtype: ~azure.mgmt.databox.models.JobResourceList
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.JobResourceList"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-09-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_resource_group.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}  # type: Dict[str, Any]
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
            if skip_token is not None:
                query_parameters['$skipToken'] = self._serialize.query("skip_token", skip_token, 'str')

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('JobResourceList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs'}

    async def get(
        self,
        resource_group_name: str,
        job_name: str,
        expand: Optional[str] = None,
        **kwargs
    ) -> "models.JobResource":
        """Gets information about the specified job.

        :param resource_group_name: The Resource Group Name.
        :type resource_group_name: str
        :param job_name: The name of the job Resource within the specified resource group. job names
         must be between 3 and 24 characters in length and use any alphanumeric and underscore only.
        :type job_name: str
        :param expand: $expand is supported on details parameter for job, which provides details on the
         job stages.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JobResource or the result of cls(response)
        :rtype: ~azure.mgmt.databox.models.JobResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.JobResource"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-09-01"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'jobName': self._serialize.url("job_name", job_name, 'str', max_length=24, min_length=3, pattern=r'^[-\w\.]+$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('JobResource', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName}'}

    async def _create_initial(
        self,
        resource_group_name: str,
        job_name: str,
        location: str,
        sku: "models.Sku",
        tags: Optional[Dict[str, str]] = None,
        details: Optional["models.JobDetails"] = None,
        delivery_type: Optional[Union[str, "models.JobDeliveryType"]] = None,
        delivery_info: Optional["models.JobDeliveryInfo"] = None,
        **kwargs
    ) -> "models.JobResource":
        cls = kwargs.pop('cls', None)  # type: ClsType["models.JobResource"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _job_resource = models.JobResource(location=location, tags=tags, sku=sku, details=details, delivery_type=delivery_type, delivery_info=delivery_info)
        api_version = "2019-09-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._create_initial.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'jobName': self._serialize.url("job_name", job_name, 'str', max_length=24, min_length=3, pattern=r'^[-\w\.]+$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_job_resource, 'JobResource')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('JobResource', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName}'}

    async def create(
        self,
        resource_group_name: str,
        job_name: str,
        location: str,
        sku: "models.Sku",
        tags: Optional[Dict[str, str]] = None,
        details: Optional["models.JobDetails"] = None,
        delivery_type: Optional[Union[str, "models.JobDeliveryType"]] = None,
        delivery_info: Optional["models.JobDeliveryInfo"] = None,
        **kwargs
    ) -> "models.JobResource":
        """Creates a new job with the specified parameters. Existing job cannot be updated with this API and should instead be updated with the Update job API.

        :param resource_group_name: The Resource Group Name.
        :type resource_group_name: str
        :param job_name: The name of the job Resource within the specified resource group. job names
     must be between 3 and 24 characters in length and use any alphanumeric and underscore only.
        :type job_name: str
        :param location: The location of the resource. This will be one of the supported and registered
     Azure Regions (e.g. West US, East US, Southeast Asia, etc.). The region of a resource cannot be
     changed once it is created, but if an identical region is specified on update the request will
     succeed.
        :type location: str
        :param sku: The sku type.
        :type sku: ~azure.mgmt.databox.models.Sku
        :param tags: The list of key value pairs that describe the resource. These tags can be used in
     viewing and grouping this resource (across resource groups).
        :type tags: dict[str, str]
        :param details: Details of a job run. This field will only be sent for expand details filter.
        :type details: ~azure.mgmt.databox.models.JobDetails
        :param delivery_type: Delivery type of Job.
        :type delivery_type: str or ~azure.mgmt.databox.models.JobDeliveryType
        :param delivery_info: Delivery Info of Job.
        :type delivery_info: ~azure.mgmt.databox.models.JobDeliveryInfo
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :return: An instance of LROPoller that returns JobResource
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.databox.models.JobResource]

        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.JobResource"]
        raw_result = await self._create_initial(
            resource_group_name=resource_group_name,
            job_name=job_name,
            location=location,
            sku=sku,
            tags=tags,
            details=details,
            delivery_type=delivery_type,
            delivery_info=delivery_info,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('JobResource', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = AsyncARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName}'}

    async def _delete_initial(
        self,
        resource_group_name: str,
        job_name: str,
        **kwargs
    ) -> None:
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-09-01"

        # Construct URL
        url = self._delete_initial.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'jobName': self._serialize.url("job_name", job_name, 'str', max_length=24, min_length=3, pattern=r'^[-\w\.]+$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
          return cls(pipeline_response, None, {})

    _delete_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName}'}

    async def delete(
        self,
        resource_group_name: str,
        job_name: str,
        **kwargs
    ) -> None:
        """Deletes a job.

        :param resource_group_name: The Resource Group Name.
        :type resource_group_name: str
        :param job_name: The name of the job Resource within the specified resource group. job names
     must be between 3 and 24 characters in length and use any alphanumeric and underscore only.
        :type job_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]

        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        raw_result = await self._delete_initial(
            resource_group_name=resource_group_name,
            job_name=job_name,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = AsyncARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName}'}

    async def _update_initial(
        self,
        resource_group_name: str,
        job_name: str,
        if_match: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        details: Optional["models.UpdateJobDetails"] = None,
        destination_account_details: Optional[List["DestinationAccountDetails"]] = None,
        **kwargs
    ) -> "models.JobResource":
        cls = kwargs.pop('cls', None)  # type: ClsType["models.JobResource"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _job_resource_update_parameter = models.JobResourceUpdateParameter(tags=tags, details=details, destination_account_details=destination_account_details)
        api_version = "2019-09-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._update_initial.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'jobName': self._serialize.url("job_name", job_name, 'str', max_length=24, min_length=3, pattern=r'^[-\w\.]+$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_job_resource_update_parameter, 'JobResourceUpdateParameter')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('JobResource', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName}'}

    async def update(
        self,
        resource_group_name: str,
        job_name: str,
        if_match: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        details: Optional["models.UpdateJobDetails"] = None,
        destination_account_details: Optional[List["DestinationAccountDetails"]] = None,
        **kwargs
    ) -> "models.JobResource":
        """Updates the properties of an existing job.

        :param resource_group_name: The Resource Group Name.
        :type resource_group_name: str
        :param job_name: The name of the job Resource within the specified resource group. job names
     must be between 3 and 24 characters in length and use any alphanumeric and underscore only.
        :type job_name: str
        :param if_match: Defines the If-Match condition. The patch will be performed only if the ETag
     of the job on the server matches this value.
        :type if_match: str
        :param tags: The list of key value pairs that describe the resource. These tags can be used in
     viewing and grouping this resource (across resource groups).
        :type tags: dict[str, str]
        :param details: Details of a job to be updated.
        :type details: ~azure.mgmt.databox.models.UpdateJobDetails
        :param destination_account_details: Destination account details.
        :type destination_account_details: list[~azure.mgmt.databox.models.DestinationAccountDetails]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :return: An instance of LROPoller that returns JobResource
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.databox.models.JobResource]

        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.JobResource"]
        raw_result = await self._update_initial(
            resource_group_name=resource_group_name,
            job_name=job_name,
            if_match=if_match,
            tags=tags,
            details=details,
            destination_account_details=destination_account_details,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('JobResource', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = AsyncARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName}'}

    async def book_shipment_pick_up(
        self,
        resource_group_name: str,
        job_name: str,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        shipment_location: str,
        **kwargs
    ) -> "models.ShipmentPickUpResponse":
        """Book shipment pick up.

        :param resource_group_name: The Resource Group Name.
        :type resource_group_name: str
        :param job_name: The name of the job Resource within the specified resource group. job names
         must be between 3 and 24 characters in length and use any alphanumeric and underscore only.
        :type job_name: str
        :param start_time: Minimum date after which the pick up should commence, this must be in local
         time of pick up area.
        :type start_time: ~datetime.datetime
        :param end_time: Maximum date before which the pick up should commence, this must be in local
         time of pick up area.
        :type end_time: ~datetime.datetime
        :param shipment_location: Shipment Location in the pickup place. Eg.front desk.
        :type shipment_location: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ShipmentPickUpResponse or the result of cls(response)
        :rtype: ~azure.mgmt.databox.models.ShipmentPickUpResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ShipmentPickUpResponse"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _shipment_pick_up_request = models.ShipmentPickUpRequest(start_time=start_time, end_time=end_time, shipment_location=shipment_location)
        api_version = "2019-09-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.book_shipment_pick_up.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'jobName': self._serialize.url("job_name", job_name, 'str', max_length=24, min_length=3, pattern=r'^[-\w\.]+$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_shipment_pick_up_request, 'ShipmentPickUpRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ShipmentPickUpResponse', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    book_shipment_pick_up.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName}/bookShipmentPickUp'}

    async def cancel(
        self,
        resource_group_name: str,
        job_name: str,
        reason: str,
        **kwargs
    ) -> None:
        """CancelJob.

        :param resource_group_name: The Resource Group Name.
        :type resource_group_name: str
        :param job_name: The name of the job Resource within the specified resource group. job names
         must be between 3 and 24 characters in length and use any alphanumeric and underscore only.
        :type job_name: str
        :param reason: Reason for cancellation.
        :type reason: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _cancellation_reason = models.CancellationReason(reason=reason)
        api_version = "2019-09-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.cancel.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'jobName': self._serialize.url("job_name", job_name, 'str', max_length=24, min_length=3, pattern=r'^[-\w\.]+$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_cancellation_reason, 'CancellationReason')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
          return cls(pipeline_response, None, {})

    cancel.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName}/cancel'}

    def list_credentials(
        self,
        resource_group_name: str,
        job_name: str,
        **kwargs
    ) -> "models.UnencryptedCredentialsList":
        """This method gets the unencrypted secrets related to the job.

        :param resource_group_name: The Resource Group Name.
        :type resource_group_name: str
        :param job_name: The name of the job Resource within the specified resource group. job names
     must be between 3 and 24 characters in length and use any alphanumeric and underscore only.
        :type job_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: UnencryptedCredentialsList or the result of cls(response)
        :rtype: ~azure.mgmt.databox.models.UnencryptedCredentialsList
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.UnencryptedCredentialsList"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-09-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_credentials.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'jobName': self._serialize.url("job_name", job_name, 'str', max_length=24, min_length=3, pattern=r'^[-\w\.]+$'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}  # type: Dict[str, Any]
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.post(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('UnencryptedCredentialsList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_credentials.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName}/listCredentials'}
