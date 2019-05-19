from __future__ import print_function
from CSMACD import *


QUIT  = 0
START = 1
SIM   = 2

cur_state = START
sources = []

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
          \nADD A4 inputs station name 'A' with 5 frames\nCHA A5 changes station A's number of frames\
        \nADD - add station\nCHA - change station\
        \nDONE - done\nQUIT - quit\n")
      if(inpu == 'QUIT'):
        cur_state = QUIT
      elif (inpu == 'DONE'):
        sim = CSMA_CD_sim( sources )
        cur_state = SIM
      elif (inpu[0:3] == 'ADD'):
        print ("adding...\n")
        inp = int(inpu[5:])
        if (inp == 0):
          print ("Adding station with 0 frames")
        else:
          sources.append(Source(inpu[4],inp))
        
      elif (inpu[0:3] == 'CHA'):
        print ("changing...")
        for i in sources:
          if(i.info()==inpu[4]):
            i.setFrames(int(inpu[6:]))
      
    if (cur_state == SIM):
      sim.print_sources()
      sim.print_progress()
      sim.print_curr_state()
      sim.print_choices()
      sim.calc_posi()
      inpu = raw_input("\nChoose:\n")
      if inpu == "QUIT":
        cur_state = QUIT
      elif inpu == "RESTART":
        cur_state = START
        sources = []
      elif inpu[0:5] == "CYCLE":
        idx = int(inpu[5:])
        ans = sim.decode(idx)
        if (ans != -1):
          sim.cycle(ans)  
    print("----------------------------")
    # else:
    #   print("Wrong Command - try again")