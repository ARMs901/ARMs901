
import matplotlib.pyplot as plt

import numpy as np

'''序列1三核苷酸组成'''

plt.rcParams.update({'font.size': 28})

plt.figure(figsize=(60,20))

trimers = ["AAA", "AAC" ,"AAG" ,"AAT" ,"ACA" ,"ACC" ,"ACG" ,"ACT" ,"AGA" ,"AGC" ,"AGG" ,"ATA" ,"ATC","ATG","CAA","CAC","CAG","CCA","CCC","CCG","CGA","CGC","CTA","CTC","GAA","GAC","GCA","GCC","GGA","GTA","TAA","TCA"]

x1 = [float (x) for x in "0.052215 0.037806 0.046290 0.042991 0.053057 0.026966 0.037133 0.012355 0.032420 0.026899 0.044809 0.037234 0.032757 0.025586 0.050532 0.034743 0.033867 0.032117 0.009797 0.005790 0.030501 0.025350 0.010571 0.009393 0.042318 0.034642 0.042217 0.018819 0.034238 0.036561 0.022320 0.017708".split()]

plt.plot(trimers, x1, linewidth=5.0, color="blue")

plt.ylabel('Normalised frequency', fontsize=28)
plt.ylim(0, 0.07)
plt.yticks(np.arange(0, 0.07, 0.01))

plt.xticks(rotation=60)
plt.xlabel('Trinucleotides', fontsize=28)
plt.title('Trinucleotide Composition of sequence1')

plt.grid(True)
plt.show()

'''序列一GC含量'''

sequence = ""

with open("D:\sequence1.fasta") as myfile:
    line = myfile.readline()
    line = myfile.readline()

    while line!="":
        sequence += line
        line = myfile.readline()

g_count = sequence.count("G")
c_count = sequence.count("C")

gc_content_sequence1 = (g_count+c_count)/len(sequence)*100
print("GC content of sequence1:", gc_content_sequence1)

'''序列二三核苷酸组成'''

plt.figure(figsize=(60,20))

x2 = [float (x) for x in "0.059832 0.041745 0.050134 0.044295 0.053826 0.027685 0.039228 0.012550 0.036107 0.025638 0.060436 0.038993 0.028087 0.022987 0.050034 0.034799 0.031946 0.030906 0.008691 0.006141 0.031376 0.021678 0.008087 0.007047 0.050235 0.035235 0.039866 0.017819 0.035960 0.032617 0.021510 0.014530".split()]

plt.plot(trimers, x2, linewidth=5.0, color="green")

plt.ylabel('Normalised frequency', fontsize=28)
plt.ylim(0, 0.07)
plt.yticks(np.arange(0, 0.07, 0.01))

plt.xticks(rotation=60)
plt.xlabel('Trinucleotides', fontsize=28)
plt.title('Trinucleotide Composition of sequence2')

plt.grid(True)
plt.show()

'''序列二GC含量'''

sequence = ""

with open("D:\sequence2.fasta") as myfile:
    line = myfile.readline()
    line = myfile.readline()

    while line!="":
        sequence += line
        line = myfile.readline()

g_count = sequence.count("G")
c_count = sequence.count("C")

gc_content_sequence2 = (g_count+c_count)/len(sequence)*100
print("GC content of sequence2:", gc_content_sequence2)

'''序列三三核苷酸组成'''

plt.figure(figsize=(60,20))

x3 = [float (x) for x in "0.064446 0.043978 0.051303 0.046079 0.055751 0.027758 0.039497 0.011204 0.036554 0.026053 0.060433 0.038360 0.027491 0.022508 0.050834 0.033812 0.031203 0.030367 0.008361 0.005017 0.033042 0.019531 0.006956 0.006187 0.053343 0.036052 0.039430 0.016421 0.035216 0.030735 0.020367 0.013712".split()]

plt.plot(trimers, x3, linewidth=5.0, color="red")

plt.ylabel('Normalised frequency', fontsize=28)
plt.ylim(0, 0.07)
plt.yticks(np.arange(0, 0.07, 0.01))

plt.xticks(rotation=60)
plt.xlabel('Trinucleotides', fontsize=28)
plt.title('Trinucleotide Composition of sequence3')

plt.grid(True)
plt.show()

'''序列三GC含量'''

sequence = ""

with open("D:\sequence3.fasta") as myfile:
    line = myfile.readline()
    line = myfile.readline()

    while line!="":
        sequence += line
        line = myfile.readline()

g_count = sequence.count("G")
c_count = sequence.count("C")

gc_content_sequence3 = (g_count+c_count)/len(sequence)*100
print("GC content of sequence3:", gc_content_sequence3)

'''序列123三核苷酸对比'''

plt.figure(figsize=(60,20))

plt.plot(trimers, x1, linewidth=5.0, color="blue")
plt.plot(trimers, x2, linewidth=5.0, color="red")
plt.plot(trimers, x3, linewidth=5.0, color="green")

