print("Hello world")

import myutils.employee as emp
import myutils.utils as util

emp1 = emp.Employee("Goutam", "Vedanthi", "Data Scientist", 50000)
emp2 = emp.Developer("Sumedh", "Vedanthi", "Data Engineer", "Python", 80000)

print(emp1)
print(emp2)

number = util.maker(6)
print (number(3))