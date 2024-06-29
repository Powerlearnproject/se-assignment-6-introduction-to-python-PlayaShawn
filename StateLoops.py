#If-els statement
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


#For loop
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


#Combining if-else and for loop
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")