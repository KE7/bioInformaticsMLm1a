import sys

def ReadFASTA_pos(filename):
    fp = open(filename, 'r')
    wp1 = open('data/positive_776_train.fasta', 'w')
    wp2 = open('data/positive_776_test.fasta', 'w')
    pre = ""
    cnt = 0
    for line in fp:
        if line[0] == ">":
            pre = line
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
    wp1 = open('data/negative_776_train.fasta', 'w')
    wp2 = open('data/negative_776_test.fasta', 'w')
    pre = ""
    cnt = 0
    for line in fp:
        if line[0] == ">":
            pre = line
        else:
            if cnt < 6000:
                wp1.write(pre)
                wp1.write(line)
            else:
                wp2.write(pre)
                wp2.write(line)
        cnt += 1
    fp.close()
    wp1.close()
    wp2.close()

def ReadFASTA_folds_pos(filename):
    fp = open(filename, 'r')
    wp1 = open('data/positive_folds_train.fasta', 'w')
    wp2 = open('data/positive_folds_test.fasta', 'w')
    pre = ""
    cnt = 0
    for line in fp:
        if line[0] == ">":
            pre = line
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

def ReadFASTA_folds_neg(filename):
    fp = open(filename, 'r')
    wp1 = open('data/negative_folds_train.fasta', 'w')
    wp2 = open('data/negative_folds_test.fasta', 'w')
    pre = ""
    cnt = 0
    for line in fp:
        if line[0] == ">":
            pre = line
        else:
            if cnt < 6000:
                wp1.write(pre)
                wp1.write(line)
            else:
                wp2.write(pre)
                wp2.write(line)
        cnt += 1
    fp.close()
    wp1.close()
    wp2.close()

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
        cnt += 1
    fp.close()
    wp1.close()
    wp2.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cov_file = sys.argv[1]
        fp = open(cov_file, 'r')
        wp = open('data/mouse_pos_cov_norm.fasta', 'w')
        for line in fp:
            strs = line.split()
            idx = line.find(strs[3])
            wp.write(line[idx:])
        fp.close()
        wp.close()