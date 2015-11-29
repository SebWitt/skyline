from copy import deepcopy, copy
from Board import SkylineBoard

__author__ = ""

class SkylineGame(object):
    """
    Stores the board and it's values and checks if a game is completed
    """

    def __init__(self, size):
        self.board_object = SkylineBoard(size)
        self.empty_board = self.board_object.board
        self.size = size
        self.hints_top = self.board_object.hints_top
        self.hints_bottom = self.board_object.hints_bottom
        self.hints_left = self.board_object.hints_left
        self.hints_right = self.board_object.hints_right
    

    def start(self):
        self.hasWon = False
        self.board = self.board_object.board 

    	# was muss überprüft werde: 
    	# Wird der obere, untere, linke, rechte Hinweis eingehalten?
    	# Kommt die Zahl in der Zeile nur einmal vor?
    	# Kommt die Zahl in der Spalte nur einmal vor?
    	# //TODO: ordentlich implementieren
    def check_game(self):
        if self.check_rows() and self.check_cols() and self.check_hints():
            return True
        return False


    def check_rows(self):
        #iterate over rows
        for i in range(0,4):
            is_one_checked = False
            is_two_checked = False
            is_three_checked = False
            is_four_checked = False

            for j in range(0,4):
                if self.board[i][j] == 1:
                    is_one_checked = True
                elif self.board[i][j] == 2:
                    is_two_checked = True
                elif self.board[i][j] == 3:
                    is_three_checked = True
                elif self.board[i][j] == 4:
                    is_four_checked = True

            #check if every number is in row
            if not(is_one_checked and is_two_checked and is_three_checked and is_four_checked):
                return False

        return True

    def check_cols(self):
        #iterate over cols
        for i in range(0,4):
            is_one_checked = False
            is_two_checked = False
            is_three_checked = False
            is_four_checked = False

            for j in range(0,4):
                if self.board[j][i] == 1:
                    is_one_checked = True
                elif self.board[j][i] == 2:
                    is_two_checked = True
                elif self.board[j][i] == 3:
                    is_three_checked = True
                elif self.board[j][i] == 4:
                    is_four_checked = True

            #check if every number is in col
            if not(is_one_checked and is_two_checked and is_three_checked and is_four_checked):
                return False

        return True


    def check_hints(self):

        #check top hints
        for i in range(0,4):
            if(self.hints_top[i] != 0):
                if self.board_object.sum_of_viewable_houses("top", i) != self.hints_top[i]:
                    return False

        #check bottom hints
        for i in range(0,4):
            if(self.hints_bottom[i] != 0):
                if self.board_object.sum_of_viewable_houses("bottom", i) != self.hints_bottom[i]:
                    return False

        #check left hints
        for i in range(0,4):
            if(self.hints_left[i] != 0):
                if self.board_object.sum_of_viewable_houses("left", i) != self.hints_left[i]:
                    return False

        #check right hints
        for i in range(0,4):
            if(self.hints_right[i] != 0):
                if self.board_object.sum_of_viewable_houses("right", i) != self.hints_right[i]:
                    return False

        return True