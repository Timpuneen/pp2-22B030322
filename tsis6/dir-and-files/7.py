import os

first_file = open("orig.txt", "r")
second_file = open("copiya.txt", "a")

for line in first_file.readlines():
    second_file.write(line)

