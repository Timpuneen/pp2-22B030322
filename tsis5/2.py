import re

pattern = 'ab{2,3}?'
string = input()

if re.search(pattern, string):
    print("Match found!")
else:
    print("No match found.")