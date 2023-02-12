from rouge import Rouge

model_out = [ 
#1
"Room code", "Room code", "Rooms", "Messages",
#2
"Room ID", "Room ID", "Room details", "Messages",
#3
"Room ID", "Room ID", "Room details", "Room details", "Room details", "Messages", "Messages", "Messages", "Messages", "Messages",
#4
"Room details", "Room details", "Messages", "Messages", "Messages", "Messages",
#5
"Service code", "Service code",  "Service details", "Messages",
#6
"Service code", "Service code", "Service details", "Messages",
#7
"Service details", "Service details", "Messages", "Messages", "Messages",
#8
"Service details", "Service details", "Messages", "Messages", "Messages", "Messages",
#9
"Customer details", "Customer details", "Customer details", "Messages",
#10
"Customer fiscal code", "Customer fiscal code", "Customer details", "Messages", "Messages",
#11
"Customer details", "Customer details", "Messages", "Messages", "Messages",
#12
"Customer details", "Customer details", "Messages", "Messages", "Messages",
#13
"Season configuration", "Season configuration", "Season configuration", "Messages",
#14
"Season configuration ID", "Season configuration ID", "Season configuration details", "Messages", "Messages",
#15
"Season details","Season details","Messages","Messages","Messages",
#16
"Season configuration","Season Configuration", "Messages",
#17
"Configuration details", "Configuration details", "Messages",  "Messages", "Messages", "Messages",
#18
"Rooms and Services Configuration","Configuration details", "Configuration details", "Messages",
#19
"Rooms and service configuration","Rooms and service configuration","Messages","Messages","Messages",
#20
"Room ID","Room ID","Room services", "Messages",
#21
"Service code", "Service code", "Services details", "Services details", "Services details", "Messages", "Messages",
#22
"Room service","Room service","Messages","Messages",
#23
"Room search filters","Room details","Room Commission details","Booked room details","Room details","Room details","Room details","Room services","Room details","Room services","Reservation details","Configured season details","Reservation details","Fiscal code","Customer details","Customer details","Customer details","Reservation details","Customer details","Configured season details","Reservation details","Booked room details","Room services","Children’s age","Messages","Customer details","Customer details","Messages","Messages","Messages","Messages","Messages",
#24
"Clock tick","Rooms and Services configuration","Reservations details","Blocked Rooms Warnings", "Reservations IDs",
#25
"Blocked rooms warnings","Reservation IDs","Reservation details","Messages",
#26
"Reservation ID","None","Reservation details","Messages","Messages","Messages",
#27
"Reservation ID","Reservation ID","Booked rooms","Requested services","Children’s ages","Reservation details","Booked rooms","Requested services","Children’s ages","Messages", "Messages",
#28
"Reservation ID","Services","Rooms","Ages","Reservation details","Messages","Messages","Messages",
#29
"Reservation details", "Room details","Room details","Room details","Room details","Room details","Room details","Room services","Room details","Room services","Reservation details","None","Customer details","Room services","Room details","Children’s age","Reservation header","Season configuration","Reservation header","Room details","Room services","Children’s age","Messages","Messages","Messages",
#30
"Reservation ID","Room details","Services","Services","Services","Room details","Services","Services","Services","Services","Rooms","Services","Services","Reservation details","Messages","Messages",
#31
"Filter details","Fiscal code","Reservation headers","Messages",
#32
"Search criteria","Search criteria","Agency details","Messages",
#33
"Agency ID","Agency ID","Room details","Agency details","Room details","Messages",
#34
"Agency details","Agency details","Messages","Messages",
#35
"Agency details","Agency details","Messages","Messages","Messages","Messages",
#36
"Date Interval","Room details","Room details","Room details","Room details","Room details","Room details","Messages","Messages","Messages",
#37
"Room ID","Room details","Messages","Messages",
#38
"Search criteria","Search criteria","Orders details","Messages",
#39
"Order ID","Order ID","Foods","Order details","Foods details","Messages",
#40
"Table details","Table details","Table number","Order details","Table details","Table details","Order details","Messages","Messages","Messages","Messages",
#41
"Food and Category","Food and Category","Category","Food","Category","Quantity","Food","Order","Messages","Messages",
#42
"Food ID","Food details","Order details","Messages","Messages","Messages",
#43
"Order details","Order details","Order details","Table status","Messages","Messages","Messages",
#44
"Discount","Order details","Messages","Messages",
#45
"Order details","Order details","Food details","Order details","Food details","Messages",
#46
"Order details","Order status","Table status","Messages","Messages","Messages",
#47
"Menu Category Description","Menu Category Description","Menu Categories""Messages",
#48
"Menu Category ID","Menu Category ID","Foods associated with the menu category","Menu Category details","Foods associated with the given menu category","Messages",
#49
"Menu category details","Menu category details","Messages",
#50
"Menu category details","Menu category details","Messages","Messages","Messages","Messages",
#51
"Menu category details","Menu category details","Food details","Messages","Messages","Messages","Messages",
#52
"Food details","Food details","Messages","Messages",
#53
"Food ID","Food details","Messages","Messages","Messages",
#54
"Food details","Food details","Messages","Messages","Messages","Messages",
#55
"Room ID","Room Guests","Guest details","Guest details","Customer filters","Customer filters","Customer details","Customer details","Room ID","Customer details","Room details","Room Guests","Reservation status","Messages","Customer details","Customer details","Messages","Messages","Messages",
#56
"Room service description","Room service description","Room service details","Room service details","Room service details","Messages",
#57
"Room code","Room code","Services","Services","Services details","Services","Services","Total amount","Messages","Messages",
#58
"Room code","Telephone bill","Telephone bill","Number of phone calls","Room and services configuration","Telephone bill","Reservation total amount","Messages","Messages",
#59
"Reservation details","Reservation details","Services details","Telephone bill","Total amount","Services details","Telephone bill","Messages",
#60
"Customer ID","Room type","Commission file","Booked Room","Room details","Room code","Room code","Customer ID","Room details","Requested services","Assigned services","Requestable services","Customer details","Room code","Booked Room","Requestable services","Requestable services","Room code","Total amount","Room code","Messages","Messages",
#61
"Reservation details","Reservation details","Customer details","Messages","Messages",
#62
"Reservation","Bill details","Messages"
]

