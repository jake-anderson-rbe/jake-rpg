import variables
class Player:
    def __init__(self):
      """inventory for found items"""
      self.inventory = []

    def print_inventory(self):
      """prints items and item info with inventory prompt"""
      if self.inventory:
          for item in self.inventory:
            print(item.name)
            print(item.desc)
            print(item.code)
      else:
          print("no items")