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
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class HostPoolOperations(object):
    """HostPoolOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~desktop_virtualization_api_client.models
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

    def get(
        self,
        resource_group_name,  # type: str
        host_pool_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.HostPool"
        """Get a host pool.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param host_pool_name: The name of the host pool within the specified resource group.
        :type host_pool_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: HostPool, or the result of cls(response)
        :rtype: ~desktop_virtualization_api_client.models.HostPool
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.HostPool"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-12-10-preview"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'hostPoolName': self._serialize.url("host_pool_name", host_pool_name, 'str', max_length=24, min_length=3),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('HostPool', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/hostPools/{hostPoolName}'}  # type: ignore

    def create_or_update(
        self,
        resource_group_name,  # type: str
        host_pool_name,  # type: str
        location,  # type: str
        host_pool_type,  # type: Union[str, "models.HostPoolType"]
        load_balancer_type,  # type: Union[str, "models.LoadBalancerType"]
        preferred_app_group_type,  # type: Union[str, "models.PreferredAppGroupType"]
        tags=None,  # type: Optional[Dict[str, str]]
        friendly_name=None,  # type: Optional[str]
        description=None,  # type: Optional[str]
        personal_desktop_assignment_type=None,  # type: Optional[Union[str, "models.PersonalDesktopAssignmentType"]]
        custom_rdp_property=None,  # type: Optional[str]
        max_session_limit=None,  # type: Optional[int]
        ring=None,  # type: Optional[int]
        validation_environment=None,  # type: Optional[bool]
        registration_info=None,  # type: Optional["models.RegistrationInfo"]
        vm_template=None,  # type: Optional[str]
        sso_context=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.HostPool"
        """Create or update a host pool.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param host_pool_name: The name of the host pool within the specified resource group.
        :type host_pool_name: str
        :param location: The geo-location where the resource lives.
        :type location: str
        :param host_pool_type: HostPool type for desktop.
        :type host_pool_type: str or ~desktop_virtualization_api_client.models.HostPoolType
        :param load_balancer_type: The type of the load balancer.
        :type load_balancer_type: str or ~desktop_virtualization_api_client.models.LoadBalancerType
        :param preferred_app_group_type: The type of preferred application group type, default to
         Desktop Application Group.
        :type preferred_app_group_type: str or ~desktop_virtualization_api_client.models.PreferredAppGroupType
        :param tags: Resource tags.
        :type tags: dict[str, str]
        :param friendly_name: Friendly name of HostPool.
        :type friendly_name: str
        :param description: Description of HostPool.
        :type description: str
        :param personal_desktop_assignment_type: PersonalDesktopAssignment type for HostPool.
        :type personal_desktop_assignment_type: str or ~desktop_virtualization_api_client.models.PersonalDesktopAssignmentType
        :param custom_rdp_property: Custom rdp property of HostPool.
        :type custom_rdp_property: str
        :param max_session_limit: The max session limit of HostPool.
        :type max_session_limit: int
        :param ring: The ring number of HostPool.
        :type ring: int
        :param validation_environment: Is validation environment.
        :type validation_environment: bool
        :param registration_info: The registration info of HostPool.
        :type registration_info: ~desktop_virtualization_api_client.models.RegistrationInfo
        :param vm_template: VM template for sessionhosts configuration within hostpool.
        :type vm_template: str
        :param sso_context: Path to keyvault containing ssoContext secret.
        :type sso_context: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: HostPool, or the result of cls(response)
        :rtype: ~desktop_virtualization_api_client.models.HostPool
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.HostPool"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _host_pool = models.HostPool(tags=tags, location=location, friendly_name=friendly_name, description=description, host_pool_type=host_pool_type, personal_desktop_assignment_type=personal_desktop_assignment_type, custom_rdp_property=custom_rdp_property, max_session_limit=max_session_limit, load_balancer_type=load_balancer_type, ring=ring, validation_environment=validation_environment, registration_info=registration_info, vm_template=vm_template, sso_context=sso_context, preferred_app_group_type=preferred_app_group_type)
        api_version = "2019-12-10-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'hostPoolName': self._serialize.url("host_pool_name", host_pool_name, 'str', max_length=24, min_length=3),
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
        body_content = self._serialize.body(_host_pool, 'HostPool')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('HostPool', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('HostPool', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/hostPools/{hostPoolName}'}  # type: ignore

    def delete(
        self,
        resource_group_name,  # type: str
        host_pool_name,  # type: str
        force=None,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Remove a host pool.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param host_pool_name: The name of the host pool within the specified resource group.
        :type host_pool_name: str
        :param force: Force flag to delete sessionHost.
        :type force: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-12-10-preview"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'hostPoolName': self._serialize.url("host_pool_name", host_pool_name, 'str', max_length=24, min_length=3),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        if force is not None:
            query_parameters['force'] = self._serialize.query("force", force, 'bool')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/hostPools/{hostPoolName}'}  # type: ignore

    def update(
        self,
        resource_group_name,  # type: str
        host_pool_name,  # type: str
        tags=None,  # type: Optional[Dict[str, str]]
        friendly_name=None,  # type: Optional[str]
        description=None,  # type: Optional[str]
        custom_rdp_property=None,  # type: Optional[str]
        max_session_limit=None,  # type: Optional[int]
        personal_desktop_assignment_type=None,  # type: Optional[Union[str, "models.PersonalDesktopAssignmentType"]]
        load_balancer_type=None,  # type: Optional[Union[str, "models.LoadBalancerType"]]
        ring=None,  # type: Optional[int]
        validation_environment=None,  # type: Optional[bool]
        registration_info=None,  # type: Optional["models.RegistrationInfoPatch"]
        sso_context=None,  # type: Optional[str]
        preferred_app_group_type=None,  # type: Optional[Union[str, "models.PreferredAppGroupType"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.HostPool"
        """Update a host pool.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param host_pool_name: The name of the host pool within the specified resource group.
        :type host_pool_name: str
        :param tags: tags to be updated.
        :type tags: dict[str, str]
        :param friendly_name: Friendly name of HostPool.
        :type friendly_name: str
        :param description: Description of HostPool.
        :type description: str
        :param custom_rdp_property: Custom rdp property of HostPool.
        :type custom_rdp_property: str
        :param max_session_limit: The max session limit of HostPool.
        :type max_session_limit: int
        :param personal_desktop_assignment_type: PersonalDesktopAssignment type for HostPool.
        :type personal_desktop_assignment_type: str or ~desktop_virtualization_api_client.models.PersonalDesktopAssignmentType
        :param load_balancer_type: The type of the load balancer.
        :type load_balancer_type: str or ~desktop_virtualization_api_client.models.LoadBalancerType
        :param ring: The ring number of HostPool.
        :type ring: int
        :param validation_environment: Is validation environment.
        :type validation_environment: bool
        :param registration_info: The registration info of HostPool.
        :type registration_info: ~desktop_virtualization_api_client.models.RegistrationInfoPatch
        :param sso_context: Path to keyvault containing ssoContext secret.
        :type sso_context: str
        :param preferred_app_group_type: The type of preferred application group type, default to
         Desktop Application Group.
        :type preferred_app_group_type: str or ~desktop_virtualization_api_client.models.PreferredAppGroupType
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: HostPool, or the result of cls(response)
        :rtype: ~desktop_virtualization_api_client.models.HostPool
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.HostPool"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _host_pool = models.HostPoolPatch(tags=tags, friendly_name=friendly_name, description=description, custom_rdp_property=custom_rdp_property, max_session_limit=max_session_limit, personal_desktop_assignment_type=personal_desktop_assignment_type, load_balancer_type=load_balancer_type, ring=ring, validation_environment=validation_environment, registration_info=registration_info, sso_context=sso_context, preferred_app_group_type=preferred_app_group_type)
        api_version = "2019-12-10-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'hostPoolName': self._serialize.url("host_pool_name", host_pool_name, 'str', max_length=24, min_length=3),
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
        if _host_pool is not None:
            body_content = self._serialize.body(_host_pool, 'HostPoolPatch')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('HostPool', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/hostPools/{hostPoolName}'}  # type: ignore

    def list_by_resource_group(
        self,
        resource_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.HostPoolList"]
        """List hostPools.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either HostPoolList or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~desktop_virtualization_api_client.models.HostPoolList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.HostPoolList"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-12-10-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_resource_group.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('HostPoolList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/hostPools'}  # type: ignore

    def list(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.HostPoolList"]
        """List hostPools in subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either HostPoolList or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~desktop_virtualization_api_client.models.HostPoolList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.HostPoolList"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-12-10-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('HostPoolList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DesktopVirtualization/hostPools'}  # type: ignore
