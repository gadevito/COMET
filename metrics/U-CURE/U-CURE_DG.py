from rouge import Rouge
from nltk.translate.bleu_score import SmoothingFunction, corpus_bleu, sentence_bleu

model_out = [ 
#1
["None","None","Dataset details","None","Dataset details","Dataset details","EDA details","EDA details","Variable details","None","Transformation details","Transformation details","Transformation details","None","Messages"
],
#2
["All projects","Project details","Project details","None","None","Messages"

],
#3
["Project ID","Project details","Project details","None","None","Messages"
],
#4
["Variables","Analysis request","Analysis details","Analysis details","Variables","None","T-test request","T-test details","T-test details",
],
#5
["Categorical features","Comparison request","Comparison results","Comparison results"
],
#6
["Continuous features","Continuous feature analysis request","Analysis results","Analysis results"
],
#7
["None","None","Features","None","Features","Analysis","Analysis"
],
#8
["None","None","Model parameters","None","Model parameters","Training results","Model status","Training details"
],
#9
["None","None","Model parameters","None","Model parameters","Test results","Test results"
],
#10
["Patient ID","SVC model parameters","Patient data","None","Patient classification","Patient classification"
]
]

reference = [
#1
["None","None","Dataset details","None","Dataset details","Dataset details","EDA details","EDA details","Variable details","None","Transformation details","Transformation details","Transformation details","None","Messages"
],
#2
["All projects","Project details","Project details","None","None","Messages"
],
#3
["Project ID","Project details","Project details","None","None","Messages"
],
#4
["Variables","Analysis request","Analysis details","Analysis details","Variables","None","T-test request","T-test details","T-test details",
],
#5
["Categorical features","Comparison request","Comparison results","Comparison results"
],
#6
["Continuous features","Continuous feature analysis request","Analysis results","Analysis results"
],
#7
["None","None","Features","None","Features","Analysis","Analysis"
],
#8
["None","None","Model parameters","None","Model parameters","Training results","Model status","Training details"
],
#9
["None","None","Model parameters","None","Model parameters","Test results","Test results"
],
#10
["Patient ID","SVC model parameters","Patient data","SVC model parameters","Patient classification","Patient classification"
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