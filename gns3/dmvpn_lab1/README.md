## Description

**Dynamic multipoint virtual private network**


* Configure the ip addresses and routing protocols (BGP for ISP)
    * Customer routers do not run BGP but a static route to other Customers

* Create a DHCP pool on the customer routers to allocate IP addresses for the Ubuntu clients

* Configure a full mesh DMVPN tunnels with C1 as the hub site
    * Use GRE without encryption first

* Enable NAT on the customer routers so that the Ubuntu hosts can access cisco.com

* Verify that Ubuntu PCs can ping cisco.com

* Verify that Ubuntu PCs can ping each other using their RFC 1918 addresses

* Enable IPSec encryption for DMVPN tunnels

* Verification
    * verify connectivity between ubuntu PCS
    * verify that packets are being encrypted
    * verify that Ubuntu PC can still ping cisco.com

## Usefull commands

