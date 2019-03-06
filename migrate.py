# -*- coding: utf-8 -*-
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

add_to_top = """
<alert type="info" dismiss="true" icon="fa fa-info"> **Je suis une page migrée depuis l'ancien wiki.** 

Vous pouvez me supprimer après m'avoir mis à jour si cela est nécessaire. Voir [[:migration|migration]]</alert>"""

for dossier, sous_dossiers, fichiers in os.walk('pages'):
    for fichier in fichiers:
        file_to_migrate = os.path.join(dossier, fichier)
        if file_to_migrate.endswith('.txt'):
            fileR = open(file_to_migrate, "r")
            source = fileR.read()
            fileR.close()
            text_insert = add_to_top+"\n\n\n\n"
            fileW = open(file_to_migrate, "w")
            fileW.write(text_insert + source)
            fileW.close()
            with open("migration.txt", "a") as myfile:
                myfile.write("  * [["+file_to_migrate.replace("/", ":")[6:-4]+"|"+file_to_migrate[6:]+"]] - Score " + str(len(source)) + "\n")
            with open("migration.csv", "a") as myfile:
                myfile.write("https://wiki.lghs.be/"+file_to_migrate.replace("/", ":")[6:-4]+";" + str(len(source)) + "\n")        
            print(bcolors.OKGREEN + "TXT OK " + file_to_migrate + bcolors.ENDC)
        else:
            print(bcolors.FAIL + "TXT NOK " + file_to_migrate + bcolors.ENDC)
            with open("rejected.txt", "a") as myfile:
                myfile.write(file_to_migrate)