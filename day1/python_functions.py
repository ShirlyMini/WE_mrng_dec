# def is keyword to create function
# creating function - no mem allocation happen- create a func ref
# invoke fun- mem allocation - will do the task based on statements given

# def myfunc():# creation
#     print('hello')
#
# myfunc()# invoke func
# print(myfunc)#<function myfunc at 0x000002789DAC04A0>
#
# var=myfunc
#
# var()
# print(var)

# 4 types
# no parameter and no return
# with parameter and no return
# no parameter and with return
# with parameter and with return

# return statement

# def myfunc():
#     return # come out of the func # default None
# #myfunc()# will not print any outupt
# var=myfunc()
# print(var)
# #(or)
# print(myfunc())

# def myfunc():
#     print("hello")
#     # return "hello in retun statement"
#     return 1,2,3,4# passing mutipple var return in tuple format
# myfunc()
# print(myfunc())

# no parameter and no return

# def func():
#     a=10
#     print(a)
#
# # print(func())#None
# # func()

# no parameter and with return

# def add():
#     return 1+2
#     # print("statment after return")
#
# print(add())#3

# parameters/arguments
# positional & keyword

# positional

# def addition(a,b,c,d):
#     # print(a+b+c+d)
#     return (f"{a}+{b}+{c}+{d} = {a + b + c + d}")
#
# print(addition(1,2,3,4))# postion
# print(addition(a=1,b=2,c=3,d=4))# keyword
# print(addition(b=2,c=3,a=1,d=4))# keyword
# print(addition(1,2,c=3,d=4))
# print(addition(a=1,b=2,3,4))#positional argument follows keyword argument
# print(addition(1,2,a=3,b=4))#addition() got multiple values for argument 'a'


# def addition(a,b,c=0,d=0):# default parameters
#     # # print(a+b+c+d)
#     # return (f"{a}+{b}+{c}+{d} = {a + b + c + d}")

# print(addition(1,2,3,4))# postion
# print(addition(1,2))# postion
# print(addition(1,2, 3))# postion
# print(addition(a=1,b=2,c=3,d=4))# keyword
# print(addition(a=1,b=2))# keyword
# print(addition(a=1,b=2,c=3))# keyword
# # print(addition(b=2,c=3,d=4))# keyword #addition() missing 1 required positional argument: 'a'
# print(addition(b=2,c=3,a=1,d=4))# keyword
# print(addition(1,2,c=3,d=4))
# print(addition(a=1,b=2,3,4))#positional argument follows keyword argument
# print(addition(1,2,a=3,b=4))#addition() got multiple values for argument 'a'


######################################################################################
# 2 types of variable
# global(outside funct) vs local(inside function)

# a=10
#
# def myfunc(c):
#     b=20
#     print("inside func",a,b,c)

# print("before calling func",a,b,c)#NameError: name 'b' is not defined
# myfunc(30)#inside func 10 20 30
# print("after calling func",a,b,c)#NameError: name 'b' is not defined

####################################################33
# ex1
# a=1
# def func():
#     print("inside func",a)
#
# print("before calling func",a)
# func()
# print("after calling func",a)

#ex2

# a=1
# def func():
#     a=2
#     print("inside func",a)
#
# print("before calling func",a)
# func()
# print("after calling func",a)

#ex3
# a=1
# def func():
#     global a
#     a=2
#     print("inside func",a)
#
# print("before calling func",a)#before calling func 1
# func()#inside func 2
# print("after calling func",a)#after calling func 2

#ex4
# def func():
#     global a
#     a=2
#     print("inside func",a)
#
#
# func()#inside func 2
# print("after calling func",a)#after calling func 2

##############################################################
# empty func# no nothing funct
# def myfunc():
#     pass# null operation
#
# myfunc()




