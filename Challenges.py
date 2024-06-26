# 1. Assign a string to a variable:
string1 = "Hi there!"
print(string1)






# 2. Assign a multiline string to a variable:
string2 = """Ryan1 says: And then after this guy takes down the henchman,
I'll bust in, do a back flip, snap the bad guy's neck and save the day!


Ryan2: So wait, let me get this straight,
You want us to go thru all that trouble
...go thru all of that...
on the slight chance that it might work?


Ryan1:  That's it.  That's the plan.


Ryan2:  Alright.  I'm in.


Ryan1:  You son of a gun.
"""
print(string2)








# 3. Return a range of characters by using the slice syntax:
print("""
__________________________________
Four examples of using the slice method:
__________________________________""")
# First, it can be done by specifying the start index and the end index, separated by a colon. Note that the first character has an index of zero:
print(string2[340:347])


# Second, by leaving out the start index. This way, the range will start at the first character and end wherever you specify:
print(string1[:2])


# Third, if you leave out the ending index, then the range will go all the way to the end:
print(string2[330:])


# The fourth way would be using negative indexes to start counting the slice from the end of the string:
print(string2[-18:-1])








# 4. Use the len() function:
print("""
     
__________________________________________________________
The total number of characters in the string2 variable is:
__________________________________________________________""")
print(len(string2))








# 5. Use the strip() method to return a trimmed version of a string.
print("""
     
__________________________________
Two examples of using the strip method:
__________________________________""")
Ryan4 = "     Well if he's in, I'm in.                 "
stripped = Ryan4.strip( )
print('Ryan3: "I\'m in, too."  Ryan4: "' + stripped + '"')
# Note that leaving it blank only works for leading/trailing white space, NOT for white space that's in the middle of a string


# Leading/trailing letters can be specified, however:
exampleStripped = ".,,,...jkkkjbanana...jjj"
strippedExample = exampleStripped.strip(",.jk")
print(exampleStripped + " gets stripped down to become " + strippedExample)








# 6. Use the upper() method to convert a string into all uppercase letters:
Ryan5 = '"If he\'s in, I\'m out!"'
print("""
     
__________________________________
Example of using the upper method:
__________________________________""")
allCaps = Ryan5.upper()
print(allCaps)








# 7. Use the "in" or "not" in keyword to check whether or not a particular phrase or character is present in a string:
print("""
     
___________________________________________________________________
Checking whether the word 'henchman' is within the string2 variable:
___________________________________________________________________""")


print("henchman" in string2)


# ----------------------------------


print("""
     
___________________________________________________________________
Print confirmation only if the word 'henchman' is within the string2 variable:
___________________________________________________________________""")


if "henchman" in string2: print("Yes, Ryan mentioned a henchman when describing the plan")


# ----------------------------------


print("""
     
_______________________________________________________________
Check whether the word 'out' is NOT within the string2 variable:
_______________________________________________________________""")


print("out" not in string2)


# ----------------------------------


print("""
     
____________________________________________________________________________
Print confirmation only if the word 'out' is NOT within the string2 variable:
____________________________________________________________________________""")


if "out" not in string2: print("At the beginning, all of the Ryans said they were in. In the string2 variable, none said that they were out.")








# 8. Concatenate a string:
print("""
     
_____________________
Concatenating strings:
_____________________""")
string3 = "Hello!"
print(string1 + " " + string3)
RyanGreeting = '"' + string1 + ' '  + string3 +'"'
print(RyanGreeting)








# 9. Use an escape character:
print("""
     
________________________
About escape characters:
________________________""")
print("✅ See lines 66 and 78 of the code for this page to see examples of using the \ escape character")



# =========================================================================================================
# =========================================================================================================
# =========================================================================================================


num1 = "one"
num2 = 2.1


print(num1 + num2)
# Will result in an error saying that you can't concatenate a string to a floating point number


num1 = "1"
print( int(num1) + num2 )
# Will work to produce 3.1 because we converted num1 from a string into an integer


x = 5
y = 3


# =========================================================================================================
# =========================================================================================================
# =========================================================================================================


# 1. Use an arithmetic operator:
print("What is x times y?")
print(x*y)




# 2. Use two assignment operators:
print("If we add 3 to x what is the sum?")
x += 3
print(x)


