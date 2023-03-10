#!/bin/bash

/home/fiedlerl/tools/qe_development_branch/PW/src/pw.x -in Be_snapshot0.pw.scf.in | tee dft.out
/home/fiedlerl/tools/qe_development_branch/PP/src/pp.x -in Be_snapshot0.pp.ldos.in
