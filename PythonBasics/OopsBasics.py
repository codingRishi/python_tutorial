
class calculator():


    def toAdd(self, lhs, rhs):
        self.lhs= lhs
        self.rhs = rhs
        #print("in Addition : " + str(self.lhs+self.rhs))
        return self.lhs+self.rhs

    def toSub(self):
        print("in Sub")

obj1 = calculator()
obj2 = calculator()

print(obj1.toAdd(1,3))
print(obj2.toAdd(9,0))


class Tables():

    def displayTable(self, no, upto):
       # for i in range(0, upto, no):
        #    print(i)
        for i in range(0, upto):
            print(str(i*no))

table1 = Tables()
table1.displayTable(7,20)
table1.displayTable(4,10)
