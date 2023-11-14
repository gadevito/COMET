from rouge import Rouge
from nltk.translate.bleu_score import SmoothingFunction, corpus_bleu, sentence_bleu

model_out = [ 
#1
["E", "R","X"
],
#2
["E", "R", "X", "E", "W", "X", "X"
],
#3
["E", "R", "X"
],
#4
["E", "E", "W", "X", "X"
],
#5
["E", "R", "E", "R", "X"
],
#6
["E","W","X"],
#7
["E","R","X"],
#8
["E","W","X"],
#9
["E","W","X"]

]

reference = [
#1
["E", "R","X"
],
#2
["E", "R", "X", "E", "W", "X", "X"
],
#3
["E", "R", "X"
],
#4
["E", "E", "W", "X", "X"
],
#5
["E", "R", "E", "R", "X"
],
#6
["E","W","X"],
#7
["E","R","X"],
#8
["E","W","X"],
#9
["E","W","X"]
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


print("total DMs ", totalDM)
