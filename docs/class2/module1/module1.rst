CIS and ScaleN (N+1)
===========================

**Description**: 
The ScaleN architecture allows you to create a redundant system configuration for multiple BIG-IP devices on a network.This guide will focus on the tips and best practices for building this in a lab for testing. For a full guide to the installation, please refer to the official documentation on |askf5|_ or |clouddocs|_. 

**Prerequisites**: 

- BIG-IP licenses and basic understanding of the BIG-IP system.
- Existing Kubernetes cluster and basic understanding of the Kubernetes platform.

**Sample Diagram**:

|mod-1-1|

Configuration tips and caveats
------------------
- Ensure proper disaggregation in front of BIG-IP
- Ensure that AS3 Tenant/Partition names *do not* overlap
- Ensure that AS3 declaration specifies below:
    - trafficGroup property
        - number assignment method example: TG1=prod, TG2=staging
        - *details below*
    - shareNodes property
        - To allow Nodeport IPs to be configured in /Common so other partitions can use it
        - *details below*
- Only Nodeport or potentially Calico BGP could work
    - auto-sync and Flannel cannot be configured together
- Multi K8s Cluster with 1 CIS deployment per cluster
- BIG-IP in scalen A/A/S with auto config-sync (optional)
- Ensure no more than 3 CIS point to a single VE per internal testing
- Configure HA order to favor a standby before converging TGs on a single VE
- Consider multiple regions of cluster and use GSLB (DNS) for load balancing between regions
- For IPv6 addresses, use hostAliases as CIS does not connect right now to an IPv6 address

**trafficGroup property**:
You can specify the traffic group associated with any virtual address so that all associated objects float with that traffic group in a ScaleN (N+1) configuration. See |clouddocs_tg|_ for more details. 

You can then reference the :code:`Service_Address` name for the :code:`virtualAddresses` property for your virtual server. 

.. note: The :code:`"use"` pointer references an AS3 object in the same declaration. On the other hand you can use the :code:`"bigip"` pointer for objects that already exist on BIG-IP. 

**shareNodes property**: 
You can configure shareNodes so that multiple tenants can use the same node IP, which gets created in the /Common partition. See |clouddocs_sn|_ for more details. 

**serviceMain**:
If you use a template with a value of http, https, tcp, udp, or l4, you MUST specify an object with the matching Service class Service_HTTP, Service_HTTPS, Service_TCP, Service_UDP, or Service_L4 and name it serviceMain as described in the following Service Class section. See |clouddocs_sm|_ for more details.

.. note: When using the generic template, your virtual server name must not be “serviceMain”


Sample Configuration:

.. code-block:: yaml
   :emphasize-lines: 32,47

    kind: ConfigMap
    apiVersion: v1
    metadata:
    name: stg-as3-declaration-demo
    namespace: kube-system
    labels:
        f5type: virtual-server
        as3: "true"
    data:
    template: |
        {
        "class": "AS3",
        "action": "deploy",
        "persist": true,
        "declaration": {
            "class": "ADC",
            "schemaVersion": "3.18.0",
            "id": "demoapp",
            "label": "f5-istio",
            "remark": "An HTTP application",
            "stg_tenant": {
            "class": "Tenant",
            "stg_app": {
                "class": "Application",
                "template": "http",
                "stg_svc_addr": {
                    "class": "Service_Address",
                    "virtualAddress":  "240b:ab11:cd22:a101::10",
                    "arpEnabled": false,
                    "icmpEcho": "disable",
                    "routeAdvertisement": "any",
                    "trafficGroup": "/Common/traffic-group-2"
                },
                "serviceMain": {
                "class": "Service_HTTP",
                "virtualAddresses": [{"use": "stg_svc_addr"}],
                "pool": "stg_nginx_pool"
                },
                "stg_nginx_pool": {
                "class": "Pool",
                "monitors": [
                    "tcp"
                ],
                "members": [{
                    "servicePort": 80,
                    "serverAddresses": [],
                    "shareNodes": true
                }]
                }
                }
            }
            }
        }


.. |askf5| replace:: AskF5
.. _askf5: https://techdocs.f5.com/en-us/bigip-14-1-0/big-ip-device-service-clustering-administration-14-1-0/creating-an-active-active-configuration-using-the-configuration-utility.html#GUID-175E31E6-AEE5-47A1-A0FF-7DB6E3C4185E
.. |clouddocs| replace:: F5 Cloud Docs
.. _clouddocs: https://clouddocs.f5.com/training/community/adc/html/class2/module1/lab1.html
.. |clouddocs_tg| replace:: F5 Cloud Docs
.. _clouddocs_tg: https://clouddocs.f5.com/products/extensions/f5-appsvcs-extension/latest/refguide/schema-reference.html#service-address
.. |clouddocs_sn| replace:: F5 Cloud Docs
.. _clouddocs_sn: https://clouddocs.f5.com/products/extensions/f5-appsvcs-extension/latest/refguide/schema-reference.html#pool-member
.. |clouddocs_sm| replace:: F5 Cloud Docs
.. _clouddocs_sm: https://clouddocs.f5.com/products/extensions/f5-appsvcs-extension/latest/userguide/composing-a-declaration.html


.. |mod-1-1| image:: images/mod-1-1.png