# -*- coding: utf-8 -*-
#
#
# BEGIN CONFIG
# ------------
#
# REQUIRED: Your class/lab name
classname = "F5 CIS Operations Guide"

# OPTIONAL: The URL to the GitHub Repository for this class
github_repo = "https://github.com/tkam8/f5_cis_opsguide"

# OPTIONAL: Google Analytics
# googleanalytics_id = 'UA-85156643-4'

#
# END CONFIG
# ----------

import os
import sys
import time
import re
import pkgutil
import string
#import f5_sphinx_theme

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../'))

year = time.strftime("%Y")
eventname = "F5 CIS %s Ops Guide" % (year)


rst_prolog = """
.. |classname| replace:: %s
.. |classbold| replace:: **%s**
.. |classitalic| replace:: *%s*
.. |ltm| replace:: Local Traffic Manager
.. |adc| replace:: Application Delivery Controller
.. |gtm| replace:: Global Traffic Manager
.. |dns| replace:: DNS
.. |asm| replace:: Application Security Manager
.. |afm| replace:: Advanced Firewall Manager
.. |apm| replace:: Access Policy Manager
.. |pem| replace:: Policy Enforcement Manager
.. |ipi| replace:: IP Intelligence
.. |iwf| replace:: iWorkflow
.. |biq| replace:: BIG-IQ
.. |bip| replace:: BIG-IP
.. |aiq| replace:: APP-IQ
.. |ve|  replace:: Virtual Edition
.. |icr| replace:: iControl REST API
.. |ics| replace:: iControl SOAP API
.. |f5|  replace:: F5 Networks
.. |f5i| replace:: F5 Networks, Inc.
.. |year| replace:: %s
""" % (classname,
       classname,
       classname,
       year)

if 'github_repo' in locals() and len(github_repo) > 0:
    rst_prolog += """
.. |repoinfo| replace:: The content contained here leverages a full DevOps CI/CD
              pipeline and is sourced from the GitHub repository at %s.
              Bugs and Requests for enhancements can be made using by
              opening an Issue within the repository.
""" % (github_repo)
else:
    rst_prolog += ".. |repoinfo| replace:: \ \n"

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
on_snops = os.environ.get('SNOPS_ISALIVE', None) == 'True'

print "on_rtd = %s" % on_rtd
print "on_snops = %s" % on_snops

github_url = "https://github.com/tkam8/f5_cis_opsguide"

branch_map = {
    "stable":"master",
    "latest":"master"
}

try:
    if not on_rtd:
        from git import Repo
        repo = Repo("%s/../" % os.getcwd())
        git_branch = repo.active_branch
        git_branch_name = git_branch.name
    else:
        git_branch_name = os.environ.get('READTHEDOCS_VERSION', None)
except:
    git_branch_name = 'master'

print "guessed git branch: %s" % git_branch_name

if git_branch_name in branch_map:
    git_branch_name = branch_map[git_branch_name]
print " remapped to git branch: %s" % git_branch_name

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.doctest',
    'sphinxjp.themes.basicstrap',
    'cloud_sptheme.ext.table_styling',
    'sphinx.ext.extlinks'
]

html_context = {
  "github_url":github_url,
  "github_branch":git_branch_name
}

if 'googleanalytics_id' in locals() and len(googleanalytics_id) > 0:
  extensions += ['sphinxcontrib.googleanalytics']
  googleanalytics_enabled = True

eggs_loader = pkgutil.find_loader('sphinxcontrib.spelling')
found = eggs_loader is not None

if found:
  extensions += ['sphinxcontrib.spelling']
  spelling_lang='en_US'
  spelling_word_list_filename='../wordlist'
  spelling_show_suggestions=True
  spelling_ignore_pypi_package_names=False
  spelling_ignore_wiki_words=True
  spelling_ignore_acronyms=True
  spelling_ignore_python_builtins=True
  spelling_ignore_importable_modules=True
  spelling_filters=[]

