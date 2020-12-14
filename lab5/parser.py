from lab5.ParserTree import ParserTree
from lab5.grammar import Grammar
from lab5.config import *


class Parser:
    def __init__(self):
        self.grammar = Grammar("g1.in")
        self.config = Configuration(self.grammar.start)
        self.parserOutput = ParserTree(self.grammar)

    def expand(self):
        nonTerminal = self.config.inputStack.pop(0)

        firstProduction = self.grammar.productions[nonTerminal][0]

        workElement = WorkElement(nonTerminal, 1)

        self.config.workStack.append(workElement)

        self.config.inputStack = firstProduction + self.config.inputStack

    def advance(self):
        self.config.index += 1
        terminal = self.config.inputStack.pop(0)
        elem = WorkElement(terminal)
        self.config.workStack.append(elem)

    def momentaryInsucces(self):
        self.config.state = State.BACK

    def back(self):
        self.config.index -= 1
        topWorkStack = self.config.workStack.pop(-1)
        self.config.inputStack.insert(0, topWorkStack.value)

    def anotherTry(self):
        topWorkStack = self.config.workStack.pop(-1)
        # (nonTerminal, productionNumber) = topWorkStack.split("#")
        nonTerminal = topWorkStack.value
        productionNumber = topWorkStack.productionNumber

        productionNumber = int(productionNumber)

        productions = self.grammar.productions[nonTerminal]

        currentProduction = productions[productionNumber - 1]

        if productionNumber != len(productions):
            nextProduction = productions[productionNumber]

            self.config.state = State.NORMAL
            self.config.inputStack = self.config.inputStack[len(currentProduction):]

            nextInd = productionNumber + 1

            # self.__configuration.workStack.append(
            #     nonTerminal + "#" + str(nextInd))

            self.config.workStack.append(WorkElement(nonTerminal, nextInd))

            self.config.inputStack = nextProduction + self.config.inputStack

        elif self.config.index == 1 and nonTerminal == self.grammar.start:
            self.config.state = State.ERROR

        else:
            self.config.inputStack[:] = self.config.inputStack[len(currentProduction):]

            # self.__configuration.inputStack.insert(
            #     0, topWorkStack.split("#")[0])
            self.config.inputStack.insert(0, nonTerminal)

    def success(self):
        self.config.state = State.FINAL

    def run(self, w):
        while self.config.state != State.FINAL and self.config.state != State.ERROR:
            # print(self.__configuration)

            if self.config.state == State.NORMAL:
                if not self.config.inputStack and self.config.index == len(w) + 1:
                    self.success()
                else:
                    if len(self.config.inputStack) > 0 and self.config.inputStack[0] in self.grammar.nonTerminals:
                        self.expand()
                    else:
                        if len(self.config.inputStack) > 0 and self.config.index <= len(w) and \
                                self.config.inputStack[0] == w[self.config.index - 1]:
                            self.advance()
                        else:
                            self.momentaryInsucces()
            else:
                if self.config.state == State.BACK:
                    if self.config.workStack[-1].value in self.grammar.terminals:
                        self.back()
                    else:
                        self.anotherTry()

        if self.config.state == State.ERROR:
            print("ERROR")
        else:
            print("Secventa este acceptata")
            print("final configuration: " + str(self.config))
            production = []
            for elem in self.config.workStack:
                if elem.productionNumber != 0:
                    production.append(elem)
            print("Production string:" + str(['{0}'.format(element) for element in production]))
            self.parserOutput.createTree(production)
