# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
# The stored number is higher
# The stored number is lower
# You found the number: 8

stored_number = 5
guessed_number = int(input("Guess my number! "))

while stored_number != guessed_number:
    if stored_number < guessed_number:
        print("The number I thought of is lower!")
        guessed_number = int(input("Guess my number! "))
    elif stored_number > guessed_number:
        print("The number I thought of is bigger!")
        guessed_number = int(input("Guess my number! "))
else:
    print("You found the number: ", stored_number)
