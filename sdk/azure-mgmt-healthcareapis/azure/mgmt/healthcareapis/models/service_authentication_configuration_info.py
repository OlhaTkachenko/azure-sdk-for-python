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


class ServiceAuthenticationConfigurationInfo(Model):
    """Authentication configuration information.

    :param authority: The authority url for the service
    :type authority: str
    :param audience: The audience url for the service
    :type audience: str
    :param smart_proxy_enabled: If the SMART on FHIR proxy is enabled
    :type smart_proxy_enabled: bool
    """

    _attribute_map = {
        'authority': {'key': 'authority', 'type': 'str'},
        'audience': {'key': 'audience', 'type': 'str'},
        'smart_proxy_enabled': {'key': 'smartProxyEnabled', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(ServiceAuthenticationConfigurationInfo, self).__init__(**kwargs)
        self.authority = kwargs.get('authority', None)
        self.audience = kwargs.get('audience', None)
        self.smart_proxy_enabled = kwargs.get('smart_proxy_enabled', None)
