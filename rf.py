from sklearn.ensemble import RandomForestClassifier
import sys
import pickle
import numpy as np
import random

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

def GetGC(seq):
    gc = []
    gc = [GetGCSeq(sequence) for sequence in seq]
    return gc

def GetGCSeq(seq):
    nGC = [0,0,0,0]
    for seg in xrange(4):
        nGC[seg] += seq[seg*10:(seg+1)*10].count("g") +\
            seq[seg*10:(seg+1)*10].count("c")
    return [1.0 * n / len(seq) for n in nGC]

if __name__ == "__main__":
    seq_pos = ReadFASTA('data/Positive_Samples/all_pos_reads.fasta')
    seq_neg = ReadFASTA('data/Negative_Samples/human_negative_sub0.fasta')
    
    gc_pos = GetGC(seq_pos)
    gc_neg = GetGC(seq_neg)

    model = RandomForestClassifier(criterion="entropy", n_estimators = 300,\
        max_depth = 100, class_weight={0:100, 1:1})

    data = np.array(list(gc_pos) + list(gc_neg), dtype = np.float)
    print "G/C content feature matrix sample:"
    print data[0]
    print ""
    pos_len = len(gc_pos)
    neg_len = len(gc_neg)
    label = np.array([1 for x in xrange(pos_len)] +\
        [0 for x in xrange(neg_len)])
    
    model = model.fit(data, label)
    result = model.predict(data)

    err = 0.0
    for i in range(0, len(result)):
        if result[i] != label[i]:
            err += 1.0

    err_rate = 1.0 * err / len(data)
    print "Error Rate:"
    print err_rate
    print ""
    print "Predict Label:"
    print result
