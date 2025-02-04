#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 09:50:06 2025
"""

from Bio.PDB import  PDBParser
import numpy as np



def getCAatomsOfChain(pdbfile, chainId):
    # To get all CA atoms from a chain with chain ID
    parser=PDBParser()
    structure = parser.get_structure('mypdb', pdb)
    outAtoms = []   
    
    for atom in structure.get_atoms():    
       if atom.get_id() == 'CA':
           
           if atom.get_full_id()[2] == chainId:
               outAtoms.append(atom)
   
    return outAtoms


def distance(atom1,atom2):
    # To calculate distance between two atom objects from PDBparser
    distance = np.sqrt(sum((atom1.coord - atom2.coord)**2))
    return distance
    

# Lets write code to get CA atoms from pdb file 1AWR.pdb for chain A and G

pdb = '1AWR.pdb'

# Lets calculate distances between CA atoms from both chains (inter-chain).

# Lets find atom pairs with residue information to find natives < 8A interactions
# Lets find atom pairs with residue information to find natives > 8A and less tha 20A interactions