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


