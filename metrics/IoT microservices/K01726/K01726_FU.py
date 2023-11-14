from rouge import Rouge
from nltk.translate.bleu_score import SmoothingFunction, corpus_bleu, sentence_bleu

model_out = [ 
#1
["User", "Empty","Empty"
],
#2
["Actor", "Empty","Empty", "Empty"
],
#3
["Patient", "Empty","Empty"
],
#4
["Actor", "Empty","Empty"
],
#5
["Actor", "Empty","Empty"
],
#6
["Actor", "Empty","Empty"
],
#7
["Family doctor", "Empty","Empty"
],
#8
["User", "Empty","Empty"
],
#9
["Family doctor", "Empty","Empty", "Empty", "Empty"
],
#10
["User", "Empty","Empty", "Empty"
],
#11
["Actor", "Empty","Empty", "Empty", "Empty"
],
#12
["Actor", "Empty","Empty"
],
#13
["Actor", "Empty", "Empty","Actor", "Empty", "Empty"
],
#14
["Actor", "Empty","Empty"
],
#15
["Actor", "Empty","Empty", "Empty", "Empty", "Empty"
],
#16
["Specialist", "Empty","Empty"
],
#17
["Specialist", "Empty","Empty", "Empty"
],
#18
["Actor", "Empty","Empty"
],
#19
["Specialist", "Empty","Empty"
],
#20
["Specialist", "Empty","Empty"
],
#21
["Specialist, Patient", "Empty","Empty", "Specialist, Patient", "Empty", "Empty"
],
#22
["Specialist/Family doctor", "Empty"
],
#23
["Actor", "Empty", "Empty", "Empty"
],

]

reference = [
#1
["Doctor, nurse, social and health workers, Caregivers, Patient", "Empty","Empty"
],
#2
["Doctor, nurse, social and health workers, Caregivers, Patient", "Empty", "Empty", "Doctor, nurse, social and health workers, Caregivers, Patient", "Empty","Empty","Empty"],
#3
["Doctor, nurse, social and health workers, Caregivers, Patient", "Empty", "Empty"],
#4
["Sensor Device", "Mobile App", "Empty", "Empty", "Empty"],
#5
["Doctor", "Empty", "Empty", "Doctor", "Empty", "Empty"],
#6
["Doctor", "Empty","Empty"
],
#7
["Doctor", "Empty","Empty"
],
#8
["Doctor", "Empty","Empty"
],
#9
["Doctor", "Empty","Empty"
],
#### K17026
#1
["Patient", "Empty","Empty"
],
#2
["Patient", "Empty","Empty", "Empty"
],
#3
["Patient", "Empty","Empty"
],
#4
["Patient", "Empty","Empty"
],
#5
["Patient", "Empty","Empty"
],
#6
["Family doctor", "Empty","Empty"
],
#7
["Family doctor", "Empty","Empty"
],
#8
["Family doctor", "Empty","Empty"
],
#9
["Family doctor", "Empty","Empty", "Empty", "Empty"
],
#10
["Family doctor", "Empty","Empty", "Empty"
],
#11
["Patient", "Empty","Empty", "Empty", "Empty"
],
#12
["Patient", "Empty","Empty"
],
#13
["Patient, Family doctor", "Empty", "Empty","Patient, Family doctor", "Empty", "Empty"
],
#14
["Specialist", "Empty","Empty"
],
#15
["Specialist", "Empty","Empty", "Empty", "Empty", "Empty"
],
#16
["Specialist", "Empty","Empty"
],
#17
["Specialist", "Empty","Empty", "Empty"
],
#18
["Specialist", "Empty","Empty"
],
#19
["Specialist", "Empty","Empty"
],
#20
["Specialist", "Empty","Empty"
],
#21
["Specialist, Patient", "Empty","Empty", "Specialist, Patient", "Empty", "Empty"
],
#22
["Specialist/Family doctor", "Empty"
],
#23
["Specialist/Family doctor", "Empty", "Empty", "Empty"
],
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

