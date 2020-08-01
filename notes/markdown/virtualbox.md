# Upgrade Virtualbox Ubuntu Bionic (18.4)

Add following line to /etc/apt/sources.list

deb [arch=amd64] http://download.virtualbox.org/virtualbox/debian bionic contrib

apt update

apt install virtualbox


# Install Virtualbox Extensions pack

Download Extensions pack from virtualbox website

File -> Preferences -> Extensions -> (+)


# Install extensions gui-less mode

mount /dev/cdrom /media/cdrom.

sudo apt-get install -y dkms build-essential linux-headers-generic linux-headers-$(uname -r)

./VBoxLinuxAdditions.run


# Mount a shared folder dropbox

"dropbox" is the name of the shared folder in virtualbox GUI

sudo mkdir /mnt/shared/

sudo mount -t vboxsf dropbox /mnt/shared/


