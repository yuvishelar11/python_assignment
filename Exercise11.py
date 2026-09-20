#Quetion no:1

rows = int(input("enter the no. of row = "))

for i in range(1,rows+1):
    for j in range(1,rows+1):
        print(2*j-1,end="   ")

    print()

#Quetion no:2

rows = int(input("enter the no. of rows ="))

for i in range(1,rows+1):
    for j in range(1,rows+1):
        print(i+2*(j-1),end="  ")
    print()

#Quetion no:3

rows = int(input("enter the no. of rows ="))

for i in range(rows):
    num = 1 + (i*4)
    for j in range(4):
        print(num,end=" \t ")
        num+= 2
    print()


#quetion 4:
rows = int(input("enter the rows ="))

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j, end="  ")
    print()


#Quetion 5:

rows = int(input("enter the number="))

for i in range(1,rows + 1):
    for j in range(rows, rows-i,-1):
        print(j, end=" ")
    print()

#quetion 6:

rows = int(input("enter the number ="))

for i in range(rows, 0,-1):
    for j in range(i,0,-1):
        print(j,end="  ")
    print()



#quetion 7:


rows = int(input("enter the row ="))

for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()


#Quetion 8:

row = int(input("enter the row ="))

for i in range(row ,0,-1):
    for j in range(row,row-i,-1):
        print(j,end="  ")
    print()


#Quetion 9:

row = int(input("enter the rows ="))

for i in range(1, row +1):
    for j in range(i):
        print(i,end="  ")
    print()

#Quetion 10:

row = int(input("enter the rows"))

for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end="  ")

    for j in range(i-1,0,-1):
        print(j,end="  ")
    print()

#Quetion 11:

rows = int(input("enter the rows"))

for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

