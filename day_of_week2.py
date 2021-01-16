day = int(input('Day (0-6)? '))

if day == 0:
    print("The day is Sunday.")

elif day == 1:
    print("The day is Monday.")

elif day == 2:
    print("The day is Tuesday.") 

elif day == 3:
    print("The day is Wednesday.")

elif day == 4:
    print("The day is Thursday.")

elif day == 5:
    print("The day is Friday.") 

elif day == 6:
    print("The day is Saturday.")   

else:
    print ("Read the directions.")          



if(day == 0) or (day == 6):
    print('sleep in!! Hurray!')
elif(int(1-5)):
    print('Get outta bed!')
else:
    print('Wrong number fool!')