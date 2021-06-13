print('''

 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("Choose between going to the right or left: ").lower()
if direction == "left":
  choice = input("Now you gotta choose if you will swim through the river or wait for a boat: ").lower()
  if choice == "wait":
    door = input("Choose a door. You must go through one of them. Write a primary color: ").lower()
    if door == "yellow":
      print("You've found the treasure, you win! Congratulations!!!!!!!!!!")
    elif door == "red":
      print("You've been burned by fire. Game Over.")
    elif door == "blue":
      print("You've been eaten by beasts. Game Over.")
    else:
      print("Game Over.")
  else:
    print("You've been attacked by a trout. LOL. Game Over.") 
else:
  print("Oh oh, you just lost, you've been eaten by sharks or fallen into a hole I don't know bro... Game Over.")
  