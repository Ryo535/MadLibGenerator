from easygui import *
# easygui library is used to create all the guis
import sys
# sys library is used to exit the application when user clicks cancel

# function to check if a string is an integer
def str_to_int(text: str) -> int | bool:
    if text.isdigit():
        return int(text)
    return False

# function to check if an integer is within a variable range
def is_in_range(num, start: int, end: int) -> bool:
    if type(num) == type([]): 
        for i in num: 
            if not (i >= start and i <= end):
                return False # returns false if ANY of the integers are not within range
        return True
    if num >= start and num <= end:
        return True
    return False

# function to check if user clicked cancel
def check_cancel(button: str) -> str:
    if button == None:
        sys.exit(0) # closes the program
    return button

def ask_question(question: str, min_chars = 3, max_chars = 30, multiple = False, list_length = 0) -> str:
    valid = False
    while not valid:
        result = check_cancel(enterbox(question))
        if multiple:
            result = result.split()
            valid = len(result) == list_length
            if valid: valid = is_in_range([len(word) for word in result], min_chars, max_chars)
            else: 
                check_cancel(msgbox(f"Please enter {list_length} words! Remember to seperate them with a space!"))
                continue
        else: valid = is_in_range(len(result), min_chars, max_chars)
        if not valid: msgbox(f"Please enter a valid answer! Your answer must be between {min_chars}-{max_chars} characters!")
    return result

# asking questions to gather user input, making the story unique to each user.
color = ask_question("What is your favourite colour?")

adjectives = ask_question("What are two words you would use to describe your best friend? Seperate them with a space.", 3, 27, True, 2)

verb = ask_question("What is your favourite activity?")

animal = ask_question("What is your favourite animal?", 3, 42)

rand_num = ""
# loop that ensures the script only continues if the input is a valid integer within the range, preventing errors from occuring.
while not rand_num:
    rand_num = str_to_int(check_cancel(enterbox("Pick a number from 1-100")))
    if not is_in_range(rand_num, 1, 100): rand_num = False
    if not rand_num: msgbox("Please enter a valid number! It must be between 1-100!")

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