num1 = input('Enter First Number: ')
num2 = input('Enter Second Number: ')
print("Value of number1 before swapping: ", num1)
print("Value of number2 before swapping: ", num2)
temp = num1
num1 = num2
num2 = temp

print("Value of number1 after swapping: ", num1)
print("Value of number2 after swapping: ", num2)
#another approach for swapping number with add,substarction
num1=num1+num2
num2=num1-num2
num1=num1-num2
#another approach with operator and temp variable
num1,num2=num2,num1

print("Value of number1 after swapping: ", num1)
print("Value of number2 after swapping: ", num2)
