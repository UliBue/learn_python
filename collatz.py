#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

print "-----------------------------------------"
print " Testen der Collatz'schen Vermutung"
print"------------------------------------------\n"
print "Bitte geben sie die Testgrenze ein: "

number = None
while number is None:
    line = sys.stdin.readline()
    if line=='':
        print "Eingabeende"
        break
    line=line.strip()
    if not line.isdigit():
        print "Bitte geben sie eine Zahl ein!"
        continue
    number=int(line)
else:
    print "OK, ich teste bis {}.\n".format(number)

i=1
m=0
while i<=number:
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
print("\nLaengste Runde hatte {} Iterationen.".format(m))
