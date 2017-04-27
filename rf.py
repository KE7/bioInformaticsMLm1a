from sklearn.ensemble import RandomForestClassifier
from processData import *
from normalizeCoverage import *
import sys
import numpy as np
import random

# Read fasta file
def ReadFASTA(filename):
    fp = open(filename, 'r')
    Sequences = []
    labels = []
    tmpname = ""
    tmpseq = ""
    for line in fp:
        if line[0] != ">" and line[0] != "n":
            Sequences.append(line)
        if line[0] == ">":
            labels.append(line)
    fp.close()
    return (labels, Sequences)

# Read the RT file
def ReadCov(filename):
    fp = open(filename, 'r')
    Sequences = []
    for line in fp:
        strs = line.split()
        tmp = []
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

def GetModel():
    (label_pos_train, seq_pos_train) = ReadFASTA('data/positive_776_train.fasta')
    (label_neg_train, seq_neg_train) = ReadFASTA('data/negative_776_train.fasta')

    cov_pos_train = ReadCov('data/cov_pos_776_train.fasta')
    cov_neg_train = ReadCov('data/cov_neg_776_train.fasta')    
    
    gc_pos_train = GetGC(seq_pos_train)
    gc_neg_train = GetGC(seq_neg_train)

    for i in range(0, len(seq_pos_train)):
        for j in cov_pos_train[i]:
            gc_pos_train[i].append(float(j))
    for i in range(0, len(seq_neg_train)):
        for j in cov_neg_train[i]:
            gc_neg_train[i].append(float(j))

    model = RandomForestClassifier(criterion="entropy", n_estimators = 300,\
        max_depth = 100, class_weight={0:100, 1:1})

    data_train = np.array(list(gc_pos_train) + list(gc_neg_train),\
        dtype = np.float)

    print "Feature matrix sample:"
    print data_train[0]
    print ""
    pos_len_train = len(gc_pos_train)
    neg_len_train = len(gc_neg_train)

    label_train = np.array([1 for x in xrange(pos_len_train)] +\
        [0 for x in xrange(neg_len_train)])

    
    model = model.fit(data_train, label_train)
    

    return model

def validate(model):
    (label_pos_test, seq_pos_test) = ReadFASTA('data/positive_776_test.fasta')
    (label_neg_test, seq_neg_test) = ReadFASTA('data/negative_776_test.fasta')

    cov_pos_test = ReadCov('data/cov_pos_776_test.fasta')
    cov_neg_test = ReadCov('data/cov_neg_776_test.fasta')

    gc_pos_test = GetGC(seq_pos_test)
    gc_neg_test = GetGC(seq_neg_test)

    for i in range(0, len(seq_pos_test)):
        for j in cov_pos_test[i]:
            gc_pos_test[i].append(float(j))
    for i in range(0, len(seq_neg_test)):
        for j in cov_neg_test[i]:
            gc_neg_test[i].append(float(j))

    data_test = np.array(list(gc_pos_test) + list(gc_neg_test),\
        dtype = np.float)
    pos_len_test = len(gc_pos_test)
    neg_len_test = len(gc_neg_test)

    label_test = np.array([1 for x in xrange(pos_len_test)] +\
        [0 for x in xrange(neg_len_test)])

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

    label = np.array(list(label_pos_test) + list(label_neg_test))

    return (label, result)

def predict(model, seq_file, cov_file):
    (label_test, seq_test) = ReadFASTA(seq_file)

    cov_test = ReadCov(cov_file)

    gc_test = GetGC(seq_test)

    for i in range(0, len(seq_test)):
        for j in cov_test[i]:
            gc_test[i].append(float(j))

    data_test = np.array(list(gc_test), dtype = np.float)
    len_test = len(gc_test)

    result = model.predict(data_test)

    label = np.array(list(label_test))

    return (label, result)

# Training and testing phase
if __name__ == "__main__":
    fn = "data/coverage_positive_776.txt"
    ofn = "data/coverage_pos_776_norm.txt"
    inF = open(fn,'r')
    ouF = open(ofn,'w')
    for line in inF:
        ouF.write(normalize(line))
    inF.close()
    ouF.close()
    fn = "data/coverage_negative_trough_776.txt"
    ofn= "data/coverage_neg_776_norm.txt"
    inF = open(fn,'r')
    ouF = open(ofn,'w')
    for line in inF:
        ouF.write(normalize(line))
    inF.close()
    ouF.close()
    if len(sys.argv) > 1:
        seq_file = sys.argv[1]
        cov_file = sys.argv[2]
    ReadFASTA_pos('data/positive_776.txt')
    ReadFASTA_neg('data/negative_776.txt')
    split_pos()
    split_neg()
    model = GetModel()
    (label, result) = validate(model)
    if len(sys.argv) > 1:
        (label, result) = predict(model, seq_file, cov_file)
    ofn = "result/result.csv"
    ouF = open(ofn, 'w')
    for i in range(0, len(result)):
        ouF.write(str(label[i]) + str(result[i]) + '\n')
    ouF.close()
    
