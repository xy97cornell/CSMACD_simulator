# sim.py CS 4450 Project
# Xiaoyu Yan (xy97)
# Maintains the GUI like simulator for the CSMA/CD
# How to use:
# Instructions:
#   ADD A# - Adds station with A and ### frames
#   CHA A# - If station A exists, changes number of frames
#   to #
#   CYC #  - Progress one cycle with your choice of possible outputs
#   for the current slot
#   RESTART- Restarts the simulator and you can add new stations
#   DONE   - Done adding new stations, starts sim
#   QUIT   - Quit the simulation

from __future__ import print_function
from CSMACD import *

#States
QUIT  = 0
START = 1
SIM   = 2

cur_state = START
sources = []
IDS = []

if __name__ == "__main__":
  while(cur_state != QUIT):
    print ("___CSMA/CD sim___")
    # inpu = raw_input("START - start\nQUIT - quit\n")
    # if inpu == 'QUIT':
    #   cur_state = QUIT
    # elif (inpu == 'START'):
    if (cur_state == START):
      print ("Current stations: ",end='')        
      for i in sources:
        print("%s%d "%(i.info(),i.frames()),end='')
      print('')
      inpu = raw_input("\nInitialize stations:\
        \nHow the instructions work:\
          \nADD A4 inputs station name 'A' with 4 frames\nCHA A5 changes station A's number of frames to 5\
        \nADD - add station\nCHA - change station\
  \nDONE - done\nQUIT - quit\n-->")
      if(inpu == 'QUIT'):
        cur_state = QUIT
      elif (inpu == 'DONE'):
        sim = CSMA_CD_sim( sources )
        cur_state = SIM
      elif (inpu[0:3] == 'ADD'):
        print ("adding...")
        inp = int(inpu[5:])
        if (inp == 0):
          print ("ERROR: Adding station with 0 frames")
        elif inpu[4] in IDS:
          print("ERROR: ID already exists")
        else:
          sources.append(Source(inpu[4],inp))
          IDS.append(inpu[4])
        
      elif (inpu[0:3] == 'CHA'):
        print ("changing...")
        for i in sources:
          if(i.info()==inpu[4]):
            i.setFrames(int(inpu[5:]))
      
    if (cur_state == SIM):
      sim.print_sources()
      sim.print_progress()
      sim.print_curr_state()
      sim.print_choices()
      sim.calc_posi()
      inpu = raw_input("\nChoose a possibility for cuurent slot\
        \nCYC i - Cycle one slot at index i\nRESTART - restart\nQUIT - quit\n-->")
      if inpu == "QUIT":
        cur_state = QUIT
      elif inpu == "RESTART":
        cur_state = START
        sources = []
        IDS = []
      elif inpu[0:3] == "CYC":
        idx = int(inpu[4:])
        ans = sim.decode(idx)
        if (ans != -1):
          sim.cycle(ans)
        else:
          print("ERROR: Illegal index")  
    print("----------------------------")
    # else:
    #   print("Wrong Command - try again")