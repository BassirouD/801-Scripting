#!/usr/local/bin/python3
import os
import subprocess
import sys

archive_name = sys.argv[1]
install_folder = sys.argv[2]

extention = os.path.splitext(archive_name)[1][1:]

if(os.path.isfile(archive_name)):
    print("Le fichier existe bien")
    print(extention)
    
    if(extention == "tar" or extention == "tgz"):
        res=subprocess.run(['tar', 'xvf', archive_name, '-C', install_folder])
        print("000000000000000000000000")
    else:
        if(extention == 'zip'):
            res=subprocess.run(['unzip', archive_name, '-d', install_folder])
            print('11111111111111111111111111111')
    
else:
    print('Fichier existe pas...')

exit(0)