# class- blue print, template (creating class)- no mem allo- logical
# obj - invoke the class- instance create -mem alloc - pysical

# func Vs method
# func inside the class is called method
# func without the class is called func

# resume_templte(class)
# name, age, quali, mini proj

# obj(stud1)- name1, age1, BE, proj1
# obj(stud2)- name2, age2, BE, proj2


# class myclass:
#     pass
#
# print(myclass)#<class '__main__.myclass'>
# print(myclass())#<__main__.myclass object at 0x000001A734457C10>
############################################################
# print("printing outside class")
# class myclass:
#     print("printing inside class")

#print(myclass)#<class '__main__.myclass'>
#print(myclass())#<__main__.myclass object at 0x000001A734457C10>

#####################################################33

# 3 types method
# instance(default)
# class
# static method

# class myclass:
#     def func1(self,a):
#         print(self)#<__main__.myclass object at 0x000001FB62067FD0># obj
#         print(a)
#         print("instance method")
#
# obj1=myclass()
# print(obj1)
# obj1.func1(1)# backend python passess obj as first parameter

# class myclass:
#     def func1(a,b,c):
#         print(a)#<__main__.myclass object at 0x0000029D421D7FD0>
#         print(b)
#         print(c)
#         print("instance method")
#
# obj1=myclass()
# obj1.func1(1,2)# backend python passess obj as first parameter


#######################################################################

class myclass:
    def func1(self):
        print("instance method")

    @classmethod
    def func2(cls):
        print(cls)# <class '__main__.myclass'>
        print("class method")

    @staticmethod
    def func3(a,b):
        print("static method")

#######################################
# instance method
######################################

# myclass().func1() #instance method
#myclass.func1()#instance method wont go with class name
#TypeError: myclass.func1() missing 1 required positional argument: 'self'

#######################################
# class method
######################################
# myclass().func2()
# myclass.func2()

#######################################
# static method
######################################

# myclass().func3()
# myclass.func3()