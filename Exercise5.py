

#program1

num1=int(input("enter no.:"))
num2=int(input("enter no.:"))

if num1>num2:
    print(num1)

else:
    print(num2)

#program2

x = int(input("enter the number :"))

if x>0:
    print("positive",x)

elif x==0:
    print("zero",x)

else:
    print("negative",x)

#program3

x = int(input("Number:"))
if x%2==0:
    print("entered number is even")

else:
    print("entered number is odd")

#program4

num1= int(input("Enter No.:"))

if num1%5==0:
    print("divisible by 5")

else:
    print("not divisible by 5")

#program5

x=int(input("enter weekend number :"))

if x==0:
    print("monday")
elif x==1:
    print("tuesday")
elif x==2:
    print("wednesday")
elif x==3:
    print("thirsday")
elif x==4:
    print("friday")
elif x==5:
    print("satarday")
elif x==6:
    print("sunday")
else:
    print("not weekend day at this number")

#program6

x = (input("Enter the character :"))

if x>="A" and x<="Z":
    print("entered character is capital alphabet")

elif x>="a" and x<="z":
    print("entered character is small alpabet")

else:
    print("is not alphabet")


#program7

M = int(input("enter the month number:"))

if M==1:
    print("january is 31 days")

elif M==2:
    print("feb is 30 days")

elif M==3:
    print("march is 31 days")

elif M==4:
    print("april is 30 days")

elif M==5:
    print("may is 31 days")

elif M==6:
    print("june is 30 days")

elif M==7:
    print("jully is 31 days")

elif M==8:
    print("agust is 31 days ")

elif M==9:
    print("saptember is 30 days")

elif M==10:
    print("oct is 31 days")

elif M==11:
    print("nov is 30 days")

elif M==12:
    print("dec is 31 days")


#program8

x = int(input("enter the number :"))

if x>10:
    print("greater the 10")
else:
    print("not greter then 10")


#program9

char=input("enter the character:")

if char=="a" or char=="A":
    print("vowel")

elif char=="i" or char=="I":
    print("vowel")

elif char=="o" or char=="O":
    print("vowel")

elif char=="u" or char=="U":
    print("vowel")

elif char=="e" or char=="E":
    print("vowel")

else:
    print("consonant")


#program10

year=int(input("enter the year:"))

if year%4==0 or year%100!=0:
    print("entered year is leap year ")

else:
    print("no leap year")






