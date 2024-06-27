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

answer = True


print(type(answer))


newAnswer = False


print(type(newAnswer))


# =========================================================================================================
# =========================================================================================================
# =========================================================================================================


a = 500
b = 30


# 1. Run an if/else statement that prints confirmation when the condition is True:
if a > b: print(str(a) + " is greater than " + str(b))
else: print("Attempt failed")


# 2. Run an if/else statement that prints when the condition is False:
if a == b: print(str(a) + " is equal to " + str(b))
else: print("SUCCESS!!! " + str(a) + " does NOT equal " + str(b) )


# =========================================================================================================
# =========================================================================================================
# =========================================================================================================


import ourModule


if __name__ == "__main__":
    results = ourModule.getNumbers(5, 9)
    print(results)


# =========================================================================================================
# =========================================================================================================
# =========================================================================================================


import datetime


currentTime = datetime.datetime.now()


print(currentTime)


# =========================================================================================================
# =========================================================================================================
# =========================================================================================================


# 1. Import the random module:
import random


# 2. Use it to display a random number between 1 and 100:
print(random.randrange(1, 100))


# =========================================================================================================
# =========================================================================================================
# =========================================================================================================


num1 = 12
key = True


if num1 == 12:
    if key:
        print("Yes! Num1 equals 12 and you have the key!")
    else:
        print("Well, Num1 indeed equals 12, but you don't have the key.")
else:
    print("Oh noes!  Something went wrong!")


# =========================================================================================================
# =========================================================================================================
# =========================================================================================================


a = 50
b = 100


x = 35


# 1. Execute an If statement:
if b > a: print(str(b) + " is a larger number than " + str(a) + "!")


# 2. Use the Elif keyword within the if statement:
elif b == a: print("The two numbers are equal")


# 3. Use the Else keyword within the if statement:
else: print(str(a) + " is a larger number than " + str(b))


# 4. Execute a nested If statement:
if x > 10:
    print("The mystery number is larger than 10, ")
    if x > 20:
        print("and it is larger than 20 as well")
    else:
        print("but less than 21")


# =========================================================================================================
# =========================================================================================================
# =========================================================================================================



x = "Good-bye"
y = 45
z = 105


# 1. Run a condition in an if statement:
if z > y: print("The value of z is larger than the value of y")
else: print("The value of z is not greater than y")


# 2. Use the bool() function to evaluate values:
print(bool("Hello"))
print(bool(15))
print(bool(x))
print(bool(y))
# Note: Almost any value evaluates to "True" so long as it has some sort of content. Any string is True, unless empty. Any number is True except for zero.  Any list, tuple, set, or dictionary is True, unless empty.


# 3. Use the isinstance() function to check whether a number is an integer:
w = isinstance(52, int)
print(w)
# Note:  The isinstance() function will return True if the specified object is of the specified type.
# Also, if the type parameter is a tuple, then the function will return True so long as the object is one of the types in the tuple:
v = isinstance("Hello", (str, float, int, str, list, dict))
print(v)


# =========================================================================================================
# =========================================================================================================
# =========================================================================================================



#################
##  For Loop ##
#################


# Initialize i to be zero:
i = 0
# A For Loop will cycle thru the block of code a defined number of times.
# Set that number of times to 10:
for i in range(10):
    # print the wild card value of which iteration it is (which starts at zero) and then remember to set the format of what the wild card is
    print("{} iteration through the loop.".format(i))
    # In shorthand, write i = i + 1, to tell it to add one to it each cycle.
    i += 1





#################
##  While Loop ##
#################


# Initialize i to be zero:
i = 0
# A While Loop will cycle thru the block of code indefinitely until a set parameter has been reached.
# Set that parameter to have a value of 10:
while i < 10:
    # print the wild card value of which iteration it is (which starts at zero) and then remember to set the format of what the wild card is
    print("{} iteration through the loop.".format(i))
    # IMPORTANT:  In order to reach a "False" eventually of i being equal to 10, instruct the code to add one to the value of i each iteration.
    # Use shorthand, write i = i + 1:
    i += 1
# Caution:  While loops have a much greater potential to glitch into becoming an infinite loop!




# =========================================================================================================
# =========================================================================================================
# =========================================================================================================


iteration = 1
brokenLoop = 1
skipFive = 0
elseCounting = 1




# 1. Execute a While loop:
while iteration < 11:
    print(iteration)
    iteration += 1




