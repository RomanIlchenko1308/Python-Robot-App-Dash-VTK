# --------------------------------------
# PythonRobotApp

# MoveFunction
def MoveFunction(current_row, destinationCol,
                 destination_row, destinationRow):
    # sedk size 5x5

    widthDesk = 5

    if currentRow == destination_row:
        return "POSSIBLE"
    elif currentCol == destinationCol:
        return "POSSIBLE"
    else:
        return "NOT POSSIBLE"


# Driver Code
currentRow = 0
currentCol = 0
destinationRow = 1
destinationCol = 5

output = MoveFunction(currentRow, currentCol, destinationRow, destinationCol)
print(output)


class Hey:
    globalName = "Roman"

    def __init__(self):
        print("--> __init__ Hey")
        self.global_init_name = self.globalName
        print(self.global_init_name)


class HelloMr(Hey):
    def __init__(self):
        print("--> __init__ HelloMr")
        super().__init__()
        self.lastName = "Ilchenko"

    def greetings(self):
        print("--> greetings HelloMr")
        return f"Good afternoon {self.globalName} {self.lastName}"


romanObj1 = Hey()

print("----------------")
romanObj2 = HelloMr()
greetingToRomanIlchenko = romanObj2.greetings()
print(greetingToRomanIlchenko)