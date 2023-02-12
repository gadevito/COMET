from rouge import Rouge

model_out = [ 
#1
"Room", "Room","Room", "Message",
#2
"Room","Room","Room","Message",
#3
"Room","Room","Room","Room","Room","Message","Message","Message","Message", "Message",
#4
"Room","Room","Message","Message","Message","Message",
#5
"Service","Service","Service", "Message",
#6
"Service","Service","Service","Message",
#7
"Service","Service","Message","Message","Message",
#8
"Service","Service","Message","Message","Message","Message",
#9
"Customer","Customer","Customer","Message",
#10
"Customer","Customer","Customer","Message","Message",
#11
"Customer","Customer","Message","Message","Message",
#12
"Customer","Customer","Message","Message","Message",
#13
"Season","Season","Season","Message",
#14
"Season configuration","Season configuration","Season configuration","Message","Message",
#15
"Season","Season","Message","Message","Message",
#16
"Configuration","Configuration", "Message",
#17
"Configuration","Configuration","Message","Message","Message","Message",
#18
"Configuration","Configuration","Configuration","Message",
#19
"Configuration", "Configuration", "Message", "Message", "Message",
#20
"Room","Room","Room services","Message",
#21
"Service","Service","Service","Service","Service","Message","Message",
#22
"Room service","Room service","Message","Message",
#23
"Room","Room","Room Commission","Booked room","Room","Room","Room","Room services","Room","Room services","Reservation","Configured season","Reservation","Customer","Customer","Customer","Customer","Reservation","Customer","Configured season","Reservation","Booked room","Room services","Children’s age","Message","Customer","Customer","Message","Message","Message","Message","Message",
#24
"Clock","Configuration","Reservations","Warnings","ID",
#25
"Blocked rooms warnings","Reservation","Reservation","Message",
#26
"Reservation","None","Reservation","Message","Message","Message",
#27
"Reservation","Reservation","Room","Service","Age","Reservation","Room","Service","Age","Message","Message",
#28
"Reservation","Service","Room","Age","Reservation","Message","Message","Message",
#29
"Reservation","Room","Room","Room","Room","Room","Room","Room service","Room","Room service","Reservation","None","Customer","Room service","Room","Age","Reservation","Configuration","Reservation","Room","Room service","Age","Message","Message","Message",
#30
"Reservation","Room","Service","Service","Service","Room","Service","Service","Service","Service","Room","Service","Service","Reservation","Message","Message",
#31
"Filter","Reservation","Reservation","Message",
#32
"Agency","Agency","Agency","Message",
#33
"Agency","Agency","Room","Agency","Room","Message",
#34
"Agency","Agency","Message","Message",
#35
"Agency","Agency","Message","Message","Message","Message",
#36
"Date","Room","Room","Room","Room","Room","Room","Message","Message",
#37
"Room","Room","Message","Message",
#38
"Orders","Orders","Orders","Message",
#39
"Order","Order","Foods","Order","Foods","Message",
#40
"Table","Table","Table","Order","Table","Table","Order","Message","Message","Message","Message",
#41
"Food and Category","Food and Category","Category","Food","Category","Quantity","Food","Order","Message","Message",
#42
"Food","Food","Order","Message","Message","Message",
#43
"Order","Order","Order","Table","Message","Message","Message",
#44
"Discount","Order","Message",
#45
"Order","Order","Food","Order","Food","Message",
#46
"Order","Order","Table","Message",
#47
"Menu Category","Menu Category","Menu Category","Message",
#48
"Menu Category","Menu Category","Foods","Menu Category","Foods","Message",
#49
"Menu category","Menu category","Message",
#50
"Menu category","Menu category","Message","Message","Message","Message",
#51
"Menu category","Menu category","Food","Message","Message","Message","Message",
#52
"Food","Food","Message","Message",
#53
"Food","Food","Message","Message","Message",
#54
"Food","Food","Message","Message","Message","Message",
#55
"Room","Guests","Guest","Guest","Customer","Customer","Customer","Customer","Room","Customer","Room","Guest","Status","Message","Customer","Customer","Message","Message","Message",
#56
"Room service","Room service","Room service","Room service","Room service","Message",
#57
"Room","Room","Services","Services","Services","Services","Services","Total amount","Message","Message",
#58
"Room","Telephone bill","Telephone bill","Phone calls","Configuration","Telephone bill","Total amount","Message","Message",
#59
"Reservation","Reservation","Services","Telephone","Total","Services","Telephone","Message",
#60
"Customer","Room","Commission","Booked Room","Room","Room","Room","Customer","Room","Services","Services","Services","Customer","Room","Booked Room","Services","Services","Room","Amount","Room","Message","Message",
#61
"Reservation","Reservation","Customer","Message","Message",
#62
"Reservation","Bill","Message"

]

