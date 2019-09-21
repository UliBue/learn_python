#!/usr/bin/env python
# -*- coding: utf-8 -*-
i=1
m=0
while i<=100:
    r=0
    n=i
    while n!=1:
        if n%2==0:   # n ist gerade
            n/=2
        else:
            n=3*n+1
        r+=1        # Rundenzaehler
    if r==1:
        pf=""
    else:
        pf="n"
    print("Test für n={} bestanden nach {} Runde{}.".format(i,r,pf))
    i+=1
    if m<r:
        m=r         # neue laengste Runde
print("Laengste Runde hatte {} Iterationen.".format(m))
