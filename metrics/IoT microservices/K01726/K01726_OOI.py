from rouge import Rouge
from nltk.translate.bleu_score import SmoothingFunction, corpus_bleu, sentence_bleu




model_out = [ 
#1
["Patient","Televisit","Televisit","None","None","None","None","None","None","None","None","None","None"

],
#2
["None","None","Televisit request","None","Televisit request","Messanger","None","None","None","None","None","None","Message"
],
#3
["Televisit request","None","None","Televisit request","None","None","None","None","None","None","None" 
],
#4
["Televisit request","Televisit request","Televisit request","None","None","None","None","None","None"
],
#5
["None","None","Televisit request","None","Televisit request","None","None","None","None","None","None","Message"
],
#6
["Televisit","Televisit","Televisit","None","None","None","None","None","None","None"
],
#7
["None","None","Televisit request","None","Televisit request","Messenger","None","None"
],
#8
["Televisit request","Televisit request","Televisit request","None","None","None","None","None","None"
],
#9
["Televisit","Televisit","Messanger","None","None","None","Message","None","Message"
],
#10
["None","None","Televisit","None","Televisit","Message","None","None","None","None","None","Message"
],
#11
["Televisit event","Doctor","Patient","Televisit event","Email"
],
#12
["Televisit event","Televisit event","Messanger"
],
#13
["Televisit event","Televisit event","Televisit event","Televisit event","Televisit event","Televisit event","None"
],
#14
["Teleconsultation","Teleconsultation","Teleconsultation","None","None","None","None","None","None","None"
],
#15
["None","None","Teleconsultation details","None","Teleconsultation status","Teleconsultation details","Notification","None","None","None","None","None","None","Messages","None","None","Messages","None"
],
#16
["Teleconsultation","Teleconsultation","Teleconsultation","None","None","None"
],
#17
["None","None","Teleconsultation","None","Teleconsultation","None","None","Notification","None","Message","None"
],
#18
["Teleconsultation","None","None","Teleconsultation","None","None","None","None","None"
],
#19
["Teleconsultation","Teleconsultation","Agenda","None","None"
],
#20
["Teleconsultation","None","None","Teleconsultation","Messenger","None","None","None","None","None"
],
#21
["Teleconsultation","Teleconsultation","Teleconsultation","Teleconsultation","Teleconsultation","Teleconsultation","None","None","None"
],
#22
["Televisit/Teleconsultation","XXX sysem","None","None"
],
#23
["None","None","Televisit/Teleconsultation","None","Televisit/Teleconsultation","Agenda","None","None","Message"
]

]

reference = [
#1
["Patient","Televisit","Televisit","None","None","None","None","None","None","None","None","None","None"
],
#2
["None","None","Televisit","None","Televisit","Notification","None","None","None","None","None","None","Message"
],
#3
["Televisit","None","None","Televisit","None","None","None","None","None","None","None"
],
#4
["Televisit","Televisit","Televisit","None","None","None","None","None","None"
],
#5
["None","None","Televisit","None","Televisit","None","None","None","None","None","None","Message"
],
#6
["Televisit","Televisit","Televisit","None","None","None","None","None","None","None"
],
#7
["None","None","Televisit","None","Televisit","Notification","None","None"
],
#8
["Televisit","Televisit","Televisit","None","None","None","None","None","None"
],
#9
["Televisit","Televisit","Notification","None","None","None","Message","None","Message"
],
#10
["None","None","Televisit","None","Televisit","Notification","None","None","None","None","None","Message"
],
#11
["Televisit event","Televisit event","Televisit event","Televisit","Email"
],
#12
["Televisit event","Televisit event","Notification"
],
#13
["Televisit event","Televisit event","Televisit event","Televisit event","Televisit event","Televisit event","None"
],
#14
["Teleconsultation","Teleconsultation","Teleconsultation","None","None","None","None","None","None","None"
],
#15
["None","None","Teleconsultation","None","Teleconsultation","Teleconsultation","Notification","None","None","None","None","None","None","Message","None","None","Message","None"
],
#16
["Teleconsultation","Teleconsultation","Teleconsultation","None","None","None"
],
#17
["None","None","Teleconsultation","None","Teleconsultation","None","None","Notification","None","Message","None"
],
#18
["Teleconsultation","None","None","Teleconsultation","None","None","None","None","None"
],
#19
["Teleconsultation","Teleconsultation","Teleconsultation event","None","None"
],
#20
["Teleconsultation","None","None","Teleconsultation","Notification","None","None","None","None","None"
],
#21
["Teleconsultation","Teleconsultation","Teleconsultation","Teleconsultation event","Teleconsultation event","Teleconsultation event","None","None","None"
],
#22
["Teleconsultation event","Teleconsultation event","None","None"
],
#23
["None","None","Teleconsultation event","None","Teleconsultation event","Teleconsultation event","None","None","Message"
]
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
print("Total OOI ", totalDG)
