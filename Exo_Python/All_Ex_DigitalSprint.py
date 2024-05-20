# First_name = "Barack"
# Middle_name = "Hussein"
# Last_name = "Obama"
# Date_of_birth = "04/08/1961"
# Age = "We let you compute it"
# Place_of_birth = "Honolulu"
# Nationality = "USA"
# Height = 187 #cm
# Weight = 79 #kg
# tmp_ny = 41 #F
# cell = (tmp_ny - 32) * 5/9
# print(cell)

# cash = 100
# bank = 1290
# bottle = 12
# prix = 0.7
# TOTAL = cash + bank
# vac = [100, 200, 400]
# vac_total = vac[0] + vac[1] + vac[2]
# print(TOTAL)
# print(bottle * prix)
# print("Il vous reste", TOTAL - (bottle * prix))
# print(vac_total/len(vac))
# print((vac_total/len(vac))*len(vac))

# buttons = ["morning", "before lunch", "after lunch", "end of day"]
# extra_buttons = ["before dinner", "after dinner", "time to sleep!"]
# becode = ["Louis", "Basile", "Mohammed", "Justine", "Senay", "Louis"]

# all_buttons = buttons + extra_buttons
# print(all_buttons[-1])
# print(all_buttons[5:])
# buttons = extra_buttons
# buttons.append("Ordi")

# becode = {"Lou" : 23 , "Basile": 24, "Mohammed":35, "Justine":56, "Senay":78, "Louis":90}
# print(becode["Louis"])

# 6 - Loops

# import random as ra
# cel = [15, 18, 20, 22, 19, 17, 21]
# tot = 0
# high = 0
# # for tmps in cel:
# #     print(tmps)
# for som in cel:
#     tot = tot + som
# for high in cel:
#     while high > tot/len(cel):
#         print(high)
#         break
# for far in cel:
#     con = (far * 9/5) + 32
#     print("La conversion de C en F est :",(far * 9/5) + 32)
# print("La moyenne est de",round(tot/len(cel), 2))
# for ran in range(7):
#     ran_tmp = ra.randint(-15, 25)
#     if ran_tmp <= 14:
#         print("It's so fresh :", ran_tmp)
#     elif (ran_tmp >= 15) and (ran_tmp <= 23):
#         print("It's a plesant temps :", ran_tmp)
#     else:
#         print("It's hot :", ran_tmp)
# for week in range(8):
#     print(week)

# 7 - Builf-in Fonction

# import numpy as np  
# print(len("Becode is fun!"))
# con_list = "Becode is fun!"
# print("list:",con_list)
# con_set = set(con_list)
# print("Ensemble:",con_set)
# list1 = [5,6,9,65,78]
# print(max(list1))
# print(min(list1))
# print(sum(list1))
# print(list(reversed(list1)))
# # print(reversed(list1))
# absolue = -42
# print(abs(absolue))
# str1 = "4 + 3"
# print(eval(str1))
# round1 = 3.14159
# print(round(round1, 2))
# cara = "4"
# print((int(cara))*2)

#8 - Functions

# pal = input("Donner moi un palindrome :")
# def pala(palad):
#     if list(palad) == list(reversed(palad)):
#         print("True")
#     else:
#         print("False")
# print(pala(pal))

# pal = input("Donner moi un palindrome :")
# ls = list(pal)

# def pala(palad):
#     if palad == list(reversed(palad)):
#         print("True")
#     else:
#         print("False")
# pala(ls)

# num1 = 4
# num2 = 2
# def divi(a,b):
#     return a / b
# print(divi(num1, num2))

# import re
# name1 = "Becode Ghent"
# ls1 = name1.split()
# i = 0
# def ini(nm1):
#     fini=[]
#     for i in ls1:
#         reg = re.findall("^[a-zA-Z]", i)
#         fini = fini + reg
#     jo= ''.join(fini)
#     return(jo)
# print(ini(ls1))

# lst = ["Bonjour","ads","Loli","B","Malheureusement","A"]
# def long(lst1):
#     longplus = ''
#     for i in lst1:
#         if len(i) > len(longplus):
#             longplus = i
#     return(longplus)
# print(long(lst))

# num1 = 8
# num2 = 9
# def mult(a,b):
#     return(a+b)
# print(mult(num1, num2))

# price = float(input("Donne moi un prix : "))
# exchange = float(input("Donne le taux de conversion : "))
# def conv(pr, ex):
#     return(pr*ex)
# print(conv(price, exchange))

# import re
# passw = input("Donnez-votre mod de passe: ")
# print(passw)
# def verif(pas):
#     x = re.findall("(?=^.{8,}$)((?=.*\\d)|(?=.*\\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$", pas)
#         # print(nodigaplha)
#     if x:
#         ok = True
#     else:
#         ok = False
#     return(ok)
# print(verif(passw))

