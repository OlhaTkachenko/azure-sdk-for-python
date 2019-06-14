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
from msrest.exceptions import HttpOperationError


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class ContainerHostMapping(Model):
    """Container host mapping object specifying the Container host resource ID and
    its associated Controller resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param container_host_resource_id: ARM ID of the Container Host resource
    :type container_host_resource_id: str
    :ivar mapped_controller_resource_id: ARM ID of the mapped Controller
     resource
    :vartype mapped_controller_resource_id: str
    """

    _validation = {
        'mapped_controller_resource_id': {'readonly': True},
    }

    _attribute_map = {
        'container_host_resource_id': {'key': 'containerHostResourceId', 'type': 'str'},
        'mapped_controller_resource_id': {'key': 'mappedControllerResourceId', 'type': 'str'},
    }

    def __init__(self, *, container_host_resource_id: str=None, **kwargs) -> None:
        super(ContainerHostMapping, self).__init__(**kwargs)
        self.container_host_resource_id = container_host_resource_id
        self.mapped_controller_resource_id = None


class Resource(Model):
    """An Azure resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class TrackedResource(Resource):
    """The resource model definition for a ARM tracked top level resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param tags: Tags for the Azure resource.
    :type tags: dict[str, str]
    :param location: Region where the Azure resource is located.
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, *, tags=None, location: str=None, **kwargs) -> None:
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = tags
        self.location = location


class Controller(TrackedResource):
    """Controller.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param tags: Tags for the Azure resource.
    :type tags: dict[str, str]
    :param location: Region where the Azure resource is located.
    :type location: str
    :ivar provisioning_state: Provisioning state of the Azure Dev Spaces
     Controller. Possible values include: 'Succeeded', 'Failed', 'Canceled',
     'Updating', 'Creating', 'Deleting', 'Deleted'
    :vartype provisioning_state: str or
     ~azure.mgmt.devspaces.models.ProvisioningState
    :ivar host_suffix: DNS suffix for public endpoints running in the Azure
     Dev Spaces Controller.
    :vartype host_suffix: str
    :ivar data_plane_fqdn: DNS name for accessing DataPlane services
    :vartype data_plane_fqdn: str
    :param target_container_host_resource_id: Required. Resource ID of the
     target container host
    :type target_container_host_resource_id: str
    :param target_container_host_credentials_base64: Required. Credentials of
     the target container host (base64).
    :type target_container_host_credentials_base64: str
    :param sku: Required.
    :type sku: ~azure.mgmt.devspaces.models.Sku
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'host_suffix': {'readonly': True},
        'data_plane_fqdn': {'readonly': True},
        'target_container_host_resource_id': {'required': True},
        'target_container_host_credentials_base64': {'required': True},
        'sku': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'host_suffix': {'key': 'properties.hostSuffix', 'type': 'str'},
        'data_plane_fqdn': {'key': 'properties.dataPlaneFqdn', 'type': 'str'},
        'target_container_host_resource_id': {'key': 'properties.targetContainerHostResourceId', 'type': 'str'},
        'target_container_host_credentials_base64': {'key': 'properties.targetContainerHostCredentialsBase64', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
    }

    def __init__(self, *, target_container_host_resource_id: str, target_container_host_credentials_base64: str, sku, tags=None, location: str=None, **kwargs) -> None:
        super(Controller, self).__init__(tags=tags, location=location, **kwargs)
        self.provisioning_state = None
        self.host_suffix = None
        self.data_plane_fqdn = None
        self.target_container_host_resource_id = target_container_host_resource_id
        self.target_container_host_credentials_base64 = target_container_host_credentials_base64
        self.sku = sku


class ControllerConnectionDetails(Model):
    """ControllerConnectionDetails.

    :param orchestrator_specific_connection_details:
    :type orchestrator_specific_connection_details:
     ~azure.mgmt.devspaces.models.OrchestratorSpecificConnectionDetails
    """

    _attribute_map = {
        'orchestrator_specific_connection_details': {'key': 'orchestratorSpecificConnectionDetails', 'type': 'OrchestratorSpecificConnectionDetails'},
    }

    def __init__(self, *, orchestrator_specific_connection_details=None, **kwargs) -> None:
        super(ControllerConnectionDetails, self).__init__(**kwargs)
        self.orchestrator_specific_connection_details = orchestrator_specific_connection_details


class ControllerConnectionDetailsList(Model):
    """ControllerConnectionDetailsList.

    :param connection_details_list: List of Azure Dev Spaces Controller
     connection details.
    :type connection_details_list:
     list[~azure.mgmt.devspaces.models.ControllerConnectionDetails]
    """

    _attribute_map = {
        'connection_details_list': {'key': 'connectionDetailsList', 'type': '[ControllerConnectionDetails]'},
    }

    def __init__(self, *, connection_details_list=None, **kwargs) -> None:
        super(ControllerConnectionDetailsList, self).__init__(**kwargs)
        self.connection_details_list = connection_details_list


class ControllerUpdateParameters(Model):
    """Parameters for updating an Azure Dev Spaces Controller.

    :param tags: Tags for the Azure Dev Spaces Controller.
    :type tags: dict[str, str]
    :param target_container_host_credentials_base64: Credentials of the target
     container host (base64).
    :type target_container_host_credentials_base64: str
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'target_container_host_credentials_base64': {'key': 'properties.targetContainerHostCredentialsBase64', 'type': 'str'},
    }

    def __init__(self, *, tags=None, target_container_host_credentials_base64: str=None, **kwargs) -> None:
        super(ControllerUpdateParameters, self).__init__(**kwargs)
        self.tags = tags
        self.target_container_host_credentials_base64 = target_container_host_credentials_base64


