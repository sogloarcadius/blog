
## DATABASE


* Enable remote connections to centreon database

GRANT ALL PRIVILEGES
ON *.*
TO 'centreon'@'%'
IDENTIFIED BY 'centreon';


## Plugins


* Plugins path

Variable name : $CENTREONPLUGINS$

Possible Values :

- /usr/lib/centreon/plugins   <== plugins pack installed using plugins manager (clone centreon plugins from github and place it in this folder)

- /usr/lib64/nagios/plugins/
	
	

## TROUBLESHOOTING

 systemctl status httpd24-httpd
 systemctl status snmpdRéseau
 systemctl status snmptrapd
 systemctl status rh-php71-php-fpm
 systemctl status centcore
 systemctl status centreontrapd
 systemctl status cbd
 systemctl status centengine
 systemctl status centreon


 systemctl enable httpd24-httpd
 systemctl enable snmpd
 systemctl enable snmptrapd
 systemctl enable rh-php71-php-fpm
 systemctl enable centcore
 systemctl enable centreontrapd
 systemctl enable cbd
 systemctl enable centengine
 systemctl enable centreon
 
 
 
 
systemctl start rh-php71-php-fpm
systemctl start httpd24-httpd
systemctl start mysqld
systemctl start cbd
systemctl start snmpd
systemctl start snmptrapd
 


Remove cenreon files
#repoquery --installed -l httpd

#bash script 

systemctl stop rh-php71-php-fpm
systemctl stop httpd24-httpd
systemctl stop mysqld
systemctl stop cbd
systemctl stop snmpd
systemctl stop snmptrapd


 systemctl disable httpd24-httpd
 systemctl disable snmpd
 systemctl disable snmptrapd
 systemctl disable rh-php71-php-fpm
 systemctl disable centcore
 systemctl disable centreontrapd
 systemctl disable cbd
 systemctl disable centengine
 systemctl disable centreon
 systemctl disable mysql



 rm /usr/sbin/centengine
 rm /usr/sbin/cbd
 
rm -rf /usr/share/centreon
rm -rf /usr/share/centreon-engine
rm -rf /usr/share/centreon-broker
rm -rf /usr/share/centreon-packs

rm -rf /var/lib/centreon
rm -rf /var/lib/centreon-engine
rm -rf /var/lib/centreon-broker

rm -rf /etc/centreon
rm -rf /etc/centreon-engine
rm -rf /etc/centreon-broker



rm -rf /var/lib/mysql
rm /etc/my.cnf
rm ~/.my.cnf

yum remove MariaDB-server MariaDB-client
yum remove centreon-database
yum remove centreon-base-config-centreon-engine 
yum remove centreon


* centreon

/etc/centreon/centreon.conf.php

* centreon-base-config-centreon-engine

/etc/centreon/instCentPlugins.conf
/etc/centreon/instCentWeb.conf
/usr/share/centreon/www/install/install.conf.php

* centreon-database

/etc/my.cnf.d/centreon.cnf
/etc/systemd/system/mariadb.service.d/centreon.conf

rm -rf /var/lib/mysql
rm /etc/my.cnf
rm ~/.my.cnf
