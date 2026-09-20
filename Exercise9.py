#quetion 1:

def max_num(x,y,z):

    if x>y and x>z:
        return x

    elif y>x and y>z:
        return y
    
    elif z>x and z>y:
        return z


x=int(input("enter num :"))
y=int(input("enter num :"))
z=int(input("enter num :"))

retval=max_num(x,y,z)
print(retval)

#Quetion 2:

def square(a):

    return a*a

a=int(input("enter the number:"))
retval=square(a)
print(retval)

#quetion 3:

def cube(a):
    return a*a*a

a=int(input("enter the number"))
retval=cube(a)
print(retval)

#quetion 4:

def sum_range(start,end):
    total=0

    while start <=end:
        total = total + 1
        start = start + 1
    return total

start = int(input("enter the number:"))
end = int(input("enter the number:"))

print("sum =",sum_range(start,end))



#quetion 5:

def average():
    total = 0
    i = 1

    while i<=5:
        marks = int(input("enter the marks:"))
        total = total + marks 
        i = i+1

    return total/5

aver = average()
print("average marks:",aver)


#quetion 6:


def product(n):
    result = 1
    i = 1

    while i<=n:
        result = result*i
        i = i+1

    return result

n = int(input("enter number:"))
print("product",product(n))

#quetion 7:

def factorial(n):
    fact = 1
    i = 1

    while i<=n:
        fact = fact *i
        i = i+1

    return fact

n = int(input("enter number"))
print("factorial is ",factorial(n))


#quetion 8:
def is_prime(n):
    if n<2:
        return False
    i = 2

    while i<n:
        if n%2==0:
            return False
        i = i +1

    return True

n = int(input("enter the number "))

if is_prime(n):
    print(n,"is a prime number ")
else:
    print(n,"is not a prime number")


#quetion 9:

def composit(n):
    if n<=1:
        return False
    i = 2

    while i<n:
        if n%i==0:
            return True
        i = i + 1

    return False

n = int(input("enter the number"))

if composit(n):
    print(n,"is a composite numaber")
else:
    print(n,"is not composite number")


#quetion 10:

def perfect(n):
    if n<=1:
        return False

    total = 0
    i = 1

    while i<n:
        if n%i==0:
            total = total +i
        i = i+1

    return total == n 

n = int(input("enter the number :"))

if perfect(n):
    print(n,"is a perfect number")
else:
    print(n,"is not perfect number")







