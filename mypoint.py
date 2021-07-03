class Point:
    a = 0
    b = 0
    numberOfPoints = 0
    def __init__(self, x = 0, y =0):
        self.x = x
        self.y = y
        Point.numberOfPoints +=1
        
    def changeClassVars(self):
        Point.a = 10
        Point.b = 12
        
    def displayPoint(self):
        print("X = {}, Y = {}".format(self.x, self.y))
        
    #def __str__(self):
        #return "X = {}, Y = {}".format(self.x, self.y)
    
    def __repr__(self):
        return "({},{})".format(self.x, self.y)
    
    
def maker(n):
    def make(m):
        return n**m
    return make
