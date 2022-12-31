import guess_the_word

def choose_game():
  print('************************************')
  print('***** Choose a game to play! *******')
  print('************************************')
  
  print("(1) Guess the word  (2) Hangman")
  
  game_option = int(input("Choose a game to play ... "))
  
  if(game_option == 1):
    print("You're gonna play: Guess the word!!")
    print("Good luck!")
  elif(game_option == 2):
    print("You're gonna play: Hangman!!")
    print("Good luck!")
    
  print("Game over!")
  
if(__name__ == "__main__"):
  choose_game()