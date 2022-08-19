from lib2to3.pytree import LeafPattern
from pdb import line_prefix
from re import S
from string import whitespace
from this import d
import threading 
from threading import *
from time import sleep
from xml.dom.pulldom import CHARACTERS 


class Jagan (Thread):
    def run (self):
        for i in range(10):
            print ('this is thread 1')
            
class Siva (Thread):
    def run (self):
        for i in range(10):
            print ('this is thread 2')
            
a=Jagan()
b=Siva()
a.run()
b.run()


class Jagan (Thread):
    def run (self):
        for i in range(10):
            print ('this is thread 1')
            sleep(2)
class Siva (Thread):
    def run (self):
        for i in range(10):
            print ('this is thread 2')
            sleep(2)
a=Jagan()
b=Siva()
a.start()
b.start()


class Jagan (Thread):
    def run (self):
        for i in range(10):
            print ('this is thread 1')
            sleep(2)
class Siva (Thread):
    def run (self):
        for i in range(10):
            print ('this is thread 2')
            sleep(2)
a=Jagan()
b=Siva()
a.start()
sleep(1)
b.start()


class Jagan (Thread):
    def run (self):
        for i in range(10):
            print ('this is thread 1')
            sleep(2)
class Siva (Thread):
    def run (self):
        for i in range(10):
            print ('this is thread 2')
            sleep(2)
a=Jagan()
b=Siva()
a.start()
print(a.is_alive())
sleep(1)
b.start()
a.join()
print(a.is_alive())
b.join()


import threading
print(threading.current_thread().getName())

class Jagan (Thread):
    def run (self):
        for i in range(10):
            print ('this is thread 1',threading.current_thread().getName())
            sleep(2)
class Siva (Thread):
    def run (self):
        for i in range(10):
            print ('this is thread 2',threading.current_thread().getName())
            sleep(2)
a=Jagan()
b=Siva()
a.start()
print(a.is_alive())
sleep(1)
b.start()
a.join()
print(a.is_alive())
b.join()




# rejex

# ^ beginning line
# $ end of line 
# . expept new line 
# [...] single char  in brakets
# [^...] single char not in brakets
# \w word CHARACTERS
# \W non word CHARACTERS
# \s whitespace
# \S non whitespace
# \d digits 
# \D nondigits
# \A beginning of string 
# \Z end of string 
# \z end of string 
# \G last match finished 
# x|y either  x or y


# [0-9] 
# [a-z] ASC||letter 
# [A-Z] ASC||letter 
# [a-zA-Z0-9] 
# [^aeiou] lowercase vowel
# [^0-9]

















