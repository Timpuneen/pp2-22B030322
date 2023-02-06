class gtasix:
    def __init__(self):
        self.string=""
    def getString(self):
        self.string = input()
    def PrintString(self):
        print((self.string).upper())


obj = gtasix()
obj.getString()
obj.PrintString()

