### BGP Local Preference

Local Preference is BGP Well known discretionnary attribute.

*  By definition all well known attribute are transitive 
 * Local preference attribute sent in iBGP but not in eBGP (you can't influence other AS route propagation process)

### Usefull Commands

* show ip bgp
* show ip bgp _100_ : going through AS 100
* show ip bgp regexp ^100$ : filter routes directly connected to 100
* show ip bgp regexp ^$ : filter only networks originated in local AS
* show ip bgp regexp _4$  : filter routes originated in AS 4
* show ip bgp regexp ^100_. : networks behind AS 100
* show ip bgp .* : all networks