#!/usr/bin/env python
# coding: utf-8

# # <center> Homework 1: Python Programming Homework Notebook 1</center>
# ###  <center> <span style="color: blue"> Author, Mentor, Trainer:</span>  <span style="color: red">Sudhindra Goutam Vedanthi</span> </center>
# ###  <center> C3 Mentroring </center>
# #### <center> This assignment is developed as part of "Python Programming for Data science and Engineering" Course</center>
# **<center> Homework due by 03/30/2021 <center>**

# ##### Homework common rules.
# 1. Insert comments appropriately to make the program readable.
# 2. Make variable names meaningful
# 3. For larger programs create documentation using `markdown` cells
# 4. Validate inputs for int, or strings and handle the exceptions. For example: if "dont know" entered as a value for age, you should print an error and allow the user to enter the correct value.
# 5. Use all concepts taught so far - operations, data types, type conversions, expressions, boolean expressions, conditional expressions, conditional execution using `if` etc, repeated executions using iterations (`for` loops), conditinal repetitions using (`while`), formatted outputs, strings and string manipulations(slicing etc), Lists and list operations.
# 6. Try to do few programs each day, instead of completing everything on one day.
# 7. "Happy Programming, Pythonians!!"

# In[ ]:


print("Happy Programming, Pythonians!!")


# **Q1. Play with numbers**
# 
# * Q1.1 - Print numbers from 20 to 10 (not including 10) using `while` loop.
# * Q1.2 - Print all even numbers from 0 to 100 including both, using `for` loop.
# * Q1.3 - Print all even numbers from 0 to 100 including both, using `while` loop.
# * Q1.4 - Print all numbers from 1 to 20 except 9, 10, 11 and 12.

# In[ ]:


i = 20
while i > 10:
    print(i)
    i-=1


# In[ ]:


for i in range(20):
    if(i%2 == 0):
        print(i)
    else:
        if(i == 9 or i == 11):
            print(i)
    


# In[ ]:





# **Q2. Simple Logiks**
# * Q2.1 - Accept a number, and find whether it is even or odd
# * Q2.2 - Accept a number, and display countdown and "Blast Off" message with three versions - using (1) `for` loop and (2) `while` loop and (3) `if` / `else` conditions
# * Q2.3 - Accept a number find the factorial of the number
# * Q2.4 - Accept a number 'n' , and print the first 'n' fibonacci numbers (No recursion please). Fibonacci Numbers are  - 0, 1, 1, 2, 3, 5, 8, 13 etc.. (figure out the logic)
# * Q2.5 - Accept a number and find the absolute of the number
# * Q2.6 - Accept a number and print 1 if x is greater than y, 0 if x is equal to y and -1 if x is less than y.
# * Q2.7 - Accept two numbers and find if the first one is divisible by the second (Hint: means no reminder)
# * Q2.8 - Write an infinite loop, that displays a prompt ('>>>'), does not do anything for your input except when you type the following words: done, quit, exit.
# * Q2.9 - Guessing game. Create a secret number. Let user guess a number, if it is same as the secret number, print a message as "You won". Give three attempts. For every failed attempt give another chance with a message "Try Again". After 3 attempts, Display "Sorry! You lost the game"

# In[7]:


#Fibonacci
x = input("Enter a number")
x = int(x)
a = 1
b = 1
print(a)
print(b)
for i in range(1, x-1):
    print(a+b)
    temp = b
    b = a+b
    a = temp


# In[8]:


#Factorial
x = input("Enter a number")
x = int(x)
fact = 1
for i in range(1, x+1):
    fact = fact * i
print(fact)


# **Q3.No Stone Unturned - A Game**  
# 
# In this game  
# * Two players sit in front of a pile of 100 stones. 
# * They take turns, each removing between 1 and 5 stones (assuming there are at least 5 stones left in the pile. If less then 5 stones are there then you can only turn so much). 
# * The person who removes the last stone(s) wins
# 
# **_Assumptions_** - If you have made any assumptions, please print as notes to the game player.

