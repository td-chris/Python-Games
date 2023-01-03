import guess_the_number
import hangman

def choose_game():
  print('************************************')
  print('***** Choose a game to play! *******')
  print('************************************')
  
  print("(1) Guess the number  (2) Hangman")
  
  game_option = int(input("Choose a game to play ... "))
  
  if(game_option == 1):
    print("You're gonna play: Guess the number!!")
    print("Good luck!")
    guess_the_number.play()
  elif(game_option == 2):
    print("You're gonna play: Hangman!!")
    print("Good luck!")
    hangman.play()
  
  print("Thanks for playing!")
  
if(__name__ == "__main__"):
  choose_game()