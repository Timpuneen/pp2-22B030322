#this is the task number 12 but I needed to rename it because of the task number 14
def histogram(list):
    for item in list:
        for i in range(item):
            print('*', end = '')
        print()

histogram([4, 9, 7])