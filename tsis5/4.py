import re

string = input()
pattern = '[A-Z]+[a-z]+'

if re.search(pattern, string):
    print("Match found!")
else:
    print("No match found.")