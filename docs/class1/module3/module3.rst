CIS and ScaleN (N+1) - w/ out Auto Config-Sync
===========================

**Description**: 
This design pattern is similar to the previous design except auto config-sync is disabled, therefore multiple CIS instances will be used to configure other devices in the cluster. 


**Sample Diagram**:

|mod-3-1|

Configuration tips and caveats
------------------
- Ensure no more than 3 Controllers point to a single VE (max tested)
- Configure the VE non-floating Self-IP in :code:`--bigip-url`
    - Since there is one Controller per BIG-IP, no need to configure a floating IP
- Provide a unique metadata.name for each Controller
- Provide a unique :code:`--bigip-url` in each Deployment (each Controller manages a separate BIG-IP device)
- Use the same :code:`--bigip-partition` in all Deployments
- Do not define multiple Deployment configs in a single manifest.
    - If you launch multiple BIG-IP Controller instances using a single manifest, they will run on the same Pod. This means that if the Pod goes down, you lose all of your Controllers.


.. |mod-2-1| image:: images/mod-2-1.png