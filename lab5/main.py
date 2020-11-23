from lab5.Grammar import Grammar


def printProductions(grammar):
    productions = "Productions:\n"
    for prod in grammar.productions.keys():
        productions += prod + " -> "
        for val in grammar.productions[prod]:
            productions += str(val) + ' | '
        productions = productions[:-2]
        productions += '\n'
    print(productions)


def printTerminals(grammar):
    terminals = "Terminals: "
    for terminal in grammar.terminals:
        terminals += terminal + " "

    print(terminals)


def printNonTerminals(grammar):
    nonterminals = "Nonterminals: "
    for nonterminal in grammar.nonTerminals:
        nonterminals += nonterminal + " "

    print(nonterminals)


def printStartingSymbol(grammar):
    print(f"Starting symbol: {grammar.start}")


def printMenu():
    print("1. Print terminals")
    print("2. Print non-terminals")
    print("3. Print productions")
    print("4. Print starting symbol")
    print("0. Exit")


if __name__ == "__main__":
    ok = 1
    while ok == 1:
        printMenu()
        inp = input("input option:")
        grammar = Grammar("g1.in")
        if inp == "1":
            printTerminals(grammar)
        if inp == "2":
            printNonTerminals(grammar)
        if inp == "3":
            printProductions(grammar)
        if inp == "4":
            printStartingSymbol(grammar)
        if inp == "0":
            ok = 0
