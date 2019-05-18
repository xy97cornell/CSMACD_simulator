
import os
import sys

twoup = os.path.abspath(os.path.join(__file__,"../.."))
sys.path.insert(0,twoup+"\src")

from CSMACD import *



if __name__ == "__main__":
  sources = [Source('A',2), Source('B',2), Source('C',3)]

  sim = CSMA_CD_sim( sources )


  sim.print_sources()
  sim.print_progress()
  sim.print_curr_state()
  sim.print_choices()
  print ("\nchoose [1 1]")
  sim.cycle([1,1,1])  

  sim.print_progress()
  sim.print_curr_state()
  sim.print_choices()
  print ("\nchoose [1 0]")
  sim.cycle([1,0,1])  

  sim.print_progress()
  sim.print_curr_state()
  sim.print_choices()
  
  # print ("\nchoose [1 1]")
  # sim.cycle([1,1])  

  # sim.print_progress()
  # sim.print_curr_state()
  # sim.print_choices()
  
  # print ("\nchoose [1 1]")
  # sim.cycle([1,1])  

  # sim.print_progress()
  # sim.print_curr_state()
  # sim.print_choices()
  





