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


class AvailableOperationDisplayPropertyServiceSpecificationMetricsList(Model):
    """List of available operation display property service specification metrics.

    :param metric_specifications: Metric specifications of operation
    :type metric_specifications:
     list[~microsoft.vmwarecloudsimple.models.AvailableOperationDisplayPropertyServiceSpecificationMetricsItem]
    """

    _attribute_map = {
        'metric_specifications': {'key': 'metricSpecifications', 'type': '[AvailableOperationDisplayPropertyServiceSpecificationMetricsItem]'},
    }

    def __init__(self, **kwargs):
        super(AvailableOperationDisplayPropertyServiceSpecificationMetricsList, self).__init__(**kwargs)
        self.metric_specifications = kwargs.get('metric_specifications', None)
