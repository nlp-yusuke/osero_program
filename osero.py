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
            for j in range(size):
                if j == 0:
                    list.append(str(i+1))
                elif self.field[i][j-1] == 1:
                    list.append("⚪")
                elif self.field[i][j-1] == -1:
                    list.append("⚫")
                else:
                    list.append(" ")
            print(" ".join(list))

    def check_next_move(self, field, size=8): # search the next move player can select
        list =[]
        if self.turn % 2 == 1:
            pass
        else:
            field = -(field)
        for i in range(len(field)):   
            for j in range(len(field[i])):  
                direct = []
                dct1 = False
                dct2 = False
                dct3 = False
                dct4 = False
                dct5 = False
                dct6 = False
                dct7 = False
                dct8 = False
                if field[i][j] == 0:
                    move = [i, j]
                    for x in range(size-i-1):  # search downward
                        if field[i+1+x][j] == -1:
                            dct1 = True
                        elif field[i+1+x][j] == 1 and dct1 == True :
                            direct.append(1)
                            break
                        else:
                            break
                    for x in range(i-1):       # search upward
                        if field[i-1-x][j] == -1:
                            dct2 = True
                        elif field[i-1-x][j] == 1 and dct2 == True:
                            direct.append(2)
                            break
                        else:
                            break
                    for x in range(size-j-1):  # search rightward
                        if field[i][j+1+x] == -1:
                            dct3 = True
                        elif field[i][j+1+x] == 1 and dct3 == True:
                            direct.append(3)
                            break
                        else:
                            break
                    for x in range(j-1):       # search leftward
                        if field[i][j-1-x] == -1:
                            dct4 = True
                        elif field[i][j-1-x] == 1 and dct4 == True:
                            direct.append(4)
                            break
                        else:
                            break
                    k = min(size-i-1, size-j-1)
                    for x in range(k):         # search right-downward
                        if field[i+1+x][j+1+x] == -1:
                            dct5 = True
                        elif field[i+1+x][j+1+x] == 1 and dct5 == True:
                            direct.append(5)
                            break
                        else:
                            break
                    k = min(size-i-1, j-1)
                    for x in range(k):         # search left-downward
                        if field[i+1+x][j-1-x] == -1:
                            dct6 = True
                        elif field[i+1+x][j-1-x] == 1 and dct6 == True:
                            direct.append(6)
                            break
                        else:
                            break
                    k = min(i-1, j-1)
                    for x in range(k):         # search left-upward
                        if field[i-1-x][j-1-x] == -1:
                            dct7 = True
                        elif field[i-1-x][j-1-x] == 1 and dct7 == True:
                            direct.append(7)
                        else:
                            break
                    k = min(i-1, size-j-1)
                    for x in range(k):         # search right-upward
                        if field[i-1-x][j+1+x] == -1:
                            dct8 = True
                        elif field[i-1-x][j+1+x] == 1 and dct8 == True:
                            direct.append(8)
                            break
                        else:
                            break
                    if len(direct) > 0:
                        pos = []               # keep the move and direction
                        pos.append(move)
                        pos.append(direct)
                        list.append(pos)
        print(list)
        return list

    def renew_field(self, move, field, turn):
        if turn % 2 == 1:
            field[move[0][0]][move[0][1]] = 1
            if 1 in move[1]:
                x = 1
                while not field[move[0][0]+x][move[0][1]] == 1:
                    field[move[0][0]+x][move[0][1]] = 1
                    x += 1
            if 2 in move[1]:
                x = 1
                while not field[move[0][0]-x][move[0][1]] == 1:
                    field[move[0][0]-x][move[0][1]] = 1
                    x += 1
            if 3 in move[1]:
                x = 1
                while not field[move[0][0]][move[0][1]+x] == 1:
                    field[move[0][0]][move[0][1]+x] = 1
                    x += 1
            if 4 in move[1]:
                x = 1
                while not field[move[0][0]][move[0][1]-x] == 1:
                    field[move[0][0]][move[0][1]-x] = 1
                    x += 1
            if 5 in move[1]:
                x = 1
                while not field[move[0][0]+x][move[0][1]+x] == 1:
                    field[move[0][0]+x][move[0][1]+x] = 1
                    x += 1
            if 6 in move[1]:
                x = 1
                while not field[move[0][0]+x][move[0][1]-x] == 1:
                    field[move[0][0]+x][move[0][1]-x] = 1
                    x += 1
            if 7 in move[1]:
                x = 1
                while not field[move[0][0]-x][move[0][1]-x] == 1:
                    field[move[0][0]-x][move[0][1]-x] = 1
                    x += 1
            if 8 in move[1]:
                x = 1
                while not field[move[0][0]-x][move[0][1]+x] == 1:
                    field[move[0][0]-x][move[0][1]+x] = 1
                    x += 1
        else:
            field[move[0][0]][move[0][1]] = -1
            if 1 in move[1]:
                x = 1
                while not field[move[0][0]+x][move[0][1]] == -1:
                    field[move[0][0]+x][move[0][1]] = -1
                    x += 1
            if 2 in move[1]:
                x = 1
                while not field[move[0][0]-x][move[0][1]] == -1:
                    field[move[0][0]-x][move[0][1]] = -1
                    x += 1
            if 3 in move[1]:
                x = 1
                while not field[move[0][0]][move[0][1]+x] == -1:
                    field[move[0][0]][move[0][1]+x] = -1
                    x += 1
            if 4 in move[1]:
                x = 1
                while not field[move[0][0]][move[0][1]-x] == -1:
                    field[move[0][0]][move[0][1]-x] = -1
                    x += 1
            if 5 in move[1]:
                x = 1
                while not field[move[0][0]+x][move[0][1]+x] == -1:
                    field[move[0][0]+x][move[0][1]+x] = -1
                    x += 1
            if 6 in move[1]:
                x = 1
                while not field[move[0][0]+x][move[0][1]-x] == -1:
                    field[move[0][0]+x][move[0][1]-x] = -1
                    x += 1
            if 7 in move[1]:
                x = 1
                while not field[move[0][0]-x][move[0][1]-x] == -1:
                    field[move[0][0]-x][move[0][1]-x] = -1
                    x += 1
            if 8 in move[1]:
                x = 1
                while not field[move[0][0]-x][move[0][1]+x] == -1:
                    field[move[0][0]-x][move[0][1]+x] = -1
                    x += 1
        return field

    def count_score(self, size=9):
        fast_score =0
        second_score = 0
        for i in range(size-1):
            for j in range(size-1):
               if self.field[i+1][j+1] == 1:
                   fast_score += 1
               elif self.field[i+1][j+1] == -1:
                   second_score += 1
        print("黒:"+str(fast_score))
        print("白:"+str(second_score))
        if fast_score + second_score == 64:
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
                column = int(column)
            else:
                print("数字を入力してください")
        r_int = False
        while r_int == False:
            print("横")
            row = sys.stdin.readline()
            if row.strip().isdigit() == True:
                r_int = True
                row = int(row)
            else:
                print("数字を入力してください")
        player_move = [column, row]
        print(player_move)
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
    def __init__(self, field, turn, level=2):
        self.turn = turn
        self.level = level
        self.field = field
    def com_move(self, faster):
        fst_score = None
        fst_corner = None
        tmp_move = None
        tem_field = self.field.copy()
        fst_candidate_move = super(com, self).check_next_move(self.field, self.turn)
        for fst_move in fst_candidate_move:
            sec_score = None
            sec_corner = None
            self.field = tem_field.copy()
            self.field=super(com, self).renew_field(fst_move, self.field, self.turn)
            sec_candidate_move = super(com, self).check_next_move(self.field, self.turn+1)
            tem_sec_field = self.field.copy()
            for sec_move in sec_candidate_move:
                third_score = None
                third_corner = None
                self.field = tem_sec_field.copy()
                self.field = super(com, self).renew_field(sec_move, self.field, self.turn+1)
                third_candidate_move = super(com, self).check_next_move(self.field, self.turn)
                tem_third_field = self.field.copy()
                for third_move in third_candidate_move:
                    self.field = tem_third_field.copy()
                    self.field=super(com, self).renew_field(third_move, self.field, self.turn)
                    score, corner = self.evaluate_field(faster, self.field)
                    third_corner, third_score = self.select_best_field(score, corner, third_score, third_corner, "com")
                sec_corner, sec_score = self.select_best_field(third_score, third_corner, sec_score, sec_corner, "player")
            tmp_move, fst_score, fst_corner = self.select_best_field(sec_score, sec_corner, fst_score, fst_corner, "com", tmp_move, fst_move)

        return tmp_move
    
    def select_best_field(self, score, corner, tmp_score, tmp_corner, turn, tmp_move=None, move=None):
        if not move == None:
            if tmp_corner == None:
                tmp_score = score
                tmp_corner = corner
                tmp_move = move
            elif tmp_corner < corner:
                tmp_score = score
                tmp_corner = corner
                tmp_move = move
            elif tmp_corner == corner and tmp_score < score:
                tmp_score = score
                tmp_corner = corner
                tmp_move = move
            return tmp_move, tmp_corner, tmp_score
        elif turn == "player":
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
        elif turn == "com":
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
        

    def evaluate_field(self, faster, field, size=9):
        fast_score =0
        second_score = 0
        fast_corner = 0
        second_corner = 0
        if field[1][1] == 1:
            fast_corner += 1
        if field[1][8] == 1:
            fast_corner += 1
        if field[8][1] == 1:
            fast_corner+= 1
        if field[8][8] == 1:
            fast_corner+= 1
        if field[1][1] == -1:
            second_corner += 1
        if field[1][8] == -1:
            second_corner+= 1
        if field[8][1] == -1:
            second_corner+= 1
        if field[8][8] == -1:
            second_corner+= 1
        for i in range(size-1):
            for j in range(size-1):
                if field[i+1][j+1] == 1:
                    fast_score += 1
                elif field[i+1][j+1] == -1:
                    second_score += 1
        if faster == 1:
            return fast_score-second_score, fast_corner-second_corner
        else:
            return second_score-fast_score, second_corner-fast_corner
