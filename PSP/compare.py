#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 14:07:11 2025

@author: sudhanshu
"""



stride ='CCCEEEEEEEETTEEEEEEEEEETTTTTHHHHHHHHHHHHTTTTCCTTTEETTEEETTTEEEECTTTTT\
TTCCCCTTTTTTBCCCCCCCCCCTTTEEEECCCTTTTBCCCEEEECCCCGGGTTTTCEEEEEEETHHHHHHHGGGCBT\
TBBTTTTEEEEEEEECC'

## convert 
# H	α-helix	H
# G	310-helix	H
# I	π-helix	H
# E	β-strand (extended conformation)	E
# B	Isolated β-bridge	E
# T	Turn	C
# S	Bend	C
# C (or ' ')	Coil	C


cfPrediction = "EEEEEEHEEHHHTTCCCCHHHHHHHTHHHHHHHHHHHCCCCTTCCCCCTCEEEEEEEEEEEC\
TTCCCCCCCCCTTCHHHHHHHTHHEEHHCCCTCHHHHHHCCTCCCTTEEEEHHHHHHHHHTHHEEEHHHHTHHHHHHH\
HHHCCTCCTHHHHHEHHHCCCCCC"


JPredPrediction = "---EEEEEEEE-----EEEEEEE-----HHHHHHHHHHHH----------EEEE-----\
E----------------------------------EEEEE----------EEEEE----------EEEEEEEE--HHH\
HHHHHH--------EEEEEEEEEEE--"




convDict = {'H':'H', 'G':'H', 'I':'H',
            'E':'E', 'B':'E', 
            'T':'C', 'S':'C', 'C':'C', ' ':'C', '-':'C'}



# write a function to convert these sequences


## convert T and C to C

## calculate % accuracy


## calculate % accuracy for H,C, E
##
