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


class ContainerServiceCredentials(Model):
    """Information about the Azure Container Registry which contains the images
    deployed to the cluster.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar acs_kube_config: The ACS kube config file.
    :vartype acs_kube_config: str
    :ivar service_principal_configuration: Service principal configuration
     used by Kubernetes.
    :vartype service_principal_configuration:
     ~azure.mgmt.machinelearningcompute.models.ServicePrincipalProperties
    :ivar image_pull_secret_name: The ACR image pull secret name which was
     created in Kubernetes.
    :vartype image_pull_secret_name: str
    """

    _validation = {
        'acs_kube_config': {'readonly': True},
        'service_principal_configuration': {'readonly': True},
        'image_pull_secret_name': {'readonly': True},
    }

    _attribute_map = {
        'acs_kube_config': {'key': 'acsKubeConfig', 'type': 'str'},
        'service_principal_configuration': {'key': 'servicePrincipalConfiguration', 'type': 'ServicePrincipalProperties'},
        'image_pull_secret_name': {'key': 'imagePullSecretName', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ContainerServiceCredentials, self).__init__(**kwargs)
        self.acs_kube_config = None
        self.service_principal_configuration = None
        self.image_pull_secret_name = None
