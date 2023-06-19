#!/bin/bash

if [ $# -ne 5 ]; then
    echo "Paramètres manquant"
    exit 1
fi

archive_name=$1
folder_to_save_name=$2
addr_server=$3
login=$4
password=$5


tar -cvf "$archive_name" "$folder_to_save_name"

if [ $? -ne 0 ]; then
    echo "L'archive a échoué"
fi

sshpass -p "$password" sftp "$login@$addr_server" << FINSFTP

put $archive_name
exit

FINSFTP

if [ $? -ne 0 ]; then
    echo "Echec...."
else
    echo "Opération réussie...."
fi

#Test command
#./scripts-cours/bash/sc-sauvegarde.sh scripts-cours/bash/zip.tar scripts-cours/bash/sauvegarde/ 10.11.1.242 diallo toor