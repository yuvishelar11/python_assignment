
#quetion 1:

def table(n):
    for i in range(1,11):
        print(n*i)

n = int(input("Enter number for table:"))

table(n)

#quetion 2:

def number_id(n):
    if n%2==0:
        print("given no. is even")

    else:
        print("given number is odd")

n = int(input("entre the number="))

number_id(n)

#quetion 3:

def votting(age):
    if age>=18:
        print("you can eligible for votting")

    else:
        print("you not eligible for votting")

age = int(input("enter your age :"))

votting(age)


#quetion 4:

def arithmatic(x,y):

    print("addition",x+y)
    print("substraction",x-y)
    print("multiplication",x*y)
    print("division",x/y)
    print("modulus",x%y)
    print("flor divition",x//y)

x = int(input("enter num1:"))
y = int(input("enter num2:"))

arithmatic(x,y)

#quetion 5:

def char(char):
    if char=="A" or char=="a":
        print("it is vowel")
    elif char=="E" or char=="e":
        print("it is vowel")
    elif char=="I" or char=="i":
        print("it is vowel")
    elif char=="O" or char=="o":
        print("it is vowel")
    elif char=="U" or char=="u":
        print("it is vowel")
    else:
        print("it is consonant")

c = input("enter the character =")
char(c)

#quetion 6:
def asci_value(char):
    print("ASCII value of ",char,"is",ord(char))

a=input("enter the character :")
asci_value(a)

#quetion 7:

def max_num(x,y):
    if x>y:
        print("greater number is ",x)
    else:
        print("greater number is ",y)

x=int(input("enter the number="))
y=int(input("enter the number="))

max_num(x,y)

#quetion 8:

def student_details(name,age,cource):
    print(name)
    print(age)
    print(cource)

a=input("enter the name:")
b=int(input("enter the age:"))
c=input("enter the cource:")

student_details(a,b,c)


#quetion 9:
def average(*value):
    sum=0
    for i in value:
        sum=sum+i
    print(sum)    
average(1,2,3,4,5)

'''
ans= "hello,i'am the inner function"
'''
#quetion 10:

def area(r):
    area=(2*3.14*r*r)
    return area

r = int(input("enter the radius:"))
retval=area(r)
print("radius",r)
print("area of circle ",retval)



