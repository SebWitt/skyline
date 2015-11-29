from random import shuffle

gameboard = []
field_map = {(1, 1):"x1", (1, 2):"x2", (1, 3):"x3", (1, 4):"x4", (2, 1):"x5", (2, 2):"x6", (2, 3):"x7", (2, 4):"x8", (3, 1):"x9", (3, 2):"x0", (3, 3):"y1", (3, 4):"y2", (4, 1):"y3", (4, 2):"y4", (4, 3):"y5", (4, 4):"y6"}
#hint_map = {1:"l1", 2:"l2", 3:"l3", 4:}
hidden_field = "   t1 t2 t3 t4\n  *************\nl1*x1|x2|x3|x4*r1\nl2*x5|x6|x7|x8*r2\nl3*x9|x0|y1|y2*r3\nl4*y3|y4|y5|y6*r4\n  *************\n   b1 b2 b3 b4"
user_input = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def create_gameboard(size = 4):
    global gameboard
    row = [x for x in range(0, size)]
    column = [x for x in range(0, size)]
    shuffle(row)
    shuffle(column)  

    for i in range(0, size):
        gameboard.append([])
        for j in range(0, size):
            gameboard[i].append(((row[i] + column[j]) % size) + 1)
    
    gameboard.insert(0, [])
    gameboard.append([])
    #print_field(size)
    get_view(size)

def get_view(size):
    for i in range(1, size + 1):
        max_value = 0
        sky_counter = 0
        for j in range(0, size):
            if gameboard[i][j] > max_value:
                max_value = gameboard[i][j]
                sky_counter += 1
        gameboard[i].insert(0, sky_counter)

    for k in range(1, size + 1):
        max_value = 0
        sky_counter = 0
        for j in range(1, size + 1):
            m = size + 1 - j
            if gameboard[k][m] >= max_value:
                max_value = gameboard[k][m]
                sky_counter += 1
        gameboard[k].append(sky_counter)

    for j in range(1, size + 1):
        max_value = 0
        sky_counter = 0
        for i in range(1, size + 1):
            if gameboard[i][j] > max_value:
                max_value = gameboard[i][j]
                sky_counter += 1
        gameboard[0].append(sky_counter)
    gameboard[0].insert(0, 0)
    gameboard[0].append(0)

    for j in range(1, size + 1):
        max_value = 0
        sky_counter = 0
        for i in range(1, size + 1):
            m = size + 1 - i
            if gameboard[m][j] > max_value:
                max_value = gameboard[m][j]
                sky_counter += 1
        gameboard[size + 1].append(sky_counter)
    gameboard[size + 1].insert(0, 0)
    gameboard[size + 1].append(0)
    print_field(size)

def print_field(size):
    for i in range(0, size + 2):
        print(gameboard[i])

def input_():
    global hidden_field
    global user_input
    nr_range = [1, 2, 3, 4]
    while True:
        try:
            print("Gib für Zeile, Spalte und Wert eine Zahl von 1 bis 4 ein")
            a = int(input("Zeile: "))
            b = int(input("Spalte: "))
            c = int(input("Wert: "))
        except ValueError:
            print("Bitte gib eine Zahl von 1 bis 4 ein")
            continue
        if a in nr_range and b in nr_range and c in nr_range:
            break
        else:
            print("Fehler: Gib jeweils eine Zahl von 1 bis 4 ein!")
            continue
    user_input[a - 1][b - 1] = c
    hidden_field = hidden_field.replace(field_map[(a, b)], (' ' + str(c)))
    print_gamefield()
    print(user_input)

def check_win():
    global gameboard
    global user_input
    tmp_field = []
    for i in range(1, 5):
        tmp_field.append([])
        for j in range(1,5):
            tmp_field[i - 1].append(gameboard[i][j])
    print(tmp_field)
    if tmp_field == user_input:
        print("Win")
        return True
    else:
        return False

def create_hints():
    pass
    
def print_gamefield():
    global gameboard
    screen_field = hidden_field
    screen_field = screen_field.replace('t1', (' ' + str(gameboard[0][1])))
    screen_field = screen_field.replace('t2', ' ')
    screen_field = screen_field.replace('t3', (' ' + str(gameboard[0][3])))
    screen_field = screen_field.replace('t4', ' ')
    screen_field = screen_field.replace('b1', ' ')
    screen_field = screen_field.replace('b2', ('  ' + str(gameboard[5][2])))
    screen_field = screen_field.replace('b3', ' ')
    screen_field = screen_field.replace('b4', ('  ' + str(gameboard[5][4])))
    screen_field = screen_field.replace('r1', ('' + str(gameboard[1][5])))
    screen_field = screen_field.replace('r2', ' ')
    screen_field = screen_field.replace('r3', ('' + str(gameboard[3][5])))
    screen_field = screen_field.replace('r4', ' ')
    screen_field = screen_field.replace('l1', '  ')
    screen_field = screen_field.replace('l2', (' ' + str(gameboard[2][0])))
    screen_field = screen_field.replace('l3', '  ')
    screen_field = screen_field.replace('l4', (' ' + str(gameboard[4][0])))
    screen_field = screen_field.replace('x1', '  ')
    screen_field = screen_field.replace('x2', '  ')
    screen_field = screen_field.replace('x3', '  ')
    screen_field = screen_field.replace('x4', '  ')
    screen_field = screen_field.replace('x5', '  ')
    screen_field = screen_field.replace('x6', '  ')
    screen_field = screen_field.replace('x7', '  ')
    screen_field = screen_field.replace('x8', '  ')
    screen_field = screen_field.replace('x9', '  ')
    screen_field = screen_field.replace('x0', '  ')
    screen_field = screen_field.replace('y1', '  ')
    screen_field = screen_field.replace('y2', '  ')
    screen_field = screen_field.replace('y3', '  ')
    screen_field = screen_field.replace('y4', '  ')
    screen_field = screen_field.replace('y5', '  ')
    screen_field = screen_field.replace('y6', '  ')
    
    print(screen_field)

def main_menu():
    create_gameboard()
    while not check_win():
        input_()
    
    
main_menu()