print("--------------------------")
# 2. Use the "break" statement within a while loop to stop it running despite the while condition still being true:
while brokenLoop < 11:
    print(brokenLoop)
    if brokenLoop == 3: break
    brokenLoop += 1




print("--------------------------")
# 3. Use the "continue" statement within a while loop to skip over an iteration:
while skipFive < 10:
    skipFive += 1
    if skipFive == 5: continue
    print(skipFive)




print("--------------------------")
# 4. Use the "else" statement within a while loop:
while elseCounting < 11:
    print(elseCounting)
    elseCounting += 1
else:
    print("...We have reached the number 10. Counting is done.")



# =========================================================================================================
# =========================================================================================================
# =========================================================================================================



sequence = ["fox", "coyote", "wolf"]
brokenSequence = ["cup", "saucer", "plate", "fork", "spoon", "knife", "table", "chair"]
skipBanana = ["peach", "papaya", "banana", "plum", "pear"]


# A for loop doesn't need an indexing variable to be set beforehand




# 1. Execute a For loop:
for x in sequence: print(x)


# Iterating thru the characters of a word:
for x in "Gourmet": print(x)




# 2. Use the "break" statement within a for loop to stop it before it loops thru all of the items:
for x in brokenSequence:
    print(x)
    if x == "knife": break




# 3. Use the "continue" statement within a for loop to skip over a specified element:
for x in skipBanana:
    if x == "banana": continue
    print(x)




# 4. Use the range() function within a for loop to return a sequence of numbers, starting at zero and ending at a specified number:
for x in range(20): print(x)    # It will count 20 times, meaning that the displayed numbers will stop at 19.
print("____________________")
# To count between a certain range of numbers, specify which integer to start at followed by which one to stop just before:
for x in range(10, 21): print(x)
print("____________________")
# To count using a different incremental value, specify it as the third parameter:
for x in range(3, 31, 3): print(x)






print("____________________")






# 5. Use the "else" keyword within a for loop to print something once the loop has ended:
for x in range(11): print(x)
else: print("We have now finished counting to 10")



# =========================================================================================================
# =========================================================================================================
# =========================================================================================================



name = 'Python'


# Count the total number of characters within the string:
print(len(name))


# Use the built-in enumerate method to iterate through all of the elements within the string:
for i in enumerate(name): print(i)



# =========================================================================================================
# =========================================================================================================
# =========================================================================================================





# Create a variable:
mySentence = "loves the color"


# Create a list:
colorList = ['red', 'white', 'blue', 'pink', 'purple', 'black', 'green']


# Create a function to show a sentence for each color
def color_function(nameParameter):
    # Create a temporary list and leave it empty:
    tempList = []
    # Iterate thru the color list:
    for i in colorList:
        # Use a variable named "message" and insert three wild cards and format those strings by plugging in the nameParameter, then the mySentence variable, and lastly followed by the iteration:
        message = "{} {} {}".format(nameParameter, mySentence, i)
        # Append each iteration's result into the end of the list to form an array:
        tempList.append(message)
    # After the entire list of colors is finished, end the loop with a "return" command to show the array of resulting sentences:
    return tempList
   


# Call the function with the desired argument name and save the result inside a variable
colorSentences = color_function("Sally")


# Loop thru the array of sentences to print each to the screen. This step is needed so that the result doesn't look like an array.  It is needed so that instead we see only the resulting sentences each one after another.
for i in colorSentences:
    print(i)



# =========================================================================================================
# =========================================================================================================
# =========================================================================================================



# Create a variable:
loopingSentence = "loves the color"


# Create a list:
colors = ['red', 'white', 'blue', 'pink', 'purple', 'black', 'green']


# Create a function to show a sentence for each color
def colorSententence_function(nameParameter):
    # Create a temporary list and leave it empty:
    tempList = []
    # Iterate thru the color list:
    for i in colors:
        # Use a variable named "message" and insert three wild cards and format those strings by plugging in the nameParameter, then the loopingSentence variable, and lastly followed by the iteration:
        message = "{} {} {}".format(nameParameter, loopingSentence, i)
        # Append each iteration's result into the end of the list to form an array:
        tempList.append(message)
    # After the entire list of colors is finished, end the loop with a "return" command to show the array of resulting sentences:
    return tempList
   


# Create a function to get the user's name and then loop it thru all the sentences:
def getName_function():
    go = True
    while go:
        userName = input('What is your name? ')
        if userName == "": print("Please provide a name")
        elif userName == 'Myra': print("That name is not allowed. Sorry!")
        else: go = False
    resultingSentence = colorSententence_function(userName)
    for i in resultingSentence: print(i)


