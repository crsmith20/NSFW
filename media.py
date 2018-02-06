class Media:
    def __init__(self, type, title, tags):
        self.__type = type
        self.__title = title
        self.__tags = tags

    def setType(self, type):
        self.__type = type

    def setTitle(self, title):
        self.__title = title

    def setTags(self, tag):
        self.__tags.add(type)

    def getType(self):
        return self.__type

    def getTitle(self):
        return self.__title

    def getTags(self):
        return self.__tags
