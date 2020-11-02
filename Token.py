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
    "&&": 40,
    "length": 41

}

operators = ['+', '-', '*', '/', '=', '<', '<=', '>', '>=', '&', '|', '||', '&&', '==']

reservedWords = ["if", "while", "read", "write", "for", "length", "int", "bool", "string", "character", "else",
                 "function", "true", "false"]

separators = ['(', ')', '[', ']', '{', '}', ';', ':']


def getTokens():
    tokens = {}
    currentId = 0
    with open("token.in", 'r') as file:
        for line in file:
            line = line.strip("\n")
            token = line
            if token == "":
                token = " "
            tokens[token] = currentId
            currentId += 1
        tokens['\n'] = currentId
    return tokens
