"""
  Internal script for drawing pairs of users for Secret Santa game
  Developed by Fatima Velic, February 2022.
  Updated by Fatima Velic, November 2022.
"""
def generate_match(people):
    """ 
      Function designed in such way that one person and the next person 
      from a randomly shuffled list are chosen and paired while list counter is 
      incremented for 2. First person is appended to a new list named givers and second 
      person is appended to another list named receivers. In case where there is odd number
      of participants, on givers list a null flag is appended while person is stored on 
      receivers list and removed from the main list of participants. Alogrithm ensures:
      
      - No person can be assigned to itself (there’s no x-x pair)
      - Once matched, the pair won’t appear more than once on the list. 
      - Person can be sorted into only one pair. (if x is matched to y as a giver, x has 
        to be matched to z as a receiver but cannot be matched to y as receiver nor
        it can be matched to z as a giver)
    """
    givers = []
    receivers = []
    for i in range(len(people)):
        givers.append(people[i])
        receivers.append(people[(i+1)%(len(people))])
    return givers, receivers