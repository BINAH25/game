def game():
    import random
    choices = ['R','P','S']
    computer = random.choice(choices)
    player = None
    print("### starting game ###")
    player = input("enter R, P OR S \n").upper()

    for i in player:
        if i in choices:
            if player == computer:
                print("computer: ", computer)
                print("player: ", player)
                print("it is tie")
                game()
            elif player == "R":
                if computer == "P":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("computer win")
                if computer == "S":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("Congratulation you win")

            elif player == "P":
                if computer == "S":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("computer win")
                if computer == "R":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("Congratulation you win")
            
            elif player == "S":
                if computer == "R":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("computer win")
                if computer == "P":
                    print("computer: ", computer)
                    print("player: ", player)
                print("Congratulation you win")
        else:
            print("INVALID LETTER ENTERED")        
            game()
game()
