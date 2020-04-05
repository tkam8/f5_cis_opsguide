CIS Service Labels
================================================


**Description**: 
This section will cover some best practices, tips, and caveats when configuring CIS labels in the Kubernetes Service. These labels are used for service discovery on the BIG-IP. For a full guide to these topics, please refer to the official documentation on |clouddocs|_. 

**Prerequisites**: 
- Basic understanding REST APIs and declarative configuration.

Summary
------------------
CIS can dynamically discover and update the BIG-IP system’s load balancing pool members using Service Discovery. CIS maps each pool definition in the AS3 template to a Kubernetes Service resource using Labels. To create this mapping, add the following labels to your Kubernetes Service:

|mod-2-1|


.. |clouddocs| replace:: F5 Cloud Docs
.. _clouddocs: https://clouddocs.f5.com/containers/v2/kubernetes/kctlr-k8s-as3.html#cis-service-discovery

.. |mod-2-1| image:: images/mod-2-1.png