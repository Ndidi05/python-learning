# Write a simple Python program that takes a person's name as input and greets them. 
# Write a simple Python program that takes a person's name and age as input. 
# Then welcome the page and their age plus 20 
# Hint: Make sure all the collected input is stored as a variable. 
# Any little computation should be stored as a variable

name = 'Deborah'
print('Hello', name)

name = input("Enter your name: ")
greeting = ("Hi," + name)
print (greeting)

name = input("Enter your name: ")
age = int (input("Enter your age: ")) + 20
print(age)
print('welcome ' +  name,  'you are now '  +  str (age), 'years of old')


# Write a Python script that prompts for a student's name and last exam grade. 
# Add 50 to their score, and divide their score by 4. Save the result. 
# Then print their name and their result

student_name = input('Enter your name: ')
grade = float (input('Enter your score: '))
final_grade = (grade + 50)/4
result = final_grade
print(student_name)
print(result)

