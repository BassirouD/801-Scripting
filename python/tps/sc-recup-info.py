#!/usr/local/bin/python3
import os
import subprocess

cpt = 0
fileName = 'toto' + str(cpt) + '.txt'

while (os.path.isfile(fileName)):
    cpt = cpt + 1
    fileName = 'toto' + str(cpt) + '.txt'

files = open(fileName, 'w+')
res = subprocess.run(['id'], capture_output=True)
files.write(str(res))
print(files.read())
files.close()
exit(0)