import sys
outf = open(sys.argv[2],'w+')
currword = "" 
with open(sys.argv[1]) as f:
    line = f.readline()
    while(line!=""):        
        words = line.split(':')
        if currword == words[0]:
            outf.write(",")
            outf.write(words[1].strip())
        else:
            outf.write("\n")
            outf.write(line.strip())
        currword = words[0]
        line = f.readline()
outf.close()