print("If we multiply 3 times y what is product?")
y *= 3
print(y)




print("The values of x and y have now changed to those answers!")


# 3. Use four comparison operators:
print("Is x equal to y?")
print(x == y)


print("Is x NOT equal to y?")
print(x != y)


print("Is the new value of x greater than the new value of y?")
print(x > y)


print("Is x less than or equal to y?")
print(x <= y)




# 4. Use a logical operator:
x = 5
print("Is 5 greater than 3 AND less than 10?")
print(x > 3 and x < 10)




# 5. Use an identity operator:
print("Are x and y the same?")
print(x is y)




# 6. Use a membership operator:
z = ["apple", "grapes", "banana", "cherry"]
print("Does z contain 'banana' within its array?")
print("banana" in z)




# 7. Use two bitwise operators to compare binary numbers:
print("Set each bit to 1 if BOTH bits are 1:")
print(6 & 3)


print("Set each bit to 1 if one of the two bits is 1. Otherwise set it to 0:")
print(6 | 3)



# =========================================================================================================
# =========================================================================================================
# =========================================================================================================


# Tuples use parentheses and are immutable objects that cannot be changed
animal = ('zebra', 'alligator', 'giraffe', 'goat', 'ox')
print(animal)


# Lists, however, CAN be changed
listOfAnimals = list(animal)
print(listOfAnimals)
listOfAnimals.append("honey badger")
print(listOfAnimals)


# Strings are also considered immutable objects that cannot be changed
myString = "Hello!  Pleased to meet you!"


# Therefore, attempting to create a list with one would create an array where every character and empty space is its own element!
newString = list(myString)
print(newString)


# So, to split the array apart into separate words, use the split method and pass in an empty space as the condition
corrected_New_String = myString.split(" ")
print(corrected_New_String)



# =========================================================================================================
# =========================================================================================================
# =========================================================================================================


myList = [2, 3, 4]


# Display how many values are inside the array:
print(len(myList))


# Use a for loop to iterate thru and display each value of each index inside of the array:
for i in myList: print(i)


# Show the value of the third item:
print(myList[2])


# Show the value of the first:
print(myList[0])


# Add the number 5 onto the end of the array:
myList.append(5)


# Loop thru and display each of the values NOW in the new array:
for i in myList: print(i)


# Confirm the length of the new array:
len(myList)


# To show that the list is an array:
print(myList)



# =========================================================================================================
# =========================================================================================================
# =========================================================================================================




# 1. Create a list:
plumTrees = ["satsuma", "santa rosa", "black beauty", "friar"]
print(plumTrees)


# 2. Loop through the list using a "for" loop:
for x in plumTrees: print(x)


# 3. Use the append() method:
plumTrees.append("victoria")
print(plumTrees)


# 4. Make a copy of the list.  For example, use the List method copy():
secondCopy = plumTrees.copy()
print(secondCopy)


# 5. Concatenate two lists:
appleTrees = ["anna", "braeburn", "cortland", "fuji"]


fruitTrees = plumTrees + appleTrees
print(fruitTrees)


# 6.  Use the reverse() method on a list:
appleTrees.reverse()
print(appleTrees)


# =========================================================================================================
# =========================================================================================================
# =========================================================================================================


# 1. Create a tuple and print it:
cherryTreeTuple = ("Japanese", "sour", "black", "wild")
print(cherryTreeTuple)


# 2. Loop through the tuple items by using a for loop:
for c in cherryTreeTuple: print(c)


# 3. Use the count() mehtod on the tuple:
numberOfJapaneseCherryTrees = cherryTreeTuple.count("Japanese")
print(numberOfJapaneseCherryTrees)


# =========================================================================================================
# =========================================================================================================
# =========================================================================================================


# 1. Create a set:
painkillers = {"Acetaminophen", "Ibuprofen", "Naproxen", "Diclofenac topical", "Aspirin"}
# Note that the items will appear in random order when printed, since they are unordered:
print(painkillers)


# 2. Add an item to the set using the add() method:
painkillers.add("Demerol")
print(painkillers)


# 3. Use the remove() method to take an item out of the set:
painkillers.remove("Demerol")
print(painkillers)


# 4. Use the difference() method on two sets to show only the items that exist in the first set and NOT in the second set:
heartattackRisk = {"Ibuprofen", "Diclofenac topical", "Naproxen"}


