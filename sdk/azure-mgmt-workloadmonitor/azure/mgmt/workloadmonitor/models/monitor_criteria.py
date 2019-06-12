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


class MonitorCriteria(Model):
    """Criteria for monitor configuration.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar health_state: Target health state of the criteria. Possible values
     include: 'Error', 'Warning', 'Success', 'Unknown', 'Uninitialized'
    :vartype health_state: str or
     ~azure.mgmt.workloadmonitor.models.HealthState
    :ivar threshold: Threshold value for this criteria
    :vartype threshold: float
    :ivar comparison_operator: Comparison enum on threshold of this criteria.
     Possible values include: 'Equals', 'GreaterThan', 'GreaterThanOrEqual',
     'LessThan', 'LessThanOrEqual', 'NotEquals'
    :vartype comparison_operator: str or
     ~azure.mgmt.workloadmonitor.models.Operator
    """

    _validation = {
        'health_state': {'readonly': True},
        'threshold': {'readonly': True},
        'comparison_operator': {'readonly': True},
    }

    _attribute_map = {
        'health_state': {'key': 'healthState', 'type': 'HealthState'},
        'threshold': {'key': 'threshold', 'type': 'float'},
        'comparison_operator': {'key': 'comparisonOperator', 'type': 'Operator'},
    }

    def __init__(self, **kwargs):
        super(MonitorCriteria, self).__init__(**kwargs)
        self.health_state = None
        self.threshold = None
        self.comparison_operator = None