# In[10]:


N = 100
while N > 5:
    x = input("X, your turn, pick some stones")
    N = N - int(x)
    if N >= 5:
        y = input("Y, your turn, pick some stones")
        N = N - int(y)
        if N < 5:
            print("Y is a winner")
    else:
        print("X is a winner")


# **Q4. Pig Latin**  
# Write a function pig latin that takes in a single word, then converts the word to Pig Latin. To review, Pig Latin takes the first letter of a word, puts it at the end, and appends “ay”. The only exception is if the first letter is a vowel, in which case we keep it as it is and append “hay” to the end.
# 
# >E.g. “boot” → “ootbay”, and “image” → “imagehay”.
# 
# **_Points to Note:_** It will be useful to define a list at the top of your code file called VOWELS. This way, you can check if a letter x is a vowel with the expression x in VOWELS.  
# 
# **_Remember_** - to get a word except for the first letter, you can use word `[1:]`.

# In[42]:


vowels = ['a', 'e', 'i', 'o', 'u']

given_word = input("Please type a word")

if(given_word[0] in vowels):
    pig_latin = given_word + "hay"
else:
    pig_latin = given_word[1:]
    pig_latin = pig_latin + "ay"
    
print(pig_latin)


# **Q5. Name Game**  
# 
# Do the following:
# * Get the users name as input.
# * Find the length of the name
# * If the name contains more than 30 characters, truncate the name to 30 characters and let the user know that the name has a limit.
# * Find how many vowels and how many constants and how many spaces
# * Split the name into a list
# * Create a piglatin code - a replaced by z, b replaced by y etc also in the reverse z replaced by a etc.
# * Using the code above, create your code name.

# In[54]:


#Finding how many vowels, consonants, and space are there in a given sentence.
#This solution assumes no other special characters or non-printable characters

vowels = ['a', 'e', 'i', 'o', 'u']
white_space = " "

num_vowel = 0
num_space = 0
num_conso = 0

given_word = input("Please type a word")

for i in range(len(given_word)):
    if(given_word[i] in vowels):
        num_vowel += 1
    elif given_word[i] == white_space:
        num_space += 1
    else:
        num_conso += 1
count_list = [["vowels", num_vowel], ["spaces", num_space], ["consonants", num_conso]]  
print(count_list)


# **Q6. Play with `Lists`**
# 
# Write a program to take 'n' numbers from the user
# * Create a list - L
# * Create a list of squares of L
# * Create a list of cubes of L
# * Find the max, min, average of the values of L (do not use pre-defined funtions)
# * Find the standard deviation and variance (do not use any pre-defined functions)
# * Find the mean, median and mode
# * Ask of a number from the user and find whether it exists or not
# * Find the place (location in the list) of the above number in the list
# * Accept and add a new number to the list at the end
# * Accept and add a new number to the list at a particular location
# * Sort the list and created a sorted list sortedL, using the standard function and write your own logic to sort.
# * Ask for a number from the user and delete it.
# * Conduct various slice operations.

# In[ ]:





# **Q7. Roll the dice.**
# * Create Dice as a list
# * Use `random` module for rolling the dice.
# * Set a target value like 100. Find how many times you have to roll the dice to get the is number. Create the dice roll outcomes as a list.

# In[38]:


import random as rand

dice_face = [1,2,3,4,5,6]
n = 0
sum = 0
while sum < 100:
    roll_num = rand.randrange(1,6)
    sum+=roll_num
    n+=1
print ("It took " + str(n) + " rolls to get a sum of " + str(sum))


