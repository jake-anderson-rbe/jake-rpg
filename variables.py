class Items:
    """defines info for items"""
    def __init__(self, name, desc):
      self.name = name
      self.desc = desc

class Code(Items):
    """defines info for paper item"""
    def __init__(self, name, desc, code):
      self.name = name
      self.desc = desc
      self.code = code
  
class Rooms:
    """defines info for tiles and map"""
    tile = ["Entrance", "Classroom", "Cafeteria", "DeadEnd", "SchoolExit"]
    tiles = {
    tile[0] : {"description" : "you are at the entrance"},
    tile[1] : {"description" : "you are in a classroom"},
    tile[2] : {"description" : "you are in the cafeteria"},
    tile[3] : {"description" : "there is nothing here"},
    tile[4] : {"description" : "you found the exit! congrats!"}  
}

    school_map = [
    [tile[3], tile[2], tile[1], tile[3]],
    [tile[1], tile[1], tile[1], tile[1]],
    [tile[3], tile[0], tile[3], tile[4]],
    [tile[4], tile[1], tile[1], tile[1]]
     ]
  
    row = 2 
      
    col = 1