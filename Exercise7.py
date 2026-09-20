

#Blood donation eligibility

age=int(input("enter the your age :"))
weight=int(input("enter yor weight :"))
Hb=float(input("enter your Hb :"))

if age>=18 and age<=65:
    if weight>=50:

        if Hb>12.5:
            print("you can donate the blood")
        else:
            print("not eligible")
    else:
       print("not eligilble")

else:
    print("not eligible")

#student grade evaluater 

marks = int(input("enter your marks:"))

if 90<=marks<=100:
    print("grade: A+")

elif 80<=marks<=89:
    print("grade: A")

elif 70<=marks<=79:
    print("grade:B")

elif 60<=marks<=69:
    print("grade: C")

elif 50<=marks<=59:
    print("grade: D")

elif 0<=marks<=50:
    print("fail")

else:
    print("not valid marks")

#Electricity bill calucalator 

units = int(input("enter the number :"))

if units<=100:
    print("Total bill : ",units*5)

elif 101<=units>=200:
    print("Total bill : ",units*7)

elif 201<=units>=300:
    print("Total bill : ",units*10)

elif units>300:
    print("Total bill :",units*15)

#income tax calculator 

income= int(input("enter your income :"))

if income<=250000:
    print("no tax")

elif 250000<=income<=500000:
    print("tax:",income*(5/100))
elif 500001<=income<=1000000:
    print("tax :",income*(20/100))
elif income>1000000:
    print("tax :",income*(30/100))

#Temperture condition

temp = int(input("enter the tempratur :"))

if temp <0:
    print("freezing cold")
elif 0<=temp<=10:
    print("very cold")
elif 11<=temp<=20:
    print("cold")
elif 21<=temp<=30:
    print("warm")
elif 31<=temp<40:
    print("hot")
elif temp>40:
    print("extream heat")


#character clasifier

char = input("enter the character :")

if "a"<=char<="z":
    print("it's lowercase char")
elif "A"<=char<="Z":
    print("it's uppercase char")
elif "1"<=char<="9":
    print("is's number")
else:
    print("special character")



#university addmition system

a= int(input("enter the percentage ="))
b= int(input("enter entrace exam marks="))

if a>=90 and b>=90:
    print("Elite program")

elif a>=80 and b>=70:
    print("standard program")

elif a>=60 and b>=50:
    print("basic program")

else:
    print("not eligible")

#number cataegory analyzer

num = int(input("enter the number="))

if num>=0 and num%2==0:
    print("positive even")
elif num>=0 and num%2!=0:
    print("positive negative")
elif num<0 and num%2==0:
    print("negative Even ")
elif num<0 and num%2!=0:
    print("negative odd")
elif num==0:
    print("zero")

#shoping discount system

a = int(input("enter your purchace amount="))

if a<1000:
    print("no discount")
elif a>=1000 and a<=4999:
    print("total amount is =",a*(5/100))
elif a>=5000 and a<=9999:
    print("total amount is =", a*(10/100))
elif a>=10000 and a<=19999:
    print("total amount is =",a*(20/100))
elif a>=20000:
    print("total amount is =",a*(30/100))


#triagle type checker 

x = int(input("enter the angle="))
y =  int(input("enter the angle="))
z = int(input("enter the angle="))

if (x+y+z)==180:

    if x<90 or y<90 or z<90:
        print("triangle is acute angle tringle")

    if x>90 or y>90 z>90:
        print("triangle is abtuse angle tringle")

    else:
        print("invalid triangle")



