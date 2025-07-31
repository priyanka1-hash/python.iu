print("select the services you want:")
print('1 withdraw')
print('2 deposite \n3 savings \n4 balance')
service=int(input('plz select:'))
if service==1:
    print('withdraw')
    amount=int(input('enter the amount'))
    print('collect your amount',amount)
elif service==2:
   print('deposite')
elif service==3:
   print('savings')
elif service==4:
    print('balance')
else:
    print('kindly select the above services')
