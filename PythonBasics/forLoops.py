i =4
j =3.4
k = 3+7j

str1 = "INDIA"
str2= 'India'

#While loop
while(i<6):
    print("This is while loop")
    i=i+1



#for a in range(10, 13):
   # print("Value of a : " + str(a) + " Value of i : " + str(i) +" Their additions : " + str(a+i))

sum=0
for a in range(10, 0, -2):
   # print(a)
    sum = sum+a

print(sum)

countI=0
index=-1
for x in "INDIAISINDIANCOUNTRY":
    index=index+1
    if (x=="I" or x=="i"):
        countI=countI+1
        print("Position of I : " + str(index))

print("Number of Is : " + str(countI))

userName, City = input("Enter your name, city  : ").split()
print("Hi, " + userName + " How are you! You live in : " + City)