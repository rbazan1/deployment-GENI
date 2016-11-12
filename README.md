# Infrastructure & software deployment automation for InstaGENI resources

IaaS + SaaS
========================

## Deployment

This back-end code intent to deploy Infrastructure Software Resources in GENI (a National Science Foundation funded suite of software and hardware to support "at scale" research and to share resources for experimentation and research) by using *geni-lib*  [gebi-lib documentation](http://geni-lib.readthedocs.io/en/latest/) for infrastructure deployment and Shell Scripts for the Software deployment.

The input parameters are:

* Number and types of nodes (i.e. XenVM)
* Aggregate Manager (i.e. IG.Stanford, IG.Clemson)
* Slice name
* Nodes names
* Manifest name to store the generated XML file
* Software (a list of software names needed in the node/s)
* Public IP (Boolean value)

## Networking

At this point, the topology for multiples nodes is *star*, where all the nodes are connected to the same network link.
We focused on this topology since we want to provisiong master-workers type cluster.

## Usage

A geni-lib context needs to be created. A main function was created to facilitate implementation/execution.

