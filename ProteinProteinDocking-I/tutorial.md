Protein Protein Docking 
======================= 

**System: ARNASE-BARSTAR COMPLEX**  
a bacterial ribonuclease and its mutant inhibitor barstar


**Steps to perform docking using Cluspro**  
***Let's save Chain A and D for docking study***  
steps:   
1) download pdb file 1BRS  
2) open in chimera  

**Clean PDB file:**  
3) select water molecules (Select -> Residues -> HOH) [it will display nothing]  
4) Action -> Atom/Bonds -> Show [it will show hidden water molecules]  
5) Action -> Atom/Bonds -> delete [it will delete selected atoms]  
  
**Save chain A**  
6) select chain A (Select -> Chain -> A)  
7) open save pdb option (File -> Save PdB)  
8) give filename 1BRS_A.pdb, and tick option of "save selected atoms only" and save.  

**Save chain D**  
9) Rotate the pdb structure a little to give some randomness  
10) select chain D (Select -> Chain -> D)  
11) open save pdb option (File -> Save PdB)  
12) give filename 1BRS_D.pdb, and tick option of "save selected atoms only" and untick "use untransformed coordinates" and and save  

**13: Perform docking using Cluspro2**  



Prform docking using AlphaFold2 (ColabFold Version) 
===================================================  

Link: (https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb)   
Obtained chains from RCSB (PDB: 1BRS)  

```sh
>1BRS_1|Chains A, B, C|BARNASE|Bacillus amyloliquefaciens (1390)
AQVINTFDGVADYLQTYHKLPDNYITKSEAQALGWVASKGNLADVAPGKSIGGDIFSNREGKLPGKSGRTWREADINYTSGFRNSDRILYSSDWLIYKTTDHYQTFTKIR
>1BRS_2|Chains D, E, F|BARSTAR|Bacillus amyloliquefaciens (1390)
KKAVINGEQIRSISDLHQTLKKELALPEYYGENLDALWDALTGWVEYPLVLEWRQFEQSKQLTENGAESVLQVFREAKAEGADITIILS
```
Combine chains using ":"  

```sh
AQVINTFDGVADYLQTYHKLPDNYITKSEAQALGWVASKGNLADVAPGKSIGGDIFSNREGKLPGKSGRTWREADINYTSGFRNSDRILYSSDWLIYKTTDHYQTFTKIR:KKAVINGEQIRSISDLHQTLKKELALPEYYGENLDALWDALTGWVEYPLVLEWRQFEQSKQLTENGAESVLQVFREAKAEGADITIILS  
```  

Submit to ColabFold.






