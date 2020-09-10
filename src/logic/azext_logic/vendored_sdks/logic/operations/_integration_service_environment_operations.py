# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class IntegrationServiceEnvironmentOperations(object):
    """IntegrationServiceEnvironmentOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~logic_management_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_by_subscription(
        self,
        top=None,  # type: Optional[int]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.IntegrationServiceEnvironmentListResult"]
        """Gets a list of integration service environments by subscription.

        :param top: The number of items to be included in the result.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either IntegrationServiceEnvironmentListResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~logic_management_client.models.IntegrationServiceEnvironmentListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.IntegrationServiceEnvironmentListResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-05-01"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_by_subscription.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('IntegrationServiceEnvironmentListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_subscription.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Logic/integrationServiceEnvironments'}  # type: ignore

    def list_by_resource_group(
        self,
        resource_group,  # type: str
        top=None,  # type: Optional[int]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.IntegrationServiceEnvironmentListResult"]
        """Gets a list of integration service environments by resource group.

        :param resource_group: The resource group.
        :type resource_group: str
        :param top: The number of items to be included in the result.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either IntegrationServiceEnvironmentListResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~logic_management_client.models.IntegrationServiceEnvironmentListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.IntegrationServiceEnvironmentListResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-05-01"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_by_resource_group.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroup': self._serialize.url("resource_group", resource_group, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('IntegrationServiceEnvironmentListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments'}  # type: ignore

    def get(
        self,
        resource_group,  # type: str
        integration_service_environment_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.IntegrationServiceEnvironment"
        """Gets an integration service environment.

        :param resource_group: The resource group.
        :type resource_group: str
        :param integration_service_environment_name: The integration service environment name.
        :type integration_service_environment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IntegrationServiceEnvironment, or the result of cls(response)
        :rtype: ~logic_management_client.models.IntegrationServiceEnvironment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.IntegrationServiceEnvironment"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-05-01"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroup': self._serialize.url("resource_group", resource_group, 'str'),
            'integrationServiceEnvironmentName': self._serialize.url("integration_service_environment_name", integration_service_environment_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('IntegrationServiceEnvironment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName}'}  # type: ignore

    def _create_or_update_initial(
        self,
        resource_group,  # type: str
        integration_service_environment_name,  # type: str
        location=None,  # type: Optional[str]
        tags=None,  # type: Optional[Dict[str, str]]
        sku=None,  # type: Optional["models.IntegrationServiceEnvironmentSku"]
        provisioning_state=None,  # type: Optional[Union[str, "models.WorkflowProvisioningState"]]
        state=None,  # type: Optional[Union[str, "models.WorkflowState"]]
        integration_service_environment_id=None,  # type: Optional[str]
        endpoints_configuration=None,  # type: Optional["models.FlowEndpointsConfiguration"]
        network_configuration=None,  # type: Optional["models.NetworkConfiguration"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.IntegrationServiceEnvironment"
        cls = kwargs.pop('cls', None)  # type: ClsType["models.IntegrationServiceEnvironment"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _integration_service_environment = models.IntegrationServiceEnvironment(location=location, tags=tags, sku=sku, provisioning_state=provisioning_state, state=state, integration_service_environment_id=integration_service_environment_id, endpoints_configuration=endpoints_configuration, network_configuration=network_configuration)
        api_version = "2019-05-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._create_or_update_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroup': self._serialize.url("resource_group", resource_group, 'str'),
            'integrationServiceEnvironmentName': self._serialize.url("integration_service_environment_name", integration_service_environment_name, 'str'),
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
        body_content = self._serialize.body(_integration_service_environment, 'IntegrationServiceEnvironment')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('IntegrationServiceEnvironment', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('IntegrationServiceEnvironment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_or_update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName}'}  # type: ignore

    def begin_create_or_update(
        self,
        resource_group,  # type: str
        integration_service_environment_name,  # type: str
        location=None,  # type: Optional[str]
        tags=None,  # type: Optional[Dict[str, str]]
        sku=None,  # type: Optional["models.IntegrationServiceEnvironmentSku"]
        provisioning_state=None,  # type: Optional[Union[str, "models.WorkflowProvisioningState"]]
        state=None,  # type: Optional[Union[str, "models.WorkflowState"]]
        integration_service_environment_id=None,  # type: Optional[str]
        endpoints_configuration=None,  # type: Optional["models.FlowEndpointsConfiguration"]
        network_configuration=None,  # type: Optional["models.NetworkConfiguration"]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["models.IntegrationServiceEnvironment"]
        """Creates or updates an integration service environment.

        :param resource_group: The resource group.
        :type resource_group: str
        :param integration_service_environment_name: The integration service environment name.
        :type integration_service_environment_name: str
        :param location: The resource location.
        :type location: str
        :param tags: The resource tags.
        :type tags: dict[str, str]
        :param sku: The sku.
        :type sku: ~logic_management_client.models.IntegrationServiceEnvironmentSku
        :param provisioning_state: The provisioning state.
        :type provisioning_state: str or ~logic_management_client.models.WorkflowProvisioningState
        :param state: The integration service environment state.
        :type state: str or ~logic_management_client.models.WorkflowState
        :param integration_service_environment_id: Gets the tracking id.
        :type integration_service_environment_id: str
        :param endpoints_configuration: The endpoints configuration.
        :type endpoints_configuration: ~logic_management_client.models.FlowEndpointsConfiguration
        :param network_configuration: The network configuration.
        :type network_configuration: ~logic_management_client.models.NetworkConfiguration
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either IntegrationServiceEnvironment or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~logic_management_client.models.IntegrationServiceEnvironment]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.IntegrationServiceEnvironment"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._create_or_update_initial(
                resource_group=resource_group,
                integration_service_environment_name=integration_service_environment_name,
                location=location,
                tags=tags,
                sku=sku,
                provisioning_state=provisioning_state,
                state=state,
                integration_service_environment_id=integration_service_environment_id,
                endpoints_configuration=endpoints_configuration,
                network_configuration=network_configuration,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('IntegrationServiceEnvironment', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName}'}  # type: ignore

    def _update_initial(
        self,
        resource_group,  # type: str
        integration_service_environment_name,  # type: str
        location=None,  # type: Optional[str]
        tags=None,  # type: Optional[Dict[str, str]]
        sku=None,  # type: Optional["models.IntegrationServiceEnvironmentSku"]
        provisioning_state=None,  # type: Optional[Union[str, "models.WorkflowProvisioningState"]]
        state=None,  # type: Optional[Union[str, "models.WorkflowState"]]
        integration_service_environment_id=None,  # type: Optional[str]
        endpoints_configuration=None,  # type: Optional["models.FlowEndpointsConfiguration"]
        network_configuration=None,  # type: Optional["models.NetworkConfiguration"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.IntegrationServiceEnvironment"
        cls = kwargs.pop('cls', None)  # type: ClsType["models.IntegrationServiceEnvironment"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _integration_service_environment = models.IntegrationServiceEnvironment(location=location, tags=tags, sku=sku, provisioning_state=provisioning_state, state=state, integration_service_environment_id=integration_service_environment_id, endpoints_configuration=endpoints_configuration, network_configuration=network_configuration)
        api_version = "2019-05-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._update_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroup': self._serialize.url("resource_group", resource_group, 'str'),
            'integrationServiceEnvironmentName': self._serialize.url("integration_service_environment_name", integration_service_environment_name, 'str'),
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
        body_content = self._serialize.body(_integration_service_environment, 'IntegrationServiceEnvironment')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('IntegrationServiceEnvironment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName}'}  # type: ignore

    def begin_update(
        self,
        resource_group,  # type: str
        integration_service_environment_name,  # type: str
        location=None,  # type: Optional[str]
        tags=None,  # type: Optional[Dict[str, str]]
        sku=None,  # type: Optional["models.IntegrationServiceEnvironmentSku"]
        provisioning_state=None,  # type: Optional[Union[str, "models.WorkflowProvisioningState"]]
        state=None,  # type: Optional[Union[str, "models.WorkflowState"]]
        integration_service_environment_id=None,  # type: Optional[str]
        endpoints_configuration=None,  # type: Optional["models.FlowEndpointsConfiguration"]
        network_configuration=None,  # type: Optional["models.NetworkConfiguration"]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["models.IntegrationServiceEnvironment"]
        """Updates an integration service environment.

        :param resource_group: The resource group.
        :type resource_group: str
        :param integration_service_environment_name: The integration service environment name.
        :type integration_service_environment_name: str
        :param location: The resource location.
        :type location: str
        :param tags: The resource tags.
        :type tags: dict[str, str]
        :param sku: The sku.
        :type sku: ~logic_management_client.models.IntegrationServiceEnvironmentSku
        :param provisioning_state: The provisioning state.
        :type provisioning_state: str or ~logic_management_client.models.WorkflowProvisioningState
        :param state: The integration service environment state.
        :type state: str or ~logic_management_client.models.WorkflowState
        :param integration_service_environment_id: Gets the tracking id.
        :type integration_service_environment_id: str
        :param endpoints_configuration: The endpoints configuration.
        :type endpoints_configuration: ~logic_management_client.models.FlowEndpointsConfiguration
        :param network_configuration: The network configuration.
        :type network_configuration: ~logic_management_client.models.NetworkConfiguration
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either IntegrationServiceEnvironment or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~logic_management_client.models.IntegrationServiceEnvironment]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.IntegrationServiceEnvironment"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._update_initial(
                resource_group=resource_group,
                integration_service_environment_name=integration_service_environment_name,
                location=location,
                tags=tags,
                sku=sku,
                provisioning_state=provisioning_state,
                state=state,
                integration_service_environment_id=integration_service_environment_id,
                endpoints_configuration=endpoints_configuration,
                network_configuration=network_configuration,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('IntegrationServiceEnvironment', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName}'}  # type: ignore

    def delete(
        self,
        resource_group,  # type: str
        integration_service_environment_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes an integration service environment.

        :param resource_group: The resource group.
        :type resource_group: str
        :param integration_service_environment_name: The integration service environment name.
        :type integration_service_environment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-05-01"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroup': self._serialize.url("resource_group", resource_group, 'str'),
            'integrationServiceEnvironmentName': self._serialize.url("integration_service_environment_name", integration_service_environment_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName}'}  # type: ignore

    def restart(
        self,
        resource_group,  # type: str
        integration_service_environment_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Restarts an integration service environment.

        :param resource_group: The resource group.
        :type resource_group: str
        :param integration_service_environment_name: The integration service environment name.
        :type integration_service_environment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-05-01"

        # Construct URL
        url = self.restart.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroup': self._serialize.url("resource_group", resource_group, 'str'),
            'integrationServiceEnvironmentName': self._serialize.url("integration_service_environment_name", integration_service_environment_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    restart.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName}/restart'}  # type: ignore
