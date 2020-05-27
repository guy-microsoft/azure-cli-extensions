# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Dict, List, Optional, Union

import msrest.serialization


class ApiKey(msrest.serialization.Model):
    """API key payload which is exposed in the request/response of the resource provider.

    :param key_name: Gets or sets the API key name.
    :type key_name: str
    :param value: Gets or sets the API key value.
    :type value: str
    """

    _attribute_map = {
        'key_name': {'key': 'keyName', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        key_name: Optional[str] = None,
        value: Optional[str] = None,
        **kwargs
    ):
        super(ApiKey, self).__init__(**kwargs)
        self.key_name = key_name
        self.value = value


class ApiKeyCollection(msrest.serialization.Model):
    """Collection of the API key payload which is exposed in the response of the resource provider.

    :param keys: Gets or sets the collection of API key.
    :type keys: list[~azure.mgmt.blockchain.models.ApiKey]
    """

    _attribute_map = {
        'keys': {'key': 'keys', 'type': '[ApiKey]'},
    }

    def __init__(
        self,
        *,
        keys: Optional[List["ApiKey"]] = None,
        **kwargs
    ):
        super(ApiKeyCollection, self).__init__(**kwargs)
        self.keys = keys


class Resource(msrest.serialization.Model):
    """The core properties of the resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the service - e.g. "Microsoft.Blockchain".
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class TrackedResource(Resource):
    """The resource model definition for a top level resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the service - e.g. "Microsoft.Blockchain".
    :vartype type: str
    :param location: The GEO location of the blockchain service.
    :type location: str
    :param tags: A set of tags. Tags of the service which is a list of key value pairs that
     describes the resource.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(TrackedResource, self).__init__(**kwargs)
        self.location = location
        self.tags = tags


class BlockchainMember(TrackedResource):
    """Payload of the blockchain member which is exposed in the request/response of the resource provider.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the service - e.g. "Microsoft.Blockchain".
    :vartype type: str
    :param location: The GEO location of the blockchain service.
    :type location: str
    :param tags: A set of tags. Tags of the service which is a list of key value pairs that
     describes the resource.
    :type tags: dict[str, str]
    :param sku: Gets or sets the blockchain member Sku.
    :type sku: ~azure.mgmt.blockchain.models.Sku
    :param protocol: Gets or sets the blockchain protocol. Possible values include: "NotSpecified",
     "Parity", "Quorum", "Corda".
    :type protocol: str or ~azure.mgmt.blockchain.models.BlockchainProtocol
    :param validator_nodes_sku: Gets or sets the blockchain validator nodes Sku.
    :type validator_nodes_sku: ~azure.mgmt.blockchain.models.BlockchainMemberNodesSku
    :ivar provisioning_state: Gets or sets the blockchain member provision state. Possible values
     include: "NotSpecified", "Updating", "Deleting", "Succeeded", "Failed", "Stale".
    :vartype provisioning_state: str or
     ~azure.mgmt.blockchain.models.BlockchainMemberProvisioningState
    :ivar dns: Gets the dns endpoint of the blockchain member.
    :vartype dns: str
    :ivar user_name: Gets the auth user name of the blockchain member.
    :vartype user_name: str
    :param password: Sets the basic auth password of the blockchain member.
    :type password: str
    :param consortium: Gets or sets the consortium for the blockchain member.
    :type consortium: str
    :ivar consortium_management_account_address: Gets the managed consortium management account
     address.
    :vartype consortium_management_account_address: str
    :param consortium_management_account_password: Sets the managed consortium management account
     password.
    :type consortium_management_account_password: str
    :param consortium_role: Gets the role of the member in the consortium.
    :type consortium_role: str
    :param consortium_member_display_name: Gets the display name of the member in the consortium.
    :type consortium_member_display_name: str
    :ivar root_contract_address: Gets the Ethereum root contract address of the blockchain.
    :vartype root_contract_address: str
    :ivar public_key: Gets the public key of the blockchain member (default transaction node).
    :vartype public_key: str
    :param firewall_rules: Gets or sets firewall rules.
    :type firewall_rules: list[~azure.mgmt.blockchain.models.FirewallRule]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'dns': {'readonly': True},
        'user_name': {'readonly': True},
        'consortium_management_account_address': {'readonly': True},
        'root_contract_address': {'readonly': True},
        'public_key': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'protocol': {'key': 'properties.protocol', 'type': 'str'},
        'validator_nodes_sku': {'key': 'properties.validatorNodesSku', 'type': 'BlockchainMemberNodesSku'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'dns': {'key': 'properties.dns', 'type': 'str'},
        'user_name': {'key': 'properties.userName', 'type': 'str'},
        'password': {'key': 'properties.password', 'type': 'str'},
        'consortium': {'key': 'properties.consortium', 'type': 'str'},
        'consortium_management_account_address': {'key': 'properties.consortiumManagementAccountAddress', 'type': 'str'},
        'consortium_management_account_password': {'key': 'properties.consortiumManagementAccountPassword', 'type': 'str'},
        'consortium_role': {'key': 'properties.consortiumRole', 'type': 'str'},
        'consortium_member_display_name': {'key': 'properties.consortiumMemberDisplayName', 'type': 'str'},
        'root_contract_address': {'key': 'properties.rootContractAddress', 'type': 'str'},
        'public_key': {'key': 'properties.publicKey', 'type': 'str'},
        'firewall_rules': {'key': 'properties.firewallRules', 'type': '[FirewallRule]'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        sku: Optional["Sku"] = None,
        protocol: Optional[Union[str, "BlockchainProtocol"]] = None,
        validator_nodes_sku: Optional["BlockchainMemberNodesSku"] = None,
        password: Optional[str] = None,
        consortium: Optional[str] = None,
        consortium_management_account_password: Optional[str] = None,
        consortium_role: Optional[str] = None,
        consortium_member_display_name: Optional[str] = None,
        firewall_rules: Optional[List["FirewallRule"]] = None,
        **kwargs
    ):
        super(BlockchainMember, self).__init__(location=location, tags=tags, **kwargs)
        self.sku = sku
        self.protocol = protocol
        self.validator_nodes_sku = validator_nodes_sku
        self.provisioning_state = None
        self.dns = None
        self.user_name = None
        self.password = password
        self.consortium = consortium
        self.consortium_management_account_address = None
        self.consortium_management_account_password = consortium_management_account_password
        self.consortium_role = consortium_role
        self.consortium_member_display_name = consortium_member_display_name
        self.root_contract_address = None
        self.public_key = None
        self.firewall_rules = firewall_rules


class BlockchainMemberCollection(msrest.serialization.Model):
    """Collection of the blockchain member payload which is exposed in the request/response of the resource provider.

    :param value: Gets or sets the collection of blockchain members.
    :type value: list[~azure.mgmt.blockchain.models.BlockchainMember]
    :param next_link: Gets or sets the URL, that the client should use to fetch the next page (per
     server side paging).
     It's null for now, added for future use.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[BlockchainMember]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["BlockchainMember"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(BlockchainMemberCollection, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class BlockchainMemberNodesSku(msrest.serialization.Model):
    """Payload of the blockchain member nodes Sku for a blockchain member.

    :param capacity: Gets or sets the nodes capacity.
    :type capacity: int
    """

    _attribute_map = {
        'capacity': {'key': 'capacity', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        capacity: Optional[int] = None,
        **kwargs
    ):
        super(BlockchainMemberNodesSku, self).__init__(**kwargs)
        self.capacity = capacity


class TransactionNodePropertiesUpdate(msrest.serialization.Model):
    """Update the payload of the transaction node properties in the transaction node payload.

    :param password: Sets the transaction node dns endpoint basic auth password.
    :type password: str
    :param firewall_rules: Gets or sets the firewall rules.
    :type firewall_rules: list[~azure.mgmt.blockchain.models.FirewallRule]
    """

    _attribute_map = {
        'password': {'key': 'password', 'type': 'str'},
        'firewall_rules': {'key': 'firewallRules', 'type': '[FirewallRule]'},
    }

    def __init__(
        self,
        *,
        password: Optional[str] = None,
        firewall_rules: Optional[List["FirewallRule"]] = None,
        **kwargs
    ):
        super(TransactionNodePropertiesUpdate, self).__init__(**kwargs)
        self.password = password
        self.firewall_rules = firewall_rules


class BlockchainMemberPropertiesUpdate(TransactionNodePropertiesUpdate):
    """Update the payload of the blockchain member properties for a blockchain member.

    :param password: Sets the transaction node dns endpoint basic auth password.
    :type password: str
    :param firewall_rules: Gets or sets the firewall rules.
    :type firewall_rules: list[~azure.mgmt.blockchain.models.FirewallRule]
    :param consortium_management_account_password: Sets the managed consortium management account
     password.
    :type consortium_management_account_password: str
    """

    _attribute_map = {
        'password': {'key': 'password', 'type': 'str'},
        'firewall_rules': {'key': 'firewallRules', 'type': '[FirewallRule]'},
        'consortium_management_account_password': {'key': 'consortiumManagementAccountPassword', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        password: Optional[str] = None,
        firewall_rules: Optional[List["FirewallRule"]] = None,
        consortium_management_account_password: Optional[str] = None,
        **kwargs
    ):
        super(BlockchainMemberPropertiesUpdate, self).__init__(password=password, firewall_rules=firewall_rules, **kwargs)
        self.consortium_management_account_password = consortium_management_account_password


class BlockchainMemberUpdate(msrest.serialization.Model):
    """Update the payload of the blockchain member which is exposed in the request/response of the resource provider.

    :param tags: A set of tags. Tags of the service which is a list of key value pairs that
     describes the resource.
    :type tags: dict[str, str]
    :param password: Sets the transaction node dns endpoint basic auth password.
    :type password: str
    :param firewall_rules: Gets or sets the firewall rules.
    :type firewall_rules: list[~azure.mgmt.blockchain.models.FirewallRule]
    :param consortium_management_account_password: Sets the managed consortium management account
     password.
    :type consortium_management_account_password: str
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'password': {'key': 'properties.password', 'type': 'str'},
        'firewall_rules': {'key': 'properties.firewallRules', 'type': '[FirewallRule]'},
        'consortium_management_account_password': {'key': 'properties.consortiumManagementAccountPassword', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        password: Optional[str] = None,
        firewall_rules: Optional[List["FirewallRule"]] = None,
        consortium_management_account_password: Optional[str] = None,
        **kwargs
    ):
        super(BlockchainMemberUpdate, self).__init__(**kwargs)
        self.tags = tags
        self.password = password
        self.firewall_rules = firewall_rules
        self.consortium_management_account_password = consortium_management_account_password


class Consortium(msrest.serialization.Model):
    """Consortium payload.

    :param name: Gets or sets the blockchain member name.
    :type name: str
    :param protocol: Gets or sets the protocol for the consortium. Possible values include:
     "NotSpecified", "Parity", "Quorum", "Corda".
    :type protocol: str or ~azure.mgmt.blockchain.models.BlockchainProtocol
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'protocol': {'key': 'protocol', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        protocol: Optional[Union[str, "BlockchainProtocol"]] = None,
        **kwargs
    ):
        super(Consortium, self).__init__(**kwargs)
        self.name = name
        self.protocol = protocol


class ConsortiumCollection(msrest.serialization.Model):
    """Collection of the consortium payload.

    :param value: Gets or sets the collection of consortiums.
    :type value: list[~azure.mgmt.blockchain.models.Consortium]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Consortium]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Consortium"]] = None,
        **kwargs
    ):
        super(ConsortiumCollection, self).__init__(**kwargs)
        self.value = value


class ConsortiumMember(msrest.serialization.Model):
    """Consortium approval.

    :param name: Gets the consortium member name.
    :type name: str
    :param display_name: Gets the consortium member display name.
    :type display_name: str
    :param subscription_id: Gets the consortium member subscription id.
    :type subscription_id: str
    :param role: Gets the consortium member role.
    :type role: str
    :param status: Gets the consortium member status.
    :type status: str
    :param join_date: Gets the consortium member join date.
    :type join_date: ~datetime.datetime
    :param date_modified: Gets the consortium member modified date.
    :type date_modified: ~datetime.datetime
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'role': {'key': 'role', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'join_date': {'key': 'joinDate', 'type': 'iso-8601'},
        'date_modified': {'key': 'dateModified', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display_name: Optional[str] = None,
        subscription_id: Optional[str] = None,
        role: Optional[str] = None,
        status: Optional[str] = None,
        join_date: Optional[datetime.datetime] = None,
        date_modified: Optional[datetime.datetime] = None,
        **kwargs
    ):
        super(ConsortiumMember, self).__init__(**kwargs)
        self.name = name
        self.display_name = display_name
        self.subscription_id = subscription_id
        self.role = role
        self.status = status
        self.join_date = join_date
        self.date_modified = date_modified


class ConsortiumMemberCollection(msrest.serialization.Model):
    """Collection of consortium payload.

    :param value: Gets or sets the collection of consortiums.
    :type value: list[~azure.mgmt.blockchain.models.ConsortiumMember]
    :param next_link: Gets or sets the URL, that the client should use to fetch the next page (per
     server side paging).
     It's null for now, added for future use.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ConsortiumMember]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ConsortiumMember"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(ConsortiumMemberCollection, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class FirewallRule(msrest.serialization.Model):
    """Ip range for firewall rules.

    :param rule_name: Gets or sets the name of the firewall rules.
    :type rule_name: str
    :param start_ip_address: Gets or sets the start IP address of the firewall rule range.
    :type start_ip_address: str
    :param end_ip_address: Gets or sets the end IP address of the firewall rule range.
    :type end_ip_address: str
    """

    _attribute_map = {
        'rule_name': {'key': 'ruleName', 'type': 'str'},
        'start_ip_address': {'key': 'startIpAddress', 'type': 'str'},
        'end_ip_address': {'key': 'endIpAddress', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        rule_name: Optional[str] = None,
        start_ip_address: Optional[str] = None,
        end_ip_address: Optional[str] = None,
        **kwargs
    ):
        super(FirewallRule, self).__init__(**kwargs)
        self.rule_name = rule_name
        self.start_ip_address = start_ip_address
        self.end_ip_address = end_ip_address


class NameAvailability(msrest.serialization.Model):
    """Name availability payload which is exposed in the response of the resource provider.

    :param name_available: Gets or sets the value indicating whether the name is available.
    :type name_available: bool
    :param message: Gets or sets the message.
    :type message: str
    :param reason: Gets or sets the name availability reason. Possible values include:
     "NotSpecified", "AlreadyExists", "Invalid".
    :type reason: str or ~azure.mgmt.blockchain.models.NameAvailabilityReason
    """

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'message': {'key': 'message', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name_available: Optional[bool] = None,
        message: Optional[str] = None,
        reason: Optional[Union[str, "NameAvailabilityReason"]] = None,
        **kwargs
    ):
        super(NameAvailability, self).__init__(**kwargs)
        self.name_available = name_available
        self.message = message
        self.reason = reason


class NameAvailabilityRequest(msrest.serialization.Model):
    """Name availability request payload which is exposed in the request of the resource provider.

    :param name: Gets or sets the name to check.
    :type name: str
    :param type: Gets or sets the type of the resource to check.
    :type type: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        type: Optional[str] = None,
        **kwargs
    ):
        super(NameAvailabilityRequest, self).__init__(**kwargs)
        self.name = name
        self.type = type


class OperationResult(msrest.serialization.Model):
    """Operation result payload which is exposed in the response of the resource provider.

    :param name: Gets or sets the operation name.
    :type name: str
    :param start_time: Gets or sets the operation start time.
    :type start_time: ~datetime.datetime
    :param end_time: Gets or sets the operation end time.
    :type end_time: ~datetime.datetime
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        **kwargs
    ):
        super(OperationResult, self).__init__(**kwargs)
        self.name = name
        self.start_time = start_time
        self.end_time = end_time


class ResourceProviderOperation(msrest.serialization.Model):
    """Operation payload which is exposed in the response of the resource provider.

    :param origin: Gets or sets the origin.
    :type origin: str
    :param name: Gets or sets the operation name.
    :type name: str
    :param is_data_action: Gets or sets a value indicating whether the operation is a data action
     or not.
    :type is_data_action: bool
    :param display: Gets or sets operation display.
    :type display: ~azure.mgmt.blockchain.models.ResourceProviderOperationDisplay
    """

    _attribute_map = {
        'origin': {'key': 'origin', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
        'display': {'key': 'display', 'type': 'ResourceProviderOperationDisplay'},
    }

    def __init__(
        self,
        *,
        origin: Optional[str] = None,
        name: Optional[str] = None,
        is_data_action: Optional[bool] = None,
        display: Optional["ResourceProviderOperationDisplay"] = None,
        **kwargs
    ):
        super(ResourceProviderOperation, self).__init__(**kwargs)
        self.origin = origin
        self.name = name
        self.is_data_action = is_data_action
        self.display = display


class ResourceProviderOperationCollection(msrest.serialization.Model):
    """Collection of operation payload which is exposed in the response of the resource provider.

    :param value: Gets or sets the collection of operations.
    :type value: list[~azure.mgmt.blockchain.models.ResourceProviderOperation]
    :param next_link: Gets or sets the URL, that the client should use to fetch the next page (per
     server side paging).
     It's null for now, added for future use.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ResourceProviderOperation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ResourceProviderOperation"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(ResourceProviderOperationCollection, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ResourceProviderOperationDisplay(msrest.serialization.Model):
    """Operation display payload which is exposed in the response of the resource provider.

    :param provider: Gets or sets the name of the provider for display purposes.
    :type provider: str
    :param resource: Gets or sets the name of the resource type for display purposes.
    :type resource: str
    :param operation: Gets or sets the name of the operation for display purposes.
    :type operation: str
    :param description: Gets or sets the description of the provider for display purposes.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        super(ResourceProviderOperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class ResourceTypeSku(msrest.serialization.Model):
    """Resource type Sku.

    :param resource_type: Gets or sets the resource type.
    :type resource_type: str
    :param skus: Gets or sets the Skus.
    :type skus: list[~azure.mgmt.blockchain.models.SkuSetting]
    """

    _attribute_map = {
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'skus': {'key': 'skus', 'type': '[SkuSetting]'},
    }

    def __init__(
        self,
        *,
        resource_type: Optional[str] = None,
        skus: Optional[List["SkuSetting"]] = None,
        **kwargs
    ):
        super(ResourceTypeSku, self).__init__(**kwargs)
        self.resource_type = resource_type
        self.skus = skus


class ResourceTypeSkuCollection(msrest.serialization.Model):
    """Collection of the resource type Sku.

    :param value: Gets or sets the collection of resource type Sku.
    :type value: list[~azure.mgmt.blockchain.models.ResourceTypeSku]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ResourceTypeSku]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ResourceTypeSku"]] = None,
        **kwargs
    ):
        super(ResourceTypeSkuCollection, self).__init__(**kwargs)
        self.value = value


class Sku(msrest.serialization.Model):
    """Blockchain member Sku in payload.

    :param name: Gets or sets Sku name.
    :type name: str
    :param tier: Gets or sets Sku tier.
    :type tier: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        tier: Optional[str] = None,
        **kwargs
    ):
        super(Sku, self).__init__(**kwargs)
        self.name = name
        self.tier = tier


class SkuSetting(msrest.serialization.Model):
    """Sku Setting.

    :param name: Gets or sets the Sku name.
    :type name: str
    :param tier: Gets or sets the Sku tier.
    :type tier: str
    :param locations: Gets or sets the locations.
    :type locations: list[str]
    :param required_features: Gets or sets the required features.
    :type required_features: list[str]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
        'locations': {'key': 'locations', 'type': '[str]'},
        'required_features': {'key': 'requiredFeatures', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        tier: Optional[str] = None,
        locations: Optional[List[str]] = None,
        required_features: Optional[List[str]] = None,
        **kwargs
    ):
        super(SkuSetting, self).__init__(**kwargs)
        self.name = name
        self.tier = tier
        self.locations = locations
        self.required_features = required_features


class TransactionNode(Resource):
    """Payload of the transaction node which is the request/response of the resource provider.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the service - e.g. "Microsoft.Blockchain".
    :vartype type: str
    :param location: Gets or sets the transaction node location.
    :type location: str
    :ivar provisioning_state: Gets or sets the blockchain member provision state. Possible values
     include: "NotSpecified", "Updating", "Deleting", "Succeeded", "Failed".
    :vartype provisioning_state: str or ~azure.mgmt.blockchain.models.NodeProvisioningState
    :ivar dns: Gets or sets the transaction node dns endpoint.
    :vartype dns: str
    :ivar public_key: Gets or sets the transaction node public key.
    :vartype public_key: str
    :ivar user_name: Gets or sets the transaction node dns endpoint basic auth user name.
    :vartype user_name: str
    :param password: Sets the transaction node dns endpoint basic auth password.
    :type password: str
    :param firewall_rules: Gets or sets the firewall rules.
    :type firewall_rules: list[~azure.mgmt.blockchain.models.FirewallRule]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'dns': {'readonly': True},
        'public_key': {'readonly': True},
        'user_name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'dns': {'key': 'properties.dns', 'type': 'str'},
        'public_key': {'key': 'properties.publicKey', 'type': 'str'},
        'user_name': {'key': 'properties.userName', 'type': 'str'},
        'password': {'key': 'properties.password', 'type': 'str'},
        'firewall_rules': {'key': 'properties.firewallRules', 'type': '[FirewallRule]'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        password: Optional[str] = None,
        firewall_rules: Optional[List["FirewallRule"]] = None,
        **kwargs
    ):
        super(TransactionNode, self).__init__(**kwargs)
        self.location = location
        self.provisioning_state = None
        self.dns = None
        self.public_key = None
        self.user_name = None
        self.password = password
        self.firewall_rules = firewall_rules


class TransactionNodeCollection(msrest.serialization.Model):
    """Collection of transaction node payload which is exposed in the request/response of the resource provider.

    :param value: Gets or sets the collection of transaction nodes.
    :type value: list[~azure.mgmt.blockchain.models.TransactionNode]
    :param next_link: Gets or sets the URL, that the client should use to fetch the next page (per
     server side paging).
     It's null for now, added for future use.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[TransactionNode]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["TransactionNode"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(TransactionNodeCollection, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class TransactionNodeUpdate(msrest.serialization.Model):
    """Update the transaction node payload which is exposed in the request/response of the resource provider.

    :param password: Sets the transaction node dns endpoint basic auth password.
    :type password: str
    :param firewall_rules: Gets or sets the firewall rules.
    :type firewall_rules: list[~azure.mgmt.blockchain.models.FirewallRule]
    """

    _attribute_map = {
        'password': {'key': 'properties.password', 'type': 'str'},
        'firewall_rules': {'key': 'properties.firewallRules', 'type': '[FirewallRule]'},
    }

    def __init__(
        self,
        *,
        password: Optional[str] = None,
        firewall_rules: Optional[List["FirewallRule"]] = None,
        **kwargs
    ):
        super(TransactionNodeUpdate, self).__init__(**kwargs)
        self.password = password
        self.firewall_rules = firewall_rules
