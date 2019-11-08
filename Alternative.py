
class Alternative:
    def __init__(self, line, number):
        self.number = number
        self.name = line.pop(0)
        self.values = []
        for v in line:
            if v != '':
                self.values.append(float(v))

    def __getitem__(self, item):
        return self.values[item]

    def __setitem__(self, key, value):
        self.values[key] = value

    def getlist(self):
        return self.values