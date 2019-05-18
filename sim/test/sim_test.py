
import os
import sys

twoup = os.path.abspath(os.path.join(__file__,"../.."))
sys.path.insert(0,twoup+"\src")

from CSMACD import *



if __name__ == "__main__":
  sources = [Source('A',2)]

  sim = CSMA_CD_sim( sources )

  sim.print_sources()