# ##### Q8. Creat a Geometry Helper
# The Geometry helper displays a menu to compute the following:
# 1. Calculation of metrics
#    > Compute the distance between two points - each point has a x and y coordinates. Like point a = `[x1, y1]`
#    > ![image.png](attachment:image.png)
#      ![image-2.png](attachment:image-2.png)
#      Fill in the values:	 	
#      ![image-3.png](attachment:image-3.png)
#      ![image-4.png](attachment:image-4.png)
#      
# 2. Find the area of the rectangle, triangle, square and circle
# 3. Find the volume of the cube, box (rectangular), and sphere
# 4. Based on the choice, accept the values required.
# 5. Use math functions like power, square root, constants like `pi` etc
# 6. Menu should be displayed and the calculations should be done until the user selects a "quit" option
#  	 

# In[ ]:





# ##### Q9. Create a Conversion Calculator
# The calculator should display a menu for the following conversions
#   >   * Convert from Farenheit to Celcius
#       * Convert from Celcius to Farenheit
#       * Convert from Pounds to Kilograms
#       * Convert from Kilograms to Pounds
#       * Convert from Miles to Kilometers
#       * Convert from Kilometers to Miles
# 
# Other features similar to Question 8 above.  
# For conversion formulas look up to Google sir.

# In[ ]:





# #### <span style="color: red"> Q10.  Health Calculators </span>
# Create a program to display the option of calculating BMI or BMR   
# 
# **1. BMI (Body Mass Index)**
#    * Accept body weight in kilo grams, accept height in centimeters
#    * Convert height from cm to meters
#    * Calculate BMI
#    * Print BMI interpretation based on the table given below
# 
# **2. BMR (Basal Metabolic Rate)**
#    * Accept body weight in kilo grams, accept height in centimeters
#    * Accept the gender (Male or Female)
#    * Calculate BMR
#    * Accept the Level of activity
#    * Multiply the BMR found earlier with the factor given in the calculation
#    * Display the BMR and adjusted BMR
#    
# 
# **BMI is calculated as follows:**  
# The body mass index (BMI) is a statistic developed by Adolphe Quetelet in the 1900’s for evaluating body mass. It is not related to gender and age. It uses the same formula for men as for women and children.
# > The body mass index is calculated based on the following formula:
#        >> Bodyweight in kilograms divided by height in meters squared
#                    or
#           BMI = x in k  / (y in meters)\**2
#           Where:
#                x=bodyweight in KG
#                y=height in m
#          Example for 175 cm height und 70 kg weight:
#                  BMI = 70 / (1.75 * 1.75) = 22.86
#                  
# > BMI Interpretation Table
#           Meaning	            BMI
#          Normal weight	     19–24.9
#          Overweight	         25–29.9
#          Obesity level I	 30–34.9
#          Obesity level II	 35–39.9
#          Obesity level III	 ≥ 40
# 
# 
#                  
# **BMR is calculated as follows:**  
# You use energy no matter what you're doing, even when sleeping. Your Basal Metabolic Rate (BMR) is the number of calories you'd burn if you stayed in bed all day, the amount of energy expended while at rest in a neutrally temperate environment, and in a post-absorptive state (meaning that the digestive system is inactive, which requires about 12 hours of fasting).
# 
# If you've noticed that every year, it becomes harder to eat whatever you want and stay slim, you've also learnt that your BMR decreases as you age. Likewise, depriving yourself of food in hopes of losing weight also decreases your BMR, a foil to your intentions. However, a regular routine of cardiovascular exercise can increase your BMR, improving your health and fitness when your body's ability to burn energy gradually slows down.
# > The BMR is calculated using Revised Harris-Benedict Equations:
# >>  
#     **For men:**  
#        BMR = 13.397W + 4.799H - 5.677A + 88.362
# >>  
#     **For women:**  
#        BMR = 9.247W + 3.098H - 4.330A + 447.593
# >>  
# >>  where:  
# >>  - W is body weight in kg
# >>  - H is body height in cm
# >>  - A is age
#           
# > BMR calculated above will be the resting calorie needs. To get the actual calorie needs based on the activity that an individual is performing: To determine your total daily calorie needs, multiply your BMR by the appropriate activity factor, as follows:
#     
# >>    - If you are sedentary (little or no exercise) : Calorie-Calculation = BMR x 1.2
# >>    - If you are lightly active (light exercise/sports 1-3 days/week) : Calorie-Calculation = BMR x 1.375
# >>    - If you are moderatetely active (moderate exercise/sports 3-5 days/week) : Calorie-Calculation = BMR x 1.55
# >>    - If you are very active (hard exercise/sports 6-7 days a week) : Calorie-Calculation = BMR x 1.725
# >>    - If you are extra active (very hard exercise/sports & physical job or 2x training) : Calorie-Calculation = BMR x 1.9
#     
# 

