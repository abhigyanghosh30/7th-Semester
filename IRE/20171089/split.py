import sys
with open(sys.argv[1]) as f:
    line = f.readline()
    while(line!=""):
        print(line[0])
        with open(line[0]+".txt",'a+') as outf:
            outf.write(line)
        line = f.readline()