IPv6 Support in CIS and F5 IPAM Controller
================================================


**Description**: 
This section will cover some best practices, tips, and caveats when configuring CIS and F5 IPAM Controller with manifest files using IPv6 addresses. 


Summary
------------------
BIG-IP itself supports IPv6 addresses for all objects. As of CIS v2.6.0, you can specify an IPv6 address in the deployment manifest that determines the BIG-IP address to connect to in the :code:`bigip_url` parameter. The new configuration parameter for the deployment manifest is called :code:`enable-ipv6` , which also enables use of IPv6 in custom resources such as VirtualServer, TransportServer and ServiceTypeLB service.

Example for BIG-IP URL in the CIS deployment manifest:

    .. code-block:: console
        
        "--bigip-url=[2400:c:1:c:0:0:0:114]",


Example for VirtualServer CR:

    .. code-block:: console

        apiVersion: "cis.f5.com/v1"
        kind: VirtualServer
        metadata:
        name: cafe-virtual-server
        labels:
            f5cr: "true"
        spec:
        # This is an insecure virtual, Please use TLSProfile to secure the virtual
        # check out tls examples to understand more.
        host: cafe.example.com
        virtualServerAddress: "2002:0:0:0:10:0:0:2"
        virtualServerName: "cafe-virtual-server"
        pools:
        - path: /coffee
            service: svc-2
            servicePort: 80


F5 IPAM Controller v0.1.6 and later also supports configuration of IPv6 address ranges. 

Example for IPv6 ip-range:

    .. code-block:: yaml
        
        --ip-range='{"Test-v4":"10.192.75.113-10.192.75.116","Prod-v4":"10.192.125.30-10.192.125.50","Prod-v6":"2001:db8:5::ffff-2001:db8:6::9"}'



For earlier version of CIS, the below workaround is available for the big-ip url:

Workaround
------------------

The current workaround is to use :code:`hostAliases` to define a hostname that resolves to the IPv6 address. 
See below snippet for a sample configuration:

.. code-block:: yaml
   :emphasize-lines: 20-23

    apiVersion: apps/v1
    kind: Deployment
    metadata:
    name: k8s-bigip-ctlr-deployment
    namespace: kube-system
    spec:
    # DO NOT INCREASE REPLICA COUNT
    selector:
        matchLabels:
        app: k8s-bigip-ctlr
    replicas: 1
    template:
        metadata:
        name: k8s-bigip-ctlr
        labels:
            app: k8s-bigip-ctlr
        spec:
        # Name of the Service Account bound to a Cluster Role with the required
        # permissions
        hostAliases:
            - ip: "240b:ab11:cd22:a101::10"
            hostnames:
            - "stagingbigip1"
        serviceAccountName: bigip-ctlr

