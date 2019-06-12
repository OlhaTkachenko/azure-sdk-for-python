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

from msrest.serialization import Model


class OperationProperties(Model):
    """Properties of an operation supported by the resource provider.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar description: The description of the resource provider.
    :vartype description: str
    :ivar operation: This operation name.
    :vartype operation: str
    :ivar provider: The provider name.
    :vartype provider: str
    :ivar resource: The resource name.
    :vartype resource: str
    """

    _validation = {
        'description': {'readonly': True},
        'operation': {'readonly': True},
        'provider': {'readonly': True},
        'resource': {'readonly': True},
    }

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OperationProperties, self).__init__(**kwargs)
        self.description = None
        self.operation = None
        self.provider = None
        self.resource = None
