from random import randrange

def play():
  print('**************************************')
  print('Wellcome to the guess the number game!')
  print('**************************************')
  
  secret_number = randrange(1, 101)
  total_tries = 0
  score = 1000
  
  print("Choose the game level: ")
  print("(1) Easy (2) Medium (3) Hard")
  level = int(input("Choose the level: "))
  
  if(level == 1):
    total_tries = 20
  elif(level == 2):
    total_tries = 10
  else:
    total_tries = 5
    
  for tries in range(1, total_tries + 1):
    # print("Secret number = {}".format(secret_number))
    print("Try {} of {}".format(tries, total_tries))
    
    player_guess = int(input("Type a number between 1 and 100: "))
    
    if(player_guess < 1 or player_guess > 100):
      print("You must type a number between 1 and 100!")
      continue
      
    right_guess = secret_number == player_guess
    bigger_guess = secret_number < player_guess
    lower_guess = secret_number > player_guess
    
    if(right_guess):
      print("Congratulations!! You made it and scored {} points!".format(score))
      break
    else:
      if(bigger_guess):
        print("Wrong number! Your number was bigger than the computer number!")
      elif(lower_guess):
        print("Wrong number! Your number was lower than the computer number!")
        
      lost_points = abs(secret_number - player_guess)
      score = score - lost_points
      
  print("Game Over")        