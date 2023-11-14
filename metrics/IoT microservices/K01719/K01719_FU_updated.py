from rouge import Rouge
from nltk.translate.bleu_score import SmoothingFunction, corpus_bleu, sentence_bleu

model_out = [ 
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
]


rouge = Rouge()

totalDM = 0
avgB  = 0
avgR = [0, 0, 0]

for i in range(0,len(reference)):
    r = []
    m = []
    totalDM = totalDM + len(reference[i])
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
    avgR[0] = avgR[0] + r1['p']
    avgR[1] = avgR[1] + r1['r']
    avgR[2] = avgR[2] + r1['f']
    print(i+1,') ', "Rouge-1 ", r1, "Bleu ", c)

avgB = avgB/len(reference)
#avg = sentence_bleu([r],m)
print("AVG BLEU: ", avgB)


avgR[0] = avgR[0]/len(reference)
avgR[1] = avgR[1]/len(reference)
avgR[2] = avgR[2]/len(reference)
print("AVG ROUGE: ", "Precision ", avgR[0], "Recall", avgR[1], "F1-score ", avgR[2])


print("total FU ", totalDM)
