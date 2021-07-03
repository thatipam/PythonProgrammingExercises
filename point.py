import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y, color="red", size=10):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        
    def __add__(self, other):
        if isinstance(other, Point):
            x = self.x + other.x
            y = self.y + other.y
            return Point(x,y)
        else:
            x = self.x + other
            y = self.y + other
            return Point(x,y)

    def plot(self):
        plt.scatter(self.x, self.y, c=self.color, s=self.size)
  
"""
if __name__ == "__main__":
    a = Point(1,3)
    b = Point(2,4)
    c = a + b
    c.plot()
    plt.show()
"""
"""
import matplotlib.pyplot as plt

x1, y1 = [-1, 12], [1, 4]
x2, y2 = [1, 10], [3, 2]
x3 = 1
y3 = 3
x4 = 8
y4 = 10
plt.plot(x3, y3, x4, y4, marker = 'o')
x = [1, 8]
y = [3, 10]
plt.plot(x, y)


#plt.plot(x1, y1, x2, y2, marker = 'o')
plt.show()"""
import matplotlib.pyplot as plt
point1 = (1, 2)
point2 = (3, 4)

x = [point1[0], point2[0]]
y = [point1[1], point2[1]]

plt.plot(x, y, color='green', marker='o', linewidth=2, markersize = 20)
x = [5, 8]
y = [7, point2[1]]

plt.plot(x, y, 'go--', linewidth=2, markersize = 12)

#plt.plot([1, 2, 3, 4], color='blue', marker='o', linestyle='dashed', linewidth=2, markersize = 12)
plt.ylabel('Person Looks')
plt.xlabel('Age')
plt.show()
