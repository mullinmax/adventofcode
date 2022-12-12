class monkey():
    def __init__(self, raw_str):
        lines = raw_str.strip().split('\n')
        self.id = int(lines[0].strip().split(' ')[1][:-1])
        self.items = [int(i.strip()) for i in lines[1].strip().split(':')[1].split(',')]
        raw_op_str = lines[2].strip().split(':')[1].split('=')[1].strip()
        if raw_op_str == 'old * old':
            self.operation = lambda x: x*x
        elif raw_op_str == 'old + old':
            self.operation = lambda x: x+x
        elif '+' in raw_op_str:
            op_str_const = int(raw_op_str.split(' ')[-1])
            self.operation = lambda x: x + op_str_const
        elif '*' in raw_op_str:
            op_str_const = int(raw_op_str.split(' ')[-1])
            self.operation = lambda x: x * op_str_const
        self.test = int(lines[3].strip().split(' ')[-1])
        self.test_true_monkey = int(lines[4].strip().split(' ')[-1])
        self.test_false_monkey = int(lines[5].strip().split(' ')[-1])
        self.total_inspections = 0

    def inspect(self):
        self.items = [self.operation(item) for item in self.items]
        self.total_inspections += len(self.items)
        # for i in range(len(self.items)):
        #     old = self.items[i]
        #     self.total_inspections += 1
        #     self.items[i] = eval(self.operation)
        #     # print(f'inspect {old} -> {self.items[i]}')

    def releif(self, amt):
        for i in range(len(self.items)):
            if self.items[i] > amt :
                self.items[i] = self.items[i] % amt

    def throw(self, monkeys):
        true_items = []
        false_items = []
        for item in self.items:
            if item % self.test == 0:
                true_items.append(item)
            else:
                false_items.append(item)

        monkeys[self.test_true_monkey].items += true_items
        monkeys[self.test_false_monkey].items += false_items
        self.items = []

import sys
with open(sys.argv[1]) as f:
    raw_monkey_strings = f.read().split('\n\n')


# print(raw_monkey_strings)
# print(monkey(raw_monkey_strings[0]))

monkeys = []
for raw_monkey_string in raw_monkey_strings:
    monkeys.append(monkey(raw_monkey_string))


releif_value = 1
for m in monkeys:
    releif_value *= m.test
print(releif_value)

for r in range(10000):
    # print(r, max([max(m.items+[0]) for m in monkeys]))
    for monkey in monkeys:
        monkey.inspect()
        monkey.releif(releif_value)
        throws = monkey.throw(monkeys)
    if (r+1) % 1000 == 0:
        print(f'-----{r+1}-----')
        for monkey in monkeys:
            print(monkey.id, monkey.total_inspections)

sl = sorted([monkey.total_inspections for monkey in monkeys])
print(sl)
print(sl[-1], sl[-2])
print(sl[-1] * sl[-2])