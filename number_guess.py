
import random
# Asks for players name
name = input("What is your name? ")
# Greets player with their name
print("Hello", name, "Goodluck and have fun")

number = random.randint(0,10) # returns a random int in the range of 0-10


guesses = 0
# Creates the loop for player can keep trying without rerunning the code over and over again
while guesses != 1:
    # Ask's the user for there guess
    guess = int(input("What's your guess?: "))
# If the guess is correct it + 1 to guesses
    if guess == number:
        guesses += 1
    # If the guess is incorrect it says try again then gives a hint
    elif guess != number:
        print("Try Again")
        # gives a hint if the guess is wrong
        if guess < number:
            print("Hint the number is higher!")
        elif guess > number:
            print("Hint the number is lower!")
    # If guesses is 1 then it tells you, you won and tells you what the number was
    if guesses == 1:
        print("You Win!")
        print("The number was", number)
        break