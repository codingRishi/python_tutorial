from setuptools.command.saveopts import saveopts

a = """India"""
b = '"India"'
c = "'India'"

#NDI
print(a[1:4])
print(a[1:-1])
print(a[-4:-1])

#NDIA
print(a[1:5])
print(a[1:])
print(a[-4:])

#INDI
print(a[0:4])
print(a[0:-1])
print(a[-5:-1])

x="PROGRAM"


print(x[:-4])



strOne = "HELLO"

for i in strOne:
    print(i+i, end="")

print()

for index in range(len(strOne)):
    print(strOne[index]+ strOne[index], end="")

class employee():
    company="google"

    def __init__(self, name, id):
        self.name= name
        self.id=id

    def __getname__(self):
        self.name=name


e1=employee("r",11)
e2=employee("s",2)

print(e2.company)
print(e2.name)
