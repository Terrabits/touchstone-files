#!/usr/bin/env python
import numpy       as np
from   pathlib import Path
import skrf        as rf

root_path = Path(__file__).parent

N_MAX = 24
ports = range(1,N_MAX+1)
freq  = [0.0, 1.0E3] # GHz
z0    = 50.0

for n in ports:
    filename = str(root_path / 're-im.s{0}p'.format(n))
    s  = []
    for f in freq:
        s_f = []
        for i in range(1,n+1):
            s_row = []
            for j in range(1,n+1):
                ij   = float('{0}{1}'.format(i, j))
                s_ij = complex(ij, ij)
                s_row.append(s_ij)
            s_f.append(np.array(s_row))
        s.append(np.array(s_f))
    rf.Network(f=np.array(freq), s=np.array(s), z0=z0).write_touchstone(filename)
