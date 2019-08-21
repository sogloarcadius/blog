sestatus


systemctl enable firewalld

systemctl start firewalld

systemctl status firewalld

sudo /sbin/iptables -I INPUT -p tcp -m tcp --dport 80 -j ACCEPT

sudo /sbin/service iptables save

firewall-cmd --zone=public --add-port=80/tcp

firewall-cmd --zone=public --add-port=80/tcp --permanent 

firewall-cmd --reload


systemctl stop firewalld

systemctl disable firewalld


## docker issue

cat /etc/passwd

sudo groupadd docker
sudo usermod -aG docker $USER


sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p udp --dport 80 -j ACCEPT
sudo iptables -A OUTPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A OUTPUT -p udp --dport 80 -j ACCEPT




sudo iptables -A INPUT -p tcp --dport 32769 -j ACCEPT
sudo iptables -A INPUT -p udp --dport 32769 -j ACCEPT
sudo iptables -A OUTPUT -p tcp --dport 32769 -j ACCEPT
sudo iptables -A OUTPUT -p udp --dport 32769 -j ACCEPT