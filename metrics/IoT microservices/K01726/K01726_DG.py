from rouge import Rouge
from nltk.translate.bleu_score import SmoothingFunction, corpus_bleu, sentence_bleu

model_out = [ 
#1
["Patient ID","Televisit details","Televisit details","None","None","None","None","None","None","None","None","None","None"
],
#2
["None","None","Televisit request details","None","Televisit request details","Notification","None","None","None","None","None","None","Messages"
],
#3
["Televisit request ID","None","None","Televisit request status","None","None","None","None","None","None","None"
],
#4
["Televisit request ID","Televisit request ID","Televisit request details","None","None","None","None","None","None"
],
#5
["None","None","Televisit request details","None","Televisit request details","None","None","None","None","None","None","Messages"
],
#6
["Televisit request","Televisit request","Televisit request","None","None","None","None","None","None","None"
],
#7
["None","None","Rejection reason","None","Televisit request status","Notification","None","None"
],
#8
["Televisit request ID","Televisit request details","Televisit request details","None","None","None","None","None","None"
],
#9
["Televisit request","Televisit status","Notification","None","None","None","Messages","None","Messages"
],
#10
["None","None","Televisit details","None","Televisit details","Notification","None","None","None","None","None","Messages"
],
#11
["Televisit event details","Doctor's agenda","Patient's agenda","Televisit request status","Email details"
],
#12
["Televisit event ID","Televisit event status","Notification"
],
#13
["Televisit events","Televisit events","Today's televisit events","Televisit event ID","Televisit event details","Televisit event details","None"
],
#14
["Teleconsultation request","Teleconsultation details","Teleconsultation details","None","None","None","None","None","None","None"
],
#15
["None","None","Teleconsultation details","None","Teleconsultation status","Teleconsultation details","Notification","None","None","None","None","None","None","Messages","None","None","Messages","None"
],
#16
["Teleconsultation ID","Teleconsultation details","Teleconsultation details","None","None","None"
],
#17
["None","None","Teleconsultation details","None","Teleconsultation details","None","None","Notification","None","Messages","None"
],
#18
["Teleconsultation ID","None","None","Teleconsultation details","None","None","None","None","None"
],
#19
["Teleconsultation ID","Teleconsultation status","Teleconsultation details","None","None"
],
#20
["Teleconsultation ID","None","None","Teleconsultation details","Notification","None","None","None","None","None"
],
#21
["Teleconsultation date","Teleconsultation details","Teleconsultation details","Teleconsultation ID","Teleconsultation details","Teleconsultation details","None","None","None"],
#22
["Televisit/Teleconsultation details","Start request","None","None"
],
#23
["None","None","Outcome","None","Executed event","Agenda","None","None","Messages"
]
]

reference = [
#1
["Patient ID","Televisit details","Televisit details","None","None","None","None","None","None","None","None","None","None"
],
#2
["None","None","Televisit request details","None","Televisit request details","Notification","None","None","None","None","None","None","Messages"
],
#3
["Televisit request ID","None","None","Televisit request status","None","None","None","None","None","None","None"
],
#4
["Televisit request ID","Televisit details","Televisit details","None","None","None","None","None","None"
],
#5
["None","None","Televisit request details","None","Televisit request details","None","None","None","None","None","None","Messages"
],
#6
["Televisit request","Televisit request","Televisit request","None","None","None","None","None","None","None"
],
#7
["None","None","Rejection reason","None","Televisit request status","Notification","None","None"
],
#8
["Televisit request ID","Televisit request details","Televisit request details","None","None","None","None","None","None"

],
#9
["Televisit request","Televisit status","Notification","None","None","None","Messages","None","Messages"
],
#10
["None","None","Televisit details","None","Televisit details","Notification","None","None","None","None","None","Messages"
],
#11
["Televisit event details","Doctor's agenda","Patient's agenda","Televisit request status","Email details"
],
#12
["Televisit event ID","Televisit event status","Notification"
],
#13
["Televisit events","Televisit events","Televisit events","Televisit event ID","Televisit event details","Televisit event details","None"
],
#14
["Teleconsultation request","Teleconsultation details","Teleconsultation details","None","None","None","None","None","None","None"
],
#15
["None","None","Teleconsultation details","None","Teleconsultation details","Teleconsultation details","Notification","None","None","None","None","None","None","Messages","None","None","Messages","None"
],
#16
["Teleconsultation ID","Teleconsultation details","Teleconsultation details","None","None","None"
],
#17
["None","None","Teleconsultation details","None","Teleconsultation details","None","None","Notification","None","Messages","None"
],
#18
["Teleconsultation ID","None","None","Teleconsultation details","None","None","None","None","None"
],
#19
["Teleconsultation ID","Teleconsultation details","Teleconsultation details","None","None"
],
#20
["Teleconsultation ID","None","None","Teleconsultation details","Notification","None","None","None","None","None"
],
#21
["Teleconsultation date","Teleconsultation details","Teleconsultation details","Teleconsultation ID","Teleconsultation event details","Teleconsultation event details","None","None","None"],
#22
["Teleconsultation event details","Start request","None","None"
],
#23
["None","None","Outcome","None","Executed event","Agenda","None","None","Messages"
]


]


for i in range(len(reference)):
    if len(reference[i]) != len(model_out[i]):
        print(i)

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
print("Total DGs ", totalDG)
