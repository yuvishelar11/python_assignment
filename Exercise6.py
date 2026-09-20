#program1
x = int(input("enter the number:"))

if x%4==0 and x%5==0:
    print(x,"is divisible by 4 and 5 ")

else:
    print(x,"is not divisible by 4 and 5")
#program 2

a = int(input("enter the angle:"))
b = int(input("enter the angle:"))
c = int(input("enter the angle:"))

if (a+b+c)==180 and (a==90 or b==90 or c==90):
    print("given entered angle is right angle triangle")

else:
    print("given entred agles is not right angle triangle")

#program3

a = int(input("Number :"))
b = int(input("Number :"))

sum = a+b 
if sum%2==0:
    print(sum)

else:
    print("no output")


#program4

list1=[10,20,30,40,50]
num=int(input("enter the number"))

if num in list1:
    print("available")

else:
    print("not available")


#program5

x = int(input("enter the number "))

if x%2==0:
    print("core2web\n"*x)
else:
    print("no output")


#program6

a = int(input("enter the number :"))

if a%2!=0:
    print("ODD")
else:
    print("no output")

#program7

x = int(input("Number enter here:"))
y = int(input("Number enter here:"))

if x%2!=0 and y%2!=0:
    print(x+y)
else:
    print("no output")

#program8

char = input("enter character ")

N = ord(char)
if N%2==0:
    print(char)

else:
    print("Odd")

#program9

char1= input("char1")
char2= input("char2")
ch1=ord(char1)
ch2=ord(char2)

if ch1%2!=0 and ch2%2!=0:
    print("sum=",ch1+ch2)

else:
    print("sum is odd")

#program10

user = int(input("enter the number"))
if user%8==3:
    print(user)

else:
    print(user%8)

