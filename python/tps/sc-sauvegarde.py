#!/usr/local/bin/python3
import pysftp
import sys
import subprocess

host = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
archive_name = sys.argv[4]
folder_to_save_name = sys.argv[5]

if len(sys.argv) == 5:
    print('Tous les paramètres sont présent...')
else:
    print('Paramètres manquants')
    exit(1)

archive = subprocess.run(['tar', '-cvf', archive_name, folder_to_save_name])
print(archive)

with pysftp.Connection(host=host, username=username, password=password) as sftp:
    print('Connection établie....')
    sftp.put(archive_name)
    print("Le fichier a été uploadé avec succès")

exit(0)