plt.ylabel('Normalised frequency', fontsize=28)
plt.ylim(0, 0.07)
plt.yticks(np.arange(0, 0.07, 0.01))

plt.xticks(rotation=60)
plt.xlabel('Trinucleotides', fontsize=28)
plt.title('Trinucleotide Composition of different Coronaviruses')
plt.gca().legend(("sequence1", "sequence2", "sequence3"))

plt.grid(True)
plt.show()

'''四核苷酸组成'''

plt.figure(figsize=(60,20))

tetramers = ['AAAA','AAAC','AAAG','AAAT','AACA','AACC','AACG','AACT','AAGA','AAGC','AAGG','AAGT','AATA','AATC', 'AATG','AATT','ACAA','ACAC','ACAG','ACAT','ACCA','ACCC','ACCG','ACCT','ACGA','ACGC','ACGG','ACGT','ACTA','ACTC','ACTG','AGAA','AGAC','AGAG','AGAT','AGCA','AGCC','AGCG','AGCT','AGGA','AGGC','AGGG','AGTA','AGTC','AGTG','ATAA','ATAC','ATAG','ATAT','ATCA','ATCC','ATCG','ATGA','ATGC','ATGG','ATTA','ATTC','ATTG','CAAA','CAAC','CAAG','CACA','CACC','CACG','CAGA','CAGC','CAGG','CATA','CATC','CATG','CCAA','CCAC','CCAG','CCCA','CCCC','CCCG','CCGA','CCGC','CCGG','CCTA','CCTC','CGAA','CGAC','CGAG','CGCA','CGCC','CGCG','CGGA','CGGC','CGTA','CGTC','CTAA','CTAC','CTAG','CTCA','CTCC','CTGA','CTGC','CTTA','CTTC','GAAA','GAAC','GACA','GACC','GAGA','GAGC','GATA','GATC','GCAA','GCAC','GCCA','GCCC','GCGA','GCGC','GCTA','GGAA','GGAC','GGCA','GGCC','GGGA','GGTA','GTAA','GTAC','GTCA','GTGA','GTTA','TAAA','TACA','TAGA','TATA','TCAA','TCCA','TCGA','TGAA','TGCA','TTAA']

