
class Rule:
    def __init__(self, criterion):
        self.bounds = criterion.interval_bounds
        self.codes = criterion.codes
        self.weight = criterion.weight
        self.direction = criterion.direction
        self.codes = criterion.codes
        if self.direction:
            self.bounds.reverse()
        if self.direction:
            self.codes.reverse()

    def apply(self, value):
        for i in range(len(self.bounds)):
            if value < self.bounds[i]:
                return self.codes[i]
        return self.codes[-1]

    def compare(self, value1, value2):
        if self.direction:
            if value1 < value2:
                #print('weight1 {}'.format(self.weight))
                return int(self.weight)
        else:
            if value2 < value1:
                #print('weight2 {}'.format(self.weight))
                return int(self.weight)
        #print('weight {}'.format(0))
        return 0