# import math
# radius = float(input("Donne moi le radius d'un cercle : "))
# carre = radius*radius
# def cercle(radius, carre):
#     pi = math.pi
#     return(carre*pi)   
# print(cercle(radius, carre))

# pal = input("Donner un mot :")
# def pala(pal):
#    rev = list(reversed(pal))
#    jo=''.join(rev)
#    return(jo)
# print(pala(pal))

# a=3
# b=5
# def mult(a,b):
#     return(a*b)
# print(mult(a,b))

#9 - Errors and Exceptions

# num1 = float(input("Donnez moi votre premier nombre : "))
# num2 = float(input("Donnez moi votre deuxieme nombre : "))
# def mult(a,b):
#     try:
#         mu = a/b
#     except ZeroDivisionError:
#         print("Error: You can't divide by zero")
#     return(mu)
# print(mult(num1,num2))

# ind = ["list","nombre"]
# demande = int(input("Donnez moi un index de la list : "))
# def nop(dem,ind):
#     try:
#        find=ind[dem]
#     except IndexError: 
#         print("Error : cette index n'existe pas")
#     return find
# print(nop(demande,ind))

# demande = input("Donnez moi un nombre : ")
# def nop(dem):
#     try:
#        conv=int(dem)
#     except ValueError:
#         try:
#            conv=float(dem) 
#         except:
#             print("Error : ce n'est pas un type float ou int")
#     return(conv)
# print(nop(demande))

# num = int(input("Donne moi votre age : "))
# class InvalidAgeException(Exception):
#     pass
# def rais(num):
#     if num < 0 or num > 150:
#         raise InvalidAgeException("Vous etes trop vieux")
#     else:
#         msg = f"Vous avez {num} ans"
#     return(msg)
# print(rais(num))

# num1 = int(input("Donner moi le premier nombre de votre division : "))
# num2 = int(input("Donner moi le deuxieme nombre de votre division : "))
# class InvalidDivisorException(Exception):
#      pass
# def divi(a,b):
#     try:
#         if b == 0:
#             raise InvalidDivisorException("Attention l'un de vos nombre n'est pas un bon diviseur")
#     except InvalidDivisorException as er:
#         print(er)
#     else:
#         return(a/b)
# print(divi(num1,num2))

# 10 - Project - Guess the number

# import random as ra
# ranum=ra.randint(1, 101)
# print(ranum)
# def choose(ranum):
#     n=1
#     name1=input("Entrez un nom de joueur : ")
#     shooc=int(input("Essaye de trouver le numéro entre 1 et 100 : "))
#     while shooc > 100 or shooc < 0:
#         shooc=int(input("Essaye de trouver le numéro entre 1 et 100 : "))
#     # for i in range(10):
#     while shooc != ranum:
#         n=n+1
#         if n == 11:
#             print(f"{name1}, You failed, try again!")
#             break
#         if n <= 10:
#             if shooc > ranum:
#                 print("Le numéro choisi est plus grand")
#                 shooc=int(input("Essaye de trouver le numéro entre 1 et 100 : "))
#             elif shooc < ranum:
#                 print("Le numéro choisi est plus petit")
#                 shooc=int(input("Essaye de trouver le numéro entre 1 et 100 : "))
#     if shooc == ranum:
#         print(f"Player {name1}, Vous avez deviné le bon chiffre en {n} tours")
#         msg=True
#     return(msg)
# print(choose(ranum))

#11 - Python project: Tic-Tac-Toe

