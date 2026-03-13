
1) create mdin input file (simulation options)  

```sh  
polyA-polyT 10-mer: initial minimization prior to MD
 &cntrl
  imin   = 1,
  maxcyc = 500,
  ncyc   = 250,
  ntb    = 0,
  igb    = 0,
  cut    = 12
 /
```

2) run in-vacuo minimization  

```sh
sander -O -i polyAT_vac_init_min.in -o polyAT_vac_init_min.out -c polyAT_vac.rst7 -p polyAT_vac.prmtop -r polyAT_vac_init_min.ncrst  
```

now analyze the output file  


3) create pdb from minimized coordinates (ncrst)  

```sh
ambpdb -p polyAT_vac.prmtop -c polyAT_vac_init_min.ncrst > polyAT_vac_init_min.pdb
```

4) compare intial and current structure  

```sh
chimera ../nuc.pdb polyAT_vac_init_min.pdb
```

**5) run md simulation**  

a) make input file 

```sh
10-mer DNA MD in-vacuo, 12 angstrom cut off
 &cntrl
  imin = 0, ntb = 0,
  igb = 0, ntpr = 100, ntwx = 100,
  ntt = 3, gamma_ln = 1.0,
  tempi = 300.0, temp0 = 300.0
  nstlim = 100000, dt = 0.001,
  cut = 12.0
 /
```

make similar file for cut=999  

b) run simulation on minimized coordinates  

```sh
sander -O -i polyAT_vac_md1_12Acut.in -o polyAT_vac_md1_12Acut.out -c polyAT_vac_init_min.ncrst -p polyAT_vac.prmtop -r polyAT_vac_md1_12Acut.ncrst -x polyAT_vac_md1_12Acut.nc
```

```sh
sander -O -i polyAT_vac_md1_nocut.in -o polyAT_vac_md1_nocut.out -c polyAT_vac_init_min.ncrst -p polyAT_vac.prmtop -r polyAT_vac_md1_nocut.ncrst -x polyAT_vac_md1_nocut.nc
```

6) Analyze the results  

```sh
process_mdout.perl polyAT_vac_md1_nocut.out 
process_mdout.perl polyAT_vac_md1_12Acut.out 
```
```sh
xmgrace cut12/summary.EPTOT nocut/summary.EPTOT
analyze trajectory in chimera
```





