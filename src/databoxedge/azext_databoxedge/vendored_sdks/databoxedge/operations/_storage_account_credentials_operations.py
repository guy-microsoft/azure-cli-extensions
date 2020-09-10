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

class StorageAccountCredentialsOperations(object):
    """StorageAccountCredentialsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~data_box_edge_management_client.models
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

    def list_by_data_box_edge_device(
        self,
        device_name,  # type: str
        resource_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.StorageAccountCredentialList"]
        """Gets all the storage account credentials in a Data Box Edge/Data Box Gateway device.

        Gets all the storage account credentials in a Data Box Edge/Data Box Gateway device.

        :param device_name: The device name.
        :type device_name: str
        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either StorageAccountCredentialList or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~data_box_edge_management_client.models.StorageAccountCredentialList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.StorageAccountCredentialList"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-08-01"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_by_data_box_edge_device.metadata['url']  # type: ignore
                path_format_arguments = {
                    'deviceName': self._serialize.url("device_name", device_name, 'str'),
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('StorageAccountCredentialList', pipeline_response)
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
    list_by_data_box_edge_device.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/storageAccountCredentials'}  # type: ignore

    def get(
        self,
        device_name,  # type: str
        name,  # type: str
        resource_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.StorageAccountCredential"
        """Gets the properties of the specified storage account credential.

        :param device_name: The device name.
        :type device_name: str
        :param name: The storage account credential name.
        :type name: str
        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StorageAccountCredential, or the result of cls(response)
        :rtype: ~data_box_edge_management_client.models.StorageAccountCredential
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.StorageAccountCredential"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-08-01"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'deviceName': self._serialize.url("device_name", device_name, 'str'),
            'name': self._serialize.url("name", name, 'str'),
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

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('StorageAccountCredential', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/storageAccountCredentials/{name}'}  # type: ignore

    def _create_or_update_initial(
        self,
        device_name,  # type: str
        name,  # type: str
        resource_group_name,  # type: str
        alias,  # type: str
        ssl_status,  # type: Union[str, "models.SSLStatus"]
        account_type,  # type: Union[str, "models.AccountType"]
        user_name=None,  # type: Optional[str]
        account_key=None,  # type: Optional["models.AsymmetricEncryptedSecret"]
        connection_string=None,  # type: Optional[str]
        blob_domain_name=None,  # type: Optional[str]
        storage_account_id=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["models.StorageAccountCredential"]
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["models.StorageAccountCredential"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _storage_account_credential = models.StorageAccountCredential(alias=alias, user_name=user_name, account_key=account_key, connection_string=connection_string, ssl_status=ssl_status, blob_domain_name=blob_domain_name, account_type=account_type, storage_account_id=storage_account_id)
        api_version = "2019-08-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._create_or_update_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'deviceName': self._serialize.url("device_name", device_name, 'str'),
            'name': self._serialize.url("name", name, 'str'),
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

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_storage_account_credential, 'StorageAccountCredential')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('StorageAccountCredential', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_or_update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/storageAccountCredentials/{name}'}  # type: ignore

    def begin_create_or_update(
        self,
        device_name,  # type: str
        name,  # type: str
        resource_group_name,  # type: str
        alias,  # type: str
        ssl_status,  # type: Union[str, "models.SSLStatus"]
        account_type,  # type: Union[str, "models.AccountType"]
        user_name=None,  # type: Optional[str]
        account_key=None,  # type: Optional["models.AsymmetricEncryptedSecret"]
        connection_string=None,  # type: Optional[str]
        blob_domain_name=None,  # type: Optional[str]
        storage_account_id=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["models.StorageAccountCredential"]
        """Creates or updates the storage account credential.

        :param device_name: The device name.
        :type device_name: str
        :param name: The storage account credential name.
        :type name: str
        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param alias: Alias for the storage account.
        :type alias: str
        :param ssl_status: Signifies whether SSL needs to be enabled or not.
        :type ssl_status: str or ~data_box_edge_management_client.models.SSLStatus
        :param account_type: Type of storage accessed on the storage account.
        :type account_type: str or ~data_box_edge_management_client.models.AccountType
        :param user_name: Username for the storage account.
        :type user_name: str
        :param account_key: Encrypted storage key.
        :type account_key: ~data_box_edge_management_client.models.AsymmetricEncryptedSecret
        :param connection_string: Connection string for the storage account. Use this string if
         username and account key are not specified.
        :type connection_string: str
        :param blob_domain_name: Blob end point for private clouds.
        :type blob_domain_name: str
        :param storage_account_id: Id of the storage account.
        :type storage_account_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either StorageAccountCredential or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~data_box_edge_management_client.models.StorageAccountCredential]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.StorageAccountCredential"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._create_or_update_initial(
                device_name=device_name,
                name=name,
                resource_group_name=resource_group_name,
                alias=alias,
                ssl_status=ssl_status,
                account_type=account_type,
                user_name=user_name,
                account_key=account_key,
                connection_string=connection_string,
                blob_domain_name=blob_domain_name,
                storage_account_id=storage_account_id,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('StorageAccountCredential', pipeline_response)

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
    begin_create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/storageAccountCredentials/{name}'}  # type: ignore

    def _delete_initial(
        self,
        device_name,  # type: str
        name,  # type: str
        resource_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-08-01"

        # Construct URL
        url = self._delete_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'deviceName': self._serialize.url("device_name", device_name, 'str'),
            'name': self._serialize.url("name", name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
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

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/storageAccountCredentials/{name}'}  # type: ignore

    def begin_delete(
        self,
        device_name,  # type: str
        name,  # type: str
        resource_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller[None]
        """Deletes the storage account credential.

        :param device_name: The device name.
        :type device_name: str
        :param name: The storage account credential name.
        :type name: str
        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._delete_initial(
                device_name=device_name,
                name=name,
                resource_group_name=resource_group_name,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

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
    begin_delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/storageAccountCredentials/{name}'}  # type: ignore