safestAdultPainkillers = painkillers.difference(heartattackRisk)
print(safestAdultPainkillers)



# =========================================================================================================
# =========================================================================================================
# =========================================================================================================


# Dictionaries are a specialized type of list.
# The first item is a key; the second item is its value. dictionary={"key":"value"}  Together they form a key-value pair. A dictionary is an UNordered collection of key-value pairs.


myDictionary = {'index1':1, 'index2':2, 'index3':355}
print(myDictionary)


# To get only the value associated with one key:
print(myDictionary['index3'])



# =========================================================================================================
# =========================================================================================================
# =========================================================================================================




# You can nest a dictionary inside of another dictionary!
dictionaryUsers = {"employee1234":{"fName":"Bob", "lName":"Barker", "phone":"123-456-7890"}, "employee12345":{"fName":"Mary", "lName":"McKraken", "phone":"987-654-3210"}, "employee123456":{"fName":"Sam", "lName":"Smith", "phone":"555-111-2222"}  }


# To call on the second item in the dictionary:
print(dictionaryUsers["employee12345"])


# To pull out only one element, such as the phone number of the desired employee:
print(dictionaryUsers["employee12345"]["phone"])


# Use {} wild cards for the first and last names,
# then use the \n to go down one line,
# then use a {} wild card for the phone number,
# then use the format() method with the necessary variables listed:
print( "User: {} {} \nPhone: {}".format(dictionaryUsers["employee12345"]["fName"], dictionaryUsers["employee12345"]["lName"], dictionaryUsers["employee12345"]["phone"]) )


# =========================================================================================================
# =========================================================================================================
# =========================================================================================================



# As of Python version 3.7, dictionaries are ordered.  However, previously (in Python 3.6 and earlier) dictionaries were unordered.

# 1. Create a dictionary:
pickupTruck = {
    "make":"Ford",
    "model":"Ranger",
    "year":1991,
    "color":"white"
}


# Viewable using:
print(pickupTruck)




# 2. use the get() method on the dictionary to return the value of an item with a specified key:
model = pickupTruck.get("model")
print(model)




# 3. Change a value within the dictionary by referring to its key name:
pickupTruck["color"] = "blue"
print(pickupTruck)




# 4. Add an item to the dictionary by using a new index key and assigning a value to it:
pickupTruck["transmission"] = "manual"
print(pickupTruck)




# 5. Create a nested dictionary:
BlueyFamily = {
    "Mum": {
        "name":"Chilli",
        "breed":"red heeler",
        "voiced by":"Melanie Zanetti"
    },
    "Dad": {
        "name":"Bandit",
        "breed":"blue heeler",
        "voiced by":"Dave McCormack"
    },
    "eldest": {
        "name":"Bluey Christine",
        "breed":"Blue Heeler",
        "age":6
    },
    "youngest":{
        "name":"Bingo",
        "breed":"Red Heeler",
        "age":4
    }
}




print(BlueyFamily)


# 6. Use the fromkeys() method to create a dictionary with the specified keys and one specified value:
x = ("color1", "color2", "color3")
y = "red"


combinedDictionary = dict.fromkeys(x,y)


print(combinedDictionary)


# =========================================================================================================
# =========================================================================================================
# =========================================================================================================


# An array is a collection of similar values systematically stored within a collection object.
# Python treats collection objects such as liss, tuples, and dictionaries as arrays.


color = ['red', 'blue', 'green', 'orange', 'pink', 'purple', 'yellow', 'black', 'brown']


print(color)


# =========================================================================================================
# =========================================================================================================
# =========================================================================================================


# A data structure is a collection of data values arranged in a special orientation where the data can be quickly accessed from the computer's memory and applied.


"This is a string"


variable = "Bob"


print(variable)


integer = 9


a_float = 9.01


a_list = ["Bob", "Sally"]


a_tuple = (1,2,3,"a","b","c")


a_dictionary = {"index1":"value1" , "index2":"value2"}


Boolean = True


print(type(variable))


# =========================================================================================================
# =========================================================================================================
# =========================================================================================================


# Utilize the type() function


number = 10
print(type(number))



# =========================================================================================================
# =========================================================================================================
# =========================================================================================================

