greet=input('').lower().replace(" "," ")
x=greet[0:5]
if(greet=='halo'):
    money=0
elif(x=='halo'):
    money=0
elif(greet[0]=='h'):
    money=20
else :
    money=100
print('$',money)