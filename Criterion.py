class Criterion:
    def __init__(self):
        self.name = ''
        self.weight = 0
        self.scales = []
        self.codes = []
        self.interval_bounds = []
        self.direction = True

    def input_name(self):
        self.name = input('Название критерия: ')
        if self.name == "":
            raise Exception('Некорректоне имя ')

    def input_waist(self):
        self.weight = int(input('вес критерия: '))
        if self.weight <= 0:
            raise Exception('Некорректный вес ')

    def input_scales(self):
        scale = input('Шкала1: ')
        count = 2
        while scale != "":
            self.scales.append(scale)
            scale = input('Шкала{}: '.format(count))
            count += 1
        if len(self.scales) < 2:
            raise Exception('Не может быть меньше 2-х шкал')

    def input_codes(self):
        for scale in self.scales:
            self.codes.append(int(input('Код({}): '.format(scale))))

    def input_interval_bounds(self):
        for i in range(len(self.scales) - 1):
            self.interval_bounds.append(float(input("Граница интервала мажду {} и {}: ".format(self.scales[i], self.scales[i+1]))))

    def input_direction(self):
        self.direction = bool(input('Стремление: '))

    def input_criterion(self):
        self.input_name()
        self.input_waist()
        self.input_scales()
        self.input_codes()
        self.input_interval_bounds()
        self.input_direction()

    def __str__(self):
        line = self.name + ':' + str(self.weight) + ':' + self.scales[0]
        for i in range(1, len(self.scales)):
            line += '/' + self.scales[i]
        line += ':' + str(self.codes[0])
        for i in range(1, len(self.codes)):
            line += '/' + str(self.codes[i])
        line += ':' + str(self.interval_bounds[0])
        for i in range(1, len(self.interval_bounds)):
            line += '/' + str(self.interval_bounds[i])
        line += ':' + str(self.direction)
        return line

    def value_of(self, s):
        l = s.split(':')
        self.name = l[0]
        self.weight = l[1]
        self.scales = l[2].split('/')
        codes = l[3].split('/')
        for code in codes:
            self.codes.append(int(code))
        interval_bounds = l[4].split('/')
        for bound in interval_bounds:
            self.interval_bounds.append(float(bound))
        self.direction = bool(l[5] == 'True\n')


def write_criterions_to_file(filename):
    count = int(input('Количество критериев: '))
    f = open(filename, 'a')
    for i in range(count):
        c = Criterion()
        c.input_criterion()
        f.write(str(c))
        f.write('\n')
    f.close()


def read_criterions(filename):
    f = open(filename,'r')
    criterions = []
    for line in f:
        if not line.startswith('#'):
            c = Criterion()
            c.value_of(line)
            criterions.append(c)
    f.close()
    return criterions
