class ProgramInternalForm:
    def __init__(self):
        self.__content = []

    def add(self, content, id):
        self.__content.append((content, id))

    def __str__(self):
        return str(self.__content)