import re

string = input()
pattern = '^[a-z]+_[a-z]+'

if re.search(pattern, string):
    print("Match found!")
else:
    print("No match found.")