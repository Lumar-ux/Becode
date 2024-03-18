def player_name():
    player1 = list(input("Player 1, Choisi ton signe entre X et O : "))
    player2 = list(input("Player 2, Choisi ton signe entre X et O : "))
    while player1 == player2:
        player2 = list(input("Player 2, Choisi un autre signe entre X et O : "))
    return(player1, player2)
grid = [[" ","1","2","3"],["1","-","-","-"],["2","-","-","-"],["3","-","-","-"]]
def print_grid(grid):
    for pr_grid in grid:
        print(''.join(pr_grid))
def input_player(num_ply):
    if num_ply == 1:
        ply = "Player 1"
    else:
        ply = "Player 2"
    take = list(input(f"{ply}, Veuillez choisir le numero de colonne et de la range : "))
    return(take)
def game(grid):
    player1, player2 = player_name()
    print_grid(grid)
    ok=True
    while ok == True:  
        take1 = input_player(1)
        while not (1 <= int(take1[0]) <= 3 and 1 <= int(take1[1]) <= 3):
            take1 = list(input("Veuillez choisir des coordonnées valides (entre 1 et 3) : "))
        row_ply1=int(take1[0])
        col_ply1=int(take1[1])
        if (grid[row_ply1][col_ply1] != "-"):
            print("Player 1, Cette case est déjà occupée, veuillez choisir une autre case.")
            continue
        take2 = input_player(2)
        while not (1 <= int(take2[0]) <= 3 and 1 <= int(take2[1]) <= 3):
            take2 = input("Veuillez choisir des coordonnées valides (entre 1 et 3) : ")
        while take1 == take2:
            take2 = list(input("Player 2, Vous avez choisi une colonne et une range deja joue. Veuillez re-joue : "))
        row_ply2=int(take2[0])
        col_ply2=int(take2[1])
        if (grid[row_ply2][col_ply2] != "-"):
            print("Player 2, Cette case est déjà occupée, veuillez choisir une autre case.")
            continue
        grid[row_ply1][col_ply1] = player1[0]
        grid[row_ply2][col_ply2] = player2[0]
        print_grid(grid)
        ok=check(grid, player1, player2)
def check(grid, player1, player2):
    ok = True
    draw_count = 0
    for row in range(1, 4):
        if (grid[row][1] == grid[row][2] == grid[row][3]) and (grid[row][1] == player1[0]):
            print(f"{''.join(player1)}, You Win")
            draw_count = draw_count + 1
            ok=False
        elif (grid[row][1] == grid[row][2] == grid[row][3]) and (grid[row][1] == player2[0]):
            print(f"{''.join(player2)}, You Win")
            draw_count = draw_count + 1
            ok=False
    for col in range(1, 4):
        if (grid[1][col] == grid[2][col] == grid[3][col]) and (grid[1][col] == player1[0]):
            print(f"{''.join(player1)}, You Win")
            draw_count = draw_count + 1
            ok=False
        elif (grid[1][col] == grid[2][col] == grid[3][col]) and (grid[1][col] == player2[0]):
            print(f"{''.join(player2)}, You Win")
            draw_count = draw_count + 1
            ok=False
    if (grid[1][1] == grid[2][2] == grid[3][3]) and (grid[1][1] == player1[0]):
        print(f"{''.join(player1)}, You Win")
        draw_count = draw_count + 1
        ok=False
    elif (grid[1][1] == grid[2][2] == grid[3][3]) and (grid[1][1] == player2[0]):
        print(f"{''.join(player2)}, You Win")
        draw_count = draw_count + 1
        ok=False
    elif (grid[3][1] == grid[2][2] == grid[1][3]) and (grid[3][1] == player1[0]):
        print(f"{''.join(player1)}, You Win")
        draw_count = draw_count + 1
        ok=False
    elif (grid[3][1] == grid[2][2] == grid[1][3]) and (grid[3][1] == player2[0]):
        print(f"{''.join(player2)}, You Win")
        draw_count = draw_count + 1
        ok=False
    print(draw(grid, draw_count))
    return(ok)
def draw(grid, draw_count):
    draw_full = 0
    msg_draw=""
    if draw_count == 2:
        msg_draw="You both Win,So It's a Draw"
        # print("You both Win,So It's a Draw")
    for draw in grid:
        if draw != '-':
            draw_full = draw_full + 1
        if draw_full == 16:
            msg_draw="It's a Draw"
            # print("It's a Draw")
    return(msg_draw)
game(grid)