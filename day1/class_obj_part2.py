# global- defined outside class, local inside the method
# class - defined inside class

# a=1
# class myclass:
#     b=10
#     def func1(self,d):
#         c=100
#         print(myclass)#<class '__main__.myclass'>
#         print(self)#<__main__.myclass object at 0x00000190E4297F90>
#         #print("instance method", a,b,c,d)#NameError: name 'b' is not defined
#         print("instance method", a, self.b, c, d)#instance method 1 10 100 1000
#         print("instance method", a, myclass.b, c, d)#instance method 1 10 100 1000
#
# class myclass1:
#     print(myclass.b)
#
# # obj=myclass()
# # obj.func1(1000)
# # print(obj.b)
# # print(myclass.b)


# a=1# global
# class myclass:
#     a=10# class
#     def func1(self):
#         a=100# local
#         #print("instance method", a, self.a)
#         #print(globals())# dict contains global variable
#         #print("instance method", a, myclass.a, globals()['a'])
#         return print("instance method", a, myclass.a, globals()['a'])
#
# obj=myclass()
# # obj.func1()
# # print(obj.a)
# obj.func1()

#####################################################################################3

# class method

a="global"# global
class myclass:
    a="class var"# class
    @classmethod
    def func1(cls):
        global a
        a="local var"# local
        #cls.a="class var 1"

        print("class method", a,cls.a)
        print("class method", a,myclass.a, globals()['a'])

    @staticmethod
    def func2():
        #global a
        a="local var"# local
        myclass.a="class var 1"
        print("static method", a, myclass.a, globals()['a'])


# myclass().func1()
# print(myclass().a)
myclass().func2()
print(myclass().a)