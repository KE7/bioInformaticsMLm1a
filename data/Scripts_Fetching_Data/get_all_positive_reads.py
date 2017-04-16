

import urllib2
import sys
def modified_chr_sites():
	reads_loci_fn = "/Users/Alex/Desktop/DataPracticum/GSE70485_human_peaks.txt"
	file = open(reads_loci_fn,"r")
	pos = []
	c = 0
	for line in file:
		if c >= 1:
			vals = line.split("\t")
			if "HEPG2" in vals[4]:
				site = []
				for i in range(0,2):
					site.append(vals[i])
				pos.append(site)
		c+=1
	file.close()
	print(len(pos))
	return(pos)

def fetchData(window_size,file_name):
	website = "http://genome.ucsc.edu/cgi-bin/das/hg38/dna?segment="
	file = open(file_name,"w")
	for i in range(len(pos)):
		chrms = pos[i][0]
		loci = pos[i][1]
		loci_left = str(int(loci) - window_size/2)
		loci_right = str(int(loci) + window_size/2)
		seq_site = website + chrms +":"+loci_left + "," + loci_right
		response = urllib2.urlopen(seq_site)
		html = response.read().split("\n")[5]
		file.write("> %s:%s, %s \n" %(chrms,loci_left,loci_right))
		file.write(html)
		file.write("\n")
		print("%s / %s" %(i+1,len(pos)))
	file.close()

if __name__ == "__main__":
	pos = modified_chr_sites()
	window_size = int(sys.argv[1])
	file_name = sys.argv[2]
	fetchData(window_size,file_name)

