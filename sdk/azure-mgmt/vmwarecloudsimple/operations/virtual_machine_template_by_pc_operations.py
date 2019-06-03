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

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class VirtualMachineTemplateByPCOperations(object):
    """VirtualMachineTemplateByPCOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Client API version. Constant value: "2019-04-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2019-04-01"

        self.config = config

    def get(
            self, pc_name, virtual_machine_template_name, custom_headers=None, raw=False, **operation_config):
        """Implements virtual machine template GET method.

        Returns virtual machine templates by its name.

        :param pc_name: The privae cloud name.
        :type pc_name: str
        :param virtual_machine_template_name: virtual machine template id
         (vsphereId)
        :type virtual_machine_template_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: VirtualMachineTemplate or ClientRawResponse if raw=true
        :rtype: ~microsoft.vmwarecloudsimple.models.VirtualMachineTemplate or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`CSRPErrorException<microsoft.vmwarecloudsimple.models.CSRPErrorException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'regionId': self._serialize.url("self.config.region_id", self.config.region_id, 'str'),
            'pcName': self._serialize.url("pc_name", pc_name, 'str'),
            'virtualMachineTemplateName': self._serialize.url("virtual_machine_template_name", virtual_machine_template_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 404]:
            raise models.CSRPErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VirtualMachineTemplate', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/providers/microsoft.vmwarecloudsimple/locations/{regionId}/privateclouds/{pcName}/virtualmachinetemplates/{virtualMachineTemplateName}'}
