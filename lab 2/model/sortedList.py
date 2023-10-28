class SortedList:
    def __init__(self):
        self.__list = []
        self.__count = 0

    def getId(self,value):
        for i in self.__list:
            if i[0] == value:
                return i[1]
        return -1

    def sort(self):
        l = self.__list
        for i in range(0,len(self.__list)):
            for j in range(i+1,len(self.__list)):
                if l[i][0] >= l[j][0]:
                    l[i], l[j] = l[j], l[i]
        return self.__list
    def add(self,value):
        id = self.getId(value)
        if id != -1:
            return id
        self.__list.append((value,self.__count))
        self.__count +=1
        self.__list = self.sort()
        return self.__count - 1
        #self.__list = sorted(self.__list, key=lambda x:x[0])


    def __str__(self):
        return str(self.__list)