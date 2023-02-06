def reverser(str):
    my_list = list(str.split())
    result = ""
    for slovo in my_list[::-1]:
        result += slovo+' '
    return result
print(reverser(input()))