# CSMA/CD Simulator CS 4450 Project
# Xiaoyu Yan (xy97)
# This is CSMA/CD simulator:
# This module simulates how the CSMA/CD would act in response to 
# multiple mediums contesting a broadcast slot.


class CSMA_CD_sim():
  """
    Simulator that handles the incoming mMdiums using CSMA/CD 
    _ _ _ _ <--slots
    A _ _ _ <--one slot filled
  """

  def __init__ (self,sources):
    assert isinstance(sources,list)
    self.sources = sources 
    self.slots = []

  def print_sources(self):
    for i in self.sources:
      print (i.info() + ", ")


class Source():

  """
  Broadcase medium from a transmission. Shared with other sources and resolved using
  CSMA/CD
  """

  def dec_frames(self,frames):
    self.frames -= 1

  def __init__ (self,name,frames):
    assert isinstance(name,str)
    assert isinstance(frames,int)
    self.name = name
    self.frames = frames
    self.collisions = 0

  def info(self):
    return self.name
  



