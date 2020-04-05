IPv6 Addresses
================================================


**Description**: 
This section will cover some best practices, tips, and caveats when configuring CIS and manifest files with IPv6 addresses. 


Summary
------------------
BIG-IP supports IPv6 addresses for all objects. However, currently there is a known issue where CIS is not able to connect to an IPv6 address as configured in the CIS deployment manifest file. This has been raised internally as well as on GitHub. For details and current status of this issue, refer to below link. 

GitHub issue: https://github.com/F5Networks/k8s-bigip-ctlr/issues/1216 

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

