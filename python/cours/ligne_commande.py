#!/usr/local/bin/python3
import sys
import os
import shutil
import filecmp
import subprocess
import re
import zipfile
import syslog

# Récup des arguments donnés en parametre
print("Nombre d'argument {}".format(len(sys.argv)))
print("La ligne de commande: ")

for txt in sys.argv:
    print(txt)

# Acces a la platform
print("Platform d'execution: {} - {}".format(sys.platform, os.name))

# Flux standard

# sys.stdin.write("Je suis la sortie standard")
sys.stderr.write("Je suis la sortie d'erreur")
# lg = sys.stdin.readlines()
# sys.stdin.write("J'ai lu {}".format(lg))
# print("J'ai lu {}".format(lg))

# Acces au contenu fichier
# ______écriture_____________
fd = open("mdp.txt", "+w")
i = fd.write("Scripting python")
print("{} octect écrits".format(i))
fd.close()

# ______Lecture_____________
fd = open("mdp.txt", "r")
i = fd.read()
print("Contenu dans le fichier: {}".format(i))
fd.close()

print("---------------------------------------------------------")
fd = open("mdp.txt", "r")
i = fd.readlines()
for line in i:
    print("Ligne: {}".format(line))
fd.close()
print("---------------------------------------------------------")

fd = open("mdp.txt", "r")
i = fd.readline()
while line:
    print("New Ligne: {}".format(line))
    line = fd.readline()
fd.close()

# Le system de fichier
# os.chdir('..') #Il te retourne au repertoir home
fic = os.listdir('./')
for i in fic:
    print(i)

try:
    os.makedirs("New_Reps")
    if os.path.isdir("./New_Reps"):
        print('Cest un foler')
    else:
        print('I dont known')
    os.rmdir('New_Reps')

    shutil.copy('mdp.txt', 'toto.txt')

    result = filecmp.cmp('mdp.txt', 'toto2.txt')
    if result:
        print('Les files sont identiques')
    else:
        print('Les files sont différent')
except Exception as e:
    print(f'Une exception sest produite {e}')

p = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
print("=======================================================")
print(p.communicate())

# Avec la methode RUN
print('*************************************')

res = subprocess.run(['ls', '-l'])
print('res: ', res.returncode)
print('_____________avec shell _____________')
res = subprocess.run(['ls', '-l'], shell=True)
print('res: ', res.returncode)

try:
    print('------------------avec check---------------------')
    res = subprocess.run('ls -l', shell=True, check=True)
    print('res: ', res.returncode)
except subprocess.CalledProcessError as err:
    print('Error: ', err)
    exit(1)

print('------------------avec stdout---------------------')
res = subprocess.run(['ls', '-al'], stdout=subprocess.PIPE)
print('res: ', res.returncode)
print('Il ya {} octects dans la sorties standard'.format(len(res.stdout)))
out = res.stdout.decode('utf-8')
print('out:', out)

# The regular expression
print('-------------------Les expressions régulières-----------------------')
pattern = 'RT0801'
text = 'Chapitre 2 - RT0801 : expressions régulières...'
match = re.search(pattern, text)
s = match.start()
e = match.end()

print("{} trouvé dans l'expressions {} \n entre {} et {} ({})".format(
    match.re.pattern, match.string, s, e, text[s:e]))


# Découpage avec la méthode split()
print('-------------------Découpage avec la méthode split-----------------------')
text = 'Bonjour;à;tout;le;monde'
tab = text.split(';')
for element in tab:
    print('--------->{}'.format(element))

# Remplacement avec la méthode sub()
print('-------------------Remplacement avec la méthode sub-----------------------')
text = 'bonjour;à;tous'
text2 = re.sub(';', '----', text)
print('Remplacement {} devient {}'.format(text, text2))


# Compression de fichier avec la biblio zipfile
print('-------------------Compression de fichier avec la biblio zipfile-----------------------')
for element in ['mdp.txt,' 'toto.txt', 'toto2.txt', 'myzip.zip']:
    print('{:>15} {}'.format(element, zipfile.is_zipfile(element)))

# Creation de l'archive
print('Creation dune archive')
zipf = zipfile.ZipFile('myzip.zip', 'w')
zipf.write('mdp.txt')
zipf.write('toto.txt')
zipf.close()

# Extraction dune archive
print('Extraction dune archive')
zipf = zipfile.ZipFile('myzip.zip', 'r')
zipf.extractall('extract')
zipf.close()


# Les logs
print('-------------------Les logs-----------------------')
syslog.openlog(ident='toto', logoption=syslog.LOG_PID,
               facility=syslog.LOG_AUTH)
syslog.syslog(priority=syslog.LOG_INFO, message='Utilisateur identifié')
syslog.closelog()

exit(0)
