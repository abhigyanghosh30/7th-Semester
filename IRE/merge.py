import sys
out = open(sys.argv[3], 'w+')
with open(sys.argv[1]) as f1:
    with open(sys.argv[2]) as f2:
        line1 = f1.readline()
        line2 = f2.readline()
        word1 = line1.split(":")[0]
        word2 = line2.split(":")[0]
        while line1 != "" and line2 != "":
            if word1 < word2:
                out.write(line1)
                line1 = f1.readline()
                word1 = line1.split(":")[0]
            else:
                out.write(line2)
                line2 = f2.readline()
                word2 = line2.split(":")[0]
        while(line1 != ""):
            out.write(line1)
            word1 = line1.split(":")[0]
            line1 = f1.readline()

        while(line2 != ""):
            out.write(line2)
            word2 = line2.split(":")[0]
            line2 = f2.readline()

out.close()
