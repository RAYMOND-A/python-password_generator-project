import random
# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

# print(fruits)

# Average student height coding challenge

# student_heights = [180, 124, 165, 173, 189, 169, 146]

student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
total_students = 0

for student in range(0, len(student_heights)):
    total_students = total_students + student_heights[student]

print(total_students)

for height in student_heights:
    total_height += 1

print(total_height)

average_height = round(total_students/total_height)

print(f"The average height is {average_height}")


# Highest score coding challenge

student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = student_scores[0]
for score in student_scores:
    if score > max_score:
        max_score = score
        # print(f"The highest score in the class is : {max_score}")

print(f"The highest score in the class is : {max_score}")

# coding challenge printing the sum of all even integers from 1 to 100 using the range function and for loop

sum = 0

for even_number in range(0, 101, 2):
    sum += even_number

print(sum)

# fizzing buzz coding exercise
 
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    
print(number)

# Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '@', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-']

print("Welcome to the PyPassword Generator!")

letter_number = int(input("How many letters would you like in your password? \n"))
symbol_number = int(input("How many symbols would you like? \n"))
nr_number = int(input("How many numbers would you like? \n"))

# Easy level
final_letter = ''
for letter in range(0, letter_number):
    y = random.randint(1, len(letters))
    final_letter += letters[y] 
print(final_letter)

final_symbol = ''
for symbol in range(0, symbol_number):
    x = random.randint(1, len(symbols))
    final_symbol += symbols[x]
print(final_symbol)

final_number = ''
for number in range(0, nr_number):
    z = random.randint(1, len(numbers))
    final_number += numbers[z]
print(final_number)

print(f'easy level password is {final_letter}{final_number}{final_symbol}')


# Hard level

password_list = []

for char in range(0, nr_number):
    password_list += random.choice(numbers)
    # password_list.append(random.choice(numbers))

for char in range(0, letter_number):
    password_list += random.choice(letters)

for char in range(0, symbol_number):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ''

for char in password_list:
    password += char

print(f"Your password is : {password}")