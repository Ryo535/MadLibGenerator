from easygui import *
# easygui library is used to create all the guis
from math import ceil
from sys import exit
# used to exit the application when user clicks cancel

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
        exit(0) # closes the program
    return button

# function to create a gui containing a question that returns the user's input once it is valid.
def ask_question(question: str, min_chars = 3, max_chars = 30, multiple = False, list_length = 0) -> str:
    valid = False
    while not valid:
        result = check_cancel(enterbox(question))
        if multiple:
            result = result.split()
            valid = len(result) == list_length
            if valid: valid = sorted(list(set(result))) == sorted(result) # check for duplicate words
            else:
                check_cancel(msgbox(f"Please enter {list_length} words! Remember to seperate them with a space!"))
                continue
            if valid: valid = is_in_range([len(word) for word in result], min_chars, max_chars) # check if all words in the list are within the allowed range
            else: 
                check_cancel(msgbox(f"Please enter different words! Remember to seperate them with a space!"))
                continue
        else: valid = is_in_range(len(result), min_chars, max_chars) # check if the user's input is within the allowed range
        if not valid: msgbox(f"Please enter a valid answer! Your answer must be between {min_chars}-{max_chars} characters!")
    return result

# loop that ensures the script only continues if the input is a valid integer within the range, preventing errors from occuring.
story_num = None
while not story_num:
    story_num = str_to_int(check_cancel(enterbox("Pick a number from 1-100")))
    if not is_in_range(story_num, 1, 100): story_num = False
    if not story_num: msgbox("Please enter a valid number! It must be between 1-100!")

# shows a different story depending on the user's chosen number
story = ceil(story_num/50)

if story == 1:
    name = ask_question("Who is your favourite movie character?")
    color = ask_question("What is your least favourite colour?")
    adjectives = ask_question("What are two words you would use to describe your best friend? Seperate them with a space.", 3, 27, True, 2)  # the shortest english adjectives are 3 characters long and the longest english adjective is 27 characters long
    verb = ask_question("What is your least favourite activity?")
    animal = ask_question("What is your least favourite animal?", 3, 42)
    exclamation = ask_question("What is your catchphrase?", 2, 60)
    silly_noun = ask_question("What would you call a potion that turns people into snowmen?", 1, 50)
    noun_plural = ask_question("What is one thing you wish you had lots of?")
    place = ask_question("What's your favourite fantasy location?")
    food = ask_question("What's your favourite food?")
    verb_past = ask_question("What is one thing you regret doing yesterday?")

    msgbox(f'One day, {name} woke up feeling incredibly {adjectives[0]}. Outside, a giant {animal} was {verb} on the front lawn. "{exclamation}!" shouted {name}, grabbing a {silly_noun} and running outside. Suddenly, the sky turned {color} and started raining {noun_plural}. Everyone in {place} panicked and started eating {food} to stay calm. Just when things couldn’t get weirder, the {animal} {verb_past} and flew away, leaving behind a trail of glitter and confusion. And that’s why you should never trust a {animal} before breakfast.')
    
else:
    color = ask_question("What is your favourite colour?")
    animal = ask_question("What is your favourite animal?", 3, 42)
    verb_past = ask_question("What is one thing that you did yesterday?")
    place = ask_question("If you could go on vacation anywhere you wanted, where would it be?")
    noun_plural = ask_question("What is one thing that you have a lot of?")
    adjectives = ask_question("What are two words you would use to describe your worst enemy? Seperate them with a space.", 3, 27, True, 2)
    verb = ask_question("What is your favourite activity?")
    noun = ask_question("What is one object that you frequently interact with?")
    exclamation = ask_question("What is your favourite character's catchphrase?", 2, 60)
    move = ask_question("What is an interesting movement? (run, flip, roll, etc.)")
    silly_noun = ask_question("What would you call a potion that turns people into spaghetti?", 1, 50)

    msgbox(f'Today I went to the zoo and saw a {color} {animal} that {verb_past} right in front of me! I couldn’t believe it—it reminded me of the time I went to {place} and saw a bunch of {noun_plural} doing the same thing. The zookeeper was wearing a {adjectives[0]} hat and was {verb} with a giant {noun}. I shouted, "{exclamation}!" and tried to {move} away, but I tripped over a {silly_noun}. It was the most {adjectives[1]} day ever!')