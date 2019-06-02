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


class LogicAppReceiver(Model):
    """A logic app receiver.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the logic app receiver. Names must be
     unique across all receivers within an action group.
    :type name: str
    :param resource_id: Required. The azure resource id of the logic app
     receiver.
    :type resource_id: str
    :param callback_url: Required. The callback url where http request sent
     to.
    :type callback_url: str
    :param use_common_alert_schema: Required. Indicates whether to use common
     alert schema.
    :type use_common_alert_schema: bool
    """

    _validation = {
        'name': {'required': True},
        'resource_id': {'required': True},
        'callback_url': {'required': True},
        'use_common_alert_schema': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'callback_url': {'key': 'callbackUrl', 'type': 'str'},
        'use_common_alert_schema': {'key': 'useCommonAlertSchema', 'type': 'bool'},
    }

    def __init__(self, *, name: str, resource_id: str, callback_url: str, use_common_alert_schema: bool, **kwargs) -> None:
        super(LogicAppReceiver, self).__init__(**kwargs)
        self.name = name
        self.resource_id = resource_id
        self.callback_url = callback_url
        self.use_common_alert_schema = use_common_alert_schema
