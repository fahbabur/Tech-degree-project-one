# imports for picking random number
import random

#creating the list of numbers for 1 to 10

numberrange = range(1, 11)
numberlist = list(numberrange)

#instruction function for the game

def instructions():
  print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

  print("Wecome to the Annual numbers Game where you get to guess the number\n".upper())

  print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

  print("a number between 1-10 has been chosen randomly,your mission is to guess which number\n""".upper())


#main function for the game

def main():
  numberlist = list(numberrange)

  pickednumber = random.choice(numberrange)
  
  count = 0
  
  instructions()
  
  
  
  
  
  while (True):
    try:
      print()
      
      print("Pick from {} \n".format(numberlist))
      print()
      print("you have {} made attempts".format(count).upper())
      print()
      
      number = int(input("what number do you think it is ==>   ".upper()))
      
      print()
      
      
      
      
        
      
    except ValueError:
      print("Oop thats not a number, try again".upper())
    
    else:
      
      
      if number == pickednumber:
        print("well done you guess the correct Number : {}\n ".format(number).upper())
        print("!!!!you win!!!!".upper())
        break
		
        
      elif number > 10 or number < 0:
        print("the number you choose is outside of the range, please try again".upper())
        continue
		
      
      elif number not in numberlist:
        print("you have already picked this number, try another".upper())
        
        
      elif number > pickednumber:
        print("nice try, you need to guess lower, try again")
        numberlist.remove(number)
        count += 1
        continue
		
		
      elif number < pickednumber:
        print("nice try, you need to guess higher, try again")
        numberlist.remove(number)
        count += 1
        continue
        
      

  
  print()
  
  print("it took you {} Attempts".format(count).upper())
  print()
  print("++++++++++++++++++++++++++++")
  print()
  print("thank you for participating".upper())
  print()
  print("++++++++++++++++++++++++++++\n")
  
main()

# while loop so players can play again if the choose to

while True:
  answered = input("would you like to play again? Y or N ==>   ".lower())
  if answered == "y":
    main()
  else:
    print("+++++++++++++++++++++++++++++++++++++++++++++++\n")
    print("    goodbye and thank you for playing\n".upper())
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    break

