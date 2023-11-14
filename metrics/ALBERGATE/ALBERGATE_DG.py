from rouge import Rouge
from nltk.translate.bleu_score import SmoothingFunction, corpus_bleu, sentence_bleu

model_out = [ 
#1
["None", "None", "Room code", "Room details", "None", "None", "Messages"],
#2
["Room code", "Room code", "Room details", "None", "Messages"],
#3
["Room ID", "Room ID", "Room details", "Room details", "None","None","Room details", "Messages","None","Messages", "None", "None", "None", "Messages", "None", "None", "None", "Messages", "Messages"],
#4
["None","None","Room details","None","None","None","None","Messages","None","Messages","Messages","Messages"],
#5
["None","None","Service code", "Service code", "Service details","None","None","Messages"],
#6
["Service code", "Service code", "Service details","None","Messages"],
#7
["None","None","Service details","None","None","None","Service details","Messages","None","None","Messages","Messages"],
#8
["None","None","Service details","None","None","None","None","Service details","Messages","None","Messages","Messages","Messages"],
#9
["None","None","None","Customer filters","None","Customer details","Customer details","None","None","Messages"],
#10
["Customer fiscal code", "Customer code", "Customer details","None","Messages","Messages"],
#11
["None","None","Customer details","None","None","None","None","Customer details","Messages","None","Messages","Messages"],
#12
["None","None","Customer details","None","None","None","None","None","Customer details","Messages","None","Messages","Messages","Messages"],
#13
["Seasons Configuration","Season details", "Seasons details","None","None","Messages"],
#14
["Configuration ID", "Configuration ID", "Configuration details", "None","Messages","Messages"],
#15
["None","None","Season configuration details", "None","None","None","None","Season configuration details", "Messages","None","Messages","Messages"],
#16
["Configuration ID","None","None", "Configuration details","Messages","None","None","None","None","Messages"],
#17
["None","None","Season configuration details","None","None","None","None","None","Season configuration details","Messages","None","Messages","Messages","Messages"],
#18
["Configurations request","Configuration details","Configuration details","None","None","Messages"],
#19
["None","None","Configuration details","None","None","None","Configuration details","Messages","None","Messages","Messages"],
#20
["Room ID", "Room services","Room services","None","None","Messages"],
#21
["None","None","Service code","None","Servie details","Service details","Service details","None","None","Service details","Messages","None","None","None","None","None","None","None","None","Messages"],
#22
["Service ID","None","None","Service details","Messages","None","None","None","None","Messages"],
#23
["None","None","Room filters","None","None","Room details","Room details","Room details","Room details","None","Reservation details","Room details","Room services","Room details","Room services","Reservation details","Supplements","Reservation details","None","Fiscal code","Customer details","Customer details","None","None","Customer details","Reservation details","Customer details","Season configuration","Reservation header","Booked room details","Requested services","Children's ages","Messages","None","Customer details","None","None","Customer details","None","None","None","None","None","None","Messages","Messages","Messages","Messages","Messages"],
#24
["Clock tick","Blocked rooms configuration","Reservations details","Blocked rooms warnings","Reservations IDs","None","None","None"],
#25
["Blocked rooms warnings","Reservation Ids","Reservation details","None","None","Messages"],
#26
["Reservation ID","None","New status","None","Reservation details","Messages","None","Messages","Messages","Messages"],
#27
["Reservation ID","Reservation header","Booked rooms","Requested services","Children’s ages","Reservation details","Booked rooms","Requested services","Children’s ages","None","Messages","Messages"],
#28
["Reservation ID","None","None","Requested Services","Children's ages","Booked Rooms","Reservation details","Messages","None","None","None","None","Messages","Messages"],
#29
["None","None","Reservation filters","None","None","Room details","Commission details","Booked room details","Available room details","Reservation details","Room details","Service details","Selected room details","Service details","Reservation details","None","Customer details","Service details","Booked room details","Children's ages","Reservation details","Season configuration","Reservation details","Booked room details","Service details","Children's Ages","Messages","None","None","None","None","Messages"],
#30
["Reservation ID","Room details","Available services","Selected services","Extra services","Room details","Selected services","Available services","Extra services","Selected services","Selected rooms","None","Selected services","Removed services","Reservation details","Messages","None","Messages"],
#31
["None","None","Filter details","None","Reservation details","Reservation details","None","None","Messages"],
#32
["None","None","Search criteria","None","Agency details","Agency details","None","None","Messages"],
#33
["Agency ID","Agency ID","Room details","Agency details","Room details","None","Messages"],
#34
["None","None","Agency details","None","None","None","None","None","Agency details","Messages","None","Messages"],
#35
["None","None","Agency details","None","None","None","None","None","None","Agency details","Messages","None","Messages","Messages","Messages"],
#36
["None","None","Date interval","None","None","Uncommissioned rooms","Unbooked rooms","Room details","Room details","Selected rooms","None","Selected rooms","Messages","None","None","None","None","None","None","None","Messages","Messages"],
#37
["Room ID","None","None","Room details","Messages","None","None","None","None","Messages"],
#38
["None","None","Search criteria","None","Order details","Order details","None","None","None","Messages"],
#39
["Order ID","Order ID","Food details","Order details","Food details","None","Messages"],
#40
["None","None","Tables status","Free tables","Table ID","Order details","None","None","None","Tables status","Table status","Order details","Messages","None","Messages","Messages","Messages"],
#41
["None","None","Search detail","Food detail","Category details","Category details","Food details","Food ID","None","Order details","Order details","Messages","None","Messages"],
#42
["Food ID","None","None","Food details","Order total price","Messages","None","None","None","None","Messages","Messages"],
#43
["Order ID","None","None","Food details","Order details","Table status","Messages","None","None","None","Messages","Messages"],
#44
["None","None","Discount detail","None","Order details","Messages","None","Messages"],
#45
["Order ID","Order details","Food details","Order details","Food details","None","Messages"],
#46
["Order details","None","None","Order status","Table status","Messages","None","None","None","Messages","Messages"],
#47
["None","None","Menu category description","None","Menu category details","Menu category details","None","None","Messages"],
#48
["Menu category ID","Menu category ID","Food details","Menu category details","Food details","None","Messages"],
#49
["None","None","Menu categoy details","None","None","Menu categoy details","Messages","None","Messages"],
#50
["None","None","Menu category details","None","None","Menu category details","Messages","None","Messages","Messages","Messages"],
#51
["Menu category ID","None","None","Menu category details","Food details","Messages","None","None","None","None","Messages","Messages","Messages"],
#52
["None","None","Food details","None","None","None","Food details","Messages","None","Messages"],
#53
["Food ID","None","None","Food detail","Messages","None","None","None","None","Messages","Messages"],
#54
["None","None","Food details","None","None","None","Food details","Messages","None","Messages","Messages","Messages"],
#55
["None","None","Room details","Guest deails","Guest deails","Guest deails","None","None","Customer details","Customer details","Customer details","None","None","Customer details","Room details","None","None","None","Customer details","Room details","Guest details","Reservation status","Messages","None","None","None","Messages","None","Customer details","None","None","Customer details","None","None","None","None","None","None","None","None","None","None","Messages","Messages","Messages"],
#56
["None","None","Filter fields","None","Room service details","Service details","Requested service","Service details","None","None","Messages"],
#57
["Room code","Assigned services","Service details","Service details","Assigned services","Service details","None","Service details","Reservation details","Messages","None","Messages"],
#58
["Room code","Telephone bill details","Telephone bill details","Number of phone calls","None","None","Phone call cost","None","Telephone bill details","Reservation total amount","Messages","None","Messages","Messages"],
#59
["Reservation ID","Reservation details","Requested services","Telephone bill","Total amount","Requested services","Telephone bill","None","None","None","Messages","Messages"],
#60
["Customer details","Room details","Room details","Room details","Room details","Room code","None","Service details","Service details","Room details","Service details","Service details","Service details","Customer details","Room code","Room details","Service details","Service details","Room code","Total amount","Room code","Messages","None","None","None","Messages","Messages","Messages","Messages"],
#61
["Checkout command","Reservation status","Room reference","Messages","None","Messages"],
#62
["Reservation details","Bill details","None","None","Messages"]
]

