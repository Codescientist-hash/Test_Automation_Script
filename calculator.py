def get_input():
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    return a,b

def sum(a,b):
    c = a+b
    return c

a,b = get_input()
c = sum(a,b)
print(c)

