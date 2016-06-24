#!/usr/bin/env python
# -*- coding : Utf-8 -*-

# Les dictionnaires
#-----------------------------------------------------------------------------
tel = {'Valérie': 2660, 'Christian':2078, 'Anne':3310}
tel['Adèle'] = 4242
tel['Christian']

# Les ensembles
#-----------------------------------------------------------------------------
fruits = {'pomme', 'pomme', 'poire', 'pomme', 'orange', 'grenade', 42}

def trouve(mot, lettre):
    n = 0
    for x in mot:
        n += 1
        if x == lettre:
            return n
    return -1
    
mot0 = input('Mot ? ')
l1 = input('Lettre ? ')
print("La lettre {} est en position {} dans le "
    "mot {}".format(l1, trouve(mot0, l1), mot0))
