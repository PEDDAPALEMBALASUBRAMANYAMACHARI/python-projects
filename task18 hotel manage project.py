user_name='khader'
pass_word=123
username=input('enterusername\n')
paswrd=int(input('enteryourpassword\n'))
if username==user_name and paswrd==pass_word:
   print("*loginsuccess*")
   print("Available servicesare\n Rooms\n wifi\n Hotwater\n AC\n Food\n TV\nPool\n")
   Rooms={'suit':50000,'luxury':20000,'special':10000,'express':5000,'normal':1000}
   Hotwater={'hot':200,'normal':0,}
   Food={'super':500,'normal':200}
   wifiTV={'single':500,'double':1000}
   selection=(input('The available room Services are \nsuit\tluxury\tspecial\texpress\tnormal\nenteryourchoiceforRooms\n'))
   x=selection 
   a=(Rooms[x]) 
   print(a)
   if selection=='suit':
    print("youhavechosen'suit'andcostoftheRoom is\t")
    print(Rooms['suit'])
   elif selection=='luxury':
    print("youhavechosen'luxury'andcostoftheRoom is\t")
    print(Rooms.get('luxury'))
   elif selection=='special':
    print("youhavechosen'special'andcostoftheRoom is\t")
    print(Rooms.get('special'))
   elif selection=='express':
    print("youhavechosen'express'andcostoftheRoom is\t")
    print(Rooms.get('express'))
   elif selection=="normal":
    print("youhavechosen'normal'andcostoftheRoom is\t")
    print(Rooms.get('normal'))
    water=(input('availablewaterserviceishot(cost:200)andnormal(cost:Free)andenteryourchoiceforhot/normal\n'))
    y=water
    b=(Hotwater[y])
   if water=='hot':
    print("youhavechosen'hot'andcostofthehotwateris\t")
    print(Hotwater['hot'])
   elif water=='normal':
    print("youhavechosen'normal'andcostofthenormalis\t")
    print(Hotwater.get('normal'))
   sf=(input('available foodsare superand normalenteryourchoice offood is super\normal\n'))
   z=sf
   c=(Food[z])
   if sf=='super':
    print("youhavechosen'super'andcostofthesuperis\t")
    print(Food['super'])
   elif sf=='normal':
    print("youhavechosen'normal'andcostofthenormalfoodis\t")
    print(Food.get('normal'))
   wtv=(input('availablefacilitiesarewifiandtv, enteryourchoiceforsingle/double\n'))
   zz=wtv
   d=(wifiTV[zz])
   if wtv=='single':
    print("youhavechosen'single'andcostofthesinglewifiserviceis\t")
    print(wifiTV['single'])
   elif wtv=='double':
    print("youhavechosen'double'andcostofthedouble(wifiandTV)is\t")
    print(wifiTV['double'])
   totalbill_without_gst=a+b+c+d
   print('='*50)
   print(''*22,'HotelBill',''*22)
   print('='*50)
   print('CustomerName\t:',user_name)
   print('Usedservicesare\t:')
   print('Room serviceyouchosen is',''*5,x, a)
   print('Waterserviceyouchosen is',''*5,y, b)
   print('Foodserviceyouchosen is',''*5,z, c)
   print('Wifi/TVserviceyouchosenis',''*5,zz, d)
   print('='*50)
   print('totalbillwithoutGstis',''*18,totalbill_without_gst)
   totalbill_with_gst=totalbill_without_gst+0.005*totalbill_without_gst
   print('='*50)
   print('totalbillwithGstis',''*19,totalbill_with_gst)
   print('='*50)
elif username==user_name and paswrd!=pass_word:
   print("invaldpasswordentercorrectpasswordandtryagain")
else:
   print("invalidlogintryagain")