######################################################
#                                                    #
#  A simple program to simulate the flipping a coin  #
#                    multiple times.                 #
#                                                    #
######################################################

# Importing the random module, this will be used to 
# simulate a coin flip, random number between 1-2
import random

# Function for flipping coin x times
def flip_coins(number_of_flips): 
  # Variable to track the number of heads and tails
  number_of_heads = 0
  number_of_tails = 0

  # Loop number_of_flip times 
  for _ in range(number_of_flips):
    # Flip coin (Heads - 1, Tails - 2)
    flipped_coin = random.randint(1,2)
    # If flipped_coin was 1
    if flipped_coin == 1:
      # Increment heads counter by 1
      number_of_heads += 1
    # If flipped_coin was 2
    else:
      # Increment tails counter by 1
      number_of_tails += 1
  
  # If number_of_flips was greater than 1,
  if number_of_flips > 1:
    # Print number of heads Vs number of tails
    print("Number of heads: ", number_of_heads)
    print("Number of tails: ", number_of_tails)
  else:
    # If the coin was only flipped once 
    if number_of_heads == 1:
      # Print heads
      print("It was heads")
    else:
      # Print tails
      print("It was tails")

# Set to 1 for a head/tails tool
# Set to anyhing greater than 1 to calculate the probability
times_to_flip = 10

# Run the simulation
flip_coins(times_to_flip)