x1 = [float (x) for x in "0.014, 0.0116, 0.0127, 0.0138, 0.0167, 0.0078, 0.0033, 0.01, 0.0137, 0.0094, 0.0083, 0.0116, 0.0102, 0.0074, 0.0144, 0.0071, 0.0173, 0.0117, 0.0103, 0.0137, 0.0123, 0.0036, 0.0021, 0.009, 0.0038, 0.0027, 0.0022, 0.0018, 0.0091, 0.0077, 0.0087, 0.0125, 0.0074, 0.0093, 0.0079, 0.0142, 0.0062, 0.0027, 0.0048, 0.0074, 0.0057, 0.0035, 0.0105, 0.006, 0.0105, 0.0109, 0.0066, 0.0082, 0.0034, 0.012, 0.0046, 0.0023, 0.0116, 0.0099, 0.0096, 0.0121, 0.0074, 0.013, 0.0144, 0.0112, 0.0119, 0.013, 0.0079, 0.0033, 0.0093, 0.0099, 0.0059, 0.0098, 0.0101, 0.0053, 0.0092, 0.0065, 0.0068, 0.004, 0.0013, 0.001, 0.0011, 0.0015, 0.0005, 0.006, 0.0054, 0.0032, 0.0023, 0.0027, 0.0035, 0.0016, 0.0007, 0.0013, 0.0014, 0.0033, 0.0024, 0.0086, 0.0087, 0.0026, 0.0086, 0.0047, 0.0086, 0.0081, 0.0092, 0.0093, 0.0112, 0.0064, 0.0102, 0.0037, 0.0063, 0.0059, 0.0056, 0.0019, 0.0108, 0.0077, 0.0081, 0.0025, 0.0026, 0.0013, 0.0076, 0.006, 0.0035, 0.0075, 0.0011, 0.0023, 0.0076, 0.0097, 0.0048, 0.0091, 0.0089, 0.0085, 0.0126, 0.0132, 0.0079, 0.0034, 0.0132, 0.0078, 0.0015, 0.0125, 0.0056, 0.0066".split(", ")]
x2 = [float (x) for x in "0.0171, 0.0126, 0.0149, 0.0152, 0.0183, 0.0081, 0.0035, 0.0118, 0.0146, 0.0091, 0.0079, 0.0127, 0.0121, 0.0078, 0.0129, 0.0087, 0.0187, 0.0121, 0.0106, 0.0125, 0.0133, 0.0033, 0.0024, 0.0087, 0.0034, 0.0025, 0.0025, 0.0021, 0.0097, 0.0072, 0.0096, 0.014, 0.0076, 0.0089, 0.0085, 0.012, 0.0055, 0.0018, 0.0044, 0.0064, 0.0047, 0.0033, 0.0104, 0.006, 0.0109, 0.0135, 0.0066, 0.0084, 0.0038, 0.0112, 0.0043, 0.0016, 0.0105, 0.0086, 0.0088, 0.0144, 0.0081, 0.0125, 0.015, 0.0124, 0.0101, 0.0122, 0.0084, 0.0032, 0.0093, 0.008, 0.0051, 0.0099, 0.0087, 0.0045, 0.0091, 0.0067, 0.0062, 0.0037, 0.0008, 0.001, 0.001, 0.0015, 0.0005, 0.0055, 0.0045, 0.0026, 0.0017, 0.0022, 0.003, 0.0011, 0.0006, 0.0015, 0.0012, 0.0036, 0.0022, 0.0099, 0.008, 0.0025, 0.0072, 0.0034, 0.0084, 0.0068, 0.0098, 0.0095, 0.0115, 0.0069, 0.0099, 0.0033, 0.0059, 0.0041, 0.0053, 0.002, 0.0097, 0.0076, 0.0066, 0.002, 0.0016, 0.0007, 0.0069, 0.0059, 0.0042, 0.0064, 0.0008, 0.0026, 0.0079, 0.0112, 0.0047, 0.008, 0.0084, 0.0099, 0.0162, 0.0134, 0.0093, 0.0044, 0.0126, 0.0073, 0.001, 0.0134, 0.0056, 0.0078".split(", ")]
x3 = [float (x) for x in "0.0194, 0.0138, 0.0152, 0.016, 0.0196, 0.0088, 0.003, 0.0126, 0.0141, 0.0087, 0.008, 0.0133, 0.0118, 0.008, 0.0132, 0.0092, 0.0193, 0.012, 0.0109, 0.0135, 0.0132, 0.0037, 0.0019, 0.0089, 0.0026, 0.0024, 0.0019, 0.0021, 0.0104, 0.0067, 0.0091, 0.0141, 0.0074, 0.0075, 0.0094, 0.0114, 0.0047, 0.0017, 0.0048, 0.0057, 0.0045, 0.0034, 0.0107, 0.0058, 0.0103, 0.0136, 0.0068, 0.0087, 0.0037, 0.0115, 0.0034, 0.0018, 0.0105, 0.0077, 0.0087, 0.0146, 0.0085, 0.0122, 0.0157, 0.0133, 0.0096, 0.0115, 0.0086, 0.0034, 0.0092, 0.0079, 0.0051, 0.0103, 0.0088, 0.004, 0.0091, 0.0066, 0.006, 0.0032, 0.001, 0.0008, 0.0013, 0.0011, 0.0003, 0.0055, 0.004, 0.0025, 0.0012, 0.0015, 0.0026, 0.0011, 0.0004, 0.001, 0.0013, 0.003, 0.0017, 0.0101, 0.0082, 0.003, 0.0074, 0.0031, 0.0078, 0.0065, 0.0098, 0.0095, 0.0109, 0.0064, 0.01, 0.0028, 0.0053, 0.0036, 0.0053, 0.002, 0.0095, 0.0071, 0.0063, 0.0016, 0.0015, 0.0006, 0.0074, 0.006, 0.0039, 0.0058, 0.0011, 0.0021, 0.0076, 0.0123, 0.0044, 0.0079, 0.0082, 0.0105, 0.0185, 0.0147, 0.0098, 0.0046, 0.0129, 0.0077, 0.0007, 0.0126, 0.0055, 0.0087".split(", ")]

plt.plot(tetramers, x1, linewidth=5.0, color="blue")
plt.plot(tetramers, x2, linewidth=5.0, color="red")
plt.plot(tetramers, x3, linewidth=5.0, color="green")

plt.ylabel('Normalised frequency', fontsize=28)
plt.ylim(0, 0.025)
plt.yticks(np.arange(0, 0.025, 0.01))

plt.xticks(rotation=60)
plt.xlabel('Tetranucleotides', fontsize=16)
plt.title('Tetranucleotide Composition of different Coronaviruses')
plt.gca().legend(("sequence1", "sequence2", "sequence3"))

plt.grid(True)
plt.show()

'''GC含量比较'''

gc = [gc_content_sequence1, gc_content_sequence2, gc_content_sequence3]

viruses = ["sequence1", "sequence2", "sequence3"]

fig = plt.figure(figsize=(60,20))
ax = fig.add_axes([0.1,0.1,0.8,0.8])

ax.bar(viruses,gc)
ax.set_axisbelow(True)

plt.title('GC Composition of different Coronaviruses')
plt.ylabel('GC Content (%)', fontsize=28)
plt.xlabel('Type of Coronavirus', fontsize=28)
plt.grid(True)
plt.show()