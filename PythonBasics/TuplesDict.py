listOne = ["abc","def","ghi"]
print(id(listOne))
listOne[0]="tuv"
print(listOne)
print(id(listOne))
tupleOne = ("abc", "def","ghi")
print(id(tupleOne))
tupleOne = ("xyz","ijk")
print((tupleOne))

a = "india"
a ="y"
print(a)

Dict_One = {1:"ind", "country":"usa", 3:["sri","nz","bang"]}
Dict_One[4]="test"
print(Dict_One)
Dict_Two = dict({1:"ind","country":"usa"})
listtest = Dict_One[3]
print(listtest[1])
print("keys " + str( Dict_One.keys()))
print("Vaues " + str(Dict_One.values()))
print(Dict_One.pop("country"))
print("Dict after Pop " + str(Dict_One))
print(Dict_One.get(3))
Dict_One.clear()
print(Dict_One)

Dict_Three = {"a":"Hi", "b":"There"}
thirdKey=""
thirdValue=""

for i in  Dict_Three.keys():
    print(i)
    thirdKey=thirdKey+i
    print(thirdKey)
for j in Dict_Three.values():
    print(j)
    thirdValue=thirdValue+j
    print(thirdValue)
Dict_Three[thirdKey]=thirdValue
print(Dict_Three)






