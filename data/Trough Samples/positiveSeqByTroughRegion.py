

import urllib2
import sys
def modified_chr_sites():
	reads_loci_fn = "/Users/Alex/Desktop/DataPracticum/TroughData/trough_regions.csv"
	file = open(reads_loci_fn,"r")
	pos = []
	c = 0
	for line in file:
		print line
		if c >= 1:
			print line
			vals = line.split("\r\n")[0].split(",")
			print vals
			site = []
			for i in range(0,3):
				site.append(vals[i])
			pos.append(site)
		c+=1
	file.close()
	print(len(pos))
	return(pos)

def fetchData():
	website = "http://genome.ucsc.edu/cgi-bin/das/hg38/dna?segment="
	file = open("human_positive_trough.fasta","w")
	for i in range(len(pos)):
		chrms = pos[i][0]
		loci_left = pos[i][1]
		loci_right = pos[i][2]
		seq_site = website + chrms +":"+str(loci_left) + "," + str(loci_right)
		response = urllib2.urlopen(seq_site)
		html = response.read().split("\n")[5]
		if html != "":
			if html[0] in ["a","g","c","t"]:
				file.write(">%s:%s:%s\n" %(chrms,loci_left,loci_right))
				file.write(html)
				file.write("\n")
		print("%s / %s" %(i+1,len(pos)))
	file.close()

if __name__ == "__main__":
	pos = modified_chr_sites()
	fetchData()