# In[ ]:





# **Q11. Create a problem. State the problem and Write a program to solve the problem.**

# In[ ]:





# ### Project 1: Student Grade Report
# 1. Create a class list with five class code (example: CS101, CS205, SE301). Class codes contain 2 alpha characters and 3 digits.
# 2. Create a Student List - This list contains lists of Student info like student name and id, list of lists example 
#     `StudentList = [["Goutam", 101], ["Ramanujan", 102], .... ]`
# 3. Create a list of Score Cards - It is a two dimensional list of lists containing studentID, score1, score2 etc Scores are percentage got in the corresponding course from the Course/Class List
#    Example
#    101, 95.6, 87.6, ......  (this is the first list element in the outer list - studentId, score1, etc..)
#    102, ................... (this is the second element for the second student etc...)
#    
# 4. Create all the lists statically - created inside the program 
# 5. Create all the lists dynamically - created using the input from the user.
# 6. Scores are given as percentages in the format of nn.n 
# 7. Find the average of all the five courses
# 8. Find the GPA:
#    * 90 - 100  --> A
#    * 80 - 89.9 --> B
#    * 70 - 79.9 --> C
#    * 60 - 69.9 --> D
#    * <60       --> F (Fail)
# 9. Create a Score Report for each student as follows:
#    ```
#    |-----------------------------------------------------------------------------|
#    |Student's Name:                                                              |
#    |-----------------------------------------------------------------------------|
#    |Class Code          |  Score      |   GPA        |      Comments             |
#    |-----------------------------------------------------------------------------|
#    |CS101               |  95.6       |    A         |                           |
#    
#    ...................
#    |-----------------------------------------------------------------------------|
#    |Overall Scores      | Average     | Overall GPA  |                           |
#    |-----------------------------------------------------------------------------|
#     
#    Important Notes: The following courses need to be taken again: CS205, etc.. (All classes with GPA 'D' or 'F')```
#    
# 10. Calculate the Class Average Score across all students for every course.
# 11. Calcualte the standard deviation and variance
# 12. How many students with each GPA for each class
# 13. What is the overall mean GPA for each class and the overall mean GPA for the entire group
# 14. A school administrator wants to use this program. Please make it as much user friendly as possible.
# 11. Create proper menus, display until the user wants to quit. 
# 12. Validate the data as alpha, alphanumeric or numeric before saving it in the lists.
# 13. We will be doing more things with this problem like adding new courses, student ages, address, contact info, course names and descriptions.
# 14. Build the programs gradually.
# 15. Use all the concepts taught so far.
# 16. All the best

# In[ ]:


print("Welcome to Student Grade System")

login = True
enter = True

while login:
    student_name = input("Enter student name: ")
    while enter:
        course_name = input("Enter course number: ")
        if len(course_name == 5) and isalpha(course_name[0:2]) and isdigit(course_name[2:]):
            course_grade = input("Enter the grade for " + course_name + ": ")
        else:
            print("Course number entered is not correct")
            break
    more_courses = input("More courses to enter? Y/N: ")
    if lower(more_courses) == "y":
        continue
    elif lower(more_courses) = "n"
        enter = False
        break


# In[ ]:




