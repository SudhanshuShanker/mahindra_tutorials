#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 14:07:11 2025

@author: sudhanshu
"""



stride ='CCCEEEEEEEETTEEEEEEEEEETTTTTHHHHHHHHHHHHTTTTCCTTTEETTEEETTTEEEECTTTTT\
TTCCCCTTTTTTBCCCCCCCCCCTTTEEEECCCTTTTBCCCEEEECCCCGGGTTTTCEEEEEEETHHHHHHHGGGCBT\
TBBTTTTEEEEEEEECC'

cfPrediction = "EEEEEEHEEHHHTTCCCCHHHHHHHTHHHHHHHHHHHCCCCTTCCCCCTCEEEEEEEEEEEC\
TTCCCCCCCCCTTCHHHHHHHTHHEEHHCCCTCHHHHHHCCTCCCTTEEEEHHHHHHHHHTHHEEEHHHHTHHHHHHH\
HHHCCTCCTHHHHHEHHHCCCCCC"


JPredPrediction = "---EEEEEEEE-----EEEEEEE-----HHHHHHHHHHHH----------EEEE-----\
E----------------------------------EEEEE----------EEEEE----------EEEEEEEE--HHH\
HHHHHH--------EEEEEEEEEEE--"



convDict = {'H':'H', 'G':'H', 'I':'H',
            'E':'E', 'B':'E', 
            'T':'C', 'S':'C', 'C':'C', ' ':'C', '-':'C'}


def Conv2HEC(inSeq):    
    OutSeq=''    
    for c in inSeq:
        cOut =  convDict[c]
        OutSeq = OutSeq + cOut
    
    return OutSeq

convStride = Conv2HEC(stride)
convCF = Conv2HEC(cfPrediction)
convJP = Conv2HEC(JPredPrediction)


count = 0
for i,j in zip(convStride, convJP):
    if i==j:
        count +=1
        
print(count/len(convStride))
    

## convert 
# H	α-helix	H
# G	310-helix	H
# I	π-helix	H
# E	β-strand (extended conformation)	E
# B	Isolated β-bridge	E
# T	Turn	C
# S	Bend	C
# C (or ' ')	Coil	C









# write a function to convert these sequences


## convert T and C to C

## calculate % accuracy


## calculate % accuracy for H,C, E
##
