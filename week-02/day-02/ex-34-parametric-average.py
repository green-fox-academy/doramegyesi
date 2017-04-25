# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
# Sum: 22, Average: 4.4

number = int(input("A number is needed: "))
list_of_numbers = []

for n in range(number):
    n = int(input("Give me another number! "))
    list_of_numbers.append(n)

print("Sum: ", sum(list_of_numbers), " Average: ", sum(list_of_numbers)/number)
