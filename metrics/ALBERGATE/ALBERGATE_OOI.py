from rouge import Rouge
from nltk.translate.bleu_score import SmoothingFunction, corpus_bleu, sentence_bleu




model_out = [ 
#1
["None", "None", "Room", "Room", "Room", "None", "None", "Message"],
#2
["Room", "Room", "Room", "None", "Message"],
#3
["Room", "Booked Room", "Room", "Room", "None", "None", "Room", "Message", "None", "Message", "None","None","None", "Message", "None", "None", "None", "Message", "Message"],
#4
["None","None","Room","None","None","None","None","Room","Message","None","Message", "Message","Message"],
#5
["None","None","Service","Service","Service","None","None","Message"],
#6
["Service","Service","Service","None","Message"],
#7
["None","None","Service","None","None","None","Service","Message","None","None","Message","Message"],
#8
["None","None","Service","None","None","None","None","Service","Message","None","Message","Message","Message"],
#9
["None","None","None","Customer","None","Customer","Customer","None","None","Message"],
#10
["Customer","Customer","Customer","None","Message","Message"],
#11
["None","None","Customer","None","None","None","None","Customer","Message","None","Message","Message"],
#12
["None","None","Customer","None","None","None","None","None","Customer","Message","None","Message","Message","Message"],
#13
["Season", "Season", "Season","None","None","Message"],
#14
["Season configuration", "Season configuration", "Season configuration", "None","Messages","Messages","None"],
#15
["None","None","Season configuration", "None","None","None","None","Season configuration", "Message","None","Message","Message"],
#16
["Season configuration","None","None","Season configuration","Message","None","None","None","None","Message"],
#17
["None","None","Season configuration","None","None","None","None","None","Season configuration","Message","None","Message","Message","Message"],
#18
["Configuration","Configuration","Configuration","None","None","Message"],
#19
["None","None","Configuration","None","None","None","Configuration","Message","None","Message","Message"],
#20
["Room", "Services","Services","None","None","Message"],
#21
["None","None","Service","None","Service","Service","Service","None","None","Service","Message","None","None","None","None","None","None","None","None","Message"],
#22
["Service","None","None","Service","Message","None","None","None","None","Message"],
#23
["None","None","Room","None","None","Room","Commission file","Booked rooms file","Room","None","Reservation","Room","Services","Room","Services","Reservation","Configured season file","Reservation","None","Customer","Customer","Customer","None","None","Customer","Reservation","Customer","Season","Reservation","Booked room","Services","Reservation","Message","None","Customer","None","None","Customer","None","None","None","None","None","None","Message","Message","Message","Message","Message"],
#24
["Clock","Rooms and Services configuration file","Reservation","Blocked Rooms Warnings file","Blocked Rooms Warnings file","None","None","None"],
#25
["Blocked Rooms Warning file","Blocked Rooms Warning file","Reservation","None","None","Message"],
#26
["Reservation","None","Reservation","None","Reservation","Message","None","Message","Message","Message"],
#27
["Reservation","Reservation","Reservation","Reservation","Reservation","Reservation","Reservation","Reservation","Reservation","None","Message","Message"],
#28
["Reservation","None","None","Services","Children","Rooms","Reservation","Message","None","None","None","None","Message","Message"],
#29
["None","None","Reservation","None","None","Room","Commission","Booked room","Available room","Reservation","Room","Service","Selected room","Service","Reservation","None","Customer","Service","Booked room","Children","Reservation","Season","Reservation","Booked room","Service","Children","Message","None","None","None","None","Message"],
#30
["Reservation","Room","Services","Services","Services","Room","Services","Services","Services","Services","Room","None","Services","Services","Reservation","Message","None","Message"],
#31
["None","None","Reservation","None","Reservation","Reservation","None","None","Message"],
#32
["None","None","Agency","None","Agency","Agency","None","None","Message"],
#33
["Agency","Agency","Room","Agency","Room","None","Message"],
#34
["None","None","Agency","None","None","None","None","None","Agency","Message","None","Message"],
#35
["None","None","Agency details","None","None","None","None","None","None","Agency details","Messages","None","Messages","Messages","Messages"],
#36
["None","None","Room","None","None","Commission file","Booked Room file","Room file","Room","Room","None","Commission file","Message","None","None","None","None","None","None","None","Message","Message"],
#37
["Room","None","None","Room","Message","None","None","None","None","Message"],
#38
["None","None","Order","None","Order","Order","None","None","None","Message"],
#39
["Order","Order","Food","Order","Food","None","Message"],
#40
["None","None","Table","Table","Table","Order","None","None","None","Table","Table","Order","Message","None","Message","Message","Message"],
#41
["None","None","Food","Food","Category","Category","Food","Food","None","Order","Order","Message","None","Message"],
#42
["Food","None","None","Food","Order","Message","None","None","None","None","Message","Message"],
#43
["Order","None","None","Food","Order","Table","Message","None","None","None","Message","Message"],
#44
["None","None","Order","None","Order","Message","None","Message"],
#45
["Order","Order","Food","Order","Food","None","Message"],
#46
["Order","None","None","Order","Table","Message","None","None","None","Message","Message"],
#47
["None","None","Menu category","None","Menu category","Menu category","None","None","Message"],
#48
["Menu category","Menu category","Food","Menu category","Food","None","Message"],
#49
["None","None","Menu category","None","None","Menu category","Message","None","Message"],
#50
["None","None","Menu category","None","None","Menu category","Message","None","Message","Message","Message"],
#51
["Menu category","None","None","Menu category","Food","Message","None","None","None","None","Message","Message","Message"],
#52
["None","None","Food","None","None","None","Food","Message","None","Message"],
#53
["Food","None","None","Food","Message","None","None","None","None","Message","Message"],
#54
["None","None","Food","None","None","None","Food","Message","None","Message","Message","Message"],
#55
["None","None","Room","Guest","Guest","Guest","None","None","Customer","Customer","Customer","None","None","Customer","Room","None","None","None","Customer","Room","Guest","Reservation","Message","None","None","None","Message","None","Customer","None","None","Customer","None","None","None","None","None","None","None","None","None","None","Message","Message","Message"],
#56
["None","None","Room service","None","Room service","Service","Room service","Service","None","None","Message"],
#57
["Room","Services","Services","Services","Services","Services","None","Services","Reservation","Message","None","Message"],
#58
["Room","Telephone bill","Telephone bill","Telephone bill","None","None","Services configuration","None","Telephone bill","Reservation","Message","None","Message","Message"],
#59
["Reservation","Reservation","Services","Telephone","Reservation","Services","Telephone","None","None","None","Messages","Messages"],
#60
["Customer","Room","Commission file","Booked Room file","Room","Room","None","Service","Service","Room","Service","Service","Service","Customer","Customer","Reservation","Service","Service","Telephone Bill","Reservation","Room Guest","Message","None","None","None","Message","Message","Message","Message"],
#61
["Reservation","Customer file","Customer","Message","None","Message"],
#62
["Reservation","Bill","None","None","Message"]

]