reference = [
#1
"Room code", "Room details", "Rooms data", "Messages",
#2
"Room code", "Room details", "Room details data", "Messages",
#3
"Room code", "Room details", "Room details", "Room details", "Room details", "Messages", "Messages", "Messages", "Messages", "Messages",
#4
"Room details", "Room details", "Messages", "Messages", "Messages", "Messages",
#5
"Service code", "Service details", "Service details data", "Messages",
#6
"Service code", "Service details", "Service details data", "Messages",
#7
"Service details", "Service details", "Messages", "Messages", "Messages",
#8
"Service details", "Service details", "Messages", "Messages", "Messages", "Messages",
#9
"Customer filters", "Customer details",  "Customer details data", "Messages",
#10
"Customer fiscal code", "Customer details", "Customer details", "Messages", "Messages",
#11
"Customer details", "Customer details", "Messages", "Messages", "Messages"
#12
"Customer details", "Customer details", "Messages", "Messages", "Messages",
#13
"Configured Seasons request", "Configured Season details", "Configured Season data", "Messages",
#14
"Season configuration ID", "Configured Season details", "Configured Season details", "Messages", "Messages",
#15
"Configured Season details", "Configured Season details", "Messages", "Messages", "Messages",
#16
"Season configuration ID","Configured Season details", "Messages",
#17
"Configured season details", "Configured season details","Messages","Messages","Messages", "Messages",
#18
"Rooms and services Configurations request", "Rooms and services Configuration details", "Rooms and services Configurations details", "Messages",
#19
"Rooms and service configuration details","Rooms and service configuration details","Messages","Messages", "Messages",
#20
"Room code","Assigned service details","Assigned services data", "Messages",
#21
"Service code","Service details","Services details data","Assigned Services details", "Assigned Services details", "Messages","Messages",
#22
"Assigned service details", "Assigned service details", "Messages", "Messages",
#23
"Room search filters","Room details","Commissioned Room details","Booked rooms details","Room details data","Room codes","Room details","Assigned services details","Room details","Requestable services data","Reservation details","Configured season details","Reservation details","Customer’s Fiscal code","Customer details","Customer details","Customer details","Reservation details","Customer details","Configured season details","Reservation details","Booked room details","Requested services details","Children's age details","Messages","Customer details","Customer details","Messages","Messages","Messages","Messages","Messages",
#24
"Clock tick","Rooms and Services configuration details","Reservation details","Blocked Rooms details","Blocked rooms details",
#25
"Blocked rooms warnings request","Blocked room details","Blocked room data","Messages",
#26
"None","Reservation details","Reservation details","Messages","Messages","Messages",
#27
"Reservation ID","Reservation details","Booked rooms details","Requested services details","Children's age details","Reservation details","Booked rooms details","Requested services details","Children's age details","Messages","Messages",
#28
"Reservation ID","Requested Services details","Booked Rooms details","Children’s Ages","Reservation details","Messages","Messages","Messages",
#29
"Availability filter","Room details","Commissioned Room details","Booked Room details","Room details data","Room codes","Room details","Assigned services details","Room details","Requestable services data","Reservation details","Customer details","Customer details","Requested services details","Booked Room details","Children's age details","Reservation header details","Configured season details","Reservation header details","Booked Room details","Requested services details","Children's age details","Messages","Messages","Messages",
#30
"Reservation ID","Booked Room details","Room details","Assigned Services details","Requested Services details","Booked Room details","Room details","Requestable Services data","Assigned Services details","Services data","Booked Rooms details","Assigned Services details","Assigned Services details","Reservation details","Messages", "Messages",
#31
"Filter details","Reservation details","Reservation headers data","Messages",
#32
"Search criteria","Agency details","Agency details data","Messages",
#33
"Agency ID","Agency details","Commissioned Room details","Agency details","Commissioned Room details data","Messages",
#34
"Agency details","Agency details","Messages","Messages",
#35
"Agency details","Agency details","Messages","Messages","Messages","Messages",
#36
"Date interval","Uncommissioned Room details","Booked Room details","Room details","Uncommissioned Room details data","Room details data","Commissioned Room details","Messages","Messages","Messages",
#37
"Room code","Commissioned Room details","Messages","Messages",
#38
"Search criteria","Orders details","Orders details","Messages",
#39
"Order ID","Order details","Ordered Foods details","Order details","Ordered Foods details data","Messages",
#40
"Table details","Table details data","Order details","Table number","Table details","Table details","Order details","Messages","Messages","Messages","Messages",
#41
"Food and Category","Food details","Menu Category details","Selected food data","Selected Category data","Ordered Food details","Ordered Food details","Order details","Messages","Messages",
#42
"Food ID","Ordered Food details","Order details","Messages","Messages","Messages",
#43
"Order ID","Order details","Ordered Food details","Table status","Messages","Messages","Messages",
#44
"Order details","Order details","Messages","Messages",
#45
"Order ID","Order details","Ordered Food details","Order details","Ordered Food details data","Messages",
#46
"Order Id","Order details","Table details","Messages","Messages","Messages",
#47
"Menu Category Description","Menu category details","Menu Categories","Messages",
#48
"Menu Category ID","Menu Category Details","Foods associated with the menu category","Menu Category Details","Foods associated with the menu category","Message",
#49
"Menu category details","Menu category details","Messages",
#50
"Menu category details","Menu category details","Messages","Messages","Messages","Messages",
#51
"Menu Category ID","Menu category details","Food details","Messages","Messages","Messages","Messages",
#52
"Food details","Food details","Messages","Messages",
#53
"Food ID","Food details","Messages","Messages","Messages",
#54
"Food details","Food details","Messages","Messages","Messages","Messages",
#55
"Room ID","Room Guests details","Customer details","Customer details data","Customer filters","Customer details","Customer data","Customer details","Room Guests details","Customer details","Booked Room details","Room Guest details","Reservation details","Messages","Customer details","Customer details","Messages","Messages","Messages",
#56
"Room service description","Requested services details","service details","Requested service details","service details","Messages",
#57
"Room code","Assigned Services details","Service Details","Assigned Services data","Services details","Requested Services details","Requested Services details","Reservation details","Messages","Messages",
#58
"Room code","Telephone bill Details","Telephone bill details","Telephone bill details","Rooms and services configuration details","Telephone bill details","Reservation detail","Messages","Messages",
#59
"Reservation ID","Requested Service details","Services details","Telephone bill details","Telephone bill details","Requested Services details","Service details","Messages",
#60
"Customer fiscal code","Room details","Commissioned room details","Booked Room details","Room code","Room details","Assigned service details","Old Room Assigned service details","Room details","Old room Selected services data","New room Selected services data","Requestable services details","Customer details","Customer details","Booked Room details","Requestable services details","Requestable services details","Telephone bill details","Reservation details","Room code","Messages","Messages",
#61
"Reservation Id","Reservation details","Customer details","Messages","Messages",
#62
"Reservation details","Bill details","Messages"


]

print("NUMBER OF DGs: " , len(model_out))

rouge = Rouge()
print(rouge.get_scores(model_out, reference, avg=True))

