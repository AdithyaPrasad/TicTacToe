import random
import time
game_board = " 7 | 8 | 9\n 4 | 5 | 6\n 1 | 2 | 3"
#1,5,9   12, 16, 20   23, 27, 31
print (game_board)
print("")
available_nums = "123456789"
used_number = ""
result = ""
def winning(player, symbol):
    for i in (1, 12, 23):
        global result
        if game_board[i] == symbol and game_board[i+4] == symbol and game_board[i+8] == symbol:
            result = player + " has won!"
            return result
    for i in (1, 5, 9):
        if game_board[i] == symbol and game_board[i+11] == symbol and game_board[i+22] == symbol:
            result = player + " has won!"
            return result
    if game_board[1] == symbol and game_board[16] == symbol and game_board[31]==symbol:
        result = player + " has won!"
        return result
    if game_board[9] == symbol and game_board[16] == symbol and game_board[23] == symbol:
        result = player + " has won!"
        return result
    return ""
for x in range(5):
    play = input("Enter a number to place your piece: ")
    while play in used_number or play not in game_board:
        play = input("Either a player has already played that position or the number inputted is a invalid input! Try again ")
    if int(play) in range(1,10):
        used_number += play
        game_board = game_board.replace(play, 'X')
    print (game_board)
    print("")
    print(winning('Player', 'X'))
    if 'won' in result:
        break
    if x == 4:
        print("It's a tie!")
        break
    play = random.choice(available_nums)
    while play in used_number or play not in game_board:
        play = random.choice(available_nums)
    if int(play) in range(1,10):
        used_number += play
        game_board = game_board.replace(play, 'O')
    time.sleep(1)
    print (game_board)
    print("")
    print(winning('Player 2', 'O'))
    if 'won' in result:
        break