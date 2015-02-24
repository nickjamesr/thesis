#!/usr/bin/python
#--------------------------------------------------------------------------#
# BINTREE.PY                                                               #
# Binary tree class to describe time intervals for PT data                 #
#                                                                          #
#--------------------------------------------------------------------------#

class node:
  '''Node class for binary tree. Each node describes a range of values'''
  def __init__(self,lo,hi,parent=None):
    self.lo=lo
    self.hi=hi
    self.parent=parent
    self.left=None
    self.right=None

  def split(self):
    '''Split the node. This spawns two new nodes, each containing half the
range of the original node
return : None'''
    self.left=node(self.lo,(self.hi+self.lo)/2.,self)
    self.right=node((self.hi+self.lo)/2.,self.hi,self)

  def visit(self):
    '''Find leaves of a node
return : list of leaf nodes rooted at self'''
    rtn = []
    if self.left is None:
      rtn.append(self)
    else:
      rtn+=self.left.visit()
      rtn+=self.right.visit()
    return rtn

class bintree:
  '''Binary tree class for describing an interval split into multiple sub-
intervals.'''
  def __init__(self,lo,hi):
    '''Constructor
lo     : minimum of range
hi     : maximum of range
return : self'''
    self.root=node(lo,hi)

  def leaves(self):
    '''Find leaf nodes
return : list of leaf nodes (i.e. nodes with no children).'''
    return self.root.visit()

  def points(self):
    '''Find the points dividing the sub-intervals
return : list of instants'''
    l=self.leaves()
    rtn=[l[0].lo]
    for leaf in l:
      rtn.append(leaf.hi)
    return rtn
