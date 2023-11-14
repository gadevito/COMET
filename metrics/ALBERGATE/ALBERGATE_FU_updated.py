from rouge import Rouge
from nltk.translate.bleu_score import SmoothingFunction, corpus_bleu, sentence_bleu

model_out = [ 
#1
["Hotel Manager", "Empty", "Empty", "Empty"],
#2
["Hotel Manager", "Empty", "Empty", "Empty"],
#3
["Hotel Manager", "Empty", "Empty", "Hotel Manager", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty"],
#4
["Hotel Manager", "Empty", "Empty", "Empty", "Empty", "Empty"],
#5
["Hotel Manager", "Empty",  "Empty", "Empty"],
#6
["Hotel Manager", "Empty", "Empty", "Empty"],
#7
["Hotel Manager", "Empty", "Empty", "Empty", "Empty"],
#8
["Hotel Manager", "Empty", "Empty", "Empty", "Empty", "Empty"],
#9
["Hotel Manager", "Empty", "Empty", "Empty"],
#10
["Hotel Manager", "Empty", "Empty", "Empty", "Empty"],
#11
["Hotel Manager", "Empty", "Empty", "Empty", "Empty"],
#12
["Hotel Manager", "Empty", "Empty", "Empty", "Empty"],
#13
["Hotel Manager", "Empty", "Empty", "Empty"],
#14
["Hotel Manager", "Empty", "Empty", "Empty", "Empty"],
#15
["Hotel Manager","Empty","Empty","Empty","Empty"],
#16
["Hotel Manager","Empty", "Empty"],
#17
["Hotel Manager", "Empty", "Empty",  "Empty", "Empty", "Empty"],
#18
["Hotel Manager","Empty", "Empty", "Empty"],
#19
["Hotel Manager","Empty","Empty","Empty","Empty"],
#20
["Hotel Manager","Empty","Empty", "Empty"],
#21
["Hotel Manager", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty"],
#22
["Hotel Manager","Empty","Empty","Empty"],
#23
["Hotel Manager","Empty","Empty","Empty","Empty","Hotel Manager","Empty","Empty","Empty","Empty","Hotel Manager","Empty","Empty","Hotel Manager","Empty","Empty","Hotel Manager","Hotel Manager","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Hotel Manager","Empty","Empty","Empty","Empty","Empty","Empty"],
#24
["System Timer","Empty","Empty","Empty", "Empty"],
#25
["Hotel Manager","Empty","Empty","Empty"],
#26
["Hotel Manager, Operator","Hotel Manager, Operator","Empty","Empty","Empty","Empty", "Empty"], #Here
#27
["Hotel Manager","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty", "Empty"],
#28
["Hotel Manager","Empty","Empty","Empty","Empty","Empty","Empty","Empty"],
#29
["Hotel Manager","Empty","Empty","Empty","Empty","Hotel Manager","Empty","Empty","Empty","Empty","Hotel Manager","Empty","Empty Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"],
#30
["Hotel Manager","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Hotel Manager","Hotel Manager","Empty","Empty","Empty","Empty","Empty"],
#31
["Hotel Manager","Empty","Empty","Empty"],
#32
["Hotel Manager","Empty","Empty","Empty"],
#33
["Hotel Manager","Empty","Empty","Empty","Empty","Empty"],
#34
["Hotel Manager","Empty","Empty","Empty"],
#35
["Hotel Manager","Empty","Empty","Empty","Empty","Empty"],
#36
["Hotel Manager","Empty","Empty","Empty","Empty","Hotel Manager","Empty","Empty","Empty","Empty"],
#37
["Hotel Manager","Empty","Empty","Empty"],
#38
["Hotel Manager","Empty","Empty","Empty"],
#39
["Hotel Manager","Empty","Empty","Empty","Empty","Empty"],
#40
["Empty","Empty","Waiter","Waiter","Empty","Empty","Empty","Empty","Empty","Empty","Empty"],
#41
["Waiter","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"],
#42
["Waiter","Empty","Empty","Empty","Empty","Empty"],
#43
["Waiter","Empty","Empty","Empty","Empty","Empty","Empty"],
#44
["Waiter","Empty","Empty","Empty"],
#45
["Waiter","Empty","Empty","Empty","Empty","Empty"],
#46
["Waiter","Empty","Empty","Empty","Empty","Empty"],
#47
["Hotel Manager","Empty","Empty","Empty"],
#48
["Hotel Manager","Empty","Empty","Empty","Empty","Empty"],
#49
["Hotel Manager","Empty","Empty"],
#50
["Hotel Manager","Empty","Empty","Empty","Empty","Empty"],
#51
["Hotel Manager","Empty","Empty","Empty","Empty","Empty","Empty"],
#52
["Hotel Manager","Empty","Empty","Empty"],
#53
["Hotel Manager","Empty","Empty","Empty","Empty"],
#54
["Hotel Manager","Empty","Empty","Empty","Empty","Empty"],
#55
["Hotel Manager","Empty","Empty","Empty","Hotel Manager","Empty","Empty","Hotel Manager","Empty","Empty","Empty","Empty","Empty","Hotel Manager","Empty","Empty","Empty","Empty","Empty"],
#56
["Hotel Manager","Empty","Empty","Empty","Empty","Empty"],
#57
["Hotel Manager","Empty","Empty","Empty","Empty","Hotel Manager","Empty","Empty","Empty","Empty"],
#58
["Hotel Manager","Empty","Empty","Hotel Manager","Empty","Empty","Empty","Empty","Empty"],
#59
["Hotel Manager","Empty","Empty","Empty","Empty","Empty","Empty","Empty"],
#60
["Hotel Manager","Empty","Empty","Empty","Empty","Hotel Manager","Empty","Empty","Empty","Empty","Empty","Hotel Manager","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"],
#61
["Hotel Manager","Empty","Empty","Empty","Empty"],
#62
["Hotel Manager","Empty","Empty"]
]

reference = [
#1
["Hotel Manager", "Empty", "Empty", "Empty"],
#2
["Hotel Manager", "Empty", "Empty", "Empty"],
#3
["Hotel Manager", "Empty", "Empty", "Hotel Manager", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty"],
#4
["Hotel Manager", "Empty", "Empty", "Empty", "Empty", "Empty"],
#5
["Hotel Manager", "Empty",  "Empty", "Empty"],
#6
["Hotel Manager", "Empty", "Empty", "Empty"],
#7
["Hotel Manager", "Empty", "Empty", "Empty", "Empty"],
#8
["Hotel Manager", "Empty", "Empty", "Empty", "Empty", "Empty"],
#9
["Hotel Manager", "Empty", "Empty", "Empty"],
#10
["Hotel Manager", "Empty", "Empty", "Empty", "Empty"],
#11
["Hotel Manager", "Empty", "Empty", "Empty", "Empty"],
#12
["Hotel Manager", "Empty", "Empty", "Empty", "Empty"],
#13
["Hotel Manager", "Empty", "Empty", "Empty"],
#14
["Hotel Manager", "Empty", "Empty", "Empty", "Empty"],
#15
["Hotel Manager","Empty","Empty","Empty","Empty"],
#16
["Hotel Manager","Empty", "Empty"],
#17
["Hotel Manager", "Empty", "Empty",  "Empty", "Empty", "Empty"],
#18
["Hotel Manager","Empty", "Empty", "Empty"],
#19
["Hotel Manager","Empty","Empty","Empty","Empty"],
#20
["Hotel Manager","Empty","Empty", "Empty"],
#21
["Hotel Manager", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty"],
#22
["Hotel Manager","Empty","Empty","Empty"],
#23
["Hotel Manager","Empty","Empty","Empty","Empty","Hotel Manager","Empty","Empty","Empty","Empty","Hotel Manager","Empty","Empty","Hotel Manager","Empty","Empty","Hotel Manager","Hotel Manager","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Hotel Manager","Empty","Empty","Empty","Empty","Empty","Empty"],
#24
["System Timer","Empty","Empty","Empty", "Empty"],
#25
["Hotel Manager","Empty","Empty","Empty"],
#26
["None","Hotel Manager, Operator","Empty","Empty","Empty","Empty", "Empty"], #Here
#27
["Hotel Manager","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty", "Empty"],
#28
["Hotel Manager","Empty","Empty","Empty","Empty","Empty","Empty","Empty"],
#29
["Hotel Manager","Empty","Empty","Empty","Empty","Hotel Manager","Empty","Empty","Empty","Empty","Hotel Manager","Empty","Empty Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"],
#30
["Hotel Manager","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Hotel Manager","Hotel Manager","Empty","Empty","Empty","Empty","Empty"],
#31
["Hotel Manager","Empty","Empty","Empty"],
#32
["Hotel Manager","Empty","Empty","Empty"],
#33
["Hotel Manager","Empty","Empty","Empty","Empty","Empty"],
#34
["Hotel Manager","Empty","Empty","Empty"],
#35
["Hotel Manager","Empty","Empty","Empty","Empty","Empty"],
#36
["Hotel Manager","Empty","Empty","Empty","Empty","Hotel Manager","Empty","Empty","Empty","Empty"],
#37
["Hotel Manager","Empty","Empty","Empty"],
#38
["Hotel Manager","Empty","Empty","Empty"],
#39
["Hotel Manager","Empty","Empty","Empty","Empty","Empty"],
#40
["Empty","Empty","Waiter","Waiter","Empty","Empty","Empty","Empty","Empty","Empty","Empty"],
#41
["Waiter","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"],
#42
["Waiter","Empty","Empty","Empty","Empty","Empty"],
#43
["Waiter","Empty","Empty","Empty","Empty","Empty","Empty"],
#44
["Waiter","Empty","Empty","Empty"],
#45
["Waiter","Empty","Empty","Empty","Empty","Empty"],
#46
["Waiter","Empty","Empty","Empty","Empty","Empty"],
#47
["Hotel Manager","Empty","Empty","Empty"],
#48
["Hotel Manager","Empty","Empty","Empty","Empty","Empty"],
#49
["Hotel Manager","Empty","Empty"],
#50
["Hotel Manager","Empty","Empty","Empty","Empty","Empty"],
#51
["Hotel Manager","Empty","Empty","Empty","Empty","Empty","Empty"],
#52
["Hotel Manager","Empty","Empty","Empty"],
#53
["Hotel Manager","Empty","Empty","Empty","Empty"],
#54
["Hotel Manager","Empty","Empty","Empty","Empty","Empty"],
#55
["Hotel Manager","Empty","Empty","Empty","Hotel Manager","Empty","Empty","Hotel Manager","Empty","Empty","Empty","Empty","Empty","Hotel Manager","Empty","Empty","Empty","Empty","Empty"],
#56
["Hotel Manager","Empty","Empty","Empty","Empty","Empty"],
#57
["Hotel Manager","Empty","Empty","Empty","Empty","Hotel Manager","Empty","Empty","Empty","Empty"],
#58
["Hotel Manager","Empty","Empty","Hotel Manager","Empty","Empty","Empty","Empty","Empty"],
#59
["Hotel Manager","Empty","Empty","Empty","Empty","Empty","Empty","Empty"],
#60
["Hotel Manager","Empty","Empty","Empty","Empty","Hotel Manager","Empty","Empty","Empty","Empty","Empty","Hotel Manager","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"],
#61
["Hotel Manager","Empty","Empty","Empty","Empty"],
#62
["Hotel Manager","Empty","Empty"]

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
print("Total FU ", totalDG)

differences = 0
for i in range(0,len(reference)):
    for j in range(0, len(reference[i])):
        if model_out[i][j] != reference[i][j]:
            differences = differences +1

print("DIFFERENCES: ", differences)