# Call the function
getName_function()




# =========================================================================================================
# =========================================================================================================
# =========================================================================================================



# 1. Create a function:
def my_function():
    print("Hi there, hello!  You are seeing this because you called this function!")


# 2. Call the function:
my_function()





# =========================================================================================================
# =========================================================================================================
# =========================================================================================================

# Note: Python doesn't have built-in support for anything called "Arrays."  Lists need to be used instead.


# 1. Create an array:
recyclables = ['glass', 'cardboard', 'paper', 'aluminum', 'steel']


# 2. Loop through all the elements of the array using a for loop:
for r in recyclables: print(r)


# 3. Use the count() method on the array:
number = len(recyclables)
print(number)


# 4. Use the sort() method on the array:
recyclables.sort()
for alphabetized in recyclables: print(alphabetized)


# Reverse alphabetical order:
recyclables.sort(reverse=True)
for reverseOrder in recyclables: print(reverseOrder)



# =========================================================================================================
# =========================================================================================================
# =========================================================================================================

def multiply(i):
    return i * i;


print(multiply(3))




# The lambda keyword is used as an anonymous function.  That is a single-line function that has no name and can have any number of arguments but only one expression.  It is used for a shorter amount of time than a regular function, and is used when you want to pass another function in as an argument.
y = lambda x: x * x * x


print(y(20))



# =========================================================================================================
# =========================================================================================================
# =========================================================================================================

# Create a lambda function:
addition = lambda x: x + 10


# Call the function:
print(addition(5))

# =========================================================================================================
# =========================================================================================================
# =========================================================================================================

location1 = "Seattle"
location2 = "Iceland"
location3 = "London"


# Wildcard placeholders can be used to reserve a spot for a variable before explicitly saying what the variable is. Use {} to do so.
print("I flew from {} to {} to get to {}". format(location1, location2, location3))

# =========================================================================================================
# =========================================================================================================
# =========================================================================================================



fname = "Daniel"
lname = "Christie"


print("Hello there, {} {}! Welcome!".format(fname, lname))

# =========================================================================================================
# =========================================================================================================
# =========================================================================================================

# A placeholder doesn't need to be blank inside of the {}.  Instead, they can be identified using word or numbered indexes.


# A 2 decimal format for listing prices can be created using .2f


# Challenge = Execute a format() method to show a price:
salesText = "Buy now for only {price:.2f} dollars!"
print(salesText.format(price = 49))


personIntroduction = "Hello!  My name is {firstname}, and I am {age} years old".format(firstname="Johnny", age=36)
print(personIntroduction)



# =========================================================================================================
# =========================================================================================================
# =========================================================================================================

# The format() function can do more than just format strings!  It can also convert a value into a specific data type format.  Plus, it can also format values into binary or into floats.


# To do so, the format() function takes 2 parameters -- the values that need to be formatted and the format specification




# To format a number into binary:
binaryExample = format(8, 'b')
print(binaryExample)


# To format a number into hexadecimal:
hexadecimalExample = format(4, 'x')
print(hexadecimalExample)


# To format a number into percentage:
percentageExample = format(1, '%')
print(percentageExample)


# Formatting a value into different data types, written out in string format concatenation:
print("Here is the number 3 written as... binary: {0:b}, hexadecimal: {0:x}, percentage: {0:%}".format(3))

# =========================================================================================================
# =========================================================================================================
# =========================================================================================================



# Execute format() functions:


rightAlign = format(4, '>')
print(rightAlign)


centerAlign = format(40, '^')
print(centerAlign)


leftAlign = format(400, '<')
print(leftAlign)


commaThousand = format(4000, ',')
print(commaThousand)


unicodeCharacter = format(40000, 'c')
print(unicodeCharacter)


octalFormat = format(400000, 'o')
print(octalFormat)


underscoreThousand = format(4000000, '_')
print(underscoreThousand)


binaryFormat = format(40000000, 'b')
print(binaryFormat)



# =========================================================================================================
# =========================================================================================================
# =========================================================================================================

def getSum(number1, number2):
    answer = number1 + number2
    print("The sum is {}".format(answer))




# Variables can be used to store functions.
additionVariable = getSum


additionVariable(2, 4)




# Variables can also be used to store entire dictionaries of information.
# Variables can also be used to store an extensive list of items.

# =========================================================================================================
# =========================================================================================================
# =========================================================================================================
