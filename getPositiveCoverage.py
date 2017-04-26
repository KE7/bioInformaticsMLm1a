import pysam

# get trough regions
def getTroughRegions():
	bedFile = open("trough_regions.csv","r")
	c = 0
	regions = []
	for line in bedFile:
		if c > 0:
			region = line.split("\r\n")[0].split(",")
			regions.append(region)
			print line
		c += 1
	return regions

# find the coverage at specified regions
def processBamFile(chrNum,start,stop):
	samfile = pysam.AlignmentFile("/Users/Alex/Desktop/DataPracticum/Coverage/aln776_sort.bam", "rb")
	results = []
	for pileupcolumn in samfile.pileup(chrNum, start-1, stop-1):
		if pileupcolumn.pos in range(start-1,stop):
			if pileupcolumn.n > 0:
				results.append(pileupcolumn.n)
			else:
				results.append(0)
	samfile.close()
	return "\t".join([str(x) for x in results])

if __name__ == "__main__":
	regions = getTroughRegions()
	file = open("coverage_positive_776.txt","w")
	results = []
	for region in regions:
		if int(region[2])-int(region[1]) == 20:
			file.write("\t".join(region)+"\t"+processBamFile(region[0],int(region[1]),int(region[2]))+"\n")
	file.close()