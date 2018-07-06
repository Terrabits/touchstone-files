#!/usr/bin/env python
import numpy       as np
from   pathlib import Path
import skrf        as rf

root_path = Path(__file__).parent

DB_MAX = 10
GAMMA  = complex(1E-12, 0)
freq   = [0.0, 1.0E3] # GHz
z0     = 50.0

def db_to_ri(x):
    x = 10**(x/10.0)
    return complex(x, 0)


for db in range(1, DB_MAX+1):
    filename = str(root_path / '{0} dB.s2p'.format(db))
    thru = db_to_ri(db)
    s1x = [GAMMA, thru]
    s2x = [thru, GAMMA]
    s   = [[s1x, s2x]]*len(freq)
    s   = np.array(s)
    rf.Network(f=np.array(freq), s=s, z0=z0).write_touchstone(filename)
