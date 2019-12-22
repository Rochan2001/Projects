import random

class RPS:
    def __init__(self):
        pass
    def computer_choice(self):
        c = random.randint(1,3)
        return c
    def play(self):
        while(1):
            temp = input("Press S to start the game : ")
            if temp=='S':
                c = int(input("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n"))
                if c==1:
                    print("You have selected Rock")
                    u_choice='rock'
                elif c==2:
                    print("you have selected Papers")
                    u_choice='papers'
                elif c==3:
                    print("You have selected scissors")
                    u_choice='scissors'
            print("Computers turn to pick a choice...")
            comp = RPS.computer_choice(RPS)
            if comp == 1:
                print("Computer has selected rock")
                c_choice='rock'
            elif comp == 2:
                print("Comuter has selected papers")
                c_choice='papers'
            elif comp == 3:
                print("Computer has selected scissors")
                c_choice='scissors'
            print( u_choice + " V/s " + c_choice)
            if((c== 1 and comp == 2) or(c == 2 and comp ==1 )): 
                print("paper wins => ", end = "") 
                result = "paper"
          
            elif((c == 1 and comp == 3) or(c == 3 and comp== 1)): 
                print("Rock wins =>", end = "") 
                result = "Rock"
            else: 
                print("scissor wins =>", end = "") 
                result = "scissor" 
            if result == c: 
                print("<== User wins ==>") 
            else: 
                print("<== Computer wins ==>") 
          
            print("Do you want to play again? (Y/N)") 
            ans = input()  
            if ans == 'n' or ans == 'N': 
                break

game = RPS()
game.play()
