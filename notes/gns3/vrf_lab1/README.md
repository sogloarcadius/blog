

## Description

Introduction aux VRFs(Virtual Routing Forwarding) : tables de routages virtuelles

Les VRF sont au routage ce que les VLAN sont au switching: les VRF sont des tables de routage virtuelles qui permettent d'isoler complètement les réseaux de 2 clients traversant le même routeur. Avec une table de routage par client, les clients peuvent agir sans avoir aucune connaissance des réseaux de l'autre client, qui ne verra et dont ils ne verront jamais le trafic, que ce soit de données ou de contrôle (comme les mises à jour de routage). 

Un client peut ainsi choisir comme bon lui semble ses adresses réseaux vues par l'ISP: c'est le but de l'ISP d'offrir ce service d'isolation entre client dont il route les paquets (l'ISP ne se comporte pas uniquement comme un switch).

On considère dans la topologie ci-dessous que le router PE d'un ISP prend en charge 2 clients CUST1 et CUST2, qui ont chacun 2 sites à interconnecter: le siège social (headquarters – HQ) et une agence (Branch).Chaque client veut utiliser OSPF comme protocole de routage, et ils veulent utiliser les même adresses réseau. De plus, l'ISP doit s'assurer qu'il n'y a aucune connectivité (aucun paquet reçu, ni de contrôle ni de data) entre les 2 compagnies. La solution dans ce contexte est l'usage de VRF par client, qu'on va ici configurer


## Reference

http://www.i3s.unice.fr/~sassatelli/M3102/TP5_VRF_etudiants.pdf


## Useful Debug commands

* sh ip vrf

* sh ip route vrf CUST1

* ping vrf CUST1 192.168.1.1

* clear ip ospf process
