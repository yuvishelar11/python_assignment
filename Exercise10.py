#quetion 1:

area=lambda side:side*side
side=float(input("enter the side"))

print(area(side))

#quetion 2:

num = float(input("enter the side"))

cube = lambda x: x*x*x

print(cube(side))

#quetion 3:

num1 = float(input("enter the num1:"))
num2 = float(input("enter the num2 :"))

maximum = lambda x,y : x if x>y else y

print(maximum(num1,num2))

#quetion 4:


lenght = float(input("enter the lenght:"))
widht = float(input("enter the widht:"))

area = lambda l,w: l*w

print(area(lenght,widht))


#quetion 5:

c = float(input("enter the temperature :"))

f = lambda c: (c*9/5)+32

print("temperature in farenhite ",f(c))


#quetion 6:

f = float(input("enter the tenperature :"))

c = lambda f: (f-32)*5/9

print("tenperature in celcius :",c(f))

#quetion 7:

num = int(input("enter the number :"))
last_no= lambda n: abs(n)%10
print("last digit",last_no(num))


#quetion 8:

lenght = float(input("enter the lenght"))

parameter = lambda l : 4*l

print(parameter(lenght))


#quetion 9:

string= input("enter the string")

check= lambda s: 'a' in s

print("contain 'a'",check(string))

#quetion 10:


year = int(input("enter the year:"))

leap_year = lambda y : (y%400==0) or (y%4==0 and y%100 !=0)

print("leap year :",leap_year(year))




