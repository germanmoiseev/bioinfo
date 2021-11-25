import pyhmmer

def scrap(info):
with pyhmmer.easel.SequenceFile("bact.faa") as file:
    alphabet = file.guess_alphabet()
    sequences = [seq.digitize(alphabet) for seq in file]

hits_his1 = set()
hits_adv = set()
hits_prv = set()
result = [None]*9

with pyhmmer.plan7.HMMFile("./proteins/His1v1.hmm") as hmms:
    hits_his1.update(set([a.name for a in next(pyhmmer.hmmsearch(hmms, sequences, E=1e-4)) if a.evalue <= 1e-4]))

with pyhmmer.plan7.HMMFile("./proteins/His1v2.hmm") as hmms:
    hits_his1.update(set([a.name for a in next(pyhmmer.hmmsearch(hmms, sequences, E=1e-4)) if a.evalue <= 1e-4]))

with pyhmmer.plan7.HMMFile("./proteins/His1v3.hmm") as hmms:
    hits_his1.update(set([a.name for a in next(pyhmmer.hmmsearch(hmms, sequences, E=1e-4)) if a.evalue <= 1e-4]))

with pyhmmer.plan7.HMMFile("./proteins/His1v4.hmm") as hmms:
    hits_his1.update(set([a.name for a in next(pyhmmer.hmmsearch(hmms, sequences, E=1e-4)) if a.evalue <= 1e-4]))

with pyhmmer.plan7.HMMFile("./proteins/His2.hmm") as hmms:
    hits_his2 = set([a.name for a in next(pyhmmer.hmmsearch(hmms, sequences, E=1e-4)) if a.evalue <= 1e-4])
    print(hits_his2)
    print(hits_his1)
    result[3] = len(hits_his1.intersection(hits_his2))

with pyhmmer.plan7.HMMFile("./proteins/Met.hmm") as hmms:
    result[4] = len([a.name for a in next(pyhmmer.hmmsearch(hmms, sequences, E=1e-4)) if a.evalue <= 1e-4])

with pyhmmer.plan7.HMMFile("./proteins/Ser.hmm") as hmms:
    a = [a.name for a in next(pyhmmer.hmmsearch(hmms, sequences, E=1e-4)) if a.evalue <= 1e-4]
    result[5] = len(a)

with pyhmmer.plan7.HMMFile("./proteins/Dig.hmm") as hmms:
    result[6] = len([a.name for a in next(pyhmmer.hmmsearch(hmms, sequences, E=1e-4)) if a.evalue <= 1e-4])

with pyhmmer.plan7.HMMFile("./proteins/Adv1.hmm") as hmms:
    hits_adv.update(set([a.name for a in next(pyhmmer.hmmsearch(hmms, sequences, E=1e-4)) if a.evalue <= 1e-4]))

with pyhmmer.plan7.HMMFile("./proteins/Adv2.hmm") as hmms:
    hits_adv.update(set([a.name for a in next(pyhmmer.hmmsearch(hmms, sequences, E=1e-4)) if a.evalue <= 1e-4]))

with pyhmmer.plan7.HMMFile("./proteins/Adv3.hmm") as hmms:
    hits_adv.update(set([a.name for a in next(pyhmmer.hmmsearch(hmms, sequences, E=1e-4)) if a.evalue <= 1e-4]))
    result[7] = len(hits_adv)

with pyhmmer.plan7.HMMFile("./proteins/Prv1.hmm") as hmms:
    hits_prv.update(set([a.name for a in next(pyhmmer.hmmsearch(hmms, sequences, E=1e-4)) if a.evalue <= 1e-4]))

with pyhmmer.plan7.HMMFile("./proteins/Prv2.hmm") as hmms:
    hits_prv.update(set([a.name for a in next(pyhmmer.hmmsearch(hmms, sequences, E=1e-4)) if a.evalue <= 1e-4]))
    result[8] = len(hits_prv)

print(result)