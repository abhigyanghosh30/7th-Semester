import re
import sys
with open(sys.argv[1]) as f:
    total = 0
    count = 0
    for line in f.readlines():
        line = line.strip()
        stat = re.split('\D', line)
        count += 1
        total += float(stat[-2]+stat[-1])/pow(10, len(stat[-1]))
    print(count, total/count)
