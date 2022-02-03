"""
  Internal script for drawing pairs of users for Secret Santa game
  Developed by Fatima Velic, February 2022.

"""

import random

def is_even(x_lst):
  """ 
  Check if list lenght is even or odd.

  """
  if len(x_lst) %2 == 0:
      return True
  else:
      return False

def generate_match(participants_names):
    """ 
      Function designed in such way that one person and the next person 
      from a randomly shuffled list are chosen and paired while list counter is 
      incremented for 2. First person is appended to a new list named givers and second 
      person is appended to another list named receivers. In case where there is odd number
      of participants, on givers list a null flag is appended while person is stored on 
      receivers list and removed from the main list of participants. Alogrithm ensures:
      
      - No person can be assigned to itself (there’s no x-x pair)
      - Once matched, the pair won’t appear more than once on the list. 
      - Person can be sorted into only one pair. (if x is matched to y, 
        x cannot be matched to z)
    """
    givers = []
    receivers = []
    flag = None
    random.shuffle(participants_names)
    i = 0
    while i < len(participants_names):
      if (is_even(participants_names)):
          givers.append(participants_names[i])
          receivers.append(participants_names[i+1])
          i += 2 
      else:
          givers.append(flag)
          receivers.append(participants_names[i])
          participants_names.pop(i)
    return givers, receivers