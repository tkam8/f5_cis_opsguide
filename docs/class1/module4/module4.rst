AS3 Configmap: Multiple Apps in Partition
================================================


**Description**: 
This section will cover some best practices, tips, and caveats when configuring multiple apps (virtual servers) in the AS3 declaration. For more examples, see |github|_. 

**Prerequisites**: 
- Basic understanding REST APIs and declarative configuration.

Summary
------------------
You can declare multiple applications (virtual servers) in a single partition/tenant. 

#. Declare one tenant
#. Declare first application in the tenant block
#. Declare second application in the same tenant block

.. code-block:: yaml
   :emphasize-lines: 78,101

    kind: ConfigMap
    apiVersion: v1
    metadata:
    name: f5-hello-world
    labels:
        f5type: virtual-server
        as3: "true"
    data:
    template: |
        {
        "class": "AS3",
        "declaration": {
            "class": "ADC",
            "schemaVersion": "3.1.0",
            "id": "urn:uuid:33045210-3ab8-4636-9b2a-c98d22ab915d",
            "label": "Sample 1",
            "remark": "Simple HTTP application with RR pool",
            "Common": {
                    "class": "Tenant",
                    "Shared": {
                            "class": "Application",
                            "template": "shared",
                            "AS3Server": {
                                    "class": "GSLB_Server",
                                    "dataCenter": 
                                            {"bigip":"/Common/UDF"}
                                    ,
                                    "devices": [{
                                                    "address": "10.1.10.240",
                                                    "addressTranslation": "10.1.10.240"
                                            }
                                    ]
                                    ,
                                    "virtualServers": [{
                                                    "address": "10.1.10.81",
                                                    "port": 80,
                                                    "addressTranslation": "10.1.10.81",
                                                    "addressTranslationPort":80
                                            },
                                            {
                                                    "address": "10.1.10.82",
                                                    "port": 80,
                                                    "addressTranslation": "10.1.10.82",
                                                    "addressTranslationPort":80
                                            },
                                            {
                                                    "address": "10.1.10.240",
                                                    "port": 6443,
                                                    "addressTranslation": "10.1.10.240",
                                                    "addressTranslationPort":6443
                                            }
                                    ]
                            }

                    }
            },
            "AS3": {
            "class": "Tenant",
            "Shared": {
                "class": "Application",
                "template":"shared",
                "serviceAddress0": {
                "class": "Service_Address",
                "virtualAddress": "10.1.10.81"
                }, "web_pool": {
                "class": "Pool",
                "monitors": [
                    "http"
                ],
                "members": [
                    {
                    "servicePort": 80,
                    "serverAddresses": []
                    }
                ]
                }
            },
            "A1": {
                "class": "Application",
                "template": "http",
                "serviceMain": {
                "class": "Service_HTTP",
                "virtualAddresses": [
                    {"use": "/AS3/Shared/serviceAddress0"}
                ],
                "pool": "/@/Shared/web_pool"
                },
                "web_pool": {
                "class": "Pool",
                "monitors": [
                    "http"
                ],
                "members": [
                    {
                    "servicePort": 80,
                    "serverAddresses": []
                    }
                ]
                }
            },
            "A2": {
                "class": "Application",
                "template": "https",
                "serviceMain": {
                "class": "Service_HTTPS",
                "virtualAddresses": [
                    {"use": "/AS3/Shared/serviceAddress0"}
                ],
                "pool": "/@/Shared/web_pool",
                "serverTLS": "webtls",
                "redirect80":false,
                "policyWAF":{"bigip":"/Common/linux-low"},
                "securityLogProfiles": [
                {
                    "bigip": "/Common/Log all requests"
                }
                ]
                },
                "web_pool": {
                "class": "Pool",
                "monitors": [
                    "http"
                ],
                "members": [
                    {
                    "servicePort": 80,
                    "serverAddresses": []
                    }
                ]
                },
                "webtls": {
                "class": "TLS_Server",
                "certificates": [
                    {
                    "certificate": "webcert"
                    }
                ]
                },
                "webcert": {
                "class": "Certificate",
                "certificate": "-----BEGIN CERTIFICATE-----\n----snip----\n-----END CERTIFICATE-----",
                "privateKey": "-----BEGIN RSA PRIVATE KEY-----\n----snip----\n-----END RSA PRIVATE KEY-----",
                "passphrase": {
                    "ciphertext": "ZjVmNQ==",
                    "protected": "----snip----"
                }
                }
            },
            "G0": {
                "class": "Application",
                "template": "generic",
                "myfrontendpool": {
                    "class": "GSLB_Pool",
                    "members": [
                        {
                            "ratio": 10,
                            "server": {
                                "use": "/Common/Shared/AS3Server"
                            },
                            "virtualServer": "0"
                        }
                    ],
                    "resourceRecordType": "A"
                },
                            "testDomain": {
                                    "class": "GSLB_Domain",
                                    "domainName": "my-frontend.apps.example.com",
                                    "resourceRecordType": "A",
                                    "pools": [{
                                                    "use": "myfrontendpool"
                                            }
                                    ]
                            }
            },
            "G1": {
                "class": "Application",
                "template": "generic",
                "ingresspool": {
                    "class": "GSLB_Pool",
                    "members": [
                        {
                            "ratio": 10,
                            "server": {
                                "use": "/Common/Shared/AS3Server"
                            },
                            "virtualServer": "1"
                        }
                    ],
                    "resourceRecordType": "A"
                },
                            "testDomain": {
                                    "class": "GSLB_Domain",
                                    "domainName": "*.f5demo.com",
                                    "resourceRecordType": "A",
                                    "pools": [{
                                                    "use": "ingresspool"
                                            }
                                    ]
                            }
            },
            "G2": {
                "class": "Application",
                "template": "generic",
                "k8sapipool": {
                    "class": "GSLB_Pool",
                    "members": [
                        {
                            "ratio": 10,
                            "server": {
                                "use": "/Common/Shared/AS3Server"
                            },
                            "virtualServer": "2"
                        }
                    ],
                    "resourceRecordType": "A"
                },
                            "testDomain": {
                                    "class": "GSLB_Domain",
                                    "domainName": "k8s.f5demo.com",
                                    "resourceRecordType": "A",
                                    "pools": [{
                                                    "use": "k8sapipool"
                                            }
                                    ]
                            }
            }
            }
        }
        }
    


.. |github| replace:: F5 DevCentral f5-k8s-demo repository
.. _github: https://github.com/f5devcentral/f5-k8s-demo/tree/master/chen-k8s-demo/deployment

.. |mod-2-1| image:: images/mod-2-1.png