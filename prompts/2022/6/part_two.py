
import sys
with open(sys.argv[1]) as f:
    for line in f:
        data = line.strip()
        marker = 'XXXXXXXXXXXXXX'
        index = 0
        for i in range(len(data)):
            substring = data[i:i+len(marker)]
            if len(set(substring)) == len(marker):
                index = i + len(marker) - 1
                break
        print(index)