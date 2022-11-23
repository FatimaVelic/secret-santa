
import io
from reportlab.pdfgen import canvas
from reportlab.lib import colors
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

def exportSanataslist(givers, receivers):
  buffer = io.BytesIO()
  c = canvas.Canvas(buffer)

  headerYpoint = 790
  startXpoint = 40
  rowSpace = 25
  extraSpace = 7
  subheaderYpoint = headerYpoint-2*rowSpace
  c.setStrokeColor(colors.black)
  c.setFont('Times-Roman', 20)
  c.drawString(250, headerYpoint, "Santa's list")
  c.setFont('Times-Roman', 14)
  c.setFillColor("#006000")
  c.rect(startXpoint, subheaderYpoint-extraSpace, 510, rowSpace, fill=True, stroke=False)
  c.setFont('Times-Roman', 16)
  c.setFillColor(colors.white)
  c.setStrokeColor(colors.white)
  c.drawString(startXpoint+5,subheaderYpoint, "Matched")
  giver = 40
  receiver = 200
  rowPoint = subheaderYpoint-rowSpace-extraSpace
  c.setFillColor(colors.black)
  c.setStrokeColor(colors.black)
  c.setFont('Times-Roman', 14)
  i = 0
  while i < len(givers): 
      c.drawString(giver, rowPoint, givers[i])
      c.drawString(receiver, rowPoint, receivers[i])
      rowPoint-=rowSpace
      i+=1

  subheaderYpoint = rowPoint-rowSpace+extraSpace
  c.setFillColor("#006000")
  c.rect(startXpoint, subheaderYpoint-extraSpace, 510, rowSpace, fill=True, stroke=False)
  c.setFont('Times-Roman', 16)
  c.setFillColor(colors.white)
  c.setStrokeColor(colors.white)
  c.drawString(startXpoint+5, subheaderYpoint, "Unmached")
  c.setFillColor(colors.black)
  c.setStrokeColor(colors.black)
  c.setFont('Times-Roman', 14)
  rowPoint = subheaderYpoint-rowSpace-extraSpace
  i = 0
  while i < len(givers):
    if (givers[i] == None):
      c.drawString(giver, rowPoint, receivers[i]) 
      rowPoint=-rowSpace
    else: 
      c.drawString(receiver+2*rowSpace, rowPoint, "Congratulations!")
      c.drawString(receiver, rowPoint-rowSpace+extraSpace, "Everyone has a match this season.")
      rowPoint=-rowSpace+extraSpace
    i+=1

  c.showPage()
  c.save()
  buffer.seek(0)
  return buffer
