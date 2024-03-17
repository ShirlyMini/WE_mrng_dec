# instance---> object creation---> n number of obj/instance


# constructor ---> normal func---> __init__()
# it will get invoked at the time of object creation

# class myclass:
#     def __init__(self):
#         print("this is constructor")
#
#     def func1(self):
#         print("this is instance method")
#
# obj=myclass()# invoke the __init__
# #obj.func1()

#######################################################

class myclass:
    a="class var"
    def __init__(self, a, b):# constructor
        print("this is constructor")
        print(a,b)
        self.a=a
        self.b=b

        myclass.a=a
        myclass.b=b
        # print(self)# obj
        # print(myclass)# class name

    def func1(self, c,d):
        print("this is instance method")
        print(self.a,self.b)
        print(myclass.a,myclass.b)
        print(self.a)
        print(c,d)

    @classmethod
    def func2(cls, c,d):
        print("this is class method")
        print(cls.a, cls.b)
        print(myclass.a, myclass.b)
        print(cls.a)
        print(c, d)

    @staticmethod
    def func3(c,d):
        print("this is static method")
        print(myclass.a, myclass.b)
        print(myclass.a)
        print(c, d)


obj = myclass(10, 20)# instance variable
obj.func1(30,40)
obj.func2(30,40)
obj.func3(30,40)
