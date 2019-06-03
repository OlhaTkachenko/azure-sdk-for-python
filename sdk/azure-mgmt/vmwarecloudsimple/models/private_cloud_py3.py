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


class PrivateCloud(Model):
    """Private cloud model.

    :param id: Azure Id, e.g.
     "/subscriptions/4da99247-a172-4ed6-8ae9-ebed2d12f839/providers/Microsoft.VMwareCloudSimple/privateClouds/cloud123"
    :type id: str
    :param location: Location where private cloud created, e.g "westus"
    :type location: str
    :param name: Private cloud name
    :type name: str
    :param availability_zone_id: Availability Zone id, e.g. "az1"
    :type availability_zone_id: str
    :param availability_zone_name: Availability Zone name, e.g. "Availability
     Zone 1"
    :type availability_zone_name: str
    :param clusters_number: Number of clusters
    :type clusters_number: int
    :param created_by: User's emails who created cloud
    :type created_by: str
    :param created_on: When private cloud was created
    :type created_on: datetime
    :param dns_servers: Array of DNS servers
    :type dns_servers: list[str]
    :param expires: Expiration date of PC
    :type expires: str
    :param nsx_type: Nsx Type, e.g. "Advanced"
    :type nsx_type: str
    :param placement_group_id: Placement Group id, e.g. "n1"
    :type placement_group_id: str
    :param placement_group_name: Placement Group name
    :type placement_group_name: str
    :param private_cloud_id: Id of a private cloud
    :type private_cloud_id: str
    :param resource_pools: The list of Resource Pools
    :type resource_pools:
     list[~microsoft.vmwarecloudsimple.models.ResourcePool]
    :param state: Private Cloud state, e.g. "operational"
    :type state: str
    :param total_cpu_cores: Number of cores
    :type total_cpu_cores: int
    :param total_nodes: Number of nodes
    :type total_nodes: int
    :param total_ram: Memory size
    :type total_ram: int
    :param total_storage: Disk space in TB
    :type total_storage: float
    :param private_cloud_properties_type: Virtualizaiton type e.g. "vSphere"
    :type private_cloud_properties_type: str
    :param v_sphere_version: e.g. "6.5u2"
    :type v_sphere_version: str
    :param vcenter_fqdn: FQDN for vcneter access e.g.
     "vcsa-4-westus.az.cloudsimple.io"
    :type vcenter_fqdn: str
    :param vcenter_refid: Vcenters' ip address
    :type vcenter_refid: str
    :param virtual_machine_templates: The list of Virtual Machine Templates
    :type virtual_machine_templates:
     list[~microsoft.vmwarecloudsimple.models.VirtualMachineTemplate]
    :param virtual_networks: The list of Virtual Networks
    :type virtual_networks:
     list[~microsoft.vmwarecloudsimple.models.VirtualNetwork]
    :param vr_ops_enabled: Is Vrops enabled/disabled
    :type vr_ops_enabled: bool
    :param type: Azure Resource type. Possible values include:
     'Microsoft.VMwareCloudSimple/privateClouds'
    :type type: str or
     ~microsoft.vmwarecloudsimple.models.PrivateCloudResourceType
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'availability_zone_id': {'key': 'properties.availabilityZoneId', 'type': 'str'},
        'availability_zone_name': {'key': 'properties.availabilityZoneName', 'type': 'str'},
        'clusters_number': {'key': 'properties.clustersNumber', 'type': 'int'},
        'created_by': {'key': 'properties.createdBy', 'type': 'str'},
        'created_on': {'key': 'properties.createdOn', 'type': 'iso-8601'},
        'dns_servers': {'key': 'properties.dnsServers', 'type': '[str]'},
        'expires': {'key': 'properties.expires', 'type': 'str'},
        'nsx_type': {'key': 'properties.nsxType', 'type': 'str'},
        'placement_group_id': {'key': 'properties.placementGroupId', 'type': 'str'},
        'placement_group_name': {'key': 'properties.placementGroupName', 'type': 'str'},
        'private_cloud_id': {'key': 'properties.privateCloudId', 'type': 'str'},
        'resource_pools': {'key': 'properties.resourcePools', 'type': '[ResourcePool]'},
        'state': {'key': 'properties.state', 'type': 'str'},
        'total_cpu_cores': {'key': 'properties.totalCpuCores', 'type': 'int'},
        'total_nodes': {'key': 'properties.totalNodes', 'type': 'int'},
        'total_ram': {'key': 'properties.totalRam', 'type': 'int'},
        'total_storage': {'key': 'properties.totalStorage', 'type': 'float'},
        'private_cloud_properties_type': {'key': 'properties.type', 'type': 'str'},
        'v_sphere_version': {'key': 'properties.vSphereVersion', 'type': 'str'},
        'vcenter_fqdn': {'key': 'properties.vcenterFqdn', 'type': 'str'},
        'vcenter_refid': {'key': 'properties.vcenterRefid', 'type': 'str'},
        'virtual_machine_templates': {'key': 'properties.virtualMachineTemplates', 'type': '[VirtualMachineTemplate]'},
        'virtual_networks': {'key': 'properties.virtualNetworks', 'type': '[VirtualNetwork]'},
        'vr_ops_enabled': {'key': 'properties.vrOpsEnabled', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'PrivateCloudResourceType'},
    }

    def __init__(self, *, id: str=None, location: str=None, name: str=None, availability_zone_id: str=None, availability_zone_name: str=None, clusters_number: int=None, created_by: str=None, created_on=None, dns_servers=None, expires: str=None, nsx_type: str=None, placement_group_id: str=None, placement_group_name: str=None, private_cloud_id: str=None, resource_pools=None, state: str=None, total_cpu_cores: int=None, total_nodes: int=None, total_ram: int=None, total_storage: float=None, private_cloud_properties_type: str=None, v_sphere_version: str=None, vcenter_fqdn: str=None, vcenter_refid: str=None, virtual_machine_templates=None, virtual_networks=None, vr_ops_enabled: bool=None, type=None, **kwargs) -> None:
        super(PrivateCloud, self).__init__(**kwargs)
        self.id = id
        self.location = location
        self.name = name
        self.availability_zone_id = availability_zone_id
        self.availability_zone_name = availability_zone_name
        self.clusters_number = clusters_number
        self.created_by = created_by
        self.created_on = created_on
        self.dns_servers = dns_servers
        self.expires = expires
        self.nsx_type = nsx_type
        self.placement_group_id = placement_group_id
        self.placement_group_name = placement_group_name
        self.private_cloud_id = private_cloud_id
        self.resource_pools = resource_pools
        self.state = state
        self.total_cpu_cores = total_cpu_cores
        self.total_nodes = total_nodes
        self.total_ram = total_ram
        self.total_storage = total_storage
        self.private_cloud_properties_type = private_cloud_properties_type
        self.v_sphere_version = v_sphere_version
        self.vcenter_fqdn = vcenter_fqdn
        self.vcenter_refid = vcenter_refid
        self.virtual_machine_templates = virtual_machine_templates
        self.virtual_networks = virtual_networks
        self.vr_ops_enabled = vr_ops_enabled
        self.type = type
