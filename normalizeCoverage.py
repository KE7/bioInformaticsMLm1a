
import sys
def normalize(line):
	values = line.split()
	pos = values[0:3]
	covs = values[3:23]
	["0" if v is None else v for v in covs]
	if len(covs) == 20:
		covs = map(float,covs)
		[v + 1.0 for v in covs]
		sums = sum(covs)
		covs = [v/sums for v in covs]
		outLine = "\t".join(pos + map(str,covs)) + "\n"
		return outLine
	covs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	outLine = "\t".join(map(str,covs)) + "\n"
	return outLine


if __name__ == "__main__":
	tp = sys.argv[1]
	fn = "data/coverage_positive_776.txt"
	ofn = "data/coverage_pos_776_norm.txt"
	if tp == "-":
		fn = "data/coverage_negative_trough_776.txt"
		ofn= "data/coverage_neg_776_norm.txt"
	inF = open(fn,'r')
	ouF = open(ofn,'w')
	for line in inF:
		ouF.write(normalize(line))
	inF.close()
	ouF.close()