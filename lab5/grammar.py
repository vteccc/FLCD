class Grammar:
    def __init__(self, file):
        self.start = ""
        self.productions = {}
        self.terminals = []
        self.nonTerminals = []
        self.file = file
        self.readFromFile()
        self.validateProduction()
        self.validateStartingSymbol()

    def readFromFile(self):
        '''
        As the name implies we read from a file
        '''
        with open(self.file, "r") as inputFile:
            self.nonTerminals = inputFile.readline().strip().strip(" ")
            self.terminals = inputFile.readline().strip().split(" ")
            self.start = inputFile.readline().strip()
            for line in inputFile.readlines():
                self.productions[line.split(
                    "-")[0].strip()] = [val.strip().split(" ") for val in line.split("-")[1].strip().split("|")]

    def validateStartingSymbol(self):
        '''
        :return: an exeception is not in the list of nonTerminals
        '''
        if self.start not in self.nonTerminals:
            raise Exception(f"Starting symbol {self.start} is not in the list of nonTerminals")

    def validateProduction(self):
        '''
        :return: an exception if the Lhs is not in the list of nonTerminals or if rhs is not in the list of terminals or nonTerminals
        '''
        for nonterminal in self.productions.keys():
            if nonterminal not in self.nonTerminals:
                raise Exception(
                    f"Lhs {nonterminal} is not in the list of nonTerminals")
            for prod in self.productions[nonterminal]:
                for prod2 in prod:
                    if prod2 not in self.nonTerminals and prod2 not in self.terminals:
                        raise Exception(
                            f"{prod2} is not in the list of terminals or nonTerminals")

    def getProductionsOfNonTerminals(self, symbol):
        if not symbol in self.nonTerminals:
            return None
        return self.productions[symbol]

    def getNextProduction(self, symbol, production):
        productions = self.getProductionsOfNonTerminals(symbol)
        for i in range(len(productions)):
            if production == production[i] and i < len(productions) - 1:
                return productions[i + 1]
        return None

    def nonTerminals(self):
        return self.nonTerminals

    def terminals(self):
        return self.terminals

    def productions(self):
        return self.productions

    def start(self):
        return self.start
