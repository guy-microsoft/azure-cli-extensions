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
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.polling import AsyncNoPolling, AsyncPollingMethod, async_poller
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class BlockchainMemberOperations:
    """BlockchainMemberOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~blockchain_management_client.models
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

    async def get(
        self,
        blockchain_member_name: str,
        resource_group_name: str,
        **kwargs
    ) -> "models.BlockchainMember":
        """Get details about a blockchain member.

        :param blockchain_member_name: Blockchain member name.
        :type blockchain_member_name: str
        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BlockchainMember, or the result of cls(response)
        :rtype: ~blockchain_management_client.models.BlockchainMember
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.BlockchainMember"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-06-01-preview"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'blockchainMemberName': self._serialize.url("blockchain_member_name", blockchain_member_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
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
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('BlockchainMember', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}'}  # type: ignore

    async def _create_initial(
        self,
        blockchain_member_name: str,
        resource_group_name: str,
        location: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        sku: Optional["models.Sku"] = None,
        protocol: Optional[Union[str, "models.BlockchainProtocol"]] = None,
        validator_nodes_sku: Optional["models.BlockchainMemberNodesSku"] = None,
        password: Optional[str] = None,
        consortium: Optional[str] = None,
        consortium_management_account_password: Optional[str] = None,
        consortium_role: Optional[str] = None,
        consortium_member_display_name: Optional[str] = None,
        firewall_rules: Optional[List["models.FirewallRule"]] = None,
        **kwargs
    ) -> "models.BlockchainMember":
        cls = kwargs.pop('cls', None)  # type: ClsType["models.BlockchainMember"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _blockchain_member = models.BlockchainMember(location=location, tags=tags, sku=sku, protocol=protocol, validator_nodes_sku=validator_nodes_sku, password=password, consortium=consortium, consortium_management_account_password=consortium_management_account_password, consortium_role=consortium_role, consortium_member_display_name=consortium_member_display_name, firewall_rules=firewall_rules)
        api_version = "2018-06-01-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._create_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'blockchainMemberName': self._serialize.url("blockchain_member_name", blockchain_member_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
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
        if _blockchain_member is not None:
            body_content = self._serialize.body(_blockchain_member, 'BlockchainMember')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('BlockchainMember', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('BlockchainMember', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}'}  # type: ignore

    async def create(
        self,
        blockchain_member_name: str,
        resource_group_name: str,
        location: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        sku: Optional["models.Sku"] = None,
        protocol: Optional[Union[str, "models.BlockchainProtocol"]] = None,
        validator_nodes_sku: Optional["models.BlockchainMemberNodesSku"] = None,
        password: Optional[str] = None,
        consortium: Optional[str] = None,
        consortium_management_account_password: Optional[str] = None,
        consortium_role: Optional[str] = None,
        consortium_member_display_name: Optional[str] = None,
        firewall_rules: Optional[List["models.FirewallRule"]] = None,
        **kwargs
    ) -> "models.BlockchainMember":
        """Create a blockchain member.

        :param blockchain_member_name: Blockchain member name.
        :type blockchain_member_name: str
        :param resource_group_name: The name of the resource group that contains the resource. You can
     obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param location: The GEO location of the blockchain service.
        :type location: str
        :param tags: Tags of the service which is a list of key value pairs that describes the
     resource.
        :type tags: dict[str, str]
        :param sku: Gets or sets the blockchain member Sku.
        :type sku: ~blockchain_management_client.models.Sku
        :param protocol: Gets or sets the blockchain protocol.
        :type protocol: str or ~blockchain_management_client.models.BlockchainProtocol
        :param validator_nodes_sku: Gets or sets the blockchain validator nodes Sku.
        :type validator_nodes_sku: ~blockchain_management_client.models.BlockchainMemberNodesSku
        :param password: Sets the basic auth password of the blockchain member.
        :type password: str
        :param consortium: Gets or sets the consortium for the blockchain member.
        :type consortium: str
        :param consortium_management_account_password: Sets the managed consortium management account
     password.
        :type consortium_management_account_password: str
        :param consortium_role: Gets the role of the member in the consortium.
        :type consortium_role: str
        :param consortium_member_display_name: Gets the display name of the member in the consortium.
        :type consortium_member_display_name: str
        :param firewall_rules: Gets or sets firewall rules.
        :type firewall_rules: list[~blockchain_management_client.models.FirewallRule]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: BlockchainMember, or the result of cls(response)
        :rtype: ~blockchain_management_client.models.BlockchainMember
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.BlockchainMember"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        raw_result = await self._create_initial(
            blockchain_member_name=blockchain_member_name,
            resource_group_name=resource_group_name,
            location=location,
            tags=tags,
            sku=sku,
            protocol=protocol,
            validator_nodes_sku=validator_nodes_sku,
            password=password,
            consortium=consortium,
            consortium_management_account_password=consortium_management_account_password,
            consortium_role=consortium_role,
            consortium_member_display_name=consortium_member_display_name,
            firewall_rules=firewall_rules,
            cls=lambda x,y,z: x,
            **kwargs
        )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('BlockchainMember', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = AsyncARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}'}  # type: ignore

    async def _delete_initial(
        self,
        blockchain_member_name: str,
        resource_group_name: str,
        **kwargs
    ) -> None:
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-06-01-preview"

        # Construct URL
        url = self._delete_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'blockchainMemberName': self._serialize.url("blockchain_member_name", blockchain_member_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
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

    _delete_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}'}  # type: ignore

    async def delete(
        self,
        blockchain_member_name: str,
        resource_group_name: str,
        **kwargs
    ) -> None:
        """Delete a blockchain member.

        :param blockchain_member_name: Blockchain member name.
        :type blockchain_member_name: str
        :param resource_group_name: The name of the resource group that contains the resource. You can
     obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: None, or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        raw_result = await self._delete_initial(
            blockchain_member_name=blockchain_member_name,
            resource_group_name=resource_group_name,
            cls=lambda x,y,z: x,
            **kwargs
        )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True: polling_method = AsyncARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}'}  # type: ignore

    async def update(
        self,
        blockchain_member_name: str,
        resource_group_name: str,
        tags: Optional[Dict[str, str]] = None,
        password: Optional[str] = None,
        firewall_rules: Optional[List["models.FirewallRule"]] = None,
        consortium_management_account_password: Optional[str] = None,
        **kwargs
    ) -> "models.BlockchainMember":
        """Update a blockchain member.

        :param blockchain_member_name: Blockchain member name.
        :type blockchain_member_name: str
        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param tags: Tags of the service which is a list of key value pairs that describes the
         resource.
        :type tags: dict[str, str]
        :param password: Sets the transaction node dns endpoint basic auth password.
        :type password: str
        :param firewall_rules: Gets or sets the firewall rules.
        :type firewall_rules: list[~blockchain_management_client.models.FirewallRule]
        :param consortium_management_account_password: Sets the managed consortium management account
         password.
        :type consortium_management_account_password: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BlockchainMember, or the result of cls(response)
        :rtype: ~blockchain_management_client.models.BlockchainMember
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.BlockchainMember"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _blockchain_member = models.BlockchainMemberUpdate(tags=tags, password=password, firewall_rules=firewall_rules, consortium_management_account_password=consortium_management_account_password)
        api_version = "2018-06-01-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update.metadata['url']  # type: ignore
        path_format_arguments = {
            'blockchainMemberName': self._serialize.url("blockchain_member_name", blockchain_member_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
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
        if _blockchain_member is not None:
            body_content = self._serialize.body(_blockchain_member, 'BlockchainMemberUpdate')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('BlockchainMember', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}'}  # type: ignore

    def list(
        self,
        resource_group_name: str,
        **kwargs
    ) -> AsyncIterable["models.BlockchainMemberCollection"]:
        """Lists the blockchain members for a resource group.

        :param resource_group_name: The name of the resource group that contains the resource. You can
     obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either BlockchainMemberCollection or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~blockchain_management_client.models.BlockchainMemberCollection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.BlockchainMemberCollection"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-06-01-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
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

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('BlockchainMemberCollection', pipeline_response)
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
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers'}  # type: ignore

    def list_all(
        self,
        **kwargs
    ) -> AsyncIterable["models.BlockchainMemberCollection"]:
        """Lists the blockchain members for a subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either BlockchainMemberCollection or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~blockchain_management_client.models.BlockchainMemberCollection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.BlockchainMemberCollection"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-06-01-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_all.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
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

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('BlockchainMemberCollection', pipeline_response)
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
    list_all.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Blockchain/blockchainMembers'}  # type: ignore

    def list_consortium_member(
        self,
        blockchain_member_name: str,
        resource_group_name: str,
        **kwargs
    ) -> AsyncIterable["models.ConsortiumMemberCollection"]:
        """Lists the consortium members for a blockchain member.

        :param blockchain_member_name: Blockchain member name.
        :type blockchain_member_name: str
        :param resource_group_name: The name of the resource group that contains the resource. You can
     obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ConsortiumMemberCollection or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~blockchain_management_client.models.ConsortiumMemberCollection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ConsortiumMemberCollection"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-06-01-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_consortium_member.metadata['url']  # type: ignore
                path_format_arguments = {
                    'blockchainMemberName': self._serialize.url("blockchain_member_name", blockchain_member_name, 'str'),
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
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

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('ConsortiumMemberCollection', pipeline_response)
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
    list_consortium_member.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/consortiumMembers'}  # type: ignore

    async def list_api_key(
        self,
        blockchain_member_name: str,
        resource_group_name: str,
        **kwargs
    ) -> "models.ApiKeyCollection":
        """Lists the API keys for a blockchain member.

        :param blockchain_member_name: Blockchain member name.
        :type blockchain_member_name: str
        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApiKeyCollection, or the result of cls(response)
        :rtype: ~blockchain_management_client.models.ApiKeyCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ApiKeyCollection"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-06-01-preview"

        # Construct URL
        url = self.list_api_key.metadata['url']  # type: ignore
        path_format_arguments = {
            'blockchainMemberName': self._serialize.url("blockchain_member_name", blockchain_member_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ApiKeyCollection', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    list_api_key.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/listApiKeys'}  # type: ignore

    async def regenerate_api_key(
        self,
        blockchain_member_name: str,
        resource_group_name: str,
        key_name: Optional[str] = None,
        value: Optional[str] = None,
        **kwargs
    ) -> "models.ApiKeyCollection":
        """Regenerate the API keys for a blockchain member.

        :param blockchain_member_name: Blockchain member name.
        :type blockchain_member_name: str
        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param key_name: Gets or sets the API key name.
        :type key_name: str
        :param value: Gets or sets the API key value.
        :type value: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApiKeyCollection, or the result of cls(response)
        :rtype: ~blockchain_management_client.models.ApiKeyCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ApiKeyCollection"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _api_key = models.ApiKey(key_name=key_name, value=value)
        api_version = "2018-06-01-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.regenerate_api_key.metadata['url']  # type: ignore
        path_format_arguments = {
            'blockchainMemberName': self._serialize.url("blockchain_member_name", blockchain_member_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
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
        if _api_key is not None:
            body_content = self._serialize.body(_api_key, 'ApiKey')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ApiKeyCollection', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    regenerate_api_key.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/regenerateApiKeys'}  # type: ignore
