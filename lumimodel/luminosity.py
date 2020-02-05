import pandas as pd 
import numpy as np

def get_bunch_luminosity(
B1N=1.15e11, B2N=1.15e11,
B1x=0,  B1px=0,  B1y=0, B1py=0,
B2x=0,  B2px=0, B2y=0, B2py=0,
B1betx=0.55, B1bety=0.55,
B2betx=0.55, B2bety=0.55,
B1epsilon_x=3e-10, B1epsilon_y=3e-10,  # geometrical emittances
B2epsilon_x=3e-10, B2epsilon_y=3e-10,  # geometrical emittances
B1sigma_s=0.07, B2sigma_s=0.07):
  '''
  This is the help.
  - all units in SI, assuming 
  - Gaussian distributions
  - alfx and alfy vanishing at the IP ultrarelativistic approach.
  We should aim to be general (round/flat optics, vertical/horizontal/skew angle, Pb-Pb/p-p/PB-p collisions)
  '''
  print('To be implemented!')
