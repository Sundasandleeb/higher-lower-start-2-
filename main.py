import random
from art import logo

print(logo)
from game_data import data
score =0
game_continue = True
y = random.choice(data)
while game_continue:
  
  x = y
  y =  random.choice(data)
  
  print(f"Compare A: {x['name']} , a {x['description']} , from {x['country']}")
  
  
  from art import vs
  print(vs)
  print(f"Against B: {y['name']} , a {y['description']} , from {y['country']}")
  def check_answer(guess, a_follower, b_follower):
    
    if a_follower > b_follower:
      
      return guess == "a"
  
    else:
      
      return guess == "b"
  
  a_follower_count = x["follower_count"]
  b_follower_count = y["follower_count"]
  
  
  guess = input("Enter your guess. A or B").lower()
  is_correct=check_answer(guess, a_follower_count, b_follower_count)

  if is_correct:
    score+=1
    print(f"Your guess is right, and score is {score}")
  else:
    game_continue = False
    print (f"Sorry guess is wrong, and score is {score}")
game_continue()