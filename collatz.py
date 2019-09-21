#!/usr/bin/env python
# -*- coding: utf-8 -*-
i=1
m=0
while i<=100:
    r=0
    n=i
    print("Test für n={}".format(n))
    while n!=1:
        if n%2==0:   # n ist gerade
            n/=2
        else:
            n=3*n+1
        r+=1        # Rundenzaehler
    print(" bestanden nach {} Runden".format(r))
    i+=1
    if m<r:
        m=r         # neue laengste Runde
print("Laengste Runde hatte {} Iterationen.".format(m))
