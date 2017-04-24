import sys

def ReadFASTA_pos(filename):
    fp = open(filename, 'r')
    wp1 = open('data/positive_776_1.fasta', 'w')
    wp2 = open('data/positive_776_2.fasta', 'w')
    pre = ""
    cnt = 0
    for line in fp:
        if line[0] == ">":
            pre = line[0] + str(cnt) + "\n"
        else:
            if cnt < 2000:
                wp1.write(pre)
                wp1.write(line)
            else:
                wp2.write(pre)
                wp2.write(line)
        cnt += 1
    fp.close()
    wp1.close()
    wp2.close()

def ReadFASTA_neg(filename):
    fp = open(filename, 'r')
    wp1 = open('data/negative_776_1.fasta', 'w')
    wp2 = open('data/negative_776_2.fasta', 'w')
    wp3 = open('data/negative_776_3.fasta', 'w')
    wp4 = open('data/negative_776_4.fasta', 'w')
    wp5 = open('data/negative_776_5.fasta', 'w')
    pre = ""
    cnt = 0
    for line in fp:
        if line[0] == ">":
            pre = line[0] + str(cnt) + "\n"
        else:
            if cnt < 2000:
                wp1.write(pre)
                wp1.write(line)
            elif cnt < 4000:
                wp2.write(pre)
                wp2.write(line)
            elif cnt < 6000:
                wp3.write(pre)
                wp3.write(line)
            elif cnt < 8000:
                wp4.write(pre)
                wp4.write(line)
            else:
                wp5.write(pre)
                wp5.write(line)
        cnt += 1
    fp.close()
    wp1.close()
    wp2.close()
    wp3.close()
    wp4.close()
    wp5.close()

def split_pos():
    fp = open('data/coverage_pos_776_norm.txt', 'r')
    wp1 = open('data/cov_pos_776_train.fasta', 'w')
    wp2 = open('data/cov_pos_776_test.fasta', 'w')
    cnt = 0
    for line in fp:
        strs = line.split()
        idx = line.find(strs[3])
        if cnt < 1000:
            wp1.write(line[idx:])
        else:
            wp2.write(line[idx:])
            # wp2.write(strs[3:len(strs)])
        cnt += 1
    fp.close()
    wp1.close()
    wp2.close()

def split_neg():
    fp = open('data/coverage_neg_776_norm.txt', 'r')
    wp1 = open('data/cov_neg_776_train.fasta', 'w')
    wp2 = open('data/cov_neg_776_test.fasta', 'w')
    cnt = 0
    for line in fp:
        strs = line.split()
        idx = line.find(strs[3])
        if cnt < 3000:
            wp1.write(line[idx:])
        else:
            wp2.write(line[idx:])
            # wp2.write(strs[3:len(strs)])
        cnt += 1
    fp.close()
    wp1.close()
    wp2.close()

if __name__ == "__main__":
    ReadFASTA_pos('data/positive_776.txt')
    ReadFASTA_neg('data/negative_776.txt')
    split_pos()
    split_neg()
