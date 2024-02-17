#Bill calculator
#If the bill was $150.00, split between 5 people, with 12% tip. 
bill=int(150)
tip = int(input('How much tip you want to give? Pick between 10%,12%,15% and 20%'))
FinalBill=int(bill+bill*(tip/100))
numOfPeople = int(input('How many people you want to split the bill with?'))
res=round(FinalBill/numOfPeople,2)
print(res)
