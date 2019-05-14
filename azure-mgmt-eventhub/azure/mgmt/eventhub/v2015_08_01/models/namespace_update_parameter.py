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


class NamespaceUpdateParameter(Model):
    """Parameters supplied to the Patch/update Namespace operation.

    :param tags: Resource tags
    :type tags: dict[str, str]
    :param sku: The sku of the created Namespace
    :type sku: ~azure.mgmt.eventhub.v2015_08_01.models.Sku
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
    }

    def __init__(self, **kwargs):
        super(NamespaceUpdateParameter, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.sku = kwargs.get('sku', None)