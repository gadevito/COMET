from rouge import Rouge
from nltk.translate.bleu_score import SmoothingFunction, corpus_bleu, sentence_bleu

model_out = [ 
#1
["E","R","X","X"],
#2
["E","R","X","X"],
#3
["E","R","X","E","W","X","X","X","X","X"],
#4
["E","W","X","X","X","X"],
#5
["E","R","X","X"],
#6
["E","R","X","X"],
#7
["E","W","X","X","X"],
#8
["E","W","X","X","X","X"],
#9
["E","R","X","X"],
#10
["E","R","X","X","X"],
#11
["E","W","X","X","X"],
#12
["E","W","X","X","X"],
#13
["E","R","X","X"],
#14
["E","R","X","X","X"],
#15
["E","W","X","X","X"],
#16
["E","W","X"],
#17
["E","W","X","X","X","X"],
#18
["E","R","X","X"],
#19
["E","W","X","X","X"],
#20
["E","R","X","X"],
#21
["E","R","X","E","W","X","X"],
#22
["E","W","X","X"],
#23
["E","R","R","R","X","E","R","R","X","X","E","R","X","E","R","X","E","E","W","R","W","W","W","W","X","E","W","X","X","X","X","X"],
#24
["E","R","R","W","W"],
#25
["E","R","X","X"],
#26
["E","E","R","X","X","X"],
#27
["E","R","R","R","R","X","X","X","X","X","X"],
#28
["E","W","W","W","W","X","X","X"],
#29
["E","R","R","R","X","E","R","R","X","X","E","N","W","W","W","W","W","R","W","W","W","W","X","X","X"],
#30
["E","R","R","R","R","X","X","X","X","E","E","W","W","W","X","X"],
#31
["E","R","X","X"],
#32
["E","R","X","X"],
#33
["E","R","R","X","X","X"],
#34
["E","W","X","X"],
#35
["E","W","X","X","X","X"],
#36
["E","R","R","R","X","E","W","X","X","X"],
#37
["E","W","X","X"],
#38
["E","R","X","X"],
#39
["E","R","R","X","X","X"],
#40
["R","X","E","E","R","W","W","X","X","X","X"],
#41
["E","R","R","X","X","X","W","W","X","X"],
#42
["E","W","W","X","X","X"],
#43
["E","W","W","W","X","X","X"],
#44
["E","W","X","X"],
#45
["E","R","R","X","X","X"],
#46
["E","R","R","X","X","X"],
#47
["E","R","X","X"],
#48
["E","R","R","X","X","X"],
#49
["E","W","X"],
#50
["E","W","X","X","X","X"],
#51
["E","W","W","X","X","X","X"],
#52
["E","W","X","X"],
#53
["E","W","X","X","X"],
#54
["E","W","X","X","X","X"],
#55
["E","R","R","X","E","R","X","E","E","W","W","W","W","X","E","W","X","X","X"],
#56
["E","R","R","X","X","X"],
#57
["E","R","R","X","X","E","W","W","X","X"],
#58
["E","R","X","E","R","W","W","X","X"],
#59
["E","R","R","R","X","X","X","X"],
#60
["E","R","R","R","X","E","R","R","X","X","X","E","R","W","W","W","W","W","W","W","X","X"],
#61
["E","W","W","X","X"],
#62
["E","W","X"]

]

