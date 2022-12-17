
import sys
import functools
with open(sys.argv[1]) as f:
    pairs = [pair.split('\n') for pair in f.read().split('\n\n')]
    pairs = [[eval(p[0]), eval(p[1])] for p in pairs]

def compare(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l == r:
            return 0
        if l < r:
            return 1
        else:
            return -1
    if isinstance(l, list) and isinstance(r, int):
        return compare(l, [r])
    if isinstance(l, int) and isinstance(r, list):
        return compare([l], r)
    if isinstance(l, list) and isinstance(r, list):
        if len(l) == 0 and len(r) > 0:
            return 1
        elif len(l) > 0 and len(r) == 0:
            return -1
        elif len(l) == 0 and len(r) == 0:
            return 0
        elif len(l) == 1 and len(r) == 1:
            return compare(l[0], r[0])
        else:
            sub_compare = compare(l[0], r[0])
            if sub_compare == 0:
                return compare(l[1:], r[1:])
            else:
                return sub_compare


total = 0
for i in range(len(pairs)):
    correct_order = compare(pairs[i][0],pairs[i][1])
    # print(pairs[i][0], pairs[i][1], correct_order)
    print(total, i, correct_order)
    if correct_order == 1:
        total += i+1
print(total)

packets = [p[0] for p in pairs] + [p[1] for p in pairs]

print()
packets = sorted(packets, key=functools.cmp_to_key(compare))
packets.reverse()

print(packets.index([[2]])+1, packets.index([[6]])+1, (packets.index([[2]])+1) * (packets.index([[6]])+1))
