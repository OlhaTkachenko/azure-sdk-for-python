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
    from ._models_py3 import Permission
    from ._models_py3 import ProviderOperation
    from ._models_py3 import ProviderOperationsMetadata
    from ._models_py3 import ResourceType
    from ._models_py3 import RoleAssignment
    from ._models_py3 import RoleAssignmentCreateParameters
    from ._models_py3 import RoleAssignmentFilter
    from ._models_py3 import RoleAssignmentProperties
    from ._models_py3 import RoleAssignmentPropertiesWithScope
    from ._models_py3 import RoleDefinition
    from ._models_py3 import RoleDefinitionFilter
    from ._models_py3 import RoleDefinitionProperties
except (SyntaxError, ImportError):
    from ._models import Permission
    from ._models import ProviderOperation
    from ._models import ProviderOperationsMetadata
    from ._models import ResourceType
    from ._models import RoleAssignment
    from ._models import RoleAssignmentCreateParameters
    from ._models import RoleAssignmentFilter
    from ._models import RoleAssignmentProperties
    from ._models import RoleAssignmentPropertiesWithScope
    from ._models import RoleDefinition
    from ._models import RoleDefinitionFilter
    from ._models import RoleDefinitionProperties
from ._paged_models import PermissionPaged
from ._paged_models import ProviderOperationsMetadataPaged
from ._paged_models import RoleAssignmentPaged
from ._paged_models import RoleDefinitionPaged

__all__ = [
    'Permission',
    'ProviderOperation',
    'ProviderOperationsMetadata',
    'ResourceType',
    'RoleAssignment',
    'RoleAssignmentCreateParameters',
    'RoleAssignmentFilter',
    'RoleAssignmentProperties',
    'RoleAssignmentPropertiesWithScope',
    'RoleDefinition',
    'RoleDefinitionFilter',
    'RoleDefinitionProperties',
    'PermissionPaged',
    'ProviderOperationsMetadataPaged',
    'RoleAssignmentPaged',
    'RoleDefinitionPaged',
]
