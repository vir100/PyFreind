start=input("What is you Name:")
what_to_do=input(f"Hello {start},What can I do for you? \
    options: Play a game ,Do some Maths \n")
print(what_to_do)
if what_to_do=="play a game" or what_to_do== "Play a game":
    game=input("Ok what game do you want to play\
    options:Guess the number, Madlib or Snake water gun?\n")
    print(game)
    if game=="guess the number" or game=="Guess the game":
        numberToGuess = 45
        tries = 0
        currentGuess = 0
        def addTo(n):
            tries =  n + 1
            return tries
        print("I am thinking of a number between 1 and 100, guess it if you can! ")
        while currentGuess != numberToGuess:
            try:
                currentGuess = int(input("What is your guess?\n"))

                if currentGuess < 1 or currentGuess > 100:
                    tries = addTo(tries)
                    print("Your number should be between 1 and 100! ")
                elif currentGuess == numberToGuess:
                    tries = addTo(tries)
                    print(f"You got it correct!  My number was indeed {numberToGuess}!\nAnd it only took you {tries} times!")
                elif currentGuess < numberToGuess:
                    tries = addTo(tries)
                    print("The number I have in mind is HIGHER than that!")
                elif currentGuess > numberToGuess:
                    tries = addTo(tries)
                    print("Nope, I am thinking of a LOWER number than that!")
                else:
                    print("Try again!")

            except:
                tries = addTo(tries)
                print("You have to enter an integer!")
    if game=="madlib":
        print(f"Ok {start} lets play Madlib")
        adj=input("Adjective:")
        verb1=input("Verb1:")
        verb2=input("Verb2:")
        famous_person=input("Famous Person:")
        madlib=f"Computer programming is so {adj}! It makes me so extited all the time \
        I love to {verb1}. Stay hidrated and {verb2} like you are {famous_person}!"
        print(madlib)
    if game=="snake water gun":
            import random

    # Snake Water Gun or Rock Paper Scissors
    def gameWin(comp, you):
        # If two values are equal, declare a tie!
        if comp == you:
            return None

        # Check for all possibilities when computer chose s
        elif comp == 's':
            if you=='w':
                return False
            elif you=='g':
                return True
        
        # Check for all possibilities when computer chose w
        elif comp == 'w':
            if you=='g':
                return False
            elif you=='s':
                return True
        
        # Check for all possibilities when computer chose g
        elif comp == 'g':
            if you=='s':
                return False
            elif you=='w':
                return True

    print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
    randNo = random.randint(1, 3) 
    if randNo == 1:
        comp = 's'
    elif randNo == 2:
        comp = 'w'
    elif randNo == 3:
        comp = 'g'

    you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
    a = gameWin(comp, you)

    print(f"Computer chose {comp}")
    print(f"You chose {you}")

    if a == None:
        print("The game is a tie!")
    elif a:
        print("You Win!")
    else:
        print("You Lose!")
if what_to_do=="do some maths" or what_to_do=="Do some maths":
    print(f"Ok {start} i'll do that for you")
    print("Select an operation to perform")
    print("1.Add")
    print("2.Susract")
    print("3.Divide")
    print("4.Multiply")
    operation=input()
    if operation=="add" or operation=='1':
        num1=int(input("enter a number:"))
        num2=int(input("enter another number:"))
        print(num1+num2)
    elif operation=="Subtract" or operation=='2':
        num3=int(input("enter a number:"))
        num4=int(input("enter another number:"))
        print(num3-num4)
    elif operation=="divide" or operation=='3':
        num5=int(input("enter a number:"))
        num6=int(input("enter another number"))
        print(num5//num6)
    elif operation=="multiply" or operation=='4':
        num7=int(input("enter a nuber:"))
        num8=int(input("enter another number:"))
        print(num7*num8)
    else:
        print("Invalide entry")
