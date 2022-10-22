# Создайте программу для игры в ""Крестики-нолики"".


game_field = [1, 2, 3,
              4, 5, 6, 
              7, 8, 9]

lines_victory = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

def PrintField():
    
    print("-" * 9)
    print("|", game_field[0], end = " ")
    print( game_field[1], end = " ")
    print( game_field[2], end = " |\n")
    
    print("|", game_field[3], end = " ")
    print( game_field[4], end = " ")
    print( game_field[5], end = " |\n")
    
    print("|", game_field[6], end = " ")
    print( game_field[7], end = " ")
    print( game_field[8], end = " |\n")
    print("-" * 9)
    
def StepField(step, symbol):
    idx = game_field.index(step)
    game_field[idx] = symbol
            
def CheckWin(lines_victory):
    win = " "
    
    for i in lines_victory:
       
        if game_field[i[0]] == "X" and game_field[i[1]] == "X" and game_field[i[2]] == "X":
            win = "X"
        elif game_field[i[0]] == "O" and game_field[i[1]] == "O" and game_field[i[2]] == "O":
            win = "O" 
         
    return win        
        
game_over = False
player1 = True
player2 = True
 
while game_over == False:
 
    PrintField()
 
    if player1 == True:
        symbol = "X"
        step = int(input("Игрок №1, ваш ход: "))
    else:
        step = int(input("Игрок №2, ваш ход: "))
        symbol = "O"
 
    StepField(step,symbol)
    win = CheckWin(lines_victory) 
    if win == "X" or win == "O":
        game_over = True
 
    player1 = not(player1)        

         
PrintField()
print(win)
    
 


    
    

    
    
    
