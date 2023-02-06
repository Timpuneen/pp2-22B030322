ounces_koef = 28.3495231
def converter(grams):
    res=float(grams)/float(ounces_koef)
    return res
print(converter(input("how many grams ")))