source_parsers = {
   '.md': 'recommonmark.parser.CommonMarkParser',
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'F5 CIS Operations Guide'
copyright = u'F5 Networks, Inc.'
author = u'F5 Networks, Inc.'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''


# All substitutions
# Try to keep sorted alphabetically
rst_epilog = """
.. |cfctlr| replace:: BIG-IP Controller
.. |cf-long| replace:: BIG-IP Controller for Cloud Foundry
.. |kctlr-long| replace:: BIG-IP Controller for Kubernetes
.. |kctlr| replace:: BIG-IP Controller
.. |mctlr-long| replace:: BIG-IP Controller for Marathon
.. |mctlr| replace:: BIG-IP Controller
.. |octlr-long| replace:: BIG-IP Controller for OpenShift
.. _Apache Mesos Marathon: https://mesosphere.github.io/marathon/
.. _Apache Mesos: https://mesosphere.com/
.. _Application labels for iApp mode: %(base_url)s/products/connectors/marathon-bigip-ctlr/latest/#application-labels-for-iapp-mode
.. _Application Manifest: https://docs.pivotal.io/pivotalcf/1-7/devguide/deploy-apps/manifest.html
.. _Better or Best license: https://f5.com/products/how-to-buy/simplified-licensing
.. _BIG-IP: https://f5.com/products/big-ip
.. _BIG-IP Application Security Manager: https://f5.com/products/big-ip/application-security-manager-asm
.. _BIG-IP Controller for Cloud Foundry: %(base_url)s/products/connectors/cf-bigip-ctlr/latest/
.. _BIG-IP Controller for Kubernetes: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest
.. _BIG-IP Controller for Marathon: %(base_url)s/products/connectors/marathon-bigip-ctlr/latest
.. _BIG-IP Local Traffic Management - Getting Started with Policies: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-local-traffic-policies-getting-started-13-0-0.html
.. _BIG-IP Local Traffic Management - Profiles Reference Guide: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/ltm-profiles-reference-13-0-0.html
.. _BIG-IP partition: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-user-account-administration-13-0-0/2.html
.. _BIG-IP Automap SNAT: https://support.f5.com/csp/article/K7820#types
.. _BIG-IP SSL profile: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/ltm-profiles-reference-12-1-0/6.html
.. _BIG-IP System User Account Administration -> Administrative Partitions: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-user-account-administration-12-0-0/3.html
.. _BIG-IP TMOS Routing Adminstration Guide: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/tmos-routing-administration-13-0-0/
.. _BIG-IP user account: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-user-account-administration-13-0-0/1.html
.. _built-in middleware: %(base_url)s/products/asp/latest/#built-in-middleware
.. _cf-bigip-ctlr configuration parameters: %(base_url)s/products/connectors/cf-bigip-ctlr/latest/#configuration-parameters
.. _cf-bigip-ctlr: %(base_url)s/products/connectors/cf-bigip-ctlr/latest/
.. _cf-bigip-ctlr v1.1.0: %(base_url)s/products/connectors/cf-bigip-ctlr/v1.1/
.. _cf-bigip-ctlr reference documentation: %(base_url)s/products/connectors/cf-bigip-ctlr/latest/
.. _cf-bigip-ctlr service broker config parameters: %(base_url)s/products/connectors/cf-bigip-ctlr/latest/#broker-configs
.. _CIDR format: https://www.rfc-editor.org/info/rfc4632
.. _Cloud Foundry CLI: https://docs.cloudfoundry.org/cf-cli/getting-started.html
.. _Cloud Foundry: https://cloudfoundry.org/why-cloud-foundry/
.. _ClusterIP: https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/
.. _Cluster network: https://kubernetes.io/docs/concepts/cluster-administration/networking/
.. _Cluster Role Binding: https://kubernetes.io/docs/admin/authorization/rbac/#rolebinding-and-clusterrolebinding
.. _Cluster Role: https://kubernetes.io/docs/admin/authorization/rbac/#role-and-clusterrole
.. _Cluster: https://kubernetes.io/docs/tasks/administer-cluster/cluster-management/
.. _ConfigMap: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/
.. _configuration parameters specific to OpenShift: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#openshift-sdn
.. _contact F5 support: https://f5.com/about-us/contact/regional-offices#regional-support
.. _Create a Kubernetes Secret containing your Docker login credentials: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/
.. _Create a new namespace: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/
.. _Create a new partition: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/tmos-implementations-12-1-0/29.html
.. _create and set a non-zero default Route Domain for a partition: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/tmos-implementations-13-0-0/4.html#guid-e73e1052-8e05-4913-bba3-99f29d26bc56
.. _DaemonSet: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
.. _DC/OS and DC/OS Enterprise: https://mesosphere.com/product/
.. _Deployment: https://kubernetes.io/docs/user-guide/deployments/
.. _Diego cell: https://docs.cloudfoundry.org/concepts/architecture/#diego-cell
.. _Disable automatic configuration sync on the DSC: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-system-device-service-clustering-administration-13-1-0/5.html
.. _Disable config sync for tunnels: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-tmos-tunnels-ipsec-13-1-0/2.html#GUID-5E1E2E56-0776-4B7A-A601-98C2C2E3775C
.. _Docker: https://www.docker.com/
.. _Express middleware: https://expressjs.com/en/guide/using-middleware.html
.. _Express: https://expressjs.com/
.. _F5 Docker registry: https://hub.docker.com/r/f5networks/
.. _F5 IPAM Controller: https://github.com/F5Networks/f5-ipam-ctlr
.. _f5-ipam-ctlr docs: %(base_url)s/products/ipam-ctlr/latest/
.. _F5 Resources: %(base_url)s/containers/v2/kubernetes/kctlr-f5-resource.html#f5-resource-properties
.. _F5 schema: https://github.com/F5Networks/k8s-bigip-ctlr/tree/master/schemas
.. _F5 virtual server properties: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#virtualserver-configmap-properties
.. _F5 Helm Chart: https://github.com/F5Networks/charts/tree/master/src/stable/f5-bigip-ctlr
.. _f5-bigip-ingress chart: https://github.com/F5Networks/charts/tree/master/src/stable/f5-bigip-ingress
.. _f5-kube-proxy reference documentation: %(base_url)s/products/connectors/f5-kube-proxy/latest/
.. _f5-kube-proxy: %(base_url)s/products/connectors/f5-kube-proxy/latest/
.. _flannel: https://github.com/coreos/flannel
.. _flannel manifest: https://github.com/coreos/flannel/blob/master/Documentation/kube-flannel.yml
.. _helm: https://helm.sh
.. _iApps: https://www.f5.com/products/f5-technologies
.. _iApp Pool Member table: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#iapp-pool-member-table
.. _Ingress annotations: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#ingress-resources
.. _Ingress controller: https://kubernetes.io/docs/concepts/services-networking/ingress/#ingress-controllers
.. _Ingress Resource: https://kubernetes.io/docs/concepts/services-networking/ingress/
.. _k8s-bigip-ctlr configuration parameters: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#controller-configuration-parameters
.. _k8s-bigip-ctlr iApp configuration parameters: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#iApp
.. _k8s-bigip-ctlr reference documentation: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/
.. _k8s-bigip-ctlr virtual server configuration parameters: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#virtualserver
.. _k8s-bigip-ctlr: %(base_url)s/containers/v2/kubernetes/
.. _k8s-bigip-ctlr v1.1.0-beta.1: %(base_url)s/products/connectors/k8s-bigip-ctlr/v1.1-beta/
.. _k8s-bigip-ctlr v1.1.0: %(base_url)s/products/connectors/k8s-bigip-ctlr/v1.1/
.. _k8s-bigip-ctlr v1.2.0: %(base_url)s/products/connectors/k8s-bigip-ctlr/v1.2/
.. _k8s-bigip-ctlr v1.3.0: %(base_url)s/products/connectors/k8s-bigip-ctlr/v1.3/
.. _k8s-bigip-ctlr v1.4.0: %(base_url)s/products/connectors/k8s-bigip-ctlr/v1.4/
.. _k8s-bigip-ctlr v1.5.0: %(base_url)s/products/connectors/k8s-bigip-ctlr/v1.5/
.. _kube-proxy: https://kubernetes.io/docs/admin/kube-proxy/
.. _kubectl: https://kubernetes.io/docs/user-guide/kubectl-overview/
.. _Kubernetes clusters: https://kubernetes.io/docs/concepts/cluster-administration/cluster-administration-overview/
.. _Kubernetes Dashboard: https://kubernetes.io/docs/user-guide/ui/
.. _Kubernetes Ingress controller: https://kubernetes.io/docs/concepts/services-networking/ingress/#ingress-controllers
.. _Kubernetes Ingress: https://kubernetes.io/docs/concepts/services-networking/ingress/
.. _Kubernetes node: https://kubernetes.io/docs/admin/node/
.. _Kubernetes RBAC documentation: https://kubernetes.io/docs/admin/authorization/rbac/
.. _Kubernetes Service: https://kubernetes.io/docs/user-guide/services/
.. _Kubernetes: https://kubernetes.io/
.. _local traffic management: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/ltm-basics-12-0-0.html
.. _Local Traffic Policies: https://support.f5.com/csp/article/K04597703
.. _Marathon Applications: https://mesosphere.github.io/marathon/docs/application-basics.html
.. _Marathon Apps: https://mesosphere.github.io/marathon/docs/application-basics.html
.. _Marathon Web Interface: https://mesosphere.github.io/marathon/docs/marathon-ui.html
.. _marathon-bigip-ctlr configuration parameters: %(base_url)s/products/connectors/marathon-bigip-ctlr/latest/#configuration-parameters
.. _marathon-bigip-ctlr iApp configuration parameters: %(base_url)s/products/connectors/marathon-bigip-ctlr/latest/#iApp
.. _marathon-bigip-ctlr reference documentation: %(base_url)s/products/connectors/marathon-bigip-ctlr/latest/
.. _marathon-bigip-ctlr: %(base_url)s/products/connectors/marathon-bigip-ctlr/latest/
.. _marathon-bigip-ctlr v1.1.0-beta.1: %(base_url)s/products/connectors/marathon-bigip-ctlr/v1.1-beta/
.. _marathon-bigip-ctlr v1.1.0: %(base_url)s/products/connectors/marathon-bigip-ctlr/v1.1/
.. _marathon-bigip-ctlr v1.3.0: %(base_url)s/products/connectors/marathon-bigip-ctlr/v1.3/
.. _Marathon: https://mesosphere.github.io/marathon/
.. _namespace: https://kubernetes.io/docs/user-guide/namespaces/
.. _namespaces: https://kubernetes.io/docs/user-guide/namespaces/
.. _NATS bus: https://docs.cloudfoundry.org/concepts/architecture/router.html#use
.. _NodePort: https://kubernetes.io/docs/concepts/services-networking/service/#nodeport
.. _oc: https://docs.openshift.com/enterprise/3.0/cli_reference/basic_cli_operations.html
.. _OpenShift F5 Router: https://docs.openshift.org/latest/install_config/router/f5_router.html
.. _OpenShift Route Annotations: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#supported-route-annotations
.. _OpenShift route resources: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#openshift-route-resources
.. _Overview of SNAT features: https://support.f5.com/csp/article/K7820
.. _Overview of the Standard Virtual Server: https://support.f5.com/csp/article/K93017176
.. _Pivotal Cloud Foundry: https://pivotal.io/platform
.. _Pod: https://kubernetes.io/docs/concepts/workloads/pods/pod/
.. _Pods: https://kubernetes.io/docs/concepts/workloads/pods/pod/
.. _Projects: https://docs.openshift.org/latest/architecture/core_concepts/projects_and_users.html#projects
.. _Red Hat OpenShift: https://www.openshift.com/container-platform/index.html
.. _Route annotations: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#supported-annotations
.. _Route configuration parameters: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#openshift-routes
.. _Route domain: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/tmos-routing-administration-13-0-0/8.html
.. _Secret: https://kubernetes.io/docs/user-guide/secrets/
.. _Self IP address: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/tmos-routing-administration-13-0-0/5.html#guid-52e1f1d8-9a6b-48cc-acfa-07745b757f07
.. _Service: https://kubernetes.io/docs/concepts/services-networking/service/
.. _ServiceAccount: https://kubernetes.io/docs/admin/service-accounts-admin/
.. _Service resources: https://kubernetes.io/docs/user-guide/services/
.. _Service Broker: https://docs.cloudfoundry.org/services/overview.html
.. _Set up two or more F5 BIG-IPs in a Device Service Cluster (DSC): https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-system-device-service-clustering-administration-13-1-0/11.html
.. _SNAT automap and self IP address selection: https://support.f5.com/csp/article/K7336
.. _Splunk: https://www.splunk.com/
.. _Static Pod: https://kubernetes.io/docs/admin/static-pods/
.. _store your Docker login credentials as a Secret: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/
.. _supported Route configurations: %(base_url)s/products/connectors/k8s-bigip-ctlr/latest/#supported-route-configurations
.. _system configuration: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-system-initial-configuration-12-0-0/2.html#conceptid
.. _Using flannel with Kubernetes: https://coreos.com/flannel/docs/latest/kubernetes.html
.. _F5 AS3 Extension: %(base_url)s/products/extensions/f5-appsvcs-extension/latest/
.. _F5 AS3 Extensions: %(base_url)s/containers/v2/kubernetes/kctlr-k8s-as3.html
.. _F5 AS3 Installation: %(base_url)s/products/extensions/f5-appsvcs-extension/latest/userguide/installation.html
.. _F5 AS3 User Guide: %(base_url)s/products/extensions/f5-appsvcs-extension/latest/userguide/
.. _F5 AS3 Reference Guide: %(base_url)s/products/extensions/f5-appsvcs-extension/latest/refguide/
.. _Container Ingress Services and AS3 Extension integration: %(base_url)s/containers/v2/kubernetes/kctlr-k8s-as3.html
.. _Updating the CIS trusted certificate store: %(base_url)s/kubernetes/kctlr-as3-cert-trust.html
.. _Overview of BIG-IP device certificates: https://support.f5.com/csp/article/K15664
.. _K16951115 Changing the BIG-IP DNS system device certificate using the Configuration utility: https://support.f5.com/csp/article/K16951115
.. _ReplicaSet: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
"""% {
    'base_url': 'https://clouddocs.f5.com'
}

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_emit_warnings = True
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
#html_theme_path = f5_sphinx_theme.get_html_theme_path()
#html_sidebars = {'**': ['searchbox.html', 'localtoc.html', 'globaltoc.html']}
#html_theme_options = {
#                        'site_name': 'Community Training Classes & Labs',
#                        'next_prev_link': True
#                     }
html_last_updated_fmt = '%Y-%m-%d %I:%M:%S'

#if on_rtd:
#    templates_path = ['_templates']

extlinks = {
    'raw_github_url':( ("https://raw.githubusercontent.com/tkam8/f5_cis_opsguide/%s%%s" % git_branch_name), None)
}



# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#
# html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
html_last_updated_fmt = '%Y-%m-%d %I:%M:%S'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#
# html_use_smartypants = True

# Additional templates that should be rendered to pages, maps page names to
# template names.
#
# html_additional_pages = {}

# If false, no module index is generated.
#
html_domain_indices = True

# If false, no index is generated.
#
html_use_index = True

# If true, the index is split into individual pages for each letter.
#
html_split_index = False

# If true, links to the reST sources are added to the pages.
#
html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#
html_show_copyright = True

# Output file base name for HTML help builder.
htmlhelp_basename = 'F5CISOpsGuide'

# html_add_permalinks
# Sphinx will add “permalinks” for each heading and description environment as paragraph 
# signs that become visible when the mouse hovers over them.
# This value determines the text for the permalink; it defaults to "¶". 
# Set it to None or the empty string to disable permalinks.

html_add_permalinks = None

# -- Options for HTMLHelp output ------------------------------------------

cleanname = re.sub('\W+','',classname)

# Output file base name for HTML help builder.
htmlhelp_basename =  cleanname + 'doc'

# -- Options for LaTeX output ---------------------------------------------

front_cover_image = 'front_cover'
back_cover_image = 'back_cover'

front_cover_image_path = os.path.join('_static', front_cover_image + '.png')
back_cover_image_path = os.path.join('_static', back_cover_image + '.png')

latex_additional_files = [front_cover_image_path, back_cover_image_path]

template = string.Template(open('preamble.tex').read())

latex_contents = r"""
\frontcoverpage
\contentspage
"""

backcover_latex_contents = r"""
\backcoverpage
"""

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'preamble': template.substitute(eventname=eventname,
                                    project=project,
                                    author=author,
                                    frontcoverimage=front_cover_image,
                                    backcoverimage=back_cover_image),

    'tableofcontents': latex_contents,
    'printindex': backcover_latex_contents
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, '%s.tex' % cleanname, u'%s Documentation' % classname,
     u'F5 Networks, Inc.', 'manual', True),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, cleanname.lower(), u'%s Documentation' % classname,
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, classname, u'%s Documentation' % classname,
     author, classname, classname,
     'Training'),
]

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The basename for the epub file. It defaults to the project name.
# epub_basename = project

# The HTML theme for the epub output. Since the default themes are not
# optimized for small screen space, using the same theme for HTML and epub
# output is usually not wise. This defaults to 'epub', a theme designed to save
# visual space.
#
# epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or 'en' if the language is not set.
#
# epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
# epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#
# epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#
# epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#
# epub_pre_files = []

# HTML files that should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#
# epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#
# epub_tocdepth = 3

# Allow duplicate toc entries.
#
# epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#
# epub_tocscope = 'default'

# Fix unsupported image types using the Pillow.
#
# epub_fix_images = False

# Scale large images.
#
# epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#
# epub_show_urls = 'inline'

# If false, no index is generated.
#
# epub_use_index = True

