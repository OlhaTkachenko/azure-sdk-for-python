# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from .sku_py3 import Sku
    from .cognitive_services_account_create_parameters_py3 import CognitiveServicesAccountCreateParameters
    from .cognitive_services_account_update_parameters_py3 import CognitiveServicesAccountUpdateParameters
    from .cognitive_services_account_py3 import CognitiveServicesAccount
    from .cognitive_services_account_keys_py3 import CognitiveServicesAccountKeys
    from .regenerate_key_parameters_py3 import RegenerateKeyParameters
    from .cognitive_services_resource_and_sku_py3 import CognitiveServicesResourceAndSku
    from .cognitive_services_account_enumerate_skus_result_py3 import CognitiveServicesAccountEnumerateSkusResult
    from .metric_name_py3 import MetricName
    from .usage_py3 import Usage
    from .usages_result_py3 import UsagesResult
    from .error_body_py3 import ErrorBody
    from .error_py3 import Error, ErrorException
    from .operation_display_info_py3 import OperationDisplayInfo
    from .operation_entity_py3 import OperationEntity
    from .check_sku_availability_parameter_py3 import CheckSkuAvailabilityParameter
    from .check_sku_availability_result_py3 import CheckSkuAvailabilityResult
    from .check_sku_availability_result_list_py3 import CheckSkuAvailabilityResultList
    from .resource_sku_restriction_info_py3 import ResourceSkuRestrictionInfo
    from .resource_sku_restrictions_py3 import ResourceSkuRestrictions
    from .resource_sku_py3 import ResourceSku
except (SyntaxError, ImportError):
    from .sku import Sku
    from .cognitive_services_account_create_parameters import CognitiveServicesAccountCreateParameters
    from .cognitive_services_account_update_parameters import CognitiveServicesAccountUpdateParameters
    from .cognitive_services_account import CognitiveServicesAccount
    from .cognitive_services_account_keys import CognitiveServicesAccountKeys
    from .regenerate_key_parameters import RegenerateKeyParameters
    from .cognitive_services_resource_and_sku import CognitiveServicesResourceAndSku
    from .cognitive_services_account_enumerate_skus_result import CognitiveServicesAccountEnumerateSkusResult
    from .metric_name import MetricName
    from .usage import Usage
    from .usages_result import UsagesResult
    from .error_body import ErrorBody
    from .error import Error, ErrorException
    from .operation_display_info import OperationDisplayInfo
    from .operation_entity import OperationEntity
    from .check_sku_availability_parameter import CheckSkuAvailabilityParameter
    from .check_sku_availability_result import CheckSkuAvailabilityResult
    from .check_sku_availability_result_list import CheckSkuAvailabilityResultList
    from .resource_sku_restriction_info import ResourceSkuRestrictionInfo
    from .resource_sku_restrictions import ResourceSkuRestrictions
    from .resource_sku import ResourceSku
from .cognitive_services_account_paged import CognitiveServicesAccountPaged
from .resource_sku_paged import ResourceSkuPaged
from .operation_entity_paged import OperationEntityPaged
from .cognitive_services_management_client_enums import (
    SkuTier,
    ProvisioningState,
    KeyName,
    UnitType,
    QuotaUsageStatus,
    ResourceSkuRestrictionsType,
    ResourceSkuRestrictionsReasonCode,
)

__all__ = [
    'Sku',
    'CognitiveServicesAccountCreateParameters',
    'CognitiveServicesAccountUpdateParameters',
    'CognitiveServicesAccount',
    'CognitiveServicesAccountKeys',
    'RegenerateKeyParameters',
    'CognitiveServicesResourceAndSku',
    'CognitiveServicesAccountEnumerateSkusResult',
    'MetricName',
    'Usage',
    'UsagesResult',
    'ErrorBody',
    'Error', 'ErrorException',
    'OperationDisplayInfo',
    'OperationEntity',
    'CheckSkuAvailabilityParameter',
    'CheckSkuAvailabilityResult',
    'CheckSkuAvailabilityResultList',
    'ResourceSkuRestrictionInfo',
    'ResourceSkuRestrictions',
    'ResourceSku',
    'CognitiveServicesAccountPaged',
    'ResourceSkuPaged',
    'OperationEntityPaged',
    'SkuTier',
    'ProvisioningState',
    'KeyName',
    'UnitType',
    'QuotaUsageStatus',
    'ResourceSkuRestrictionsType',
    'ResourceSkuRestrictionsReasonCode',
]
