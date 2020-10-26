codes = {
    "identifier": 0,
    "constants": 1,
    " ": 2,
    "+": 3,
    "-": 4,
    "*": 5,
    "/": 6,
    "%": 7,
    "=": 8,
    "==": 9,
    "!=": 10,
    "<=": 11,
    ">=": 12,
    ">": 13,
    "<": 14,
    "#": 15,
    "int": 16,
    "bool": 17,
    "string": 18,
    "character": 19,
    "if": 20,
    "else": 21,
    "while": 22,
    "function:": 23,
    "read": 24,
    "write": 25,
    "true": 26,
    "false": 27,
    "for": 28,
    ":": 29,
    ";": 30,
    "(": 31,
    ")": 32,
    "{": 33,
    "}": 34,
    "[": 35,
    "]": 36,
    "&": 37,
    "|": 38,
    "||": 39,
    "&&": 40

}

operators = ['+', '-', '*', '/', '=', '<', '<=', '>', '>=', '&', '|']

reservedWords = ["int", "bool", "string", "character", "if", "else", "while", "function:", "read", "write", "true",
                 "false", "for"]

separators = ['(', ')', '[', ']', '{', '}', ';', ':']


def getTokens():
    tokens = {}
    currentId = 0
    with open("tokens.in", 'r') as file:
        for line in file:
            line = line.strip("\n")
            token = line
            if token == "":
                token = " "
            tokens[token] = currentId
            currentId += 1
        tokens['\n'] = currentId
    return tokens
