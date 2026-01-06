!/bin/bash

echo "P-Linux Installer"

lsblk
read -p "Disco alvo: " DISK

wipefs -a /dev/$DISK
parted /dev/$DISK mklabel gpt
parted /dev/$DISK mkpart primary ext4 1MiB 100%

mkfs.ext4 /dev/${DISK}1
mount /dev/${DISK}1 /mnt

cp -r rootfs/* /mnt
grub-install --root-directory=/mnt /dev/$DISK