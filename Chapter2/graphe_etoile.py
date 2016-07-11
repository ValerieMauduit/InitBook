#!/usr/bin/env python
# -*- coding : Utf-8 -*-

import turtle as ttl
import random as rd

# Initialisations
ttl.ht()
ln_lig = 20
ln_s = 15
nbl = 20
la = 45

# Point zéro
for ll in range(nbl):
    ttl.pen(speed = 5)
    ttl.up()
    ttl.goto(0, 0)
    ttl.down()
    angles = [rd.random() * 2 * la - la for x in range(ln_lig)]
    ttl.color([0, 0, 0])
    for n in range(ln_lig):
        ttl.left(angles[n])
        ttl.forward(ln_s)
    ttl.color([1, 0, 0])
    ttl.pen(speed = 0)
    ttl.begin_fill(); ttl.circle(ln_s / 4); ttl.end_fill()
    
# Fin
ttl.mainloop()
