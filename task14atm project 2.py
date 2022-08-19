# user_name='balu'
# password='90144'
# user_name=input('enter user name')
# password=input('enter password')
# amount=20000
# if('user_name=user_name and password=password'):
#     print('welcome the atm')
#     print('successful login')
#     print('1.withdrawl 2.fast cash 3.balance enquiry')
#     n=int(input('enter the desired key'))
#     if(n=='1'):
#         balance=int(input('enter your amount'))
#         if amount>5000:
#             print('amount not available')
#         else:
#             print('collect your cash')
#     elif(n=='2'):
#         print('1.1000 2.2000 3.3000 4.4000')
#         number=int(input('enter how much amount you credit'))
#         if number>4:
#             print('invalid key pressed')
#         else:
#             print('wait and collect your cash')
#     elif(n=='3'):
#         print('your accout balance is {en_amount}') 
# else:
#     print('wrong credentails')



username='balu'
password='1234'

customer_name=input('enter your name')
customer_pass=str(input('enter your password'))

if customer_name==username and customer_pass==password:
    print('''
    1.Deposite
    2.withdraw
    3.mini statement
    4.exit
    ''')
    amount=50000
    option=int(input('select your option'))
    if option==1:
        dep=int(input('enter the amount'))
        amount+=dep
        print('total amount:',amount)
    elif option==2:
        withd=int(input('enter the amount:'))
        amount-=withd
        print('total amount:',amount)
    elif option==3:
        print('======ATM======')
        print('username:',username)
        print('total amount:',amount)
        print('thanks for visiting')
        print('==================')
    elif option==4:
        exit()

else:
    print('please enter correct logins')



