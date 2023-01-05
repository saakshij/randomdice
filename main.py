#import random
import random
#loop to make it repeat again
while True:
  #loop to make sure user enters an odd number 
  while True:
    #ask user how many rounds 
    rounds = int(input("How many rounds do you want to play? "))
    #if rounds is an even number then repeat
    if rounds % 2 == 0: 
      print("Make sure it is a odd number of rounds!")
    #else break
    else: 
      break
  #declare points as 0 at the start
  i = 0
  tie = 0
  player1_points = 0
  player2_points = 0
  #number of rounds
  while i < rounds: 
    #randomly picks a number 
    player1 = random.randint(1,6)
    #prints what player 1 got
    print("\nPlayer 1 got: {}".format(player1))
    #randomly picks a number
    player2 = random.randint(1,6)
    #prints what player 2 got
    print("Player 2 got: {}".format(player2))
    #if statement if player 1 has a higher number
    if player1 > player2:
      #add a point to player 1  
      player1_points += 1
      #print player 1 won
      print("Player 1 won!")
      i += 1
    #if statement if player 2 has a higher number
    elif player2 > player1: 
      #add a point to player 1  
      player2_points += 1
      #print player 1 won
      print("Player 2 won!")
      i += 1
    else:
      #if its a tie
      print("It was a tie!")
      #add tie points
    

  #if player 1 has more points than player 2
  if player1_points > player2_points: 
    #print player 1 won
    print("\nPlayer 1 won! Rounds won: {}".format(player1_points))
  #if player 2 has more points than player 1
  elif player1_points < player2_points: 
    #print player 1 won
    print("\nPlayer 2 won! Rounds won: {}".format(player2_points))
  else: 
    #if it was a tie then print it was a tie
    print("""
      It was a tie!
      Player 1: rounds won - {}
      Player 2: rounds won - {}""".format(player1_points, player2_points))

  #ask if user wants to repeat
  rep = input("Do you want to repeat? Y for yes, N for no: ").upper()
  #if not then break
  if rep == 'N':
    break

    
