from random import *

name_list = ["Bob", "Charlie", "Ken", "Barbie", "Shantua"]
result_name = name_list[randrange(0, 4)]
marriage = []

i = 0 
while i < 2:
    name = raw_input("What is your name: ")
    age = raw_input ("What a nice name " + ", " + name + " what is your age: ")
    get_marriage = raw_input("How young! Let's continue shall we? Which gender do you want to marry: male or female: ")
    if get_marriage == "male" or "Male":
       marriage.append("female") # There something wrong with changing the gender when you insert female,
       #it still returns female.
    elif get_marriage == "female" or "Female": 
        #del.marriage(female) and marriage(Female)
        marriage.append("male")
    else: 
        marriage.apend("alien")
    
    result = raw_input ("First of all, your name is not " + name + " ,your name is now " + result_name)
    next_result = raw_input ("Ok " + result_name + "You will not marry a " + get_marriage + " you will marry a " + str(marriage[0]) )
    final_input = raw_input ("Congratulations, you have just transformed yourself. You will now play this game forever. Please press enter: ")
    i = i + 1
