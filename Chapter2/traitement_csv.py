#!/usr/bin/env python
# -*- coding : Utf-8 -*-

import csv

# Lire un fichier csv et le garder sous forme de liste
fic = open('test_notes.csv')
tableau = csv.reader(fic)
tablist = list(tableau)

# Ajouter les moyennes de chaque ligne (élève)
def mean(l):
    nb = len(l)
    if isinstance(l[0],str):
        valeurs = [eval(x) for x in l]
    else:
        valeurs = l
    return sum(valeurs) / nb

tablist[0].append('Moyennes')
for el in range(1, len(tablist)):
    tablist[el].append(mean(tablist[el][1:]))
    
# Ajouter les moyennes de chaque colonne (matière)
valeurs = [x[1:] for x in tablist[1:]]
nbm = len(valeurs[0])
moymat = ['Moyennes']
for m in range(nbm):
    moymat.append(mean([x[m] for x in valeurs]))

tablist.append(moymat)
print(tablist)

with open('test.csv','w') as fic:
    ecrire = csv.writer(fic)
    for l in tablist:
        ecrire.writerow(l)
fic.close
