# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class AllocationState(str, Enum):
    """Allocation state of the compute. Possible values are: steady - Indicates that the compute is
    not resizing. There are no changes to the number of compute nodes in the compute in progress. A
    compute enters this state when it is created and when no operations are being performed on the
    compute to change the number of compute nodes. resizing - Indicates that the compute is
    resizing; that is, compute nodes are being added to or removed from the compute.
    """

    steady = "Steady"
    resizing = "Resizing"

class ComputeType(str, Enum):
    """The type of compute
    """

    aks = "AKS"
    aml_compute = "AmlCompute"
    data_factory = "DataFactory"
    virtual_machine = "VirtualMachine"
    hd_insight = "HDInsight"
    databricks = "Databricks"
    data_lake_analytics = "DataLakeAnalytics"

class EncryptionStatus(str, Enum):
    """Indicates whether or not the encryption is enabled for the workspace.
    """

    enabled = "Enabled"
    disabled = "Disabled"

class NodeState(str, Enum):
    """State of the compute node. Values are idle, running, preparing, unusable, leaving and
    preempted.
    """

    idle = "idle"
    running = "running"
    preparing = "preparing"
    unusable = "unusable"
    leaving = "leaving"
    preempted = "preempted"

class PrivateEndpointConnectionProvisioningState(str, Enum):
    """The current provisioning state.
    """

    succeeded = "Succeeded"
    creating = "Creating"
    deleting = "Deleting"
    failed = "Failed"

class PrivateEndpointServiceConnectionStatus(str, Enum):
    """The private endpoint connection status.
    """

    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"
    disconnected = "Disconnected"
    timeout = "Timeout"

class ProvisioningState(str, Enum):
    """The current deployment state of workspace resource. The provisioningState is to indicate states
    for resource provisioning.
    """

    unknown = "Unknown"
    updating = "Updating"
    creating = "Creating"
    deleting = "Deleting"
    succeeded = "Succeeded"
    failed = "Failed"
    canceled = "Canceled"

class ReasonCode(str, Enum):
    """The reason for the restriction.
    """

    not_specified = "NotSpecified"
    not_available_for_region = "NotAvailableForRegion"
    not_available_for_subscription = "NotAvailableForSubscription"

class RemoteLoginPortPublicAccess(str, Enum):
    """State of the public SSH port. Possible values are: Disabled - Indicates that the public ssh
    port is closed on all nodes of the cluster. Enabled - Indicates that the public ssh port is
    open on all nodes of the cluster. NotSpecified - Indicates that the public ssh port is closed
    on all nodes of the cluster if VNet is defined, else is open all public nodes. It can be
    default only during cluster creation time, after creation it will be either enabled or
    disabled.
    """

    enabled = "Enabled"
    disabled = "Disabled"
    not_specified = "NotSpecified"

class ResourceIdentityType(str, Enum):
    """The identity type.
    """

    system_assigned = "SystemAssigned"
    user_assigned = "UserAssigned"
    system_assigned_user_assigned = "SystemAssigned,UserAssigned"
    none = "None"

class SslConfigurationStatus(str, Enum):
    """Enable or disable ssl for scoring
    """

    disabled = "Disabled"
    enabled = "Enabled"

class Status(str, Enum):
    """Status of update workspace quota.
    """

    undefined = "Undefined"
    success = "Success"
    failure = "Failure"
    invalid_quota_below_cluster_minimum = "InvalidQuotaBelowClusterMinimum"
    invalid_quota_exceeds_subscription_limit = "InvalidQuotaExceedsSubscriptionLimit"
    invalid_vm_family_name = "InvalidVMFamilyName"
    operation_not_supported_for_sku = "OperationNotSupportedForSku"
    operation_not_enabled_for_region = "OperationNotEnabledForRegion"

class UnderlyingResourceAction(str, Enum):

    delete = "Delete"
    detach = "Detach"

class VmPriority(str, Enum):
    """Virtual Machine priority
    """

    dedicated = "Dedicated"
    low_priority = "LowPriority"
