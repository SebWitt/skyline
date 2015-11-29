from random import randint, shuffle
import random

__author__ = ''





class SkylineBoard(object):

    def __init__(self, size=4, number_of_hints = 11):
        self.board = []
        self.size = size
        self.number_of_hints = number_of_hints
        self.hints_top = []
        self.hints_bottom = []
        self.hints_left = []
        self.hints_right = []
        self.empty_board = [[0, 0, 0, 0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
        
        self.__create_board(size)
        self.__create_hints()
        self.board = [[0, 0, 0, 0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

    def __create_board(self, size):
        row = [x for x in range(0, size)]
        column = [x for x in range(0, size)]
        shuffle(row)
        shuffle(column)

        for i in range(0, size):
            self.board.append([])
            for j in range(0, size):
                self.board[i].append(((row[i] + column[j]) % size) + 1)


    def __create_hints(self):
        hint_per_section, hint_remainder = divmod(self.number_of_hints,  self.size)

        self.hints_top = self.__create_hints_for_section("top", hint_per_section)
        self.hints_bottom = self.__create_hints_for_section("bottom", hint_per_section)
        self.hints_left = self.__create_hints_for_section("left", hint_per_section)
        self.hints_right = self.__create_hints_for_section("right", hint_remainder)


    def __create_hints_for_section(self, section, number):

        hints = [0, 0, 0, 0]

        for i in range(0, number):
            random_position = randint(0,3)
            hints[random_position] = self.sum_of_viewable_houses(section, random_position)
        return hints


    def sum_of_viewable_houses(self, section, position):

        viewable_houses = 0
        highest_house_seen = 0

        print (self.board)
        if section == "top":
            for current_row in range(0, self.size):
                if self.board[current_row][position] > highest_house_seen:
                    viewable_houses += 1
                    highest_house_seen = self.board[current_row][position]
            return viewable_houses
                
        if section == "bottom":
            for current_row in range((self.size-1), -1, -1):
                if self.board[current_row][position] > highest_house_seen:
                    viewable_houses += 1
                    highest_house_seen = self.board[current_row][position]
            return viewable_houses

        if section == "left":
            for current_col in range(0, self.size):
                if self.board[position][current_col] > highest_house_seen:
                    viewable_houses += 1
                    highest_house_seen = self.board[position][current_col]
            return viewable_houses

        if section == "right":
            for current_col in range((self.size-1), -1, -1):
                if self.board[position][current_col] > highest_house_seen:
                    viewable_houses += 1
                    highest_house_seen = self.board[position][current_col]
            return viewable_houses


