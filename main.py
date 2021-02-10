

board = ["_","_","_",
        "_","_","_",
        "_","_","_"]


game_still_going =True

winner =  None

current_player = "X"

#display board
def display_board():
  print(board[0]+"|"+board[1]+"|"+board[2])
  print(board[3]+"|"+board[4]+"|"+board[5])
  print(board[6]+"|"+board[7]+"|"+board[8])


#play the game TIC TAC TOE
def play_game():
  #display initial board
  display_board()

  #while the game is still going
  while game_still_going:
    #handle a single turn of an arbitrary player
    handle_turn(current_player)
    #check if the game has ended
    check_if_game_over()
    #Flip to the other player
    flip_player()

  #The game has ended
  if winner == "X" or winner == "O":
    print(winner +" won.")
  elif winner == None:
    print("TIE.")

#handle a single turn of an arbitrary player
def handle_turn(player):
  print(player+"'s turn.")

  position = input("Choose a position from 1-9:")
  valid = False
  while not valid:
    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position = input("Invalid input. Choose an input from 1-9:")
    
    position = int(position)-1

    if board[position] == "_":
      valid = True
    else:
      print("You Can't go there. Go somewhere else.")

  board[position] = player
  display_board()

def check_if_game_over():
  check_for_winner()
  check_if_tie()



def check_for_winner():

  #set up global variables
  global winner
  #check rows
  row_winner = check_rows()
  #check columns 
  column_winner = check_column()
  #check diagonal 
  diagonal_winner = check_diagonal()
  if row_winner:
    #there is a winner
    winner = row_winner
  elif column_winner:
    #there is a winner
    winner = column_winner
  elif diagonal_winner:
    #there is a winner
    winner = diagonal_winner
  else:
    #there is no winner
    winner = None
  return




def check_rows():
  #set up global variables
  global game_still_going
  #check if any the rows have all the same value
  row_1 = board[0] == board[1] == board[2] !="_"
  row_2 = board[3] == board[4] == board[5] !="_"
  row_3 = board[6] == board[7] == board[8] !="_"
  #if any rows does have a match
  if row_1 or row_2 or row_3:
    game_still_going = False
  #return the winner
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return

def check_column():
  #set up global variables
  global game_still_going
  #check if any the rows have all the same value
  column_1 = board[0] == board[3] == board[6] !="_"
  column_2 = board[1] == board[4] == board[7] !="_"
  column_3 = board[2] == board[5] == board[8] !="_"
  #if any rows does have a match
  if column_1 or column_2 or column_3:
    game_still_going = False
  #return the winner
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return

def check_diagonal():
  #set up global variables
  global game_still_going
  #check if any the rows have all the same value
  diagonal_1 = board[0] == board[4] == board[8] !="_"
  diagonal_2 = board[2] == board[4] == board[6] !="_"

  #if any rows does have a match
  if diagonal_1 or diagonal_2:
    game_still_going = False
  #return the winner
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  return

def check_if_tie():
  global game_still_going
  if "_" not in board:
    game_still_going = False
  return

def flip_player():
  #global variable we need
  global current_player
  #player change
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  return




play_game()