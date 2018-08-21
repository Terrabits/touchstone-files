#!/usr/bin/env python
import numpy       as np
from   pathlib import Path
import skrf        as rf

root_path = Path(__file__).parent

DB_MAX         = 10
reflection_dB  = 30.0
freq           = [0.0, 1.0E3] # GHz
z0             = 50.0

def db_to_ri(dB):
    mag = rf.db_2_mag(dB)
    return complex(mag, 0)

for attenuation_dB in range(1, DB_MAX+1):
    filename    = str(root_path / '{0} dB.s2p'.format(attenuation_dB))
    reflection  = db_to_ri(-1.0 * reflection_dB )
    attenuation = db_to_ri(-1.0 * attenuation_dB)
    points      = len(freq)
    s1x = [reflection, attenuation]
    s2x = [attenuation, reflection]
    s   = [[s1x, s2x]] * points
    s   = np.array(s)
    rf.Network(f=np.array(freq), s=s, z0=z0).write_touchstone(filename)
