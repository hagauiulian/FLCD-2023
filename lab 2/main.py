from model.sortedList import SortedList
from model.symbolTable import SymbolTable
from model.scanner import *
from model.language_specification import *
from model.pif import ProgramInternalForm

if __name__ == '__main__':
    fileName = input("Enter filename:")

    #file = open(fileName, 'r')
    # for line in file:
    # print(line)

    with open(fileName, 'r') as file:
        for line in file:
            print([token for token in tokenGenerator(line, everything)])

    symbolTable = SymbolTable()
    pif = ProgramInternalForm()

    with open(fileName, 'r') as file:
        lineNo = 0
        for line in file:
            lineNo += 1
            for token in tokenGenerator(line[0:-1], everything):
                if token == ' ':
                    continue
                if token in separators + operators + reservedWords:
                    pif.add(token, -1)
                elif isIdentifier(token):
                    id = symbolTable.add(token)
                    pif.add('id', id)
                elif isConstant(token):
                    id = symbolTable.add(token)
                    pif.add('const', id)
                else:
                    raise Exception('Unknown token ' + token + ' at line ' + str(lineNo))

    print('Program Internal Form: \n', pif)
    print('Symbol Table: \n', symbolTable)
