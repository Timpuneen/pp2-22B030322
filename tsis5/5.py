import re

string = input()
pattern = 'a.*?b$'

if re.search(pattern, string):
    print("Match found!")
else:
    print("No match found.")