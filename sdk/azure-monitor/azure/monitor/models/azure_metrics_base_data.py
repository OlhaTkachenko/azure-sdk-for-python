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


class AzureMetricsBaseData(Model):
    """AzureMetricsBaseData.

    All required parameters must be populated in order to send to Azure.

    :param metric: Required. Gets or sets the Metric name
    :type metric: str
    :param namespace: Required. Gets or sets the Metric namespace
    :type namespace: str
    :param dim_names: Gets or sets the list of dimension names (optional)
    :type dim_names: list[str]
    :param series: Required. Gets or sets the list of time series data for the
     metric (one per unique dimension combination)
    :type series: list[~azure.monitor.models.AzureTimeSeriesData]
    """

    _validation = {
        'metric': {'required': True},
        'namespace': {'required': True},
        'series': {'required': True},
    }

    _attribute_map = {
        'metric': {'key': 'metric', 'type': 'str'},
        'namespace': {'key': 'namespace', 'type': 'str'},
        'dim_names': {'key': 'dimNames', 'type': '[str]'},
        'series': {'key': 'series', 'type': '[AzureTimeSeriesData]'},
    }

    def __init__(self, **kwargs):
        super(AzureMetricsBaseData, self).__init__(**kwargs)
        self.metric = kwargs.get('metric', None)
        self.namespace = kwargs.get('namespace', None)
        self.dim_names = kwargs.get('dim_names', None)
        self.series = kwargs.get('series', None)
