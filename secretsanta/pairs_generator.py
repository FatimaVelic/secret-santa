
import random

def is_even(x_lst):
  if len(x_lst) %2 == 0:
      return True
  else:
      return False

def generate_match(participants_names):
    givers = []
    receivers = []
    flag = None
    random.shuffle(participants_names)
    i = 0
    while i < len(participants_names):
      if (is_even(participants_names)):
          print(f'{participants_names[i]} exchanges gifts with {participants_names[i + 1]}. ')
          givers.append(participants_names[i])
          receivers.append(participants_names[i+1])
          i += 2 
      else:
          print(f'{participants_names[i]} has no one to buy a gift to this year. :(')
          givers.append(flag)
          receivers.append(participants_names[i])
          participants_names.pop(i)
    return givers, receivers