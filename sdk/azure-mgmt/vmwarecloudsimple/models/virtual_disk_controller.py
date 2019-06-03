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


class VirtualDiskController(Model):
    """Virtual disk controller model.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Controller's id
    :vartype id: str
    :ivar name: The display name of Controller
    :vartype name: str
    :ivar sub_type: dik controller subtype (VMWARE_PARAVIRTUAL, BUS_PARALEL,
     LSI_PARALEL, LSI_SAS)
    :vartype sub_type: str
    :ivar type: disk controller type (SCSI)
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'sub_type': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'sub_type': {'key': 'subType', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VirtualDiskController, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.sub_type = None
        self.type = None
