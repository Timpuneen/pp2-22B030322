import os
import re

gde = input()
print("files of dir:", end=" ")
print(*os.listdir(path=gde), sep=", ")

print("dirs: ", re.findall(r'\w+[^.]\w', str(os.listdir(path=gde))))
print("all files: ", re.findall(r"\w+[.]\w+", str(os.listdir(path=gde))))
