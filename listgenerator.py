# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 18:10:42 2022

@author: Rical
"""
import random 


method_dic = {"1": [True, "append"],"2": [True, "extend"],"3": [True, "insert"],"4": [True, "pop"],"5": [True, "remove"], "6": "reverse()","7": "random.shuffle", "8": "sort()"}
# Generate number of items in array
def generateArray(items, min, max, choice):
    function_dict = {"y": randomlyGenerated, "n": orderedArray}
    array = []
    dif = max - min
    for i in range(min, max):
        array.append(i)    
    return function_dict[choice](array,items, dif)
        
def randomlyGenerated(array, items, dif):
    random_array = [] 
    for i in range(items):
        random_array.append(random.choice(array))
    return random_array           

    
def orderedArray(array, items, dif):   
    #add amount of items without the reminder
    ordered_array = array * (items // dif) 
    remainder = items % (dif)
    for r in range(remainder):
        ordered_array.append(ordered_array[r])
    return ordered_array    

while True:
    try:
        user_items = input("How many items in the integer array, choose n integer or type random (between 1-100) ")
        
        if user_items == "random":
            user_items = random.randrange(0,100)
                         
        else:
            user_items = int(user_items)
            if user_items <= 0:
                print("Please insert a positive integer bigger than 0")
            else:
                break
    except ValueError:
        print("Not an integer or random")
while True:
    try:
        user_min = int(input("What is the minimum value of the array "))
        user_max = int(input("What is the maximum value of the array "))    
        if user_min <= user_max:
            break
        else:
            print("Make sure min value is lower than max value.")
    except ValueError:
        print("Not an integer")  
choice = input("generate randomly? y/n ")
choice = choice.lower()
arraysoFar = generateArray(user_items, user_min, user_max + 1, choice) 
print(arraysoFar)

while True:
    
    user_input = input("Now choose one of the following customizations for your array: 1 - append(), 2 - extend(), 3 - insert(), 4 - pop(), 5 - remove(), 6 - reverse(), 7 - shuffle, 8 - sort(),\n when you are finished type done ")
    try:
        if user_input == "done":
            break
        elif len(method_dic[user_input]) == 2:
            user_input2 = "arraysoFar." + method_dic[user_input][1]
            num_value = input("Please insert value or index for the method:")
            user_input2 = user_input2 + "(" + num_value + ")"    
        elif user_input != "7":
            user_input2 = "arraysoFar." + method_dic[user_input]
        else:
            user_input2 = method_dic[user_input] + "(arraysoFar)"        
        user_transformation = user_input2
        exec(user_transformation)
        print(arraysoFar)
    except:
        print("Please choose a number from the list or type done.")          
    