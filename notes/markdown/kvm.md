# Introduction

On distingue les hyperviseurs de type I et type II.

Type I :

* KVM
* VMWARE ESXI
* ...

Type II :

* Virtualbox
* VMWare Player (Workstation)
* QEMU (Quick EMulator, KVM VM -> emulate # type of processor, ...)
* ...


La librairie **libvirt** fournit une abstractihttps://cloudinit.readthedocs.io/en/latest/
Le logiciel virt-manager/virt-viewer/virsh est basé sur libvirt pour permettre la création de machine virtuelle QEMU/KVM ou autres.

(virt-manager/virsh/virt-viewer/OpenStack) --> (libvirt) --> (kvm/lxc/xen/esx/...)


# Installation sous Ubuntu

``` 
$ sudo apt install libvirt-clients libvirt-daemon-system bridge-utils 

$ sudo apt install qemu-kvm qemu qemu-utils qemu-system

$ sudo apt install virt-manager virt-viewer cpu-checker virtinst

$ service libvirtd status

$ /etc/init.d/libvirt status

```

# Création d'une Image qcow2 bootable (alpine,ubuntu,...) à partir de l'ISO d'installation

[http://www.uni-koeln.de/~pbogusze/posts/Building_an_tiny_GNS3_FRR_linux_appliance.html](http://www.uni-koeln.de/~pbogusze/posts/Building_an_tiny_GNS3_FRR_linux_appliance.html)

```sh

# create disk file ~ hard drive in qcow2 format
qemu-img create -f qcow2 alpine-frr7.qcow2 1G

# boot using iso and new hard drive previously created and do installation
qemu-system-i386 -boot d -cdrom alpine-virt-3.12.0-x86.iso -hda alpine-frr7.qcow2 -enable-kvm -m 1G -serial telnet:localhost:4321,server,nowait -object rng-random,filename=/dev/urandom,id=rng0 -device virtio-rng-pci,rng=rng0

# Start VM using qcow2 file
qemu-system-i386 alpine-frr7.qcow2 -enable-kvm -m 1G -serial telnet:localhost:4321,server,nowait -object rng-random,filename=/dev/urandom,id=rng0 -device virtio-rng-pci,rng=rng0 &

```

# Création d'une VM KVM avec [Cloud images](https://cloud-images.ubuntu.com/) et  [Cloud Init](https://cloudinit.readthedocs.io/en/latest/)

Solutions utilisés par les cloud providers pour automatiser la création de machine virtuelle pour les clients.

[https://fabianlee.org/2020/02/23/kvm-testing-cloud-init-locally-using-kvm-for-an-ubuntu-cloud-image/](https://fabianlee.org/2020/02/23/kvm-testing-cloud-init-locally-using-kvm-for-an-ubuntu-cloud-image/)


```bash

# -F qcow2 : specify original image format in snapashot metadata
qemu-img create -b ~/Downloads/bionic-server-cloudimg-amd64.img -f qcow2 -F qcow2 snapshot-bionic-server-cloudimg.qcow2 10G

```