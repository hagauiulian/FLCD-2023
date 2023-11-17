import re

operators = ['%','+', '-', '/', '*', '=', '<', '<=', '>=', '>', '==']
separators = ['[', ']', '{', '}', '(', ')', ';', ' ']
reservedWords = ['char', 'int', 'boolean', 'real', 'input', 'print', 'if', 'else', 'break', 'for', 'while']

everything = operators + separators + reservedWords
def isPartOfOperator(char):
    for op in operators:
        if char in op:
            return True
    return False

def getOperatorToken(line, index):
    token = ''

    while index < len(line) and isPartOfOperator(line[index]):
        token += line[index]
        index += 1

    return token, index
def getStringToken(line, index):
    token = ''
    quoteCount = 0

    while index < len(line) and quoteCount < 2:
        if line[index] == '"' :
            quoteCount += 1
        token += line[index]
        index += 1
    return token, index

def tokenGenerator(line, separators):
    token = ''
    index = 0

    while index < len(line):
        if line[index] == '"':
            if token:
                yield token
            token, index = getStringToken(line, index)
            yield token
            token = ''

        elif isPartOfOperator(line[index]):
            if token:
                yield token
            token, index = getOperatorToken(line, index)
            yield token
            token = ''

        elif line[index] in separators:
            if token:
                yield token
            token, index = line[index], index + 1
            yield token
            token = ''

        else:
            token += line[index]
            index += 1
    if token:
        yield token

def isIdentifier(token):
    return re.match('^[a-zA-Z]([a-zA-Z]|[0-9]){,255}$', token) is not None

def isConstant(token):
    return re.match('^(0|[+-]?[1-9][0-9]*)$|^\'.\'$|^\".*\"$', token) is not None
