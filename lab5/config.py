from lab4.State import State


class WorkElement:
    def __init__(self, val, productionNumber: int = 0):
        self.value = val
        self.productionNumber = productionNumber

    def __str__(self):
        if self.productionNumber == 0:
            return str(self.value)
        else:
            return str(self.value) + "->" + str(self.productionNumber)


class Configuration:
    def __init__(self, startingSymbol):
        self.state = State.NORMAL
        self.index = 1
        self.workStack = []
        self.inputStack = [startingSymbol]

    def __str__(self):
        workStackString = "Start: WorkStack #{ "
        for element in self.workStack:
            workStackString += str(element) + " ,"
        workStackString = workStackString[:-2]
        workStackString += "}# End WorkStack"

        return "(" + self.state + " ," + str(self.index) + " ," + workStackString + " ," + str(self.inputStack) + ")"
