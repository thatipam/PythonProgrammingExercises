class Parent:
    def __init__(self, fname, lname, id):
        self.fname = fname
        self.lname = lname
        self.id = id
        
    def display(self):
        print(" Info: {} {} {}".format(self.id, self.fname, self.lname))
        
    def __str__(self):
        return ("{} {} {}".format(self.id, self.fname, self.lname))
    

class Child(Parent):
    def __init__(self, fname, lname, id, relation):
        super().__init__(fname, lname, id)
        self.relation = relation
    
    def __str__(self):
        return ("{} {} {}. Relation: {}".format(self.id, self.fname, self.lname, self.relation))
        


p1 = Parent('Goutam', 'Vedanthi', 100)
p2 = Parent('Srikali', 'Vedanthi', 101)

c1 = Child('Sumedh', 'Vedanthi', 103, 'Son')

print(p1)
print(p2)
print(c1)