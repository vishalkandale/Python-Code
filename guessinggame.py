secret_word = "vishal"
guess = ""
i = 0
guess_of_count = 3

while guess != secret_word:
    if i < guess_of_count:
        guess = input("Guess my name: ")
        i += 1
    else:    
        print("You loss the game")
        break
    
else:
    print("You win the game")