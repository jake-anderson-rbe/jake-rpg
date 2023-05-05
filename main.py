###############################################################################
# Title: Campbell RPG      
# Class: CS 30
# Date: March 22, 2023
# Coders Name: Jake Anderson
# Version: 0.0.4   
###############################################################################
'''
Current Assignment: Create a text-based RPG
An RPG set within Campbell
'''
#------------------------------------------------------------------------------
#----Imports and Global Variables----------------------------------------------
import sys
import random
import functions
from variables import Rooms
from variables import Items
from variables import Code
from player import Player

# following creates items/objects
pencil = Items('Pencil', 'a pencil to write with')
textbook = Items('Textbook', 'a textbook of knowledge')
calculator = Items('Calculator', 'a calculator for math')
binder = Items('Binder', 'a binder to put things in')
paper = Code('Paper', 'a paper with a code on it', "2004")

user = Player()

#----Tile Code----------------------------------------------------------------------
# code that defines current location and tile descriptions
while True:
  current_location = Rooms.school_map[Rooms.row][Rooms.col]
  """tracks the player's current location"""
  if current_location == Rooms.tile[1]:
    print("you are in a classroom")
    print("you can search this room!")
  elif current_location == Rooms.tile[0]:
    print("you are at the entrance of campbell")
  elif current_location == Rooms.tile[3]:
    print("there is nothing here")
  elif current_location == Rooms.tile[2]:
    print("you are in the cafeteria, and eat some food")
  elif current_location == Rooms.tile[4]:
    functions.final_door()
  else:
    print("you can't do that!")

#----Action Code----------------------------------------------------------------------
# code that defines action inputs
  try:
    action_input = input("what do you do? enter guide for inputs: ")
    if action_input.lower() == "walk":
      print("you can go:")
      functions.movement()
    elif action_input.lower() == "inventory":
      print("you currently have:")
      user.print_inventory()
    elif action_input.lower() == "search":
      if current_location == Rooms.tile[1]:
        item_chance = random.randint(0,7)
        if item_chance == 0:
          print("you found a pencil!")
          user.inventory.append(pencil)
        elif item_chance == 1:
          print("you found a textbook!")
          user.inventory.append(textbook)
        elif item_chance == 2:
          print("you found a calculator!")
          user.inventory.append(calculator)
        elif item_chance == 3:
          print("you found a binder!")
          user.inventory.append(binder)
        elif item_chance == 7:
          print("you found a piece of paper!")
          user.inventory.append(paper)
        else:
          print("you don't find anything!")
    elif current_location != Rooms.tile[1]:
      print("you can't do that!")
    elif action_input.lower() == "map":
      filename = "location.txt"
      map_text = f"you are currently in {current_location}"
      print(f"{map_text}")
      with open(filename, 'w') as file_object:
        file_object.write(map_text)
    elif action_input.lower() == "guide":
      print("you can: walk, search (if in classroom), inventory and quit")
    elif action_input.lower() == "quit":
      print("goodbye!")
      sys.exit()
  except ValueError:
    print("you can't do that!")
  finally:
    continue