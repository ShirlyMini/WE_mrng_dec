# more than one form
# func overloading (same func with different len of parameter)
# func overriding (same name)

# #func overriding - NA
# def myfunc():
#     print("first func")
#
# def myfunc():
#     print("second func")
#
# def myfunc():
#     print("third func")
#
# myfunc()
#
# class myclass:
#     def myfunc(self):
#         print("first func")
#
#     def myfunc(self):
#         print("second func")
#
#     def myfunc(self):
#         print("third func")
#
# obj=myclass()
# obj.myfunc()

# function overloading(parameter)

# def myfunc(a):
#     print("first func")
#
# myfunc(10, 20,30,40,50)#myfunc() takes 1 positional argument but 5 were given
# function overloading
# def myfunc(*a):
#     print("first func")
#     print(a)# tuple
#     print(a[1])
#     for i in a:
#         print(i)
#
# myfunc(10, 20,30,40,50,6,7,8,9,10)#(10, 20, 30, 40, 50)

# class myclass:
#     def myfunc(self, *a):
#         print(a)# tuple
#         print(a[1])
#         for i in a:
#             print(i)
#
# obj=myclass()
# obj.myfunc(10, 20,30,40,50)