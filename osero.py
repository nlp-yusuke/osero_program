# -*- coding: utf-8 -*-


import numpy as np
import random 
import sys

class field(object):
    def __init__(self, size=8):    #initialize field
        self.field = np.zeros([size, size], dtype = int)
        self.field[size/2-1][size/2-1] = 1
        self.field[size/2-1][size/2] = -1   # fast is -1
        self.field[size/2][size/2-1] = -1
        self.field[size/2][size/2] = 1      # second is 1
        self.turn = 0
        self.faster = random.randint(0,1)   # decide fast player
        self.finish = False

    def print_field(self, size=8):   # show a current field
        self.turn += 1
        print("turn: " +str(self.turn))
        print('  1 2 3 4 5 6 7 8')
        for i in range(size):
            list = []
            for j in range(size+1):
                if j == 0:
                    list.append(str(i+1))
                elif self.field[i][j-1] == 1:
                    list.append("⚪")
                elif self.field[i][j-1] == -1:
                    list.append("⚫")
                else:
                    list.append(" ")
            print(" ".join(list))

    def check_next_move(self,turn = None, size=8): # search the next move player can select
        list =[]
        if not turn == None:
            self.turn = turn

        # reverse the field to check second player move
        if self.turn % 2 == 0:
            self.field = -self.field
        for i in range(size):   
            for j in range(size):  
                direct = []
                dct1 = False
                dct2 = False
                dct3 = False
                dct4 = False
                dct5 = False
                dct6 = False
                dct7 = False
                dct8 = False
                if self.field[i][j] == 0:
                    move = [i, j]
                    for x in range(size-i-1):  # search downward
                        if self.field[i+1+x][j] == 1:
                            dct1 = True
                        elif self.field[i+1+x][j] == -1 and dct1 == True :
                            direct.append(1)
                            break
                        else:
                            break
                    for x in range(i):       # search upward
                        if self.field[i-1-x][j] == 1:
                            dct2 = True
                        elif self.field[i-1-x][j] == -1 and dct2 == True:
                            direct.append(2)
                            break
                        else:
                            break
                    for x in range(size-j-1):  # search rightward
                        if self.field[i][j+1+x] == 1:
                            dct3 = True
                        elif self.field[i][j+1+x] == -1 and dct3 == True:
                            direct.append(3)
                            break
                        else:
                            break
                    for x in range(j):       # search leftward
                        if self.field[i][j-1-x] == 1:
                            dct4 = True
                        elif self.field[i][j-1-x] == -1 and dct4 == True:
                            direct.append(4)
                            break
                        else:
                            break
                    k = min(size-i-1, size-j-1)
                    for x in range(k):         # search right-downward
                        if self.field[i+1+x][j+1+x] == 1:
                            dct5 = True
                        elif self.field[i+1+x][j+1+x] == -1 and dct5 == True:
                            direct.append(5)
                            break
                        else:
                            break
                    k = min(size-i-1, j)
                    for x in range(k):         # search left-downward
                        if self.field[i+1+x][j-1-x] == 1:
                            dct6 = True
                        elif self.field[i+1+x][j-1-x] == -1 and dct6 == True:
                            direct.append(6)
                            break
                        else:
                            break
                    k = min(i, j)
                    for x in range(k):         # search left-upward
                        if self.field[i-1-x][j-1-x] == 1:
                            dct7 = True
                        elif self.field[i-1-x][j-1-x] == -1 and dct7 == True:
                            direct.append(7)
                        else:
                            break
                    k = min(i, size-j-1)
                    for x in range(k):         # search right-upward
                        if self.field[i-1-x][j+1+x] == 1:
                            dct8 = True
                        elif self.field[i-1-x][j+1+x] == -1 and dct8 == True:
                            direct.append(8)
                            break
                        else:
                            break
                    if len(direct) > 0:
                        pos = []               # keep the move and direction
                        pos.append(move)
                        pos.append(direct)
                        list.append(pos)
        if self.turn % 2 == 0:
            self.field = -self.field
        return list

    def renew_field(self, move, field, turn=None):
        if turn != None:      # this is used for predicting moves
            if turn % 2 == 0:
                rev_stone = 1
            else:
                rev_stone = -1
            
        if self.turn % 2 == 1:
            rev_stone = -1      # reverse black stone
        else:
            rev_stone = 1       # reverse white stone
        field[move[0][0]][move[0][1]] = rev_stone
        if 1 in move[1]:
            x = 1
            while not field[move[0][0]+x][move[0][1]] == rev_stone:
                field[move[0][0]+x][move[0][1]] = rev_stone
                x += 1
        if 2 in move[1]:
            x = 1
            while not field[move[0][0]-x][move[0][1]] == rev_stone:
                field[move[0][0]-x][move[0][1]] = rev_stone
                x += 1
        if 3 in move[1]:
            x = 1
            while not field[move[0][0]][move[0][1]+x] == rev_stone:
                field[move[0][0]][move[0][1]+x] = rev_stone
                x += 1
        if 4 in move[1]:
            x = 1
            while not field[move[0][0]][move[0][1]-x] == rev_stone:
                field[move[0][0]][move[0][1]-x] = rev_stone
                x += 1
        if 5 in move[1]:
            x = 1
            while not field[move[0][0]+x][move[0][1]+x] == rev_stone:
                field[move[0][0]+x][move[0][1]+x] = rev_stone
                x += 1
        if 6 in move[1]:
            x = 1
            while not field[move[0][0]+x][move[0][1]-x] == rev_stone:
                field[move[0][0]+x][move[0][1]-x] = rev_stone
                x += 1
        if 7 in move[1]:
            x = 1
            while not field[move[0][0]-x][move[0][1]-x] == rev_stone:
                field[move[0][0]-x][move[0][1]-x] = rev_stone
                x += 1
        if 8 in move[1]:
            x = 1
            while not field[move[0][0]-x][move[0][1]+x] == rev_stone:
                field[move[0][0]-x][move[0][1]+x] = rev_stone
                x += 1

        return field

    def count_score(self, size=8):
        fast_score =0
        second_score = 0
        for i in range(size-1):
            for j in range(size-1):
               if self.field[i+1][j+1] == -1:
                   fast_score += 1
               elif self.field[i+1][j+1] == 1:
                   second_score += 1
        print("黒:"+str(fast_score))
        print("白:"+str(second_score))
        if fast_score + second_score == 64 or fast_score == 0 or second_score == 0:
            self.finishi = True
            if fast_score > second_score:
                print("勝者：黒")
            elif fast_score < second_score:
                print("勝者：白")
            else:
                print("引き分け")
