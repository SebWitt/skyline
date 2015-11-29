__author__ = ''
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 6  # Width and height of the whole board

class SkylineUI(Frame):
    """
    GUI for the skyline game
    """
    def __init__(self, parent, game):
        self.game = game
        self.parent = parent
        Frame.__init__(self, parent)

        self.row, self.col = 0, 0

        self.__initUI()

    def __initUI(self):
        self.parent.title("Skyline")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self,
                             width=WIDTH,
                             height=HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)
        clear_button = Button(self,
                              text="Reset",
                              command=self.__clear_answers)
        clear_button.pack(fill=BOTH, side=BOTTOM)

        self.__draw_grid()
        self.__draw_game()

        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)


    def __draw_grid(self):
        """
        Draws grid divided with blue lines into 3x3 squares
        """
        for i in range(self.game.size + 3):
            color = "blue" if i % 6 == 0 else "gray"
            if i == 1 or i == self.game.size + 1:
                color = "red"

            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)


    def __draw_game(self):
        
        self.canvas.delete("numbers")
        for i in range(0, self.game.size):
            for j in range(0, self.game.size):
                answer = self.game.board[i][j]
                #if answer != 0:
                x = MARGIN + (j+1) * SIDE + SIDE / 2
                y = MARGIN + (i+1) * SIDE + SIDE / 2
                original = self.game.board_object.empty_board[i][j]
                color = "black" if answer == 0 else "sea green"
                self.canvas.create_text(
                    x, y, text=answer, tags="numbers", fill=color
                )
        self.__draw_hints()


    def __clear_answers(self):
        self.game.start()
        self.canvas.delete("victory")
        self.__draw_game()


    def __draw_cursor(self):
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            x0 = MARGIN + self.col * SIDE + 1
            y0 = MARGIN + self.row * SIDE + 1
            x1 = MARGIN + (self.col + 1) * SIDE - 1
            y1 = MARGIN + (self.row + 1) * SIDE - 1
            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                outline="red", tags="cursor"
            )


    def __cell_clicked(self, event):
        if self.game.hasWon:
            return
        x, y = event.x, event.y
        if (MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN):
            self.canvas.focus_set()

            # get row and col numbers from x,y coordinates
            row, col = (y - MARGIN) / SIDE, (x - MARGIN) / SIDE

            # if cell was selected already - deselect it
            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1
            else:
                self.row, self.col = int(row), int(col)
        else:
            self.row, self.col = -1, -1

        self.__draw_cursor()


    def __key_pressed(self, event):
        if self.game.hasWon:
            return
        if self.row >= 0 and self.col >= 0 and event.char in "1234":
            self.game.board[self.row-1][self.col-1] = int(event.char)
            self.col, self.row = -1, -1
            self.__draw_game()
            self.__draw_cursor()
            if self.game.check_game():
                self.__draw_victory()


    def __draw_victory(self):
        # create text
        x = y = MARGIN + 3 * SIDE + SIDE / 2
        self.canvas.create_text(
            x, y,
            text="You win!", tags="victory",
            fill="orange", font=("Arial", 32)
        )


    def __draw_hints(self):

        #draw top hints:
        for i in range(0, self.game.size):
            color = "red"
            hint = self.game.hints_top[i]
            if hint == 0:
                color="white"
            x = SIDE + MARGIN + i * SIDE + SIDE / 2
            y = MARGIN + 0 * SIDE + SIDE / 2

            self.canvas.create_text(
                x, y, text=hint, tags="numbers", fill=color
            )

        #draw bottom hints:
        for i in range(0, self.game.size):
            color = "red"
            hint = self.game.hints_bottom[i]
            if hint == 0:
                color="white"
            x = SIDE + MARGIN + i * SIDE + SIDE / 2
            y = MARGIN + (self.game.size+1) * SIDE + SIDE / 2

            self.canvas.create_text(
                x, y, text=hint, tags="numbers", fill=color
            )     

        #draw left hints:
        for i in range(0, self.game.size):
            color = "red"
            hint = self.game.hints_left[i]
            if hint == 0:
                color="white"
            x =  MARGIN + 0 * SIDE + SIDE / 2
            y = MARGIN + (i+1) * SIDE + SIDE / 2

            self.canvas.create_text(
                x, y, text=hint, tags="numbers", fill=color
            )

        #draw right hints:
        for i in range(0, self.game.size):
            color = "red"
            hint = self.game.hints_right[i]
            if hint == 0:
                color="white"
            x =  MARGIN + (self.game.size+1) * SIDE + SIDE / 2
            y = MARGIN + (i+1) * SIDE + SIDE / 2

            self.canvas.create_text(
                x, y, text=hint, tags="numbers", fill=color
            )