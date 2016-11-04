import config

from ship import Ship
from board import Board


class Player:
    def init_ship(self):
        self.ships = []
        for ship in config.SHIP_INFO:
            self.ships.append(Ship(ship[0], ship[1]))

    def __init__(self):
        player_name = input("Enter name: ")
        self.player_name = player_name
        self.board = Board()
        self.gameboard = Board()
        self.init_ship()
        self.opponent = None
        self.shots = []
        self.sunk = 0
