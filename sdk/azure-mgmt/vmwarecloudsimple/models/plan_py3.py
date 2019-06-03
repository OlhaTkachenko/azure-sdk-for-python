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


class Plan(Model):
    """The purchase plan for CloudSimple resources.

    :param name: Plan name
    :type name: str
    :param product: Plan product
    :type product: str
    :param publisher: Plan publisher
    :type publisher: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'product': {'key': 'product', 'type': 'str'},
        'publisher': {'key': 'publisher', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, product: str=None, publisher: str=None, **kwargs) -> None:
        super(Plan, self).__init__(**kwargs)
        self.name = name
        self.product = product
        self.publisher = publisher
