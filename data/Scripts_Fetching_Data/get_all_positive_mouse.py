import urllib2
import sys

def modified_chr_sites(reads_loci_fn):
    file - open(reads_loci_fn, "r")
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

def fetchData(window_size, file_name, website):
    file = open(file_name, "w")
    for i in range(len(pos)):
        chrms = pos[i][0]


if __name__ == "__main__":
    reads_loci_fn = "C:\Users\Damon\Documents\Bio Informatics\\bioInformaticsMLm1a\data\Dominissini_Raw_Peaks\GSE70485_mouse_peaks.txt"
	pos = modified_chr_sites(reads_loci_fn)
    website = "http://genome.ucsc.edu/cgi-bin/das/hg38/dna?segment="