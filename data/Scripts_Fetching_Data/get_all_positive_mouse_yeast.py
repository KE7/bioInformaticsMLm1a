import urllib2
import sys

def modified_chr_sites(reads_loci_fn):
    file = open(reads_loci_fn, "r")
    pos = []
    c = 0
    for line in file:
        if c >= 1:
            vals = line.split("\t")
            pos.append([vals[0], vals[1]])
        c += 1
    file.close()
    print(len(pos))
    return pos

def fetchData(windowSize, fileName, website):
    file = open(fileName, "w")
    for i in range(len(pos)):
        chrms = pos[i][0]
        loci = pos[i][1]
        lociLeft = str(int(loci) - windowSize/2)
        lociRight = str(int(loci) + windowSize/2)
        seqSite = website + chrms + ":" + lociLeft + "," + lociRight

        response = urllib2.urlopen(seqSite)
        try:
            html = response.read().split("\n")[5]

            file.write("> %s:%s, %s \n" % (chrms, lociLeft, lociRight))
            file.write(html)
            file.write("\n")
        except:
            print("Error at %d" % i)
            print(html)
            raw_input("Press Enter to continue...")

        print("%s / %s" %(i+1, len(pos)))

    file.close()


if __name__ == "__main__":
    windowSize = int(sys.argv[1])
    # Mouse
    reads_loci_fn = "C:\Users\Damon\Documents\Bio Informatics\\bioInformaticsMLm1a\data\Dominissini_Raw_Peaks\GSE70485_mouse_peaks.txt"
    pos = modified_chr_sites(reads_loci_fn)
    website = "http://genome.ucsc.edu/cgi-bin/das/mm10/dna?segment="
    fileName = "C:\Users\Damon\Documents\Bio Informatics\\bioInformaticsMLm1a\data\Positive_Samples\\all_pos_mouse.fasta"
    # fetchData(windowSize, fileName, website)

    # Yeast
    reads_loci_fn = "C:\Users\Damon\Documents\Bio Informatics\\bioInformaticsMLm1a\data\Dominissini_Raw_Peaks\GSE70485_yeast_peaks.txt"
    pos = modified_chr_sites(reads_loci_fn)
    website = "http://genome.ucsc.edu/cgi-bin/das/sacCer3/dna?segment="
    fileName = "C:\Users\Damon\Documents\Bio Informatics\\bioInformaticsMLm1a\data\Positive_Samples\\all_pos_yeast.fasta"
    fetchData(windowSize, fileName, website)