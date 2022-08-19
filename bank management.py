from secrets import choice


print('='*20)

customerNames=['balu','john','jordan','david']
customerpins=['1234','2345','3456','4567']
customerbalances=[10000,20000,30000,40000]
deposition=0
withdrawal=0
balance=0
counter_1=1
counter_2=5
i=0

while True:
    print('='*20)
    print('----Welcome to Times Bank---- ')
    print('*'*20)
    print('=<< 1. Open a new account         >>=')
    print('=<< 2. Withdraw Money             >>=')
    print('=<< 3. Deposit Money              >>=')
    print('=<< 4. Check Customers & Balance  >>=')
    print('=<< 5. Exit/Quit                  >>=')
    print('*'*20)
    choiceNumber =input('select your choice number from the above menu')
    if choiceNumber == '1':
        print('choice number 1 is selected by the customer')
        NOC = eval(input('number of Customers:'))

        i=i+NOC
        if i>5:
            print('\n')
            print('customer registration exceed reached or customers registration too low')

            i=i-NOC
        else:
            while counter_1 <= i:
                name =input('Input Fullname :')
                customerNames.append(name)
                pin =str(input('please input a pin of your choice'))
                customerpins.append(pin)
                balance=0
                deposition=eval(input('please input a value to deposit to start an account'))
                balance=balance+deposition
                customerbalances.append(balance)
                print('\nName=',end='')
                print(customerNames[counter_1])
                print('pin=',end='')
                print(customerpins[counter_1])
                print('Balance=', end='')
                print(customerbalances[counter_1], end='')
                print('-/Rs')
                counter_1=counter_1+1
                counter_2=counter_2+1
                print('\nYour name is added to customers system')
                print('Your pin is added to customers system')
                print('your balance is added to customers system')
                print('----New account created successfully !----')
                print('\n')
                print('Your name is avalilable on the customers list now :')
                print(customerNames)
                print('\n')
                print('Nate! please remember the Name and pin')
                print('='*20)

        mainMenu = input('please press enter key to go back to main menu to perfect')
    elif choiceNumber == '2':
        j=0
        print('choice number 2 is selected by the customer')
        while j<1:
            k =-1
            name = input('please input name :')
            pin =input('please input pin :')
            while k< len(customerNames) -1:
                k=k+1
                if name == customerNames[k]:
                    if pin == customerpins[k]:
                        j=j+1
                        print('Your Current Balance:',end='')
                        print(customerbalances[k],end='')
                        print('-/Rs\n')
                        balance=(customerbalances[k])
                        withdrawal=eval(input('input value to Withdraw:'))
                        if withdrawal> balance:
                            deposition= eval(input('please deposit a higher valve bacause your Balance mentioned above is not enough:'))
                            balance=balance+deposition
                            print('your current Balance:',end='')
                            print(balance,end='')
                            print('-/Rs\n')
                            print('----Withdraw Successfull!----')
                            customerbalances[k]=balance
                            print('Your New BAlance:',balance,end='')
                            print('-/Rs\n\n')
                        else:
                            balance=balance-withdrawal
                            print('\n')
                            print('----Withdraw Successfull!----')
                            customerbalances[k]=balance
                            print('Your New BAlance:',balance,end='')
                            print('-/Rs\n\n')
            if j<1: 
                print('Your name and pin does not match!\n')
                break
    elif choiceNumber == '3':
        print('choice number 3 is selected by the customer')
        n=0
        while n<1:
            k =-1
            name=input('please input name:')
            pin =input('please input pin :')
            while k< len(customerNames) -1:
                k=k+1
                if name == customerNames[k]:
                    if pin == customerpins[k]:
                        n=n+1
                        print('Your Current Balance:',end='')
                        print(customerbalances[k],end='')
                        print('-/Rs')
                        balance=(customerbalances[k])
                        deposition= eval(input('enter the value you want to a higher valve :'))
                        balance=balance+deposition
                        customerbalances[k]=balance
                        print('\n')
                        print('----Deposit Successfull!----')
                        print('Your New BAlance:',balance,end='')
                        print('-/Rs\n\n')
            if n<1:
                print('Your name and pin does not match!\n')
                break
        mainMenu=input('please press enter key to go back to main menu to perfect')
    elif choiceNumber == '4':
        print('choice number 4 is selected by the customer')
        k=0
        print('costomer name list and balances mentioned below :')
        print('\n')
        while k<= len(customerNames) -1:
            print('->.Customer =', customerNames[k])
            print('->.Balance =', customerbalances[k],end='')
            print('-/Rs')
            print('-\n')
            k=k+1
        mainMenu=input('please press enter key to go back to main menu to perfect')
    elif choiceNumber == '5':
        print('choice number 5 is selected by the customer')
        print('Thank you for using our banking system!')
        print('\n')
        print('Come again')
        print('Bye bye')
        break
    else:
        print('Invalid option salected by the customer')
        print('please Try again!')
        mainMenu=input('please press enter key to go back to main menu to perfect')




                        
                            















