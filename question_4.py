##### find maximum of two numbers
#def maximum(a,b):
    #if a >= b:
        #return a
    #else:
        #return b
#a = 2
#b = 4
#print(maximum(a,b))


#### using max function
#b = 4
#a = 2
#maximum = max(a, b)
#print(maximum)


##### using ternary operator
#a = 2
#b = 4
#print(a if a >=b else b)



#### using lambda function
#x = 2
#y = 4
#maximum = lambda x,y :x if x >y else y
#print(f"{maximum(x,y)} is the maximum number")


#### using list comprihension
#a = 2
#b = 4
#x = [a if a>b else b]
#print(f"maximum no. is {x}")


#### USING SORT METHOD
a = 2
b = 4
x = [a,b]
x.sort()
print(x[-1])


