import re
import sys

posSampsFileLoc = "C:\Users\Damon\Documents\Bio Informatics\\bioInformaticsMLm1a\data\Positive_Samples\\all_pos_folds.txt"
negSamsFileLoc0 = "C:\Users\Damon\Documents\Bio Informatics\\bioInformaticsMLm1a\data\Negative_Samples\\human_negative_sub0.txt"
negSamsFileLoc1 = "C:\Users\Damon\Documents\Bio Informatics\\bioInformaticsMLm1a\data\Negative_Samples\\human_negative_sub1.txt"
negSamsFileLoc2 = "C:\Users\Damon\Documents\Bio Informatics\\bioInformaticsMLm1a\data\Negative_Samples\\human_negative_sub2.txt"
negSamsFileLoc3 = "C:\Users\Damon\Documents\Bio Informatics\\bioInformaticsMLm1a\data\Negative_Samples\\human_negative_sub3.txt"
negSamsFileLoc4 = "C:\Users\Damon\Documents\Bio Informatics\\bioInformaticsMLm1a\data\Negative_Samples\\human_negative_sub4.txt"

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
                fileWrite.write("%f, %f\n" %( toWrite[0], toWrite[1]))
                toWrite = []

            count = count - 1

    fileWrite.close()

if __name__ == "__main__":
    fileToWrite = "C:\Users\Damon\Documents\Bio Informatics\\bioInformaticsMLm1a\data\Positive_Samples\\all_pos_folds_parsed.txt"
    #parseFolds(posSampsFileLoc, fileToWrite)
    parseFolds(negSamsFileLoc0, "C:\Users\Damon\Documents\Bio Informatics\\bioInformaticsMLm1a\data\Negative_Samples\\human_negative_sub0_parsed.txt")
    parseFolds(negSamsFileLoc1, "C:\Users\Damon\Documents\Bio Informatics\\bioInformaticsMLm1a\data\Negative_Samples\\human_negative_sub1_parsed.txt")
    parseFolds(negSamsFileLoc2, "C:\Users\Damon\Documents\Bio Informatics\\bioInformaticsMLm1a\data\Negative_Samples\\human_negative_sub2_parsed.txt")
    parseFolds(negSamsFileLoc3, "C:\Users\Damon\Documents\Bio Informatics\\bioInformaticsMLm1a\data\Negative_Samples\\human_negative_sub3_parsed.txt")
    parseFolds(negSamsFileLoc4, "C:\Users\Damon\Documents\Bio Informatics\\bioInformaticsMLm1a\data\Negative_Samples\\human_negative_sub4_parsed.txt")