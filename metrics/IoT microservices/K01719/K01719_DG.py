from rouge import Rouge
from nltk.translate.bleu_score import SmoothingFunction, corpus_bleu, sentence_bleu

model_out = [ 
#1
["Patient ID","Measurement details","Measurement details","None","None","None","None","None","None","None","None","None","None"

],
#2
["None","None","Instrument ID","Instrument ID","Vital parameters","Vital Peasurements details","None","Measurement details","Messages","Measurement details","None","None","None","None","None"

],
#3
["Vital parameter","Vital parameter","Measurement graph"
],
#4
["None","Raw data","Measurement data","Measurement data","Envelope data","Messages"

],
#5
["None","Vitals list","Vitals list","Vitals list","Vital sign","Alerts list","Alerts list","None"

],
#6
["None","None","Alert details","None","Alert details","Messages","None","None","None","None","None"

],
#7
["Alert ID","Alert details","Alert details"

],
#8
["None","None","Alert details","None","Alert details","Messages","None","None","None","None","None"

],
#9
["Alert ID","None","None","Alert details","Messages","None","None","None","None","None"

]
]

reference = [
#1
["Patient ID","Measurement details","Measurement details","None","None","None","None","None","None","None","None","None","None"

],
#2
["None","None","Measuring Instrument ID","Vital parameters","Vital parameters","Measurement details","None","Measurement details","Messages","Measurement details","None","None","None","None","None"

],
#3
["Vital parameter","Measurements","Measurement graph"

],
#4
["None","Raw data","Measurement data","Measurement data","Envelope data","Messages"

],
#5
["None","Vitals request","Vitals list","Vitals list","Selected vital","Alerts list","Alerts list","None"

],
#6
["None","None","Alert details","None","Alert details","Messages","None","None","None","None","None"

],
#7
["Alert ID","Alert details","Alert details"

],
#8
["None","None","Alert details","None","Alert details","Messages","None","None","None","None","None"

],
#9
["Alert ID","None","None","Alert details","Messages","None","None","None","None","None"

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
print("Total DGs ", totalDG)