reference = [
#1
["None", "None", "Room", "Room", "Room", "None", "None", "Message"],
#2
["Room", "Room", "Room", "None", "Message"],
#3
["Room", "Booked Room", "Booked Room", "Room", "None", "None", "Room", "Message", "None", "Message", "None","None","None", "Message", "None", "None", "None", "Message", "Message"],
#4
["None","None","Room","None","None","None","None","Room","Message","None","Message", "Message","Message"],
#5
["None","None","Service","Service","Service","None","None","Message"],
#6
["Service","Service","Service","None","Message"],
#7
["None","None","Service","None","None","None","Service","Message","None","None","Message","Message"],
#8
["None","None","Service","None","None","None","None","Service","Message","None","Message","Message","Message"],
#9
["None","None","None","Customer","None","Customer","Customer","None","None","Message"],
#10
["Customer","Customer","Customer","None","Message","Message"],
#11
["None","None","Customer","None","None","None","None","Customer","Message","None","Message","Message"],
#12
["None","None","Customer","None","None","None","None","None","Customer","Message","None","Message","Message","Message"],
#13
["Configured seasons", "Configured season", "Configured season","None","None","Message"],
#14
["Configured season", "Configured season", "Configured seasons", "None","Message","Message","None"],
#15
["None","None","Configured season", "None","None","None","None","Configured season", "Message","None","Message","Message"],
#16
["Configured season","None","None","Configured season","Message","None","None","None","None","Message"],
#17
["None","None","Configured season","None","None","None","None","None","Configured season","Message","None","Message","Message","Message"],
#18
["Rooms and services Configuration","Rooms and services Configuration","Rooms and services Configuration","None","None","Message"],
#19
["None","None","Rooms and services configuration","None","None","None","Rooms and services configuration","Message","None","Message","Message"],
#20
["Assigned Service", "Assigned Service", "Assigned Service","None","None","Messages"],
#21
["None","None","Service","None","Service","Service","Assigned service","None","None","Assigned service","Message","None","None","None","None","None","None","None","None","Message"],
#22
["Assigned service","None","None","Assigned service","Message","None","None","None","None","Message"],
#23
["None","None","Room","None","None","Room","Commissioned room","Booked rooms","Room","None","Room","Room","Assigned service","Room","Assigned service","Reservation","Configured season","Reservation","None","Customer","Customer","Customer","None","None","Customer","Reservation","Customer","Configured season","Reservation","Booked room","Requested Service","Children age","Message","None","Customer","None","None","Customer","None","None","None","None","None","None","Message","Message","Message","Message","Message"],
#24
["Clock","Rooms and Services configuration","Reservation","Blocked Rooms Warnings","Blocked Rooms Warnings","None","None","None"],
#25
["Blocked rooms warnings","Blocked rooms warnings","Blocked rooms warnings","None","None","Message"],
#26
["None","None","Reservation","None","Reservation","Message","None","Message","Message","Message"],
#27
["Reservation","Reservation","Booked room","Requested services","Children’s ages","Reservation","Booked room","Requested services","Children’s ages","None","Message","Message"],
#28
["Reservation","None","None","Requested Services","Children's ages","Booked rooms","Reservation","Message","None","None","None","None","Message","Message"],
#29
["None","None","Reservation","None","None","Room","Commissioned Room","Booked room","Room","Reservation","Room","Assigned Service","Room","Assigned Service","Reservation","Customer","Customer","Requested Service","Booked room","Children's age","Reservation","Configured season","Reservation","Booked room","Requested Service","Children's age","Message","None","None","None","None","Message"],
#30
["Reservation","Booked Room","Assigned service","Requested Service","Room","Booked Room","Requested Service","Assigned service","Room","Requested Service","Booked Room","None","Requested Service","Requested Service","Reservation","Message","None","Message"],
#31
["None","None","Reservation","None","Reservation","Reservation","None","None","Message"],
#32
["None","None","Agency","None","Agency","Agency","None","None","Message"],
#33
["Agency","Agency","Commissioned Room","Agency","Commissioned Room","None","Message"],
#34
["None","None","Agency","None","None","None","None","None","Agency","Message","None","Message"],
#35
["None","None","Agency","None","None","None","None","None","None","Agency","Message","None","Message","Message","Message"],
#36
["None","None","Room","None","None","Commissioned room","Booked room","Room","Room","Commissioned room","None","Commissioned room","Message","None","None","None","None","None","None","None","Message","Message"],
#37
["Commissioned room","None","None","Commissioned room","Message","None","None","None","None","Message"],
#38
["None","None","Order","None","Order","Order","None","None","None","Message"],
#39
["Order","Order","Ordered Food","Order","Ordered Food","None","Message"],
#40
["None","None","Table","Table","Table","Order","None","None","None","Table","Table","Order","Message","None","Message","Message","Message"],
#41
["None","None","Food","Food","Menu category","Menu category","Food","Ordered food","None","Ordered food","Order","Message","None","Message"],
#42
["Ordered food","None","None","Ordered food","Order","Message","None","None","None","None","Message","Message"],
#43
["Order","None","None","Ordered food","Order","Table","Message","None","None","None","Message","Message"],
#44
["None","None","Order","None","Order","Message","None","Message"],
#45
["Order","Order","Ordered food","Order","Ordered food","None","Message"],
#46
["Order","None","None","Order","Table","Message","None","None","None","Message","Message"],
#47
["None","None","Menu category","None","Menu category","Menu category","None","None","Message"],
#48
["Menu category","Menu category","Food","Menu category","Food","None","Message"],
#49
["None","None","Menu category","None","None","Menu category","Message","None","Message"],
#50
["None","None","Menu category","None","None","Menu category","Message","None","Message","Message","Message"],
#51
["Menu category","None","None","Menu category","Food","Message","None","None","None","None","Message","Message","Message"],
#52
["None","None","Food","None","None","None","Food","Message","None","Message"],
#53
["Food","None","None","Food","Message","None","None","None","None","Message","Message"],
#54
["None","None","Food","None","None","None","Food","Message","None","Message","Message","Message"],
#55
["None","None","Booked Room","Room Guest","Customer","Customer","None","None","Customer","Customer","Customer","None","None","Customer","Room","None","None","None","Customer","Booked Room","Room Guest","Reservation","Message","None","None","None","Message","None","Customer","None","None","Customer","None","None","None","None","None","None","None","None","None","None","Message","Message","Message"],
#56
["None","None","Requested services","None","Requested service","Service","Requested service","Service","None","None","Message"],
#57
["Booked room","Assigned service","Service","Service","Assigned service","Requested service","None","Requested service","Reservation","Message","None","Message"],
#58
["Booked room","Telephone bill","Telephone bill","Telephone bill","None","None","Rooms and services configuration","None","Telephone bill","Reservation","Message","None","Message","Message"],
#59
["Reservation","Reservation","Requested Service","Telephone bill","Reservation","Requested Service","Telephone bill","None","None","None","Message","Message"],
#60
["Customer","Room","Commissiond room","Booked room","Room","Room","None","Assigned Service","Assigned Service","Booked room","Assigned Service","Assigned Service","Requested Service","Customer","Customer","Booked room","Requested Service","Requested Service","Telephone Bill","Reservation","Room Guest","Message","None","None","None","Message","Message","Message","Message"],
#61
["Reservation","Customer","Customer","Message","None","Message"],
#62
["Reservation","Bill","None","None","Message"]
]

for i in range(len(model_out)):
    if len(model_out[i]) != len(reference[i]):
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
print("Total OOI ", totalDG)
