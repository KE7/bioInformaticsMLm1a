import urllib2
import sys
def modified_chr_sites():
	reads_loci_fn = "/Users/Alex/Desktop/DataPracticum/TroughData/trough_regions.csv"
	file = open(reads_loci_fn,"r")
	pos = []
	c = 0
	for line in file:
		if c >= 1:
			print line
			vals = line.split("\r\n")[0].split(",")
			site = []
			for i in range(0,3):
				site.append(vals[i])
			pos.append(site)
		c+=1
	file.close()
	print(len(pos))
	return(pos)

def fetchData(size):
	website = "http://genome.ucsc.edu/cgi-bin/das/hg38/dna?segment="
	rounds = len(pos)
	if size != 0:
		rounds = size
	file = open("human_negative_trough.fasta","w")
	for i in range(rounds):
		chrms = pos[i][0]
		left = pos[i][1]
		right = pos[i][2]
		print("%s to %s" %(left,right))
		loci_lb = int(left) - 40
		loci_ub = int(right) + 40
		for j in range (0,5):
			if j != 2:
				loci_left = int(loci_lb) + j * 20
				loci_right = int(loci_lb) + (j+1) * 20 - 1
				seq_site = website + chrms +":"+str(loci_left) + "," + str(loci_right)
				response = urllib2.urlopen(seq_site)
				html = response.read().split("\n")[5]
				if html != "":
					if html[0] in ["a","g","c","t"]:
						file.write(">%s:%s:%s\n" %(chrms,loci_left,loci_right))
						file.write(html+"\n")
				print("%s-%s" %(loci_left,loci_right))
		print("%s / %s" %(i+1,len(pos)))
	file.close()

if __name__ == "__main__":
	pos = modified_chr_sites()
	size = int(sys.argv[1])
	fetchData(size)

