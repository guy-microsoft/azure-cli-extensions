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
    from typing import Any, Callable, Dict, Generic, Iterable, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class StorageTargetOperations(object):
    """StorageTargetOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~storage_cache_management_client.models
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

    def list_by_cache(
        self,
        resource_group_name,  # type: str
        cache_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.StorageTargetsResult"]
        """Returns a list of Storage Targets for the specified Cache.

        :param resource_group_name: Target resource group.
        :type resource_group_name: str
        :param cache_name: Name of Cache. Length of name must be not greater than 80 and chars must be
     in list of [-0-9a-zA-Z_] char class.
        :type cache_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either StorageTargetsResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~storage_cache_management_client.models.StorageTargetsResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.StorageTargetsResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-03-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_cache.metadata['url']  # type: ignore
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'cacheName': self._serialize.url("cache_name", cache_name, 'str', pattern=r'^[-0-9a-zA-Z_]{1,80}$'),
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
            deserialized = self._deserialize('StorageTargetsResult', pipeline_response)
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
    list_by_cache.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets'}  # type: ignore

    def _delete_initial(
        self,
        resource_group_name,  # type: str
        cache_name,  # type: str
        storage_target_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> object
        cls = kwargs.pop('cls', None)  # type: ClsType[object]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-03-01"

        # Construct URL
        url = self._delete_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'cacheName': self._serialize.url("cache_name", cache_name, 'str', pattern=r'^[-0-9a-zA-Z_]{1,80}$'),
            'storageTargetName': self._serialize.url("storage_target_name", storage_target_name, 'str', pattern=r'^[-0-9a-zA-Z_]{1,80}$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('object', pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize('object', pipeline_response)

        if response.status_code == 204:
            deserialized = self._deserialize('object', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _delete_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets/{storageTargetName}'}  # type: ignore

    def begin_delete(
        self,
        resource_group_name,  # type: str
        cache_name,  # type: str
        storage_target_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller
        """Removes a Storage Target from a Cache. This operation is allowed at any time, but if the Cache is down or unhealthy, the actual removal of the Storage Target may be delayed until the Cache is healthy again. Note that if the Cache has data to flush to the Storage Target, the data will be flushed before the Storage Target will be deleted.

        :param resource_group_name: Target resource group.
        :type resource_group_name: str
        :param cache_name: Name of Cache. Length of name must be not greater than 80 and chars must be
     in list of [-0-9a-zA-Z_] char class.
        :type cache_name: str
        :param storage_target_name: Name of Storage Target.
        :type storage_target_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either object or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[object]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[object]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        raw_result = self._delete_initial(
            resource_group_name=resource_group_name,
            cache_name=cache_name,
            storage_target_name=storage_target_name,
            cls=lambda x,y,z: x,
            **kwargs
        )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('object', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets/{storageTargetName}'}  # type: ignore

    def get(
        self,
        resource_group_name,  # type: str
        cache_name,  # type: str
        storage_target_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.StorageTarget"
        """Returns a Storage Target from a Cache.

        :param resource_group_name: Target resource group.
        :type resource_group_name: str
        :param cache_name: Name of Cache. Length of name must be not greater than 80 and chars must be
         in list of [-0-9a-zA-Z_] char class.
        :type cache_name: str
        :param storage_target_name: Name of the Storage Target. Length of name must be not greater than
         80 and chars must be in list of [-0-9a-zA-Z_] char class.
        :type storage_target_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StorageTarget, or the result of cls(response)
        :rtype: ~storage_cache_management_client.models.StorageTarget
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.StorageTarget"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-03-01"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'cacheName': self._serialize.url("cache_name", cache_name, 'str', pattern=r'^[-0-9a-zA-Z_]{1,80}$'),
            'storageTargetName': self._serialize.url("storage_target_name", storage_target_name, 'str', pattern=r'^[-0-9a-zA-Z_]{1,80}$'),
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

        deserialized = self._deserialize('StorageTarget', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets/{storageTargetName}'}  # type: ignore

    def _create_or_update_initial(
        self,
        resource_group_name,  # type: str
        cache_name,  # type: str
        storage_target_name,  # type: str
        junctions=None,  # type: Optional[List["models.NamespaceJunction"]]
        target_type=None,  # type: Optional[Union[str, "models.StorageTargetType"]]
        provisioning_state=None,  # type: Optional[Union[str, "models.ProvisioningStateType"]]
        nfs3=None,  # type: Optional["models.Nfs3Target"]
        clfs=None,  # type: Optional["models.ClfsTarget"]
        unknown=None,  # type: Optional["models.UnknownTarget"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.StorageTarget"
        cls = kwargs.pop('cls', None)  # type: ClsType["models.StorageTarget"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _storagetarget = models.StorageTarget(junctions=junctions, target_type=target_type, provisioning_state=provisioning_state, nfs3=nfs3, clfs=clfs, unknown=unknown)
        api_version = "2020-03-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._create_or_update_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'cacheName': self._serialize.url("cache_name", cache_name, 'str', pattern=r'^[-0-9a-zA-Z_]{1,80}$'),
            'storageTargetName': self._serialize.url("storage_target_name", storage_target_name, 'str', pattern=r'^[-0-9a-zA-Z_]{1,80}$'),
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
        if _storagetarget is not None:
            body_content = self._serialize.body(_storagetarget, 'StorageTarget')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('StorageTarget', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('StorageTarget', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_or_update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets/{storageTargetName}'}  # type: ignore

    def begin_create_or_update(
        self,
        resource_group_name,  # type: str
        cache_name,  # type: str
        storage_target_name,  # type: str
        junctions=None,  # type: Optional[List["models.NamespaceJunction"]]
        target_type=None,  # type: Optional[Union[str, "models.StorageTargetType"]]
        provisioning_state=None,  # type: Optional[Union[str, "models.ProvisioningStateType"]]
        nfs3=None,  # type: Optional["models.Nfs3Target"]
        clfs=None,  # type: Optional["models.ClfsTarget"]
        unknown=None,  # type: Optional["models.UnknownTarget"]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller
        """Create or update a Storage Target. This operation is allowed at any time, but if the Cache is down or unhealthy, the actual creation/modification of the Storage Target may be delayed until the Cache is healthy again.

        :param resource_group_name: Target resource group.
        :type resource_group_name: str
        :param cache_name: Name of Cache. Length of name must be not greater than 80 and chars must be
     in list of [-0-9a-zA-Z_] char class.
        :type cache_name: str
        :param storage_target_name: Name of the Storage Target. Length of name must be not greater than
     80 and chars must be in list of [-0-9a-zA-Z_] char class.
        :type storage_target_name: str
        :param junctions: List of Cache namespace junctions to target for namespace associations.
        :type junctions: list[~storage_cache_management_client.models.NamespaceJunction]
        :param target_type: Type of the Storage Target.
        :type target_type: str or ~storage_cache_management_client.models.StorageTargetType
        :param provisioning_state: ARM provisioning state, see https://github.com/Azure/azure-resource-
     manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property.
        :type provisioning_state: str or ~storage_cache_management_client.models.ProvisioningStateType
        :param nfs3: Properties when targetType is nfs3.
        :type nfs3: ~storage_cache_management_client.models.Nfs3Target
        :param clfs: Properties when targetType is clfs.
        :type clfs: ~storage_cache_management_client.models.ClfsTarget
        :param unknown: Properties when targetType is unknown.
        :type unknown: ~storage_cache_management_client.models.UnknownTarget
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either StorageTarget or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~storage_cache_management_client.models.StorageTarget]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.StorageTarget"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        raw_result = self._create_or_update_initial(
            resource_group_name=resource_group_name,
            cache_name=cache_name,
            storage_target_name=storage_target_name,
            junctions=junctions,
            target_type=target_type,
            provisioning_state=provisioning_state,
            nfs3=nfs3,
            clfs=clfs,
            unknown=unknown,
            cls=lambda x,y,z: x,
            **kwargs
        )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('StorageTarget', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets/{storageTargetName}'}  # type: ignore
