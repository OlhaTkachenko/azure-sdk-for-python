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


class CheckSkuAvailabilityParameter(Model):
    """Check SKU availability parameter.

    All required parameters must be populated in order to send to Azure.

    :param skus: Required. The SKU of the resource.
    :type skus: list[str]
    :param kind: Required. The Kind of the resource.
    :type kind: str
    :param type: Required. The Type of the resource.
    :type type: str
    """

    _validation = {
        'skus': {'required': True},
        'kind': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'skus': {'key': 'skus', 'type': '[str]'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CheckSkuAvailabilityParameter, self).__init__(**kwargs)
        self.skus = kwargs.get('skus', None)
        self.kind = kwargs.get('kind', None)
        self.type = kwargs.get('type', None)
