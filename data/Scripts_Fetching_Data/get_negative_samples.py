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

def fetchData(window_size,size):
	website = "http://genome.ucsc.edu/cgi-bin/das/hg38/dna?segment="
	rounds = len(pos)
	if size != 0:
		rounds = size
	for i in range(rounds):
		file = open("Negative_Reads/human_negative_sub%s.fasta"%i,"w")
		chrms = pos[i][0]
		loci = pos[i][1]
		loci_lb = int(loci) - 50
		loci_ub = int(loci) + 50
		print loci
		for j in range (loci_lb,loci_ub):
			if j + window_size/2 != int(loci):
				tl = str(j)
				tu = str(j + window_size)
				seq_site = website + chrms +":"+tl + "," + tu
				response = urllib2.urlopen(seq_site)
				html = response.read().split("\n")[5]
				file.write("> %s:%s, %s \n" %(chrms,tl,tu))
				file.write(html)
				file.write("\n")
		print("%s / %s" %(i+1,len(pos)))
	file.close()

if __name__ == "__main__":
	pos = modified_chr_sites()
	window_size = int(sys.argv[1])
	size = int(sys.argv[2])
	fetchData(window_size,size)

