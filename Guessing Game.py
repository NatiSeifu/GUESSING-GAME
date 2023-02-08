#Nati Seifu
#09/23/2022
#Create a well-functioning guessing game


try: #Creating a New File si no existe
    with open("HighscoresForGuess_Nati.txt", "r+") as f:
            f.read().splitlines()
except:
    with open("HighScoresForGuess_Nati.txt", "w+") as f:
              f.write ("0 A Weakling\n")
        

def game():
    from random import randint
    import sys
    

    correctans = randint(2,99) #Draw random integer

    '''print (correctans, "\n") #Print the correct answer if necessary'''
    

    b = 4 #"Number of Attempts Left" variable

    n = ('\nWhat number between 1 and 100 am I thinking of? You get 5 guesses.\n') #Defining messages for the inputs

    print ('\nWell well, who do we have here? You think you can test my honor? No! I am the king of the unguessables! Before we start...what is your name?')    

    while True:
        names = input() #name has to be a non-numeric string (no standalone numbers)
        
        if names.isnumeric() != True:
           break
        else:
           print ('\nUnless you are an inmate in the discriminatory and profit-based judicial/incarceration system in the United States, your name is probably not a number...Put in a legible name!') 

    if names == 'Daniel':

        print ('\nOh, no! It\'s you...You...you are here to judge my whole construct aren\'t you??! I will not be fazed though. Now, tell me this...\n')

    elif names == 'daniel':

        print ('\nOh, no! It\'s you...You...you are here to judge my whole construct aren\'t you??! I will not be fazed though. Now, tell me this...\n')
    elif names == 'Nati':
        print ('\nAh! You share names with my father! You must be a special one. Now, tell me...\n')

    else:
        print ('\nGood, good...', names + '.', 'Now, answer this...\n')
    
    while True:
        userinput = input(n) #user's guess has to be numeric (standalone number)
        
        if userinput.isnumeric() == True:
           break
        else:
           print ('I said, "What,', "\u0332".join('NUMBER') + '..."', 'Put in a number this time!') 

    userinput = int(userinput)

      
    if userinput == correctans and b == 4: #If the user's input is correct on the first try...
        print ("CORRECT ON THE FIRST?!?! YOU SLY DOG! WOOF WOOF!")
        



    while correctans != userinput and b >= 0: #While the user's input is wrong...
        if userinput > correctans:
            if b > 1: 
                print ("\nYOU THOUGHT! HAHA! Try again, number is too high. You have", b, "chances left.")
            if b == 1:
                print ("\nLAST CHANCE BEFORE YOU LEAVE IN SHAME! Number is too high!")
            if b < 1:
                print ("\nYou...crumbled...when it mattered. What would your parents think of you? ZERO chances left! On second thought...Maybe I will give you one more chance...Go again")
            while True:
                userinput = input()
                
                if userinput.isnumeric() == True:
                   break
                else:
                   print ('I said, "What,', "\u0332".join('NUMBER') + '..."', 'Put in a number!')
            userinput = int(userinput)
            b = b-1
        if userinput < correctans:
            if b > 1: 
                print ("\nYOU THOUGHT! HAHA! Try again, number is too low. You have", b, "chances left.")
            if b == 1:
                print ("\nLAST CHANCE BEFORE YOU LEAVE IN SHAME! Number is too low!")
            if b < 1:
                print ("\nYou...crumbled...when it mattered. What would your parents think of you? ZERO chances left! Actually, when I think about it...Maybe you deserve another chance...Go again.")
            while True:
                userinput = input()
                
                if userinput.isnumeric() == True:
                   break
                else:
                   print ('I said, "What,', "\u0332".join('NUMBER') + '..."', 'Put in a number!')
            userinput = int(userinput)
            b = b-1

    if userinput == correctans and b<4: #If the user's input is correct on attempts following the first one...
        print ("CORRECT! You ain't special doe.")



     # Dealing with the scores and displaying them

    PlayerScore = b+1

    if userinput!= correctans:
        print ('\n'+ "HAHA SIKE! Who do you think you are? Why would you deserve an extra chance! Nonsense! But here is your score if you want it:", PlayerScore, '\n') # Finding the score after fail and printing it. The score is the number of chances left plus one.


    if userinput == correctans:
        print ('You won the game in', 5-b, 'tries!')
        print ('\n'+ "Your score is:", PlayerScore, '\n')


        
    # Dealing with the high score file.

    
    with open ("HighscoresForGuess_Nati.txt", "a+") as f:
       f.writelines(str(PlayerScore)+ ' ' + names + '\n')
        
    with open ("HighscoresForGuess_Nati.txt", "r+") as f:
        listread = f.read().splitlines()
        listread.sort(reverse=True)
        for dodoTheGreatTutor in listread[0:3]: #shoutout to Noel for helping out with this part
            print (dodoTheGreatTutor)

    # Play Again?
    
    userinput1 = input('\nSo, would you like to play again? Press "Y" if yes. Press "N" if no.\n')

    if userinput1 == 'Y':
        return game()
    elif userinput1 == 'N':
        print ("Bye then!")
        return sys.exit()




        
        
game()

    
                      
