# Mount NAS

* step 1

yum install cifs-utils

* step2 

mkdir /mnt/nas

* step3 

mount -t cifs //nas.xpert-lab.local/volume0  /mnt/nas -o username=asoglo@xpert-lab.com

mount -t cifs //nas.xpert-lab.local/volume0  /mnt/nas -o username=asoglo@xpert-lab.com -o vers=1.0

sudo mount -t cifs //172.16.0.200/volume0  /mnt/nas -o username=asoglo@xpert-lab.com -o vers=1.0


* umount /mnt/nas


# Linux networking

sudo dhclient -v eth0

ip addr flush dev eth0


# Flush DNS Resolution caches

sudo systemd-resolve --flush-caches

sudo systemd-resolve --statistics

sudo systemctl restart nscd


# Services start on boot


```bash
sudo update-rc.d -f apache2 remove
sudo update-rc.d -f mysql remove
#enable it again
sudo update-rc.d apache2 enable
```

# Uninstall & purge packages

```bash

sudo apt-get purge --auto-remove packagename

# parse folders and clean packages (Cleaning after packages removal done)

[[ $(dpkg -l | grep ^rc) ]] && sudo dpkg -P $(dpkg -l | grep ^rc | tr -s " " | cut -d " " -f 2)
```

# Sed

* find and replace in file 


```bash
sed  's/INFO/DEBUG/' test.log
```

* find and replace only first occurence


```bash
sed '0,/INFO/s/INFO/DEBUG/' test.log
```

* find and replace only a part of pattern


```bash
sed 's/method=[a-zA-Z0-9]*/method=POST/' test.log
sed 's/HTTP\/[0-9.]*/HTTP\/2.1/' test.log
```

* find and replace only a part of pattern (replace only first occurence)


```bash
sed '0,/HTTP\/[0-9.]*/s/HTTP\/[0-9.]*/HTTP\/2.1/' test.log
```

* insert into a particular line


```bash
sed '3i text to insert \n' test.log
```

* usefull examples


```bash
#print line 0
sed -n '0,/django/p' test.log

##delete
sed -n '/django/d' test.log

#delete a line
sed '1d' test.log

#delete from x to y line
sed '1,3d' test.log

#delete from x to the end 
sed '1,$ d' test.log

#append after pattern matched
sed -n '/django/ a to be appended after pattern mached' test.log 


```

# AWK


```bash
awk 'findme' file.txt
awk 'findme/{print $0}' file.txt
awk -F: 'findme/{print $1}'
awk -F/ 'findme/{print $1}'


```

# TR


```bash
tr -d ' '
tr -d [[:space:]]
```


# Install DNSMASK (DNS SERVER + DHCP SERVER)


apt-get update
apt-get install dnsmasq
nano /etc/dnsmasq.conf

If you don't want dnsmasq to read /etc/resolv.conf or any other
file, getting its servers from this file instead (see below), then
uncomment this.

no-resolv
address=/cisco.com/8.8.4.8
address=/ubuntu1.lab/10.1.1.2
address=/ubuntu2.lab/10.1.2.2
address=/ubuntu3.lab/10.1.3.2
address=/ubuntu4.lab/10.1.4.2


* /etc/init.d/dnsmasq restart




