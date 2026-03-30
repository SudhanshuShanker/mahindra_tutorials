#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 16:12:39 2025
A very simple RabD example 
@author: sudhanshu
"""


from pyrosetta import *
from pyrosetta.rosetta import *

from rosetta.protocols.analysis import InterfaceAnalyzerMover
from rosetta.protocols.rosetta_scripts import XmlObjects


# init("-mute all")

init("-mute all -ignore_unrecognized_res -outer_cycle_rounds 5 \
     -input_ab_scheme AHo_Scheme -cdr_definition North \
         -output_ab_scheme AHo_Scheme")

pose = pose_from_pdb("rabd_/my_ab.pdb")
original_pose = pose.clone()

rabd = XmlObjects.static_get_mover(
    '<AntibodyDesignMover name="RAbD" \
    seq_design_cdrs="L1,L3" light_chain="kappa"/>')
rabd.apply(pose)
pose.dump_pdb("rabd_/designed_ab.pdb")





###
iam = InterfaceAnalyzerMover("LH_ABCDEFGIJKZ")
iam.set_pack_separated(True)
iam.apply(pose)
iam.apply(original_pose)

dg_term = 'dG_separated'
print("dG Diff:", pose.scores[dg_term] - original_pose.scores[dg_term])


#https://docs.rosettacommons.org/docs/latest/application_documentation/antibody/RosettaAntibodyDesign
