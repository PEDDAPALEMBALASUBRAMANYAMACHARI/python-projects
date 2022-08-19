# file handling
'''
open
read and write
close
'''

# file modes 
'''
r-read
w-write
a-append
r+-read and write
w+-write and read
'''


# balu=open('balu.txt',mode='r')
# content=balu.read()
# print(content)
# balu.close()

# bharat=open('balu.txt',mode='r')
# content=bharat.readline(15)
# print(content)
# bharat.close()

# bharat=open('balu.txt',mode='r')
# content=bharat.readlines()
# print(content) 
# bharat.close()             list formet 

# bharat=open('balu.txt',mode='w')
# content=bharat.write('this is balu')
# print(content)
# bharat.close()

# bharat=open('balu.txt',mode='a')
# content=bharat.write('this is balu')
# print(content)
# bharat.close()

# bharat=open('balu.txt',mode='w+')
# content=bharat.write('this is balu')
# c=bharat.read()
# print(c)
# bharat.close()

# tell method
# bharat=open('balu.txt',mode='r')
# bharat.read(7)
# print(bharat.tell())
# bharat.close()

# bharat=open('balu.txt',mode='r')
# bharat.read(7)
# bharat.seek(6)
# print(bharat.tell())
# bharat.close()

# file=open('balu.txt',mode='r+')
# content=file.read()
# v=str(content)
# print(v)
# f=v.split()
# print(f)
# f.insert(2,'good')
# print(file.tell())
# file.close()
# file=open('balu.txt',mode='w')
# for i in f:
#     file.writelines([i])


# file=open('balu.txt',mode='w+')
# content=file.write('this is write')
# file.seek(0)
# c=file.read()
# print(c)
# print(content)
# file.close()

# file=open('balu.txt',mode='w+')
# content=file.write('this is balu')
# file.seek(0)
# c=file.read()
# print(c)
# print(content)
# file.close()


# error handling
# try:
#     print('balu')
# except:
#     print('error')
# else:
#     print('no error')
# finally:
#     print('always run this code')

# raise
# s='kiran'
# try:
#     number=int(s)
# except ValueError:
#     raise ValueError('string cannot convert into int')

# try:
#     print(9/1)
# except Exception as k:
#     print('error',k)
# finally:
#     print('always run this code')


'''
indendation error   (syntax follow the line (error)
eof error           (with out colen)
value error         (dict ,int to str numeric not is)
key error           (dict)
name error           (name varible)
file not found error   (current flie)
module not found error(module)
index error   
keyboard interupt
os error
type error
zero division error   (1/0)
syntax error  (#)
import error 

'''






