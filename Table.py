import re
from Alternative import Alternative
from Criterion import Criterion, read_criterions
from Rule import Rule
from Table_printer import print_table


class Table:
    def __init__(self):
        self.colon_names = []
        self.colon_rules = []
        self.lines = []

    def read(self, filename1, filename2):
        f = open(filename1, 'r')
        i = 1
        for line in f:
            if line[0] != '#':
                line = re.split(r'\s+', line)
                self.lines.append(Alternative(line, number=i))
                i += 1
        f.close()

        criterions = read_criterions(filename2)
        table = []
        table.append('split')
        table.append(['Название', 'Вес', 'Шкала', 'Код', 'Стремление', ''])
        count = 2
        for criterion in criterions:
            table.append('split')
            count += 1
            for i in range(len(criterion.scales)):
                count += 1
                if i == len(criterion.scales)//2:
                    table.append([criterion.name, criterion.weight, criterion.scales[i], criterion.codes[i], criterion.direction, ''])
                else:
                    table.append(['', '', criterion.scales[i], criterion.codes[i], '', ''])
        table.append('split')
        count += 1
        print_table(table, count, 6)

        for criterion in criterions:
            self.colon_names.append(criterion.name)
            self.colon_rules.append(Rule(criterion))

        self.print_table()

    def print_table(self):
        print()
        print()
        table = []
        table.append('split')
        t = []
        t.append('')
        t.extend(self.colon_names)
        t.append('')
        table.append(t)
        table.append('split')
        count = 3

        for l in self.lines:
            t = []
            t.append(str(l.number) + '. ' + l.name)
            t.extend(l.getlist())
            t.append(' ')
            table.append(t)
            table.append('split')
            count += 2

        print_table(table, count, len(l.getlist()) + 2)

    def apply_rules(self):
        for i in range(len(self.lines)):
            for j in range(len(self.colon_rules)):
                self.lines[i][j] = self.colon_rules[j].apply(self.lines[i][j])


    def electre(self, value=1):
        table = []
        title = []
        best = []
        for i in range(len(self.lines)):
            title.append(' {}'.format(i + 1))
            best.append([])
            best[i].append('{}. {}'.format(self.lines[i].number, self.lines[i].name))
            best[i].append(0)
            table.append([])
            table[i].append('{}. {}'.format(self.lines[i].number, self.lines[i].name))
            for j in range(len(self.lines)):
                if i == j:
                    table[i].append(' x ')
                else:
                    P = 0
                    N = 0
                    for r in range(len(self.colon_rules)):
                        N += self.colon_rules[r].compare(self.lines[i][r], self.lines[j][r])
                        P += self.colon_rules[r].compare(self.lines[j][r], self.lines[i][r])
                    if N == 0:
                        if P != 0:
                            table[i].append(' inf ')
                            best[i][1] += 1
                        else:
                            table[i].append(' - ')
                    elif P/N > value:
                        best[i][1] += 1
                        table[i].append(' %.2f ' % (P/N))
                    else:
                        table[i].append(' - ')

        for i in range(len(table)):
            table[i].append('')

        title.insert(0, '')
        title.append('')
        table.insert(0, title)
        table.insert(1,'split')
        print_table(table, len(table), len(self.lines) + 2)

        print()
        print()
        best.sort(key=lambda x: x[1], reverse=True)
        print_table(best,len(best),2)



