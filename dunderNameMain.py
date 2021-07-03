def step1():
    print("Executing step1...")
def step2():
    print("Executing step2...")
def step3():
    print("Executing step3...")


print("The Dunder Name Main's Name is: {}".format(__name__))
step1()

if __name__ == "__main__":
    print("This is dunderNameMain")
    step1()
    step2()
    step3()

if __name__ == '__main__':
    print ("Run Directly")
else:
    print("Run from Import")

"""
if __name__ == '__main__':
    print ("Run Directly")
else:
    print("Run from Import")

"""