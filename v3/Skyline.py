from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM
from Board import SkylineBoard
from Game import SkylineGame
from UI import SkylineUI

MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 6  # Width and height of the whole board

game = SkylineGame(4)
game.start()

root = Tk()
SkylineUI(root, game)
root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
root.mainloop()
