class Manufacturer:
    def __init__(self, pkey, name):
        self.name = name
        self.pkey = pkey

    def getPkey(self):
        return self.pkey

    def setPkey(self, pkey):
        self.pkey = pkey

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
