# Question 1: Arithmetic and Assignment Operators

# TODO: Add 3 to x using the += operator
number = 18
number += 3
print(number) 
# TODO: Multiply y by 2 using the *= operator
number2 = 6
number2 *= 2
print(number2)
# TODO: Divide x by y and store the result in a variable called 'result'
number = 18
number2 = 6
number /= number2
print(number)
# TODO: Print the value of 'result'
results= 3
print(results)
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators
a= 18
b= 6
c= 3
# TODO: Create a condition that checks if a is greater than b
a > b 
# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
b % c
# TODO: Create a condition that checks if c is less than or equal to a
c <= a 
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
finalcondition= (True)

# TODO: Print the value of 'final_condition'
print(finalcondition)
#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score = input ('please input tesst score ')
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
# Given score
score = 75
if 90 <= score <= 100:
    print('grade A')
elif 80 <= score <= 89:
    print('grade b') 
elif 70 <= score <= 79:
    print('grade c') 
elif 60 <= score <= 69:
    print('grade d')   
else :
    60 <= score 
    print('fail')
      

# TODO: Print the grade for the given score
score= 75
print(score)
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
input= print('please input two numbers' )
num1= 15
print(15)
num2= 25
print(25)
# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
input= print('please input operation' )
operation= ("+")
print("+")
# TODO: Use conditional statements to perform the chosen operation on num1 and num2
num1= 15
num2= 25
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2   
elif operation == "*":
    result = num1 * num2
else:
    operation == "/"
    result = num1 /  num2 

# TODO: Print the result of the operation
print('The result of addition is: 40')