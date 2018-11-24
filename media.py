class Media:
    def __init__(self, media, title, location):
        self.media = media
        self.title = title
        self.location = location
        self.tags = []

    def setType(self, media):
        self.media = media

    def setTitle(self, title):
        self.title = title

    def setTags(self, tags):
        self.tags = tags

    def setLocation(self, location):
        self.location = location

    def addTag(self, tag):
        self.tags.append(tag)

    def getType(self):
        return self.type

    def getTitle(self):
        return self.title

    def getTags(self):
        return self.tags

    def getLocation(self):
        return self.location

    def __str__(self):
        return self.title
