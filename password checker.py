secret_word = "sid"
guess = ""
guess_limit = 0

while guess != secret_word and guess_limit <= 3:
    guess = input("\n\nEnter the password:  ")
    guess_limit += 1
    if guess == secret_word:
        print("you got it right")
    elif guess_limit == 3:
        print("You are out of tries, try again later!")
        break
