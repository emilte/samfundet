#!/bin/sh

# ssh-keygen -t rsa -b 4096 -C "username@samfundet.no"
# save as ~/.ssh/id_rsa_<username>_samfundet
# No passphrase
# ssh-copy-id -i ~/.ssh/id_rsa_<username>_samfundet username@samfundet.no

read -p "Username: " username

read -p "Type [prod/dev]: " server

folder="0"

# if [ "$server" != "prod" && "$server" != "dev" ]; then
#     exit 0
# fi

if [ "$server" = "dev" ]; then
    folder="nbb-dev"
fi

if [ "$server" = "prod" ]; then
    folder="nbb"

    read -p "Are you sure you want to deploy production-server? [y/N]: " confirmation
    if [ "$confirmation" != "y" ]; then
        exit 0
    fi
fi

if [ "$folder" != "0" ]; then
    ssh -i ~/.ssh/id_rsa_${username}_samfundet ${username}@samfundet.no "
        cd '/var/www/samfundet.no/${folder}/start3'
        git pull
        touch ../reload
    "
fi
