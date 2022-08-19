# choose=input('''select the type of operations:
# + for add
# - for sub
# * for mul
# / for sub''')
# num1 =float(input('enter the frist name'))
# num2 =float(input('enter the second name'))
# if choose=='+':
#     print('this is if')
# elif choose=='-':
#     print('this is elif')
# elif choose=='*':
#     print('this is elif')
# elif choose=='/':
#     print('this is elif')
# else:
#     print('operator is invalid')


from random import choices


x=int(input('enter the frist name:'))
y=int(input('enter the second name:'))
choice=input('enter the symbol')
if choice == '+':
    print(x+y)
    if choice == "-":
        print(x-y)
    elif choice == "*":
        print(x*y)
    elif choice == "/":
        print(x/y)
    elif choice == "<":
        print(x<y)
    elif choice == ">":
        print(x>y)
    elif choice == "=":
        print(x=y)
    elif choice == "%":
        print(x%y)
    else:
        print('this is else')
else:
    print('this value is invalid')