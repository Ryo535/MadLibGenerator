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
question = "What is your favourite colour?"
valid = False
while not valid:
    color = check_cancel(enterbox(question))
    valid = is_in_range(len(color), 3, 30)
    if not valid: msgbox("Please enter a valid colour! It must be between 3-30 characters.")

question = "What are two words you would use to describe your best friend? Seperate them with a space."
adjectives = []
valid = False
# loop that ensures the script only continues if there are exactly two valid adjectives, preventing errors from occuring.
while len(adjectives) != 2 or not valid:
    adjectives = check_cancel(enterbox(question)).split()

    valid = is_in_range([len(word) for word in adjectives], 3, 27, True)
    
    if len(adjectives) != 2: msgbox("Please enter two adjectives! Remember to seperate them with a space!")
    elif not valid: msgbox("Please enter valid english adjectives! They each must be between 3-45 characters!")

question = "What is your favourite activity?"
valid = False
while not valid:
    verb = check_cancel(enterbox(question))
    valid = is_in_range(len(verb), 3, 30)
    if not valid: msgbox("Please enter a valid verb! It must be between 3-30 characters.")

question = "What is your favourite animal?"
valid = False
while not valid:
    animal = check_cancel(enterbox(question))
    valid = is_in_range(len(verb), 3, 42)
    if not valid: msgbox("Please enter a valid animal! It must be between 3-42 characters.")

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