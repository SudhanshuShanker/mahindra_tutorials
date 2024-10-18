#!/bin/bash
mkdir test_ADCP
cd test_ADCP
wget -O https://raw.githubusercontent.com/SudhanshuShanker/mahindra_tutorials/refs/heads/main/ADCP_docking/bench_set/3q47/3q47.pdb 
wget https://raw.githubusercontent.com/SudhanshuShanker/mahindra_tutorials/refs/heads/main/ADCP_docking/bench_set/3q47/3q47_rec.pdb
wget https://raw.githubusercontent.com/SudhanshuShanker/mahindra_tutorials/refs/heads/main/ADCP_docking/bench_set/3q47/3q47_pep.pdb

exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>log.out 2>&1

echo ""
echo "Testing Reduce"
reduce 3q47_pep.pdb > 3q47_pepH.pdb
reduce 3q47_rec.pdb > 3q47_recH.pdb
echo ""
echo "Testing prepare_receptor and prepare_ligand"
prepare_receptor -r 3q47_recH.pdb
prepare_ligand -l 3q47_pepH.pdb
echo ""
echo "Testing AGFR"
agfr -r 3q47_recH.pdbqt -l 3q47_pepH.pdbqt -asv 1.1 -o 3q47
echo "Testing ADCP"
adcp -T 3q47.trg -s "npisdvd" -N 2 -n 2000 -L swiss -w testDir -o testNSAAandD -O
echo "Testing ADCP min"
adcp -T 3q47.trg -s "npisdvd" -N 2 -n 2000 -L swiss -w testDir -o testNSAAandD -O -nmin 2
echo "Testing ADCP NST min"
adcp -T 3q47.trg -s "n<ADAM>pisdvd" -N 5 -n 2000 -L swiss -w testDir -o testNSAAandD -O -nmin 2
