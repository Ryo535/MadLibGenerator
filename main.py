from easygui import *
# import everything from the easygui library, to allow me to create guis

# changed input descriptions to be questions, leading to more unexpected results.
color = enterbox("What is your favourite colour?")
adjectives = enterbox("What are two funny adjectives? Seperate them with a space.").split()
verb = enterbox("What is your favourite activity?")
animal = enterbox("What is your favourite animal?")

# adjusted story to make use of the new variables (the story is still just a 
# placeholder being used for testing)
msgbox(f"The {adjectives[0]} {color} {animal} was {verb} in a very {adjectives[1]} manner.")
