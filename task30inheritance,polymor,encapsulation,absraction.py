# 3.inheritance

# single line 

# class parent():
#     def output(self):
#         print('this is parent')
# class child(parent):
#     def outputchild (self):
#         print('this is child')
# obj=child()
# obj.output()
# obj.outputchild()


# class balu:
#     def balu(self):
#         print('this is balu')
# class balu(balu):
#     def balu(self):
#         print('this is ball')
#         super().balu()
# i=balu()
# i.balu()

# multiple 
# class father:
#     def father(self):
#         print('this is father')
# class mother(father):
#     def mother(self):
#         print('this is mother')
# class child(mother):
#     def child(self):
#         print('this is child')
# i=child()
# i.father()
# i.mother()
# i.child()

# class father:
#     def output(self):
#         print('this is father')
# class mother():
#     def output(self):
#         print('this is mother')
# class child(father,mother):
#     def output(self):
#         print('this is child')
#         super().output()
#         mother.output(self)
# i=child()
# i.output()

# class parent:
#     def parent(self):
#         print('this is parent')
# class parent1():
#     def parent(self):
#         print('this is parent1')
# class parent2():
#     def parent(self):
#         print('this is parent2')
# class child (parent,parent1,parent2):
#     def child(self):
#         print('this is child')
#         super().parent()
#         parent1.parent(self)
#         parent2.parent(self)
# i=child()
# i.child()


# multilevel

# class gfather:
#     def gfather(self):
#         print('this is gfather')
# class father(gfather):
#     def father(self):
#         print('this is father')
# class child(father):
#     def child(self):
#         print('this is child')
# i=child()
# i.child()
# i.gfather()
# i.father()


# hierarchical

# class father:
#     def op(self):
#         print('this is father')
# class child1(father):
#     def opfather(self):
#         print('this is child1')
# class child2(father):
#     def opchild(self):
#         print('this is child2')
# i=child1()
# j=child2()
# i.op()
# i.opfather()
# j.op()
# j.opchild()



# 4.poly morphism
# poly=many 
# morph=forms 

# 1.method overloading
# 2.method over ridding 
# 1.

# class methodoverloading():
#     def something(self,a='none',b='none',c='none'):
#         print(a,b,c)
# i=methodoverloading()
# i.something(1,2,3)
# i.something(1,2)
# i.something(1)
# i.something()

# class methodoverridding():
#     def something(self):
#         print('this is perent')
# class child(methodoverridding):
#     def something(self):
#         print('this is child')
#         super().something()
# i=child()
# i.something()


# constucted method __init__
# class balu():
#     def __init__(self,a,b):
#         print(a,b)
#         self.c=a
#         self.d=b
# class balu_sub(balu):
#     def __init__(self,a,b):
#         print(a,b)
#         super().__init__(a,b)
# i=balu_sub(1,2)





# 5.en capsulation
# 1.public 
# 2.private 
# 3.protected

# class gfather:
#     def __init__(self,a):
#         self._car=a
#         print(self._car)
# class father(gfather):
#     def balu(self):
#         print(self._car)
# class child(father):
#     def balu1(self):
#         print('child',self._car)
# i=child('car')
# i.balu1()
# i.balu()


# 6.data abstraction
from abc import ABC,abstractmethod

# class parent(ABC):
#     @abstractmethod
#     def done(self):
#         pass
#     @abstractmethod
#     def balu(self):
#         pass
# class child(parent):
#     def done(self,a):
#         print('this is child',a)
#     def balu(self):
#         print('this is balu')
# i=child()
# i.done('balu')
# i.balu()











