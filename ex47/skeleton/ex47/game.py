class Room(object):
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        
    def go(self, direction):
        return self.path.get(direction, None)
        
    def add_path(self, paths):
        self.path.update(paths)
        