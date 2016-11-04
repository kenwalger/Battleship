class Ship:
    def __init__(self, type_of_ship, size_of_ship):
        self.type_of_ship = type_of_ship
        self.positions = []
        self.orientation = None
        self.size = size_of_ship
        self.health = size_of_ship
