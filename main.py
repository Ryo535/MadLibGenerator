from easygui import *
# easygui library is used to create all the guis
import sys
# sys library is used to exit the application when user clicks cancel

# function to check if a string is an integer
def str_to_int(text: str):
    if text.isdigit():
        return int(text)
    return False

# function to check if an integer is within a variable range
def is_in_range(num, start: int, end: int, loop = False):
    if loop: 
        for i in num: 
            if not (i >= start and i <= end):
                return False # returns false if ANY of the integers are not within range
        return True
    
    if num >= start and num <= end:
        return True
    return False

# function to check if user clicked cancel
def check_cancel(button):
    if button == None:
        sys.exit(0) # closes the program
    return button

# asking questions to gather user input, making the story unique to each user.
color = enterbox("What is your favourite colour?")

adjectives = []
# loop that ensures the script only continues if there are exactly two adjectives, preventing errors from occuring.
while len(adjectives) != 2:
    adjectives = enterbox("What are two funny adjectives? Seperate them with a space.").split()
    if len(adjectives) != 2: msgbox("Please enter two adjectives! Remember to seperate them with a space!")

verb = enterbox("What is your favourite activity?")
animal = enterbox("What is your favourite animal?")

rand_num = ""
# loop that ensures the script only continues if the input is a valid integer, preventing errors from occuring.
while not rand_num:
    rand_num = str_to_int(enterbox("Pick a number from 1-100"))
    if not is_in_range(rand_num, 1, 100): rand_num = False
    if not rand_num: msgbox("Please enter a valid number!")

# placeholder story used for testing
msgbox(f"The {adjectives[0]} {color} {animal} was {verb} in a very {adjectives[1]} manner.")

# shows a different story depending on the user's chosen number
if is_in_range(rand_num, 1, 25):
    msgbox("story 1")
elif is_in_range(rand_num, 26, 50):
    msgbox("story 2")
elif is_in_range(rand_num, 51, 75):
    msgbox("story 3")
else:
    msgbox("story 4")