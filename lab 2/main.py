
from model.sortedList import SortedList
from model.symbolTable import SymbolTable
if __name__ == '__main__':
   sortedList =  SortedList()
   symbolTable = SymbolTable()
   symbolTable.add("a")
   symbolTable.add("5")
   symbolTable.add("b")
   symbolTable.add("11")
   symbolTable.add("10")


   print(symbolTable.get("a"))
   print(symbolTable)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
