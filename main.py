from easygui import *
# import everything from the easygui library, to allow me to create guis

# replaced text-based functions with easygui functions
adjectives = enterbox("2 adjectves: ").split() # storing two adjectives in a list
verb1 = enterbox("Verb 1: ")
noun1 = enterbox("Noun 1: ")

# using an f string to easily place variables into the story
msgbox(f"The {adjectives[0]} {noun1} was {verb1} in a very {adjectives[1]} manner.")
