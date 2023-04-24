#!/usr/local/bin/python3
import sys
import os
import shutil
import filecmp
import subprocess

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

p=subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
print("=======================================================")
print(p.communicate())

exit(0)
