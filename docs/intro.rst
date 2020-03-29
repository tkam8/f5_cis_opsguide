Overview
========

This unofficial document provides best practices, tips, and caveats when validating F5 Container Ingress Services (CIS) in a Kubernetes environment.

.. NOTE::
   This is a supplemental guide to official documentation on |clouddocs|_. 

F5 Container Ingress Services - Overview
---------------

When deploying applications in Kubernetes, you will eventually need a way to provide external access to your services. F5 enables not only load balancing, but also security, advanced functionality and high performance often required by enterprise-grade applications. 

The F5 BIG-IP Controller (k8s-bigip-ctlr) is a cloud-native connector that can use either Kubernetes or OpenShift as a BIG-IP orchestration platform.

The BIG-IP Controller watches the Kubernetes API for specially formatted resources with CIS labels.It will take those labels and update the BIG-IP configuration accordingly.

Features
---------------
- Dynamically create, and manage BIG-IP objects.
- Forward traffic from the BIG-IP device to |clusters|_ via NodePort_ or ClusterIP_.
- Support |as3|_ declarations.


.. |as3| replace:: F5 AS3 Extension
.. _as3: https://clouddocs.f5.com/products/extensions/f5-appsvcs-extension/latest/
.. |clouddocs| replace:: F5 Cloud Docs
.. _clouddocs: https://clouddocs.f5.com/containers/v2/kubernetes/
.. |clusters| replace:: Kubernetes clusters
.. _clusters: https://kubernetes.io/docs/concepts/cluster-administration/cluster-administration-overview/
.. _NodePort: https://kubernetes.io/docs/concepts/services-networking/service/#nodeport
.. _ClusterIP: https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/