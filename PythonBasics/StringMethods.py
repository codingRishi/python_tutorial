# from itertools import starmap
#
# a = "indiadiaindia"
# print(a.center(100,"*"))
# print(a.capitalize())
#
# print(a.index("a",5,8))
#
# print(a.split("d"))
# print(a.rfind("i"))
#
# print(a.count("dia"))
#
# b= "india800"
# print(b.casefold())
# print(b.upper())
# print(b.lower())
#
# print(b.endswith("IA"))
# print(b.isalpha())
# print(b.isprintable())
# help(str)
# #b.center("python",20, "*")
#
# input_ = "i am python programmer"
# splittedInput = input_.split(" ")
# for i in splittedInput:
#    # strOne = splittedInput[i]
#     print(i[0:1].upper()+i[1:], end=" ")
#
# strTwo = "\n{0}, How are you?{1} {ghg}"
# print(strTwo.format("pqr","abc", ghg="xyz"))
#
#
# fruits=['apple','mango','banana']
# for fruit in fruits:
#     print(fruit)
#
# for index in range(len(fruits)):
#     print(fruits[index])
#
# fruits.append('jackfuit')
#
# print(fruits)
#
# fruits.insert(0,'orange')
#
# print(fruits)
#
# popoeditem = fruits.pop(1)
#
# print(fruits)
# print(popoeditem)
#
# fruits.sort()
# print(fruits)
#
# listNum = [90, 45, 2, 300, 345,  560, 211]
# listNum.sort(reverse=True)
# print(listNum)

#help(list)

b=['abc','pqr','xyz']
print(b[0])
print(id(b))
b[0]='cvt'
print(b[0])
print(id(b))

a=('abc','pqr','xyz')
print(a[0])
print(id(a))
#a[0]='tuv'
print(a[0])
print(id(a))

Dict_test = {1:"abc", 2:"pqr",3:"xyz"}
print(Dict_test.keys())
print(Dict_test.values())
print(Dict_test)
Dict_test2 = dict({1:2})
print(Dict_test2)