reference = [
#1
["E","R","X","X"],
#2
["E","R","X","X"],
#3
["E","R","X","E","W","X","X","X","X","X"],
#4
["E","W","X","X","X","X"],
#5
["E","R","X","X"],
#6
["E","R","X","X"],
#7
["E","W","X","X","X"],
#8
["E","W","X","X","X","X"],
#9
["E","R","X","X"],
#10
["E","R","X","X","X"],
#11
["E","W","X","X","X"],
#12
["E","W","X","X","X"],
#13
["E","R","X","X"],
#14
["E","R","X","X","X"],
#15
["E","W","X","X","X"],
#16
["E","W","X"],
#17
["E","W","X","X","X","X"],
#18
["E","R","X","X"],
#19
["E","W","X","X","X"],
#20
["E","R","X","X"],
#21
["E","R","X","E","W","X","X"],
#22
["E","W","X","X"],
#23
["E","R","R","R","X","E","R","R","X","X","E","R","X","E","R","X","E","E","W","R","W","W","W","W","X","E","W","X","X","X","X","X"],
#24
["E","R","R","W","W"],
#25
["E","R","X","X"],
#26
["N","E","R","X","X","X"],
#27
["E","R","R","R","R","X","X","X","X","X","X"],
#28
["E","W","W","W","W","X","X","X"],
#29
["E","R","R","R","X","E","R","R","X","X","E","E","W","W","W","W","W","R","W","W","W","W","X","X","X"],
#30
["E","R","R","R","R","X","X","X","X","E","E","W","W","W","X","X"],
#31
["E","R","X","X"],
#32
["E","R","X","X"],
#33
["E","R","R","X","X","X"],
#34
["E","W","X","X"],
#35
["E","W","X","X","X","X"],
#36
["E","R","R","R","X","E","W","X","X","X"],
#37
["E","W","X","X"],
#38
["E","R","X","X"],
#39
["E","R","R","X","X","X"],
#40
["R","X","E","E","R","W","W","X","X","X","X"],
#41
["E","R","R","X","X","X","W","W","X","X"],
#42
["E","W","W","X","X","X"],
#43
["E","W","W","W","X","X","X"],
#44
["E","W","X","X"],
#45
["E","R","R","X","X","X"],
#46
["E","R","R","X","X","X"],
#47
["E","R","X","X"],
#48
["E","R","R","X","X","X"],
#49
["E","W","X"],
#50
["E","W","X","X","X","X"],
#51
["E","W","W","X","X","X","X"],
#52
["E","W","X","X"],
#53
["E","W","X","X","X"],
#54
["E","W","X","X","X","X"],
#55
["E","R","R","X","E","R","X","E","E","W","W","W","W","X","E","W","X","X","X"],
#56
["E","R","R","X","X","X"],
#57
["E","R","R","X","X","E","W","W","X","X"],
#58
["E","R","X","E","R","W","W","X","X"],
#59
["E","R","R","R","X","X","X","X"],
#60
["E","R","R","R","X","E","R","R","X","X","X","E","R","W","W","W","W","W","W","W","X","X"],
#61
["E","W","W","X","X"],
#62
["E","W","X"]

]

rouge = Rouge()
totalDG = 0
avgB = 0
avgR = [0, 0, 0]
avgRL = [0, 0, 0]

for i in range(0,len(reference)):
    r = []
    m = []
    totalDG = totalDG + len(reference[i])
    for j in reference[i]:
        ss = j.split()

        for k in ss:
            r.append(k)

    for j in model_out[i]:
        ss = j.split()
        for k in ss:
            m.append(k)
    
    cc = SmoothingFunction()
    c = sentence_bleu([r],m, weights=(1, 0, 0, 0),smoothing_function=cc.method4)
    avgB = avgB + c

    cx = rouge.get_scores(model_out[i], reference[i], avg=True)
    
    r1 = cx['rouge-1']
    r2 = cx['rouge-l']
    avgR[0] = avgR[0] + r1['p']
    avgR[1] = avgR[1] + r1['r']
    avgR[2] = avgR[2] + r1['f']
    
    avgRL[0] = avgRL[0] + r2['p']
    avgRL[1] = avgRL[1] + r2['r']
    avgRL[2] = avgRL[2] + r2['f']

    r1['p'] = "{0:.2%}".format(r1['p'])
    r1['r'] = "{0:.2%}".format(r1['r'])
    r1['f'] = "{0:.2%}".format(r1['f'])
    r2['p'] = "{0:.2%}".format(r2['p'])
    r2['r'] = "{0:.2%}".format(r2['r'])
    r2['f'] = "{0:.2%}".format(r2['f'])
    c = "{0:.2%}".format(c)
    print(i+1,') ', "Rouge-1 ", r1, "Rouge-l", r2, "Bleu ", c)

avgB = avgB/len(reference)
#avg = sentence_bleu([r],m)
print("AVG BLEU: ", "{0:.2%}".format(avgB))

avgR[0] = avgR[0]/len(reference)
avgR[1] = avgR[1]/len(reference)
avgR[2] = avgR[2]/len(reference)

avgRL[0] = avgRL[0]/len(reference)
avgRL[1] = avgRL[1]/len(reference)
avgRL[2] = avgRL[2]/len(reference)

print("AVG ROUGE-1: ", "Precision ","{0:.2%}".format(avgR[0]), "Recall ", "{0:.2%}".format(avgR[1]),"F1-score ", "{0:.2%}".format(avgR[2]))
print("AVG ROUGE-L: ", "Precision ","{0:.2%}".format(avgRL[0]), "Recall ", "{0:.2%}".format(avgRL[1]),"F1-score ", "{0:.2%}".format(avgRL[2]))
print("Total DM: ", totalDG)
