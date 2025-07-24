def get_input():
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    return a,b

#Adding two numbers
def sum(a,b):
    c = a+b
    return c

#Subtracting two numbers
def sub(a,b):
    d = a-b
    return d

a,b = get_input()
c = sum(a,b)
print("Sum of a,b is",c)
d = sub(a,b)
print("Difference of a,b is",d)

