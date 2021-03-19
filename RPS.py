import random

while True:
        RPS = ["rock", "paper", "scissors"]
        p = input("\033[1m"+"\033[36m"+"Rock, Paper or Scissors: ")
        if p.lower() in RPS:

            computer_turn = random.choice(RPS)
            print("\033[35m"+"You Played: "+"\033[37m"+p.lower()+"\033[35m"+"\nComputer Played: "+"\033[37m"+computer_turn)
            if computer_turn == p.lower():
                print("\033[1m"+"\033[37m"+"tie")
            elif computer_turn == "rock":
                if p.lower() == "paper":
                    print("\033[1m"+"\033[32m"+"Win")
                else:
                    print("\033[1m"+"\033[31m"+"Lose")
            elif computer_turn == "paper":
                if p.lower() == "scissors":
                    print("\033[1m"+"\033[32m"+"Win")
                else:
                    print("\033[1m"+"\033[31m"+"Lose")
            elif computer_turn == "scissors":
                if p.lower() == "rock":
                    print("\033[1m"+"\033[32m"+"Win")
                else:
                    print("\033[1m"+"\033[31m"+"Lose")
            else:
                print("nothing")
        else:
            print("Chaleja BSDK")
        a = input("\033[33m"+"Would u like to Play Again(y/n) --> ")
        if a.lower() != "y":
            break