def get_input(list):
    move = False
    while move == False:
        c_int = False
        r_int = False
        while c_int == False:
            print("縦")
            column = sys.stdin.readline()
            if column.strip().isdigit() == True:
                c_int = True

                #translate the input to the index
                column = int(column)-1
            else:
                print("数字を入力してください")
        r_int = False
        while r_int == False:
            print("横")
            row = sys.stdin.readline()
            if row.strip().isdigit() == True:
                r_int = True
                row = int(row)-1
            else:
                print("数字を入力してください")
        player_move = [column, row]
        for poss_move in list:
            if player_move == poss_move[0]:
                move = True
                direct = poss_move[1]
        if move == False:
            print("もう一度入力してください")
        else:
            move = True
    return [[column, row], direct]
class com(field):
    def __init__(self, field, faster, turn, level=2):
        self.faster = faster
        self.level = level
        self.field = field
        self.turn = turn
    def search_field(self, a=0, depth=3):
        candidate_move = super(com, self).check_next_move(a+self.turn)
        current_field = self.field.copy()
        tmp_score, tmp_corner = None, None
        for move in candidate_move:
            self.field = current_field.copy()
            super(com, self).renew_field(move, self.field, a+self.turn)
            if a == depth:
                score, corner = self.evaluate_field(a, self.field, self.faster)
                tmp_score, tmp_corer = self.select_best_field(score, corner, tmp_score, tmp_corner, a)
            else:
                score, corner = self.search_field(a+1)
                tmp_score, tmp_corer = self.select_best_field(score, corner, tmp_score, tmp_corner, a)
                if a == 0 and corner == tmp_corner and score == tmp_score:
                    best_move = move
        if a == 0:
            self.field = current_field.copy()
            return move
        else:
            self.field = current_field.copy()
            return tmp_score, tmp_corner
                
    def select_best_field(self, score, corner, tmp_score, tmp_corner, turn):
        if turn % 2 == 1:
            if tmp_corner == None:
                tmp_score = score
                tmp_corner = corner
            elif tmp_corner > corner:
                tmp_score = score
                tmp_corner = corner
            elif tmp_corner == corner and tmp_score > score:
                tmp_score = score
                tmp_corner = corner
            return tmp_corner, tmp_score
        else:
            if tmp_corner == None:
                tmp_score = score
                tmp_corner = corner
            elif tmp_corner < corner:
                tmp_score = score
                tmp_corner = corner
            elif tmp_corner == corner and tmp_score < score:
                tmp_score = score
                tmp_corner = corner
            return tmp_corner, tmp_score
        

    def evaluate_field(self, a, field, faster, size=8):
        fast_score =0
        second_score = 0
        fast_corner = 0
        second_corner = 0
        if field[0][0] == -1:
            fast_corner += 1
        if field[0][7] == -1:
            fast_corner += 1
        if field[7][0] == -1:
            fast_corner+= 1
        if field[7][7] == -1:
            fast_corner+= 1
        if field[0][0] == 1:
            second_corner += 1
        if field[0][7] == 1:
            second_corner+= 1
        if field[7][0] == 1:
            second_corner+= 1
        if field[7][7] == 1:
            second_corner+= 1
        for i in range(size-1):
            for j in range(size):
                if field[i][j] == -1:
                    fast_score += 1
                elif field[i][j] == 1:
                    second_score += 1
        if self.faster == 1:
            return fast_score-second_score, fast_corner-second_corner
        else:
            return second_score-fast_score, second_corner-fast_corner

def main():
    f = field()
    if f.faster == 0:
        while f.finish == False:
            f.print_field()
            f.count_score()
            next_move = f.check_next_move()
            if next_move != []:
                player_move = get_input(next_move)
                f.field = f.renew_field(player_move, f.field)
            else:
                print("パス")
            f.print_field()
            f.count_score()
            if f.check_next_move() != []:
                c = com(f.field, f.faster, f.turn)
                com_move = c.search_field()
                f.renew_field(com_move, f.field)
            else:
                print("パス")
    else:
        while f.finish == False:
            f.print_field()
            f.count_score()
            if f.check_next_move() != []:
                c = com(f.field, f.faster, f.turn)
                com_move = c.search_field()
                f.renew_field(com_move, f.field)
            else:
                print("パス")
            f.print_field()
            f.count_score()
            next_move = f.check_next_move()
            if next_move != []:
                player_move = get_input(next_move)
                f.field = f.renew_field(player_move, f.field)
            else:
                print("パス")
main()
