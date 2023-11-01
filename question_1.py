num1 = 20
num2 = 30
sum = num1 +num2
print(sum)



##### user input
num1 = float(input("enter 1st number: "))
num2 = float(input("enter 2nd number: "))
sum = num1 + num2
print(f"the Sum of {num1} and {num2} is {sum}")



#####using operator.add method
import operator
num1 = 12
num2 = 15
sum = operator.add(num1,num2)
print(f"sum of {num1} and {num2} is {sum}")



#####using lambda function
add_numbers = lambda x,y : x+y
num1 = 1
num2 = 2
result = add_numbers(num1, num2)
print(f"sum of {num1} and {num2} is {result}")



##### using recursion 
def add_numbers_recursion(x,y):
    if y == 0:
        return x
    else:
        return add_numbers_recursion(x + 1, y - 1)

num1 = 3
num2 = 7
result = add_numbers_recursion(num1 ,num2) 
print(result)

