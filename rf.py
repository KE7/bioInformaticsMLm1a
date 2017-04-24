from sklearn.ensemble import RandomForestClassifier
import sys
import pickle
import numpy as np
import random

# Read fasta file
def ReadFASTA(filename):
    fp = open(filename, 'r')
    Sequences = []
    tmpname = ""
    tmpseq = ""
    for line in fp:
        if line[0] != ">" and line[0] != "n":
            Sequences.append(line)
    fp.close()
    return Sequences

def ReadCov(filename):
    fp = open(filename, 'r')
    Sequences = []
    for line in fp:
        strs = line.split()
        tmp = []
        if len(strs) != 20:
            print line
        for s in strs:
            tmp.append(float(s))
        Sequences.append(tmp)
    fp.close()
    return Sequences

# Get G/C content feature
def GetGC(seq):
    gc = []
    gc = [GetGCSeq(sequence) for sequence in seq]
    return gc

# Sub-function for G/C content
def GetGCSeq(seq):
    nGC = [0,0,0,0]
    for seg in xrange(4):
        nGC[seg] += seq[seg*5:(seg+1)*5].count("g") +\
            seq[seg*10:(seg+1)*10].count("c")
    return [float(1.0 * n / len(seq)) for n in nGC]

# Training and testing phase
if __name__ == "__main__":
    seq_pos_train = ReadFASTA('data/positive_776_train.fasta')
    seq_neg_train = ReadFASTA('data/negative_776_train.fasta')
    seq_pos_test = ReadFASTA('data/positive_776_test.fasta')
    seq_neg_test = ReadFASTA('data/negative_776_test.fasta')

    cov_pos_train = ReadCov('data/cov_pos_776_train.fasta')
    cov_neg_train = ReadCov('data/cov_neg_776_train.fasta')
    cov_pos_test = ReadCov('data/cov_pos_776_test.fasta')
    cov_neg_test = ReadCov('data/cov_neg_776_test.fasta')    
    
    gc_pos_train = GetGC(seq_pos_train)
    gc_neg_train = GetGC(seq_neg_train)
    gc_pos_test = GetGC(seq_pos_test)
    gc_neg_test = GetGC(seq_neg_test)

    for i in range(0, len(seq_pos_train)):
        for j in cov_pos_train[i]:
            gc_pos_train[i].append(float(j))
    for i in range(0, len(seq_neg_train)):
        for j in cov_neg_train[i]:
            gc_neg_train[i].append(float(j))
    for i in range(0, len(seq_pos_test)):
        for j in cov_pos_test[i]:
            gc_pos_test[i].append(float(j))
    for i in range(0, len(seq_neg_test)):
        for j in cov_neg_test[i]:
            gc_neg_test[i].append(float(j))

    model = RandomForestClassifier(criterion="entropy", n_estimators = 300,\
        max_depth = 100, class_weight={0:100, 1:1})

    data_train = np.array(list(gc_pos_train) + list(gc_neg_train), dtype = np.float)
    data_test = np.array(list(gc_pos_test) + list(gc_neg_test), dtype = np.float)
    print "G/C content feature matrix sample:"
    print data_train[0]
    print ""
    pos_len_train = len(gc_pos_train)
    neg_len_train = len(gc_neg_train)
    pos_len_test = len(gc_pos_test)
    neg_len_test = len(gc_neg_test)
    label_train = np.array([1 for x in xrange(pos_len_train)] +\
        [0 for x in xrange(neg_len_train)])
    label_test = np.array([1 for x in xrange(pos_len_test)] +\
        [0 for x in xrange(neg_len_test)])
    
    model = model.fit(data_train, label_train)
    result = model.predict(data_test)

    err = 0.0
    for i in range(0, len(result)):
        if result[i] != label_test[i]:
            err += 1.0

    err_rate = 1.0 * err / len(data_test)
    print "Error Rate:"
    print err_rate
    print ""
    print "Predict Label:"
    print result
