CIS and AS3
================================================


**Description**: 
This section will cover some best practices, tips, and caveats when using AS3 to configure F5 Container Ingress Services (CIS) in a Kubernetes environment. For a full guide to these topics, please refer to the official documentation on |clouddocs|_. 

**Prerequisites**: 
- Basic understanding REST APIs and declarative configuration.

Below is a visualization of the configuration mappings between the AS3 configmap, Kubernetes Service, and the resulting configuration on BIG-IP. 

|mod-1-1|

*Credit to @foobz for this diagram*

.. |clouddocs| replace:: F5 Cloud Docs
.. _clouddocs: https://clouddocs.f5.com/containers/v2/kubernetes/kctlr-k8s-as3.html

.. |mod-1-1| image:: images/mod-1-1.png