### TASK 1
## You are going to get input from a student. 
# And then tell them their class of grade. 
# Ensure that you are able to filter out wrong input
#3.5- 4.00 – First Class Honours
#3.0-3.49 – Second Class Honours (Upper Division)
#2.0-2.99 – Second Class Honours (Lower Division)
#1.0-1.99 – Third Class Honours

grade = float (input('Enter your grade: '))
#submitted_project = False  #bool(input('Have you submitted your project: '))
if grade >= 3.5 and grade <= 4.0:
    print("First Class Honours")
elif grade >= 3.0 and grade <= 3.49:
    print("Second Class Honours (Upper Division)")
elif grade >= 2.0 and grade <= 2.99:
    print("Second Class Honours (Lower Division)")
elif grade >= 1.0 and grade <= 1.99:
    print("Third Class Honours")
else:
    print("Wrong input")


### task 2 - Write a Python program that iterates through integers from 1 to 100. 
# For each multiple of three, print "Fizz" instead of the number; 
# for each multiple of five, print "Buzz". 
# For numbers that are multiples of both three and five, print "FizzBuzz".

numbers = [1, 101]
for number in numbers:
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)


