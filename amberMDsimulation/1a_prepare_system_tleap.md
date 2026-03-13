1) Download pdbfile from https://ambermd.org/tutorials/basic/tutorial1/files/pdb_files/nuc.pdb  
use:  
```sh
wget https://ambermd.org/tutorials/basic/tutorial1/files/pdb_files/nuc.pdb
```

2)Run tleap: to prepapre system  

```sh
tleap -s -f $AMBERHOME/dat/leap/cmd/leaprc.DNA.bsc1
```

3) add tip3p water model  

```sh
source leaprc.water.tip3p
```

4) Load pdb file  

```sh
dna1 = loadpdb nuc.pdb
```

6) save  parameter and coordinates for in vacuo simulation  

```sh
saveamberparm dna1 polyAT_vac.prmtop polyAT_vac.rst7
```

7) save parameters for neutralized environment

```sh
addions dna1 Na+ 0
```
```sh
saveamberparm dna1 polyAT_cio.prmtop polyAT_cio.rst7
```

8) create input files for explicit environment  

```sh
dna2 = copy dna1
solvateoct dna2 TIP3PBOX 8.0
saveamberparm dna2 polyAT_wat.prmtop polyAT_wat.rst7
```






