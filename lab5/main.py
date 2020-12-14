from lab5.grammar import Grammar
from lab5.parser import Parser


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


def printANonTerminal(grammar, nt):
    prod = grammar.productions
    productions = nt + " -> "
    if grammar.productions.get(nt) is not None:
        for val in grammar.productions[nt]:
            productions += str(val) + ' | '
        productions = productions[:-2]
        productions += '\n'
        print(productions)
    else:
        print("None")


def printMenu():
    print("1. Print terminals")
    print("2. Print non-terminals")
    print("3. Print productions")
    print("4. Print starting symbol")
    print("5. Print a specific non-terminal")
    print("6. Parser Run")
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
        if inp == "5":
            nt = input("insert nonTerminal key: ")
            printANonTerminal(grammar, nt)
        if inp == "6":
            parser = Parser()
            w = ["a", "a", "c", "b", "c"]
            parser.run(w)
        if inp == "0":
            ok = 0