reference = [
#1
["None", "None", "Room code", "Room details", "None", "None", "Messages"],
#2
["Room code", "Room details", "Room details", "None", "Messages"],
#3
["Room code", "Room details", "Room details", "Room details", "None", "None", "Room details", "Messages", "None", "Messages","None","None","None","Messages","None","None","None","Messages", "Messages"],
#4
["None","None","Room details","None","None","None","None","Messages","None","Messages","Messages","Messages"],
#5
["None","None","Service code", "Service details", "Service details","None","None","Messages"],
#6
["Service code", "Service details", "Service details","None","Messages"],
#7
["None","None","Service details","None","None","None","Service details","Messages","None","None","Messages","Messages"],
#8
["None","None","Service details","None","None","None","None","Service details","Messages","None","Messages","Messages","Messages"],
#9
["None","None","None","Customer filters","None","Customer details","Customer details","None","None","Messages"],
#10
["Customer fiscal code", "Customer details", "Customer details","None","Messages","Messages"],
#11
["None","None","Customer details","None","None","None","None","Customer details","Messages","None","Messages","Messages"],
#12
["None","None","Customer details","None","None","None","None","None","Customer details","Messages","None","Messages","Messages","Messages"],
#13
["Configured Seasons request","Configured Seasons details", "Configured Seasons details","None","None","Messages"],
#14
["Season configuration ID", "Configured season details", "Configured season details", "None","Messages","Messages"],
#15
["None","None","Configured season details", "None","None","None","None","Configured season details", "Messages","None","Messages","Messages"],
#16
["Season configuration ID","None","None","Configured season details","Messages","None","None","None","None","Messages"],
#17
["None","None","Configured season details","None","None","None","None","None","Configured season details","Messages","None","Messages","Messages","Messages"],
#18
["Rooms and services Configurations request","Rooms and services Configurations details","Rooms and services Configurations details","None","None","Messages"],
#19
["None","None","Rooms and services configuration details","None","None","None","Rooms and services configuration details","Messages","None","Messages","Messages"],
#20
["Room code", "Assigned Service details", "Assigned Service details","None","None","Messages"],
#21
["None","None","Service code","None","Servie details","Service details","Assigned services details","None","None","Assigned services details","Messages","None","None","None","None","None","None","None","None","Messages"],
#22
["Assigned service details","None","None","Assigned service details","Messages","None","None","None","None","Messages"],
#23
["None","None","Room filters","None","None","Room details","Commissioned Room details","Booked rooms details","Room details","None","Room codes","Room details","Assigned services details","Room details","Requestable service details","Reservation details","Supplement details","Reservation details","None","Customer fiscal code","Customer details","Customer details","None","None","Customer details","Reservation details","Customer details","Configured season details","Reservation details","Booked room details","Requested services details","Children's ages details","Messages","None","Customer details","None","None","Customer details","None","None","None","None","None","None","Messages","Messages","Messages","Messages","Messages"],
#24
["Clock tick","Rooms and Services configuration details","Reservations details","Blocked Rooms Warnings details","Reservations IDs","None","None","None"],
#25
["Blocked rooms warnings request","Reservation Ids","Blocked rooms warnings details","None","None","Messages"],
#26
["None","None","New status","None","Reservation details","Messages","None","Messages","Messages","Messages"],
#27
["Reservation ID","Reservation details","Booked rooms details","Requested services details","Children’s ages details","Reservation details","Booked rooms details","Requested services details","Children’s ages details","None","Messages","Messages"],
#28
["Reservation ID","None","None","Requested Services details","Children's ages details","Booked rooms details","Reservation details","Messages","None","None","None","None","Messages","Messages"],
#29
["None","None","Reservation filters","None","None","Room details","Commissioned Room details","Booked room details","Available room details","Reservation details","Room details","Assigned services details","Selected room details","Service details","Reservation details","Customer details","Customer details","Requested service details","Booked room details","Children's age details","Reservation details","Configured season details","Reservation details","Booked room details","Requested service details","Children's age details","Messages","None","None","None","None","Messages"],
#30
["Reservation ID","Booked Room details","Available services","Selected services","Extra services","Booked Room details","Selected services","Available services","Room details","Selected services","Selected rooms","None","Selected services","Removed services","Reservation details","Messages","None","Messages"],
#31
["None","None","Filter details","None","Reservation details","Reservation details","None","None","Messages"],
#32
["None","None","Search criteria","None","Agency details","Agency details","None","None","Messages"],
#33
["Agency ID","Agency details","Commissioned Room details","Agency details","Commissioned Room details","None","Messages"],
#34
["None","None","Agency details","None","None","None","None","None","Agency details","Messages","None","Messages"],
#35
["None","None","Agency details","None","None","None","None","None","None","Agency details","Messages","None","Messages","Messages","Messages"],
#36
["None","None","Date interval","None","None","Uncommissioned rooms","Unbooked rooms","Room details","Room details","Selected rooms","None","Commissioned room details","Messages","None","None","None","None","None","None","None","Messages","Messages"],
#37
["Room code","None","None","Commissioned Room details","Messages","None","None","None","None","Messages"],
#38
["None","None","Search criteria","None","Order details","Order details","None","None","None","Messages"],
#39
["Order ID","Order details","Ordered Food details","Order details","Ordered Food details","None","Messages"],
#40
["None","None","Tables status","Free tables","Table ID","Order details","None","None","None","Tables status","Table details","Order details","Messages","None","Messages","Messages","Messages"],
#41
["None","None","Search detail","Food detail","Menu category details","Menu category details","Food details","Food selection","None","Ordered food details","Order details","Messages","None","Messages"],
#42
["Food ID","None","None","Ordered food details","Order details","Messages","None","None","None","None","Messages","Messages"],
#43
["Order ID","None","None","Ordered food details","Order details","Table status","Messages","None","None","None","Messages","Messages"],
#44
["None","None","Discount detail","None","Order details","Messages","None","Messages"],
#45
["Order ID","Order details","Ordered food details","Order details","Ordered food details","None","Messages"],
#46
["Order details","None","None","Order status","Table status","Messages","None","None","None","Messages","Messages"],
#47
["None","None","Menu category description","None","Menu category details","Menu category details","None","None","Messages"],
#48
["Menu category ID","Menu category details","Food details","Menu category details","Food details","None","Messages"],
#49
["None","None","Menu categoy details","None","None","Menu categoy details","Messages","None","Messages"],
#50
["None","None","Menu category details","None","None","Menu category details","Messages","None","Messages","Messages","Messages"],
#51
["Menu category ID","None","None","Menu category details","Food details","Messages","None","None","None","None","Messages","Messages","Messages"],
#52
["None","None","Food details","None","None","None","Food details","Messages","None","Messages"],
#53
["Food ID","None","None","Food detail","Messages","None","None","None","None","Messages","Messages"],
#54
["None","None","Food details","None","None","None","Food details","Messages","None","Messages","Messages","Messages"],
#55
["None","None","Room details","Guest deails","Customer details","Customer details","None","None","Customer details","Customer details","Customer details","None","None","Customer details","Room details","None","None","None","Customer details","Booked room details","Room Guest details","Reservation status","Messages","None","None","None","Messages","None","Customer details","None","None","Customer details","None","None","None","None","None","None","None","None","None","None","Messages","Messages","Messages"],
#56
["None","None","Filter fields","None","Requested service details","Service details","Requested service details","Service details","None","None","Messages"],
#57
["Room code","Assigned service details","Service details","Service details","Assigned service details","Requested service details","None","Requested service details","Reservation details","Messages","None","Messages"],
#58
["Room code","Telephone bill details","Telephone bill details","Number of phone calls","None","None","Phone call cost","None","Telephone bill details","Reservation total amount","Messages","None","Messages","Messages"],
#59
["Reservation ID","Reservation details","Requested Service details","Telephone bill details","Total amount","Requested Service details","Telephone bill details","None","None","None","Messages","Messages"],
#60
["Customer details","Room details","Commissioned room details","Booked room details","Room details","Room code","None","Assigned service details","Old Assigned service details","Booked room details","Old Assigned Service details","New Assigned Service details","Requestable Services details","Customer details","Customer details","Booked Room details","Services details","Services details","Telephone Bill details","Total amount","Room code","Messages","None","None","None","Messages","Messages","Messages","Messages"],
#61
["Reservation details","Reservation status","Customer details","Messages","None","Messages"],
#62
["Reservation details","Bill details","None","None","Messages"]

]

for i in range(len(model_out)):
    if len(model_out[i]) != len(reference[i]):
        print("RIGA ",i)

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

differences = 0
for i in range(0,len(reference)):
    for j in range(0, len(reference[i])):
        if model_out[i][j] != reference[i][j]:
            differences = differences +1

print("DIFFERENCES: ", differences)