def main():
    f = field()
    f.print_field()
    if f.faster == 0:
        while f.finish == False:
            next_move = f.check_next_move(f.field, f.turn)
            if not next_move == []:
                player_move = get_input(next_move)
                f.field = f.renew_field(player_move, f.field, f.turn)
                f.print_field()
                f.count_score()
            else:
                print("パス")
                f.turn = f.turn + 1
            if not f.check_next_move(f.field, f.turn) == []:
                c = com(f.field, f.turn)
                com_move = c.com_move(f.faster)
                f.field = f.renew_field(com_move, f.field, f.turn)
                f.print_field()
                f.count_score()
            else:
                print("パス")
                f.turn = f.turn+ 1
    elif f.faster == 1:
        while f.finish == False:
            if not f.check_next_move(f.field, f.turn) == []:
                c = com(f.field, f.turn)
                com_move = c.com_move(f.faster)
                f.field = f.renew_field(com_move, f.field, f.turn)
                f.print_field()
                f.count_score()
            else:
                print("パス")
                f.turn = f.turn+ 1
            next_move = f.check_next_move(f.field, f.turn)
            if not next_move ==[]:
                player_move = get_input(next_move)
                f.field = f.renew_field(player_move, f.field, f.turn)
                f.print_field()
                f.count_score()
            else:
                print("パス")
                f.turn = f.turn+ 1


main()
