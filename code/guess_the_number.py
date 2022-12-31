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
    print("Try {} of {}".format(tries, total_tries))
    
    player_guess = input("")