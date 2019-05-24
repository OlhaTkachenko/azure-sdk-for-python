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


class ServiceProviderResponseList(Model):
    """The list of bot service service providers response.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param next_link: The link used to get the next page of bot service
     service providers.
    :type next_link: str
    :ivar value: Gets the list of bot service service providers and their
     properties.
    :vartype value: list[~azure.mgmt.botservice.models.ServiceProvider]
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[ServiceProvider]'},
    }

    def __init__(self, **kwargs):
        super(ServiceProviderResponseList, self).__init__(**kwargs)
        self.next_link = kwargs.get('next_link', None)
        self.value = None