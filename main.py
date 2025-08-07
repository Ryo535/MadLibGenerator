from easygui import *
# import everything from the easygui library, to allow me to create guis

# function to check if a string is an integer
def str_to_int(text: str):
    if text.isdigit():
        return int(text) # returns with the integer value of the string
    else:
        return False # returns false if the string is not a valid integer

# function to check if an integer is within a variable range
def is_in_range(num: int, start: int, end: int):
    if num >= start and num <= end:
        return True # returns true if the integer is within the range
    else:
        return False # returns false if the integer is not within the range

# asking questions to gather user input, making the story unique.
color = enterbox("What is your favourite colour?")

adjectives = []
# loop that ensures the script only continues if there are exactly two adjectives, preventing errors from occuring.
while len(adjectives) != 2:
    adjectives = enterbox("What are two funny adjectives? Seperate them with a space.").split()
    if len(adjectives) != 2: msgbox("Please enter two adjectives! Remember to seperate them with a space!")

verb = enterbox("What is your favourite activity?")
animal = enterbox("What is your favourite animal?")

randomNum = ""
# loop that ensures the script only continues if the input is a valid integer, preventing errors from occuring.
while not randomNum:
    randomNum = str_to_int(enterbox("Pick a number from 1-100"))
    if not is_in_range(randomNum, 1, 100): randomNum = False
    if not randomNum: msgbox("Please enter a valid number!")

# adjusted story to make use of the new variables (the story is still just a 
# placeholder being used for testing)
msgbox(f"The {adjectives[0]} {color} {animal} was {verb} in a very {adjectives[1]} manner.")

# shows a different story depending on the user's chosen number
if is_in_range(randomNum, 1, 25):
    msgbox("story 1")
elif is_in_range(randomNum, 26, 50):
    msgbox("story 2")
elif is_in_range(randomNum, 51, 75):
    msgbox("story 3")
else:
    msgbox("story 4")