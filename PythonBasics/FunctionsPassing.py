import sys

#Position
def add(a,b):
    print(a+b)

add(2,4)

#Keyword
def students(name, age):
    print(name, age+4)

students(age = 34, name="abc")

#default
def car(color, tyres, powerstaring=0):
    print(color, tyres, powerstaring)

car("red", 4, 7864)
car("yellow",43)

#optional parameter
#*args
def students_1(name, *args):
    print(name, args)

students_1("abc", 1234568, "bike")
students_1("pqr")
students_1("xyz", 000)

#**kwargs
def students_2(**kwargs):
    print(kwargs)

students_2(name="abc", mobile =1234, rollNo="abc1233")

def sumNumber(n):
    sum =0
    while(n!=0):
        sum = sum + n
        print(sum)
        n=n-1


def sumNousingFor(n):
    if(n==0):
        return 0

    sum = n + sumNousingFor(n - 1)

    return sum

print(sumNousingFor(5))


