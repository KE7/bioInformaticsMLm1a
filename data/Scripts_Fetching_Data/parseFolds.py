import re
import sys

posSampsFileLoc = "C:\Users\Damon\Documents\Bio Informatics\\bioInformaticsMLm1a\data\\positive_776_folds.txt"
negSamsFileLoc = "C:\Users\Damon\Documents\Bio Informatics\\bioInformaticsMLm1a\data\\negative_776_folds.txt"

def parseFolds(fileLoc, fileName):
    fileWrite = open(fileName, "w")

    foldPat = "( *-*\d+\.\d+ *)"
    toWrite = []

    with open(fileLoc, "r") as fileRead:
        for line in fileRead:
            if "> chr" in line:
                fileWrite.write(line)
                count = 3

            if (count == 1): # Fold Value
                m = re.search(foldPat, line)
                toWrite.append(float(m.group(0)))

            if (count == 0): # Free energy structure
                m = re.search(foldPat, line)
                toWrite.append(float(m.group(0)))
                print(toWrite)
                fileWrite.write("%f, %f\n" %( toWrite[0], toWrite[1]))
                toWrite = []

            count = count - 1

    fileWrite.close()

if __name__ == "__main__":
    parseFolds(posSampsFileLoc, "C:\Users\Damon\Documents\Bio Informatics\\bioInformaticsMLm1a\data\Positive_Samples\\all_pos_folds_parsed.txt")
    parseFolds(negSamsFileLoc, "C:\Users\Damon\Documents\Bio Informatics\\bioInformaticsMLm1a\data\Negative_Samples\\all_negative_folds_parsed.txt")