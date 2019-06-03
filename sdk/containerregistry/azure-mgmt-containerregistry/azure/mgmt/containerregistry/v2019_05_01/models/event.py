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

from .event_info import EventInfo


class Event(EventInfo):
    """The event for a webhook.

    :param id: The event ID.
    :type id: str
    :param event_request_message: The event request message sent to the
     service URI.
    :type event_request_message:
     ~azure.mgmt.containerregistry.v2019_05_01.models.EventRequestMessage
    :param event_response_message: The event response message received from
     the service URI.
    :type event_response_message:
     ~azure.mgmt.containerregistry.v2019_05_01.models.EventResponseMessage
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'event_request_message': {'key': 'eventRequestMessage', 'type': 'EventRequestMessage'},
        'event_response_message': {'key': 'eventResponseMessage', 'type': 'EventResponseMessage'},
    }

    def __init__(self, **kwargs):
        super(Event, self).__init__(**kwargs)
        self.event_request_message = kwargs.get('event_request_message', None)
        self.event_response_message = kwargs.get('event_response_message', None)
