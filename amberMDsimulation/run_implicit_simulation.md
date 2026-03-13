MD somilation in implicit solvent
=================================


1) create minimization and mdrun files  

```sh
polyA-polyT 10-mer: initial minimization prior to MD GB model
 &cntrl
  imin   = 1,
  maxcyc = 500,
  ncyc   = 250,
  ntb    = 0,
  igb    = 1,
  cut    = 12
 /
```
```sh
polyA-polyT 10-mer: initial minimization prior to MD GB model 
 &cntrl
  imin   = 1,
  maxcyc = 500,
  ncyc   = 250,
  ntb    = 0,
  igb    = 1,
  cut    = 999
 /
```

2) Run minimization  

```sh
sander -O -i polyAT_gb_init_min.in -o polyAT_gb_init_min.out -c polyAT_vac.rst7 -p polyAT_vac.prmtop -r polyAT_gb_init_min.ncrst
```

3) create MDIN for simulation  

```sh
10-mer DNA MD Generalized Born, 12 angstrom cut off
 &cntrl
  imin = 0, ntb = 0,
  igb = 1, ntpr = 100, ntwx = 100,
  ntt = 3, gamma_ln = 1.0,
  tempi = 300.0, temp0 = 300.0
  nstlim = 100000, dt = 0.001,
  cut = 12.0
 /
```

4) run MD simulation  

```sh
sander -O -i polyAT_gb_md1_12Acut.in -o polyAT_gb_md1_12Acut.out -c polyAT_gb_init_min.ncrst -p polyAT_vac.prmtop -r polyAT_gb_md1_12Acut.ncrst -x polyAT_gb_md1_12Acut.nc
```

5) analyze rms change with ptraj  

create a file by name ptrajin with content:  
```sh
trajin polyAT_gb_md1_12Acut.nc
rms first mass out polyAT_gb_md1_12Acut.rms
```
Now run cpptraj as:  
```sh
cpptraj -i ptrajin -p polyAT_vac.prmtop 
```

Now run the explicit simulation using the following link: https://ambermd.org/tutorials/basic/tutorial1/section5.php 
