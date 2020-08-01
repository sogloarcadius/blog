# Commandes de base cisco


```python
#enter mode privilegies

enable /disable

#enter configuration mode(mode de config/ config globale)

configure terminal

#configure hostname

hostname writehostname

#enable password encryption in conf file
#password not encryped during transmission

service password-encryption

#secure connection in priviliged mode

enable secret *********


#secure line console connection

line console 0
password ********
login


#secure VTY 0 to 15

line VTY 0 15
password *****
login

#message de banniere

banner motd *********


#see configuration

show running-config

show startup-config


#save conf

copy running-config startup-config
write memory

#delete conf

erase startup-config
reload /*inactivity for a while

#activer une interface

no shutdown

#configurer l'interface de commutateur SVI (interface virtuelle)

interface vlan 1
no shutdown


#afficher résumé sur une interface

show ip interface brief

```

# Configuration de routeur cisco 


```python
# Configurer interface de loopback

conf t
interface loopback 0
ip address x.x.x.x x.x.x.x
# (Inutile de préciser no shutdown car interface logiciel toujours active)
end


#afficher la table de routage

show ip route

#afficher des informations sur le systeme d'exploitation 

show version

#ajouter une route par défaut sur switch/routeur cisco

enable
conf t
ip default-gateway xxx.xx..x.x.xx.

#configurer interface

enable
conf t
interface xxx y/z
description %%%ùùùùùùù(240 max)
no shutdown
end

```

# Configuration SSH 


```python
# pour savoir si ssh pris en compte ?

>show ip ssh

#configuration nom de domaine

>ip domain-name nom-domaine


#configurer ssh version 2

>ip ssh version 2

#générer paire de clés, active automatiquement serveur ssh

#supprimer paire de clés ssh

>crypto key zeroize rsa.


#configuration authentification locale

>username admin secret ccna


#autoriser uniquement connextion ssh

>line vty 0 15
> transport input ssh 
>login local
>exit
>ip ssh version 2
>exit

```

# Configuration des ports


```python

conf t
int fa0/0
duplex full
speed 100
end
copy running-config startup-config

```

# Surveillance DHCP


```python
ip dhcp snooping

ip dhcp snooping vlan ---

#definir des ports fiables

ip dhcp snooping trust

ip dhcp snooping limit rate fréquence

```

# Sécurité des ports


```python
switchport mode access
switchport port-security (par défaut mode shutdown, port s'éteint en cas de violation de sécurité)
switchport port-security maximum 50 (limite à 50 adresses mac différentes sur cette interface)

#activer apprentissage rémanent
                          
switchport port-security mac-address sticky

#definir type de violation

switchport port-security violation {protect | restrict | shutdown}.

#info

show port-security interface fax/x
```

# serveur NTP


```python

#serveur ntp

ntp master 1

#client ntp

#info 

show ntp associations
show ntp status
ntp server xxxxxx
```

# Configuration de VLAN


```python
vlan xxxxxx
name xxxxxx
end

#affecter interface dans un vlan et le créer si nexiste pas

interface range fax/x - y
switchport mode access
switchport access vlan xx
end

# retier interface du vlan

interface xxx
no switchport access vlan xx
end

#info
show vlan brief
show interfaces f0/1 switchport

#supprimer info vlan 

delete flash:vlan.dat

#changer vlan natif

switchport trunk native vlan 99

#filter les vlan du port trunk

switchport trunk allowed vlan 10,20,xx,xx

#AUTO NEGOCIATION (trunk ou access)

switchport mode dynamic auto (par défaut)

#desactiver DTP

switchport nonegotiate

#info sur dtp

show dtp interface fax/x


#securite sur les ports

int fax/x
switchport protected
end
```

## Routage Statique


```python
# info sur les routes 
tracert (depuis pc windows)
traceroute (depuis un routeur cisco)

#resolution dns

nslookup , linux( dig)

### configuration avec ipv6

ipv6 enable (configuration auto address link-local)


# addresse monodiffusion globale

ipv6 address ---/prefix

#monodiffusion globale eui-64

ipv6 address ---/prefix  eui-64

# addresse link local statique

ipv6 address ---/prefix link-local


###configuration des routes statiques
ip route x.x.x.x y.y.y.y z.z.z.z

show ip route


```

## Routage RIP


```python

## RIP

router rip //activation du protocole rip sur le routeur
network xx.xx.xx // annonce des réseaux connectés directement au routeur 

## ipv6

ipv6 unicast-routing

interface xxxxxx
ipv6 RIP-AS enable
```

## Routage OSPF


```python
router ospf 1 # max 2
network <network_address> <wildcard_mask> area <area_number>

```

## Routage EIGRP

## Routage BGP


```python
router bgp asnumber
neighbor x.x.x.x
network x.x.x.x mask y.y.y.y
no auto-summary

## on Route Reflector server
neighbor x.x.x.x route-reflector-client



```

## Configuration serveur dhcp


```python
ip dhcp pool CLIENT_LAN
ip dhcp excluded-address 192.168.22.1 192.168.22.10
network 192.168.0.0 255.255.255.0
dns-server 8.8.8.8
default-router 192.168.0.1
```

## Configure DNS Server on Router


```python
ip dns server
ip domain-lookup
ip name-server 4.2.2.2
ip host fileserver 192.168.0.5
ip host sftpserver 192.168.0.3
```

## Configuration NETCONF


```python
netconf-yang
netconf max-sessions 5
netconf max-message 37283
netconf lock-time 60
!netconf ssh
```

## Configuration RESTCONF


```python
!! fist configure ssh and local account
restconf
ip http server
ip http authentication local
ip http secure-server
```
