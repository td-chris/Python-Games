import random

def play():
  
  opening_game_message()
  
  secret_word = start_secret_word()
  
  right_letters = start_secret_word_letters(secret_word)
  print(right_letters)
  print("Tip: It's a fruit!")
  
  lost_game = False
  won_game = False
  wrong_guess = 0
  
  while(not lost_game and not won_game):
    player_guess = get_player_guess()
    
    if(player_guess in secret_word):
      insert_right_letters(player_guess, right_letters, secret_word)
    else:
      wrong_guess += 1
      draw_hangman(wrong_guess)
      
    lost_game = wrong_guess == 7
    won_game = "_" not in right_letters
    
    print(right_letters)
    
    if(won_game): 
      print_winner_message() 
    elif(lost_game):
      print_loser_message(secret_word) 
  
def opening_game_message():
  print('***********************************')
  print('** Wellcome to the hangman game! **')
  print('***********************************')
  
def start_secret_word():
  # please insert your word address below
  words_file = open("D:\Study\Projetos\Portifólio\Python-Games\code\words.txt", "r")
  words = []
  
  for line in words_file:
    line = line.strip()
    words.append(line)
    
  words_file.close()
  
  random_int = random.randrange(0, len(words))
  secret_word = words[random_int].upper()
  
  return secret_word

def start_secret_word_letters(word):
  return ["_" for letters in word]

def get_player_guess():
  player_guess = input("Which letter do you choose? ")
  player_guess = player_guess.strip().upper()
  
  return player_guess

def insert_right_letters(player_guess, right_letters, secret_word):
  index = 0
  for letter in secret_word:
    if letter == player_guess:
      right_letters[index] = player_guess
    index += 1
    
def print_loser_message(secret_word):
  print("Sorry, you were hanged!")
  print("The word was {}".format(secret_word))
  print("    _______________         ")
  print("   /               \       ")
  print("  /                 \      ")
  print("//                   \/\  ")
  print("\|   XXXX     XXXX   | /   ")
  print(" |   XXXX     XXXX   |/     ")
  print(" |   XXX       XXX   |      ")
  print(" |                   |      ")
  print(" \__      XXX      __/     ")
  print("   |\     XXX     /|       ")
  print("   | |           | |        ")
  print("   | I I I I I I I |        ")
  print("   |  I I I I I I  |        ")
  print("   \_             _/       ")
  print("     \_         _/         ")
  print("       \_______/           ")
 
def print_winner_message():
  print("Congratulations, you won!")
  print("       ___________      ")
  print("      '._==_==_=_.'     ")
  print("      .-\\:      /-.    ")
  print("     | (|:.     |) |    ")
  print("      '-|:.     |-'     ")
  print("        \\::.    /      ")
  print("         '::. .'        ")
  print("           ) (          ")
  print("         _.' '._        ")
  print("        '-------'       ")

def draw_hangman(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errors == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
