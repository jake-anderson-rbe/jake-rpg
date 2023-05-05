movements = ["north", "south", "east", "west"]
import sys
from variables import Rooms
#----Movement Function----------------------------------------------------------------------
def movement():
  """changes the player's current location when inputs are entered"""
  global row, col
  while True:
    for movement in movements:
      print(movement)
    movement_input = input("which direction? ")
    if movement_input.lower() == "north" and Rooms.row != 0 :
      Rooms.row -= 1
      break
    elif movement_input.lower() == "west" and Rooms.col != 0 :
      Rooms.col -= 1
      break
    elif movement_input.lower() == "south" and Rooms.row != 3 :
      Rooms.row += 1
      break
    elif movement_input.lower() == "east" and Rooms.col != 3 :
      Rooms.col += 1
      break
    else:
      print("that's not valid!")

def final_door():
  """defines the code for the exit tile"""
  print("you need a 4 digit code to unlock this door...")
  code_input = input("enter in the code: ")
  if code_input == "2004":
    print("you successfully open the door!")
    print("you win!")
    sys.exit()
  else:
    print("thats the wrong code!")
    final_door()
  