reference = [
#1
"Room", "Room", "Room", "Message",
#2
"Room", "Room", "Room", "Message",
#3
"Room","Room","Room","Room","Room","Message","Message","Message","Message","Message",
#4
"Room", "Room","Message", "Message", "Message", "Message",
#5
"Service", "Service", "Service", "Message",
#6
"Service","Service","Service","Message",
#7
"Service","Service","Message","Message","Message",
#8
"Service","Service","Message","Message","Message","Message",
#9
"Customer","Customer","Customer","Message",
#10
"Customer","Customer","Customer","Message","Message",
#11
"Customer","Customer","Message","Message","Message",
#12
"Customer","Customer","Message","Message","Message",
#13
"Configured season","Configured season","Configured season","Message",
#14
"Configured season","Configured season","Configured season","Message","Message",
#15
"Configured season","Configured season","Message","Message","Message",
#16
"Configured season","Configured season","Message",
#17
"Configured season","Configured season","Message","Message","Message","Message",
#18
"Rooms and services configuration", "Rooms and services configuration", "Rooms and services configuration", "Message",
#19
"Rooms and services configuration","Rooms and services configuration","Message","Message", "Message",
#20
"Assigned Service","Assigned Service","Assigned Service", "Message",
#21
"Service","Service","Service","Assigned Service","Assigned Service","Message","Message",
#22
"Assigned service","Assigned service","Message","Message",
#23
"Room","Room","Commissioned room","Booked rooms","Room","Room","Room","Assigned service","Room","Assigned service","Reservation","Configured Season","Reservation","Customer","Customer","Customer","Customer","Reservation","Customer","Configured season","Reservation","Booked room","Requested Service","Children age","Message","Customer","Customer","Message","Message","Message","Message","Message",
#24
"Clock","Rooms and services configuration","Reservation","Blocked room","Blocked room",
#25
"Blocked room","Blocked room","Blocked room","Message",
#26
"None","Reservation","Reservation","Message", "Message", "Message",
#27
"Reservation","Reservation","Booked room","Requested Service","Children Ages","Reservation","Booked room","Requested Service","Children Ages","Message","Message",
#28
"Reservation","Requested Service","Booked room","Children Age","Reservation","Message","Message","Message",
#29
"Reservation","Room","Commissioned Room","Booked Rooms","Room","Room","Room","Assigned service","Room","Assigned service","Reservation","Customer","Customer","Requested services","Booked Room","Children Age","Reservation","Configured season","Reservation","Booked Room","Requested service","Children Age","Message","Message","Message",
#30
"Reservation","Booked Room","Room","Assigned Service","Requested Services","Booked Room","Room","Requested Service","Assigned Service","Requested Services","Booked Room","Assigned Service","Assigned Service","Reservation","Message","Message",
#31
"Reservation","Reservation","Reservation","Message",
#32
"Agency","Agency","Agency","Message",
#33
"Agency","Agency","Commissioned Room","Agency","Commissioned Room","Message",
#34
"Agency","Agency","Message","Message",
#35
"Agency","Agency","Message","Message","Message","Message",
#36
"Date interval","Commissioned Room","Booked room","Room","Room","Commissioned Room","Commissioned Room","Message","Message",
#37
"Commissioned Room","Commissioned Room","Message","Message",
#38
"Order","Order","Order","Message",
#39
"Order","Order","Ordered Food","Order","Ordered Food","Message",
#40
"Table","Table","Order","Table","Table","Table","Order","Message","Message","Message","Message",
#41
"Food","Food","Menu Category","Food","Menu Category","Ordered Food","Ordered Food","Order","Message","Message",
#42
"Ordered Food","Ordered Food","Order","Message","Message","Message",
#43
"Order","Order","Ordered Food","Table","Message","Message","Message",
#44
"Order","Order","Message",
#45
"Order","Order","Ordered Food","Order","Ordered Food","Message",
#46
"Order","Order","Table","Message",
#47
"Menu Category","Menu Category","Menu Category","Message",
#48
"Menu Category","Menu Category","Food","Menu Category","Food","Message",
#49
"Menu category","Menu category","Message",
#50
"Menu category","Menu category","Message","Message","Message","Message",
#51
"Menu category","Menu category","Food","Message","Message","Message","Message",
#52
"Food","Food","Message","Message",
#53
"Food","Food","Message","Message","Message",
#54
"Food","Food","Message","Message","Message","Message",
#55
"Booked Room","Room Guest","Customer","Customer","Customer","Customer","Customer","Customer","Room guest","Customer","Booked Room","Room Guest","Reservation","Message","Customer","Customer","Message","Message","Message",
#56
"Requested services","Requested services","Service","Requested services","Service","Message",
#57
"Booked Room","Assigned Service","Service","Assigned Service","Service","Requested Service","Requested Service","Reservation","Message","Message",
#58
"Booked Room","Telephone bill","Telephone bill","Telephone bill","Rooms and services Configuration","Telephone bill","Reservation","Message","Message",
#59
"Reservation","Requested Service","Service","Telephone bill","Telephone bill","Requested Service","Service","Message",
#60
"Customer","Room","Commissioned Room","Booked room","Room","Room","Assigned Service","Assigned Service","Room","Assigned Service","Assigned Service","Requested Service","Customer","Customer","Booked Room","Service","Requested Service","Telephone bill","Reservation","Room guest","Message","Message",
#61
"Reservation","Reservation","Customer","Message","Message",
#62
"Reservation","Bill details","Message"

]

print("NUMBER OF DGs: " , len(model_out))

rouge = Rouge()
print(rouge.get_scores(model_out, reference, avg=True))

