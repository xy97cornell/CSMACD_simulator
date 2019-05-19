# CSMA/CD Simulator CS 4450 Project
# Xiaoyu Yan (xy97)
# This is CSMA/CD simulator:
# This module simulates how the CSMA/CD would act in response to 
# multiple mediums contesting a broadcast slot.
from __future__ import print_function
import itertools
class CSMA_CD_sim():
  """
  Simulator that handles the incoming Mediums using CSMA/CD 
  """
  
  def __init__ (self,sources):
    assert isinstance(sources,list)
    self._sources = sources 
    self._slots = []
    self._slot_number = 0
    self._time = 0
    self._choices = []

  def print_sources(self):
    print ("\nCurrent sources: ")
    for i in self._sources:
      print (" %s " %(i.info()), end='')
    print('')

  def print_progress(self):
    print ("\nProgress so far:")
    print("S# | ", end='')
    for i in range(len(self._sources)):
      print( "" + self._sources[i].info() + "  | ", end="")
    print("")
    for i in self._slots:
      for j in i:
        print(""+ j + "|", end="")
      print("")  

  def print_curr_state(self):
    print ("\nCurrent State:")
    print ("Src|Curr F|Col.|Poss. Slots")
    print ("---+------+----+-----------")
    #print out current sources
    for i in range(len(self._sources)):
      print( " "+self._sources[i].info() + " | ", end='')
      if not self._sources[i].done():
        if (self._sources[i].currFrame()<10):
          print( " "+self._sources[i].info()+\
            str(self._sources[i].currFrame()) + "  | ", end = '')
        else:
          print( " "+self._sources[i].info()+\
            str(self._sources[i].currFrame()) + " | ", end = '')
      else:
        print(" --- |",end='')
      if not self._sources[i].done():  
        if self._sources[i].collisions()<10:
          print( ""+ str(self._sources[i].collisions())\
            + "  | ", end = '')
        else:
          print( ""+ str(self._sources[i].collisions())\
            + " | ", end = '')
      else:
        print("--- | ",end='')
      print( str(self._sources[i].possibleSlots()))
  
  def print_choices(self):
    print ("\nPossibilities for slot %s" %(self._slot_number))
    for i in self._sources:
      if self._slot_number in i.possibleSlots():
        print(" %s%s "%(i.info(),i.currFrame()),end='')
    print ("")

  def cycle(self, choices):
    """
    choices: array of choices corresponding to each src
    """
    assert isinstance(choices,list)
    sl = []
    slot_num = self._slot_number
    if slot_num<10:
      sl.append(" "+str(self._slot_number)+" ")
    elif slot_num<100:
      sl.append(""+str(self._slot_number)+" ")
    else:
      sl.append(""+str(self._slot_number)+"")
    self._slot_number += 1
    if choices.count(1)>1:
      for i in range(len(self._sources)):
        spa = "  " if self._sources[i].currFrame()<10 else ""
        if choices[i]:
          sl.append(""+self._sources[i].info()+\
            str(self._sources[i].currFrame())+spa)
          self._sources[i].collision(self._slot_number)
        else:
          self._sources[i].cycle()
          sl.append("    ")
    else:
      for i in range(len(self._sources)):
        spa = "  " if self._sources[i].currFrame()<10 else ""
        if choices[i]:
          sl.append(self._sources[i].info()+\
            str(self._sources[i].currFrame())+spa)
          self._sources[i].success(self._slot_number)  
        else:
          self._sources[i].cycle()
          sl.append("    ")
    self._slots.append(sl)

  def decode(self,idx):
    assert isinstance(idx,int)
    if idx < len(self._choices):
      output = []
      lst = self._choices[idx]
      if len(lst) == 0:
        for i in range(len(self._sources)):
          output.append( 0 )
      else:
        for i in range(len(self._sources)):
          src = self._sources[i]
          idx = (src.info()+str(src.currFrame())) in lst
          if idx:
            output.append(1)
          else:
            output.append(0)     

      print (output)
      return output
    return -1

  def calc_posi(self):
    must_choose = []
    poss = []
    choi = []
    choices = []
    for i in range(len(self._sources)):
      src = self._sources[i]
      if (len(src.possibleSlots()) == 1 and not\
        src.done()):
        must_choose.append(src.info()+str(src.currFrame()))
      elif (not src.done()):
        poss.append(src.info() + str(src.currFrame()))
    for i in range(len(poss)+1):
      choi.append(list(itertools.combinations(poss,i)))    
    for i in choi:
      for j in i:
        choices.append(list(j))
    for i in choices:
      i.extend(must_choose)
    for i in range(len(choices)):
      print ("%d. %s"%(i, str(choices[i])))
    self._choices = choices

 
    
class Source():
  """
  Broadcase medium from a transmission. Shared with other sources and resolved using
  CSMA/CD
  """

  def currFrame(self):
    return self._curr_frame
  def collisions(self):
    return self._collisions
  def info(self):
    return self._name
  def possibleSlots(self):
    return self._possible_slots
  def setFrames(self,frames):
    assert type(frames)==int
    self._num_frames = frames
  def frames(self):
    return self._num_frames
  def done(self):
    return self._done

  def __init__ (self,name,num_frames):
    assert isinstance(name,str)
    assert isinstance(num_frames,int)
    self._name = name
    self._num_frames = num_frames
    self._collisions = 0
    self._curr_frame = 0
    self._possible_slots = [0] #slot numbers that are possible
    self._done = False

  def collision(self, slot_number):
    assert isinstance(slot_number,int)
    self._collisions += 1
    cur_slot = self._possible_slots
    self._possible_slots = [i for i in \
      range(slot_number,slot_number+2**self._collisions)]

  def success(self, slot_number):
    assert isinstance(slot_number,int)
    self._collisions = 0
    self._curr_frame += 1
    if(self._curr_frame == self._num_frames):
      self._done = True
      self._possible_slots = []
    else:
      self._possible_slots = [slot_number]

    return self._num_frames

  def cycle(self):
    if(self._curr_frame!=self._num_frames):
      self._possible_slots.pop(0)