# def player_name():
#     player1 = list(input("Player 1, Choisi ton signe entre X et O : "))
#     player2 = list(input("Player 2, Choisi ton signe entre X et O : "))
#     while player1 == player2:
#         player2 = list(input("Player 2, Choisi un autre signe entre X et O : "))
#     return(player1, player2)
# grid = [[" ","1","2","3"],["1","-","-","-"],["2","-","-","-"],["3","-","-","-"]]
# def print_grid(grid):
#     for pr_grid in grid:
#         print(''.join(pr_grid))
# def input_player(num_ply):
#     if num_ply == 1:
#         ply = "Player 1"
#     else:
#         ply = "Player 2"
#     take = list(input(f"{ply}, Veuillez choisir le numero de colonne et de la range : "))
#     return(take)
# def game(grid):
#     player1, player2 = player_name()
#     print_grid(grid)
#     ok=True
#     while ok == True:  
#         take1 = input_player(1)
#         while not (1 <= int(take1[0]) <= 3 and 1 <= int(take1[1]) <= 3):
#             take1 = list(input("Veuillez choisir des coordonnées valides (entre 1 et 3) : "))
#         row_ply1=int(take1[0])
#         col_ply1=int(take1[1])
#         if (grid[row_ply1][col_ply1] != "-"):
#             print("Player 1, Cette case est déjà occupée, veuillez choisir une autre case.")
#             continue
#         take2 = input_player(2)
#         while not (1 <= int(take2[0]) <= 3 and 1 <= int(take2[1]) <= 3):
#             take2 = input("Veuillez choisir des coordonnées valides (entre 1 et 3) : ")
#         while take1 == take2:
#             take2 = list(input("Player 2, Vous avez choisi une colonne et une range deja joue. Veuillez re-joue : "))
#         row_ply2=int(take2[0])
#         col_ply2=int(take2[1])
#         if (grid[row_ply2][col_ply2] != "-"):
#             print("Player 2, Cette case est déjà occupée, veuillez choisir une autre case.")
#             continue
#         grid[row_ply1][col_ply1] = player1[0]
#         grid[row_ply2][col_ply2] = player2[0]
#         print_grid(grid)
#         ok=check(grid, player1, player2)
# def check(grid, player1, player2):
#     ok = True
#     draw_count = 0
#     for row in range(1, 4):
#         if (grid[row][1] == grid[row][2] == grid[row][3]) and (grid[row][1] == player1[0]):
#             print(f"{''.join(player1)}, You Win")
#             draw_count = draw_count + 1
#             ok=False
#         elif (grid[row][1] == grid[row][2] == grid[row][3]) and (grid[row][1] == player2[0]):
#             print(f"{''.join(player2)}, You Win")
#             draw_count = draw_count + 1
#             ok=False
#     for col in range(1, 4):
#         if (grid[1][col] == grid[2][col] == grid[3][col]) and (grid[1][col] == player1[0]):
#             print(f"{''.join(player1)}, You Win")
#             draw_count = draw_count + 1
#             ok=False
#         elif (grid[1][col] == grid[2][col] == grid[3][col]) and (grid[1][col] == player2[0]):
#             print(f"{''.join(player2)}, You Win")
#             draw_count = draw_count + 1
#             ok=False
#     if (grid[1][1] == grid[2][2] == grid[3][3]) and (grid[1][1] == player1[0]):
#         print(f"{''.join(player1)}, You Win")
#         draw_count = draw_count + 1
#         ok=False
#     elif (grid[1][1] == grid[2][2] == grid[3][3]) and (grid[1][1] == player2[0]):
#         print(f"{''.join(player2)}, You Win")
#         draw_count = draw_count + 1
#         ok=False
#     elif (grid[3][1] == grid[2][2] == grid[1][3]) and (grid[3][1] == player1[0]):
#         print(f"{''.join(player1)}, You Win")
#         draw_count = draw_count + 1
#         ok=False
#     elif (grid[3][1] == grid[2][2] == grid[1][3]) and (grid[3][1] == player2[0]):
#         print(f"{''.join(player2)}, You Win")
#         draw_count = draw_count + 1
#         ok=False
#     print(draw(grid, draw_count))
#     return(ok)
# def draw(grid, draw_count):
#     draw_full = 0
#     msg_draw=""
#     if draw_count == 2:
#         msg_draw="You both Win,So It's a Draw"
#         # print("You both Win,So It's a Draw")
#     for draw in grid:
#         if draw != '-':
#             draw_full = draw_full + 1
#         if draw_full == 16:
#             msg_draw="It's a Draw"
#             # print("It's a Draw")
#     return(msg_draw)
# game(grid)

#12 Drill

# number = int(input("Enter a number: "))
# number = number + 1 
# lt=[]
# for i in range(0, number):
#     lt.append(i)
# num=lt[::-1]
# for n in num:
#     print(str(n))

import random as ra
ranum=ra.randint(1, 101)
print(ranum)
def choose(ranum):
    n=1
    name1=input("Entrez un nom de joueur : ")
    shooc=int(input("Essaye de trouver le numéro entre 1 et 100 : "))
    while shooc > 100 or shooc < 0:
        shooc=int(input("Essaye de trouver le numéro entre 1 et 100 : "))
    # for i in range(10):
    while shooc != ranum:
        n=n+1
        if n == 11:
            print(f"{name1}, You failed, try again!")
            break
        if n <= 10:
            if shooc > ranum:
                print("Le numéro choisi est plus grand")
                shooc=int(input("Essaye de trouver le numéro entre 1 et 100 : "))
            elif shooc < ranum:
                print("Le numéro choisi est plus petit")
                shooc=int(input("Essaye de trouver le numéro entre 1 et 100 : "))
    if shooc == ranum:
        print(f"Player {name1}, Vous avez deviné le bon chiffre en {n} tours")
        msg=True
    return(msg)
print(choose(ranum))

