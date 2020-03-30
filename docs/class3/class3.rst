CIS Troubleshooting
================================================


**Description**: 
First, refer to the below official documentation on |clouddocs| for a comprehensive list of troubleshooting steps: 

https://clouddocs.f5.com/containers/v2/troubleshooting/kubernetes.html

This following section will cover **additional** best practices, tips, and caveats when troubleshooting F5 Container Ingress Services (CIS) in a Kubernetes environment. 


CIS (Controller) Additional Troubleshooting
----------------------------------

- AS3 Log level: A new command-line option was introduced in Controller v1.12 that logs the AS3 error response. Add below to the arguments block in the Controller deployment manifest file. The logs will appear in the Controller pod logs

:code:`"--log-as3-response=true",`

- BIG-IP restnoded logs: There are two key daemons responsible for iControl REST and iControl LX Extensions. The two logs for these daemons are:

:code:`/var/log/restjavad.0.log`

:code:`/var/log/restnoded/restnoded.log`

.. note: For efficiency you can execute below when restarting the restnoded daemon
    
    :code:`bigstart restart restnoded; tail -f /var/log/restnoded/restnoded.log`

- AS3 Declaration Validator: If you are using Microsoft Visual Studio Code, you can follow instructions below to install a validator for your declaration. This will identify syntax errors and do auto tab complete

https://clouddocs.f5.com/products/extensions/f5-appsvcs-extension/latest/userguide/validate.html


.. |clouddocs| replace:: F5 Cloud Docs
.. _clouddocs: https://clouddocs.f5.com/containers/v2/troubleshooting/kubernetes.html
.. |ictrllogs| replace:: iControl & iControl LX Logs
.. _ictrllogs: https://clouddocs.f5.com/training/community/icontrol-lx/html/class1/module1/lab2.html


.. toctree::
   :maxdepth: 2
   :caption: Contents:
   :glob:

   module*/module*