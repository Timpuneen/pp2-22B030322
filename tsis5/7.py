import re

def snake_to_camel(string):
    camel = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), string)
    return camel

string = input()
print(snake_to_camel(string))
