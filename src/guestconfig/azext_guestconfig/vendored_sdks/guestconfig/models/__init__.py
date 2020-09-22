# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AssignmentInfo
    from ._models_py3 import AssignmentReportDetails
    from ._models_py3 import AssignmentReportResource
    from ._models_py3 import AssignmentReportResourceComplianceReason
    from ._models_py3 import ConfigurationInfo
    from ._models_py3 import ConfigurationParameter
    from ._models_py3 import ConfigurationSetting
    from ._models_py3 import ErrorResponse
    from ._models_py3 import ErrorResponseError
    from ._models_py3 import GuestConfigurationAssignment
    from ._models_py3 import GuestConfigurationAssignmentList
    from ._models_py3 import GuestConfigurationAssignmentReport
    from ._models_py3 import GuestConfigurationAssignmentReportList
    from ._models_py3 import GuestConfigurationAssignmentReportProperties
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationList
    from ._models_py3 import ProxyResource
    from ._models_py3 import Resource
    from ._models_py3 import VmInfo
except (SyntaxError, ImportError):
    from ._models import AssignmentInfo  # type: ignore
    from ._models import AssignmentReportDetails  # type: ignore
    from ._models import AssignmentReportResource  # type: ignore
    from ._models import AssignmentReportResourceComplianceReason  # type: ignore
    from ._models import ConfigurationInfo  # type: ignore
    from ._models import ConfigurationParameter  # type: ignore
    from ._models import ConfigurationSetting  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import ErrorResponseError  # type: ignore
    from ._models import GuestConfigurationAssignment  # type: ignore
    from ._models import GuestConfigurationAssignmentList  # type: ignore
    from ._models import GuestConfigurationAssignmentReport  # type: ignore
    from ._models import GuestConfigurationAssignmentReportList  # type: ignore
    from ._models import GuestConfigurationAssignmentReportProperties  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationList  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import VmInfo  # type: ignore

from ._guest_configuration_client_enums import (
    ActionAfterReboot,
    AllowModuleOverwrite,
    ComplianceStatus,
    ConfigurationMode,
    Kind,
    ProvisioningState,
    RebootIfNeeded,
    Type,
)

__all__ = [
    'AssignmentInfo',
    'AssignmentReportDetails',
    'AssignmentReportResource',
    'AssignmentReportResourceComplianceReason',
    'ConfigurationInfo',
    'ConfigurationParameter',
    'ConfigurationSetting',
    'ErrorResponse',
    'ErrorResponseError',
    'GuestConfigurationAssignment',
    'GuestConfigurationAssignmentList',
    'GuestConfigurationAssignmentReport',
    'GuestConfigurationAssignmentReportList',
    'GuestConfigurationAssignmentReportProperties',
    'Operation',
    'OperationDisplay',
    'OperationList',
    'ProxyResource',
    'Resource',
    'VmInfo',
    'ActionAfterReboot',
    'AllowModuleOverwrite',
    'ComplianceStatus',
    'ConfigurationMode',
    'Kind',
    'ProvisioningState',
    'RebootIfNeeded',
    'Type',
]
