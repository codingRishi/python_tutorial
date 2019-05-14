import re

x = "This is python"
match_result = re.match("is", x, re.IGNORECASE)

if match_result:
    print(match_result.group())
else:
    print("Pattern not found")

y = "This is good day"
search_obj= re.search("bad*", y, re.IGNORECASE)
if search_obj:
    print(search_obj.group())
else:
    print("Pattern not found")

z="Lets conclude Lets basic regular Lets exp"
findall_Obj = re.findall("Lets", z, re.IGNORECASE)
if findall_Obj:
    print(findall_Obj)
else:
    print("Pattern not pattern")


a = "Th.s is it"
a_obj = re.search("h.s", a, re.I)
print(a_obj.group())

u = "This is phone number : 105123 4"
print(re.search("10.*"
                "",u, re.IGNORECASE).group())


c = "A1223BH567JK!@#$%"
print((re.findall("[a-zA-Z0-9]  ",c,re.I)))