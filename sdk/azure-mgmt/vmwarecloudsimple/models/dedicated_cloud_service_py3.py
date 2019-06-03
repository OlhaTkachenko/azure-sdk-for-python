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


class DedicatedCloudService(Model):
    """Dedicated cloud service model.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id:
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/dedicatedcloudservices/{dedicatedCloudServiceName}
    :vartype id: str
    :param location: Required. Azure region
    :type location: str
    :ivar name: {dedicatedCloudServiceName}
    :vartype name: str
    :param plan: The plan
    :type plan: ~microsoft.vmwarecloudsimple.models.Plan
    :param gateway_subnet: Required. gateway Subnet for the account. It will
     collect the subnet address and always treat it as /28
    :type gateway_subnet: str
    :ivar is_account_onboarded: indicates whether account onboarded or not in
     a given region by nwiaas. Possible values include: 'notOnBoarded',
     'onBoarded', 'onBoardingFailed', 'onBoarding'
    :vartype is_account_onboarded: str or
     ~microsoft.vmwarecloudsimple.models.OnboardingStatus
    :param nodes: total nodes purchased
    :type nodes: int
    :param service_url: link to a service management web portal
    :type service_url: str
    :param tags: The list of tags
    :type tags: dict[str, str]
    :ivar type: {resourceProviderNamespace}/{resourceType}
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'location': {'required': True},
        'name': {'readonly': True, 'pattern': r'^[-a-zA-Z0-9]+$'},
        'gateway_subnet': {'required': True},
        'is_account_onboarded': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'plan': {'key': 'plan', 'type': 'Plan'},
        'gateway_subnet': {'key': 'properties.gatewaySubnet', 'type': 'str'},
        'is_account_onboarded': {'key': 'properties.isAccountOnboarded', 'type': 'OnboardingStatus'},
        'nodes': {'key': 'properties.nodes', 'type': 'int'},
        'service_url': {'key': 'properties.serviceURL', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, *, location: str, gateway_subnet: str, plan=None, nodes: int=None, service_url: str=None, tags=None, **kwargs) -> None:
        super(DedicatedCloudService, self).__init__(**kwargs)
        self.id = None
        self.location = location
        self.name = None
        self.plan = plan
        self.gateway_subnet = gateway_subnet
        self.is_account_onboarded = None
        self.nodes = nodes
        self.service_url = service_url
        self.tags = tags
        self.type = None