class DevSpacesErrorResponse(Model):
    """Error response indicates that the service is not able to process the
    incoming request. The reason is provided in the error message.

    :param error: The details of the error.
    :type error: ~azure.mgmt.devspaces.models.ErrorDetails
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDetails'},
    }

    def __init__(self, *, error=None, **kwargs) -> None:
        super(DevSpacesErrorResponse, self).__init__(**kwargs)
        self.error = error


class DevSpacesErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'DevSpacesErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(DevSpacesErrorResponseException, self).__init__(deserialize, response, 'DevSpacesErrorResponse', *args)


class ErrorDetails(Model):
    """ErrorDetails.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: Status code for the error.
    :vartype code: str
    :ivar message: Error message describing the error in detail.
    :vartype message: str
    :ivar target: The target of the particular error.
    :vartype target: str
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ErrorDetails, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None


class OrchestratorSpecificConnectionDetails(Model):
    """Base class for types that supply values used to connect to container
    orchestrators.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: KubernetesConnectionDetails

    All required parameters must be populated in order to send to Azure.

    :param instance_type: Required. Constant filled by server.
    :type instance_type: str
    """

    _validation = {
        'instance_type': {'required': True},
    }

    _attribute_map = {
        'instance_type': {'key': 'instanceType', 'type': 'str'},
    }

    _subtype_map = {
        'instance_type': {'Kubernetes': 'KubernetesConnectionDetails'}
    }

    def __init__(self, **kwargs) -> None:
        super(OrchestratorSpecificConnectionDetails, self).__init__(**kwargs)
        self.instance_type = None


class KubernetesConnectionDetails(OrchestratorSpecificConnectionDetails):
    """Contains information used to connect to a Kubernetes cluster.

    All required parameters must be populated in order to send to Azure.

    :param instance_type: Required. Constant filled by server.
    :type instance_type: str
    :param kube_config: Gets the kubeconfig for the cluster.
    :type kube_config: str
    """

    _validation = {
        'instance_type': {'required': True},
    }

    _attribute_map = {
        'instance_type': {'key': 'instanceType', 'type': 'str'},
        'kube_config': {'key': 'kubeConfig', 'type': 'str'},
    }

    def __init__(self, *, kube_config: str=None, **kwargs) -> None:
        super(KubernetesConnectionDetails, self).__init__(**kwargs)
        self.kube_config = kube_config
        self.instance_type = 'Kubernetes'


class ListConnectionDetailsParameters(Model):
    """Parameters for listing connection details of an Azure Dev Spaces
    Controller.

    All required parameters must be populated in order to send to Azure.

    :param target_container_host_resource_id: Required. Resource ID of the
     target container host mapped to the Azure Dev Spaces Controller.
    :type target_container_host_resource_id: str
    """

    _validation = {
        'target_container_host_resource_id': {'required': True},
    }

    _attribute_map = {
        'target_container_host_resource_id': {'key': 'targetContainerHostResourceId', 'type': 'str'},
    }

    def __init__(self, *, target_container_host_resource_id: str, **kwargs) -> None:
        super(ListConnectionDetailsParameters, self).__init__(**kwargs)
        self.target_container_host_resource_id = target_container_host_resource_id


class ResourceProviderOperationDefinition(Model):
    """ResourceProviderOperationDefinition.

    :param name: Resource provider operation name.
    :type name: str
    :param display:
    :type display:
     ~azure.mgmt.devspaces.models.ResourceProviderOperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'ResourceProviderOperationDisplay'},
    }

    def __init__(self, *, name: str=None, display=None, **kwargs) -> None:
        super(ResourceProviderOperationDefinition, self).__init__(**kwargs)
        self.name = name
        self.display = display


class ResourceProviderOperationDisplay(Model):
    """ResourceProviderOperationDisplay.

    :param provider: Name of the resource provider.
    :type provider: str
    :param resource: Name of the resource type.
    :type resource: str
    :param operation: Name of the resource provider operation.
    :type operation: str
    :param description: Description of the resource provider operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, *, provider: str=None, resource: str=None, operation: str=None, description: str=None, **kwargs) -> None:
        super(ResourceProviderOperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class Sku(Model):
    """Model representing SKU for Azure Dev Spaces Controller.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required. The name of the SKU for Azure Dev Spaces Controller.
     Default value: "S1" .
    :vartype name: str
    :param tier: The tier of the SKU for Azure Dev Spaces Controller. Possible
     values include: 'Standard'
    :type tier: str or ~azure.mgmt.devspaces.models.SkuTier
    """

    _validation = {
        'name': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    name = "S1"

    def __init__(self, *, tier=None, **kwargs) -> None:
        super(Sku, self).__init__(**kwargs)
        self.tier = tier
