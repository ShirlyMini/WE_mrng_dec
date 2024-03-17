# parent/ base/ super
# and child/derived/sub class
# single inherit
# multiple inhert
# multilevel inherit
#hierarcy inherit
#hybrid inherit

# single inherit
# parent --->child
# class parent:
#     var1="class var"
#     def parent_func(self):
#         a=10
#         print("parent function")
#         return a
#
# class child(parent):
#     def child_func(self):
#         var2=self.parent_func()
#         print(var2)
#         print(self.var1)
#         print("child function")

# obj=child()
# obj.parent_func()
# obj.child_func()

# multiple inherit
# parent1 --->child
# parent2 --->child

# class parent1:
#     var1="class var parent 1"
#     def parent1_func(self):
#         a=10
#         print("parent1 function")
#         return a
#
# class parent2:
#     var2="class var parent 2"
#     def parent2_func(self):
#         a=10
#         print("parent2 function")
#         return a
#
# class child(parent1,parent2):
#     def child_func(self):
#         print("starting child function")
#         print(self.var1)
#         print(self.var2)
#         print(self.parent1_func())
#         print(self.parent2_func())
#
#
# obj=child()
# print(obj.var1)
# print(obj.var2)
# obj.parent1_func()
# obj.parent2_func()
# obj.child_func()

# class parent1:
#     var1="class var parent 1"
#     def parent1_func(self):
#         a=10
#         print("parent1 function")
#         return a
#
# class parent2:
#     var1="class var parent 2"
#     var2="class var parent 2"
#     def parent2_func(self):
#         a=10
#         print("parent2 function")
#         return a
#
# class child(parent1, parent2):# method resolution order child--> parent1---> parent2--->parentn
#     var1 = "class var child"
#     def child_func(self):
#         # print("starting child function")
#         # print(self.var1)
#         print(super().var1)# base class
#         print(super().var2)
#         print(super().parent2_func())# base class
#         print(super().parent1_func())# base class
#         # print(parent1.var1)
#         # print(parent2.var1)
#         # print(self.parent1_func())
#         # print(self.parent2_func())
#
#
# obj=child()
# # print(obj.var1)
# # obj.parent1_func()
# # obj.parent2_func()
# obj.child_func()
#
#
#
# class parent:
#     def __init__(self, a,b):
#         print("***constructor from parent***")
#         self.a=a
#         self.b=b
#         print("***constructor from parent***", a,b)
#
#
# class child(parent):
#     def __init__(self, a, b, c,d):
#         print("***constructor from child***")
#         self.c=c
#         self.d=d
#         print("***constructor from child***", c,d)
#         # a=10
#         # b=20
#         print("***super()***")
#         super().__init__(a,b)# 1, 2
#         print("***<parent name>***")
#         parent.__init__(self,40,60)
#
#     def child_func(self):
#         print("***starting child function***")
#         print("var a", self.a)
#         print("var b", self.b)
#         print("var c", self.c)
#         print("var d", self.d)
#
# obj=child(1,2,3,4)
# obj.child_func()

#######################################
# # multilevel inherit
# parent1 ---> parent2---> parent3--->child


# class parent1:
#     def func1(self):
#         print("func1")
#
#     def func3(self):
#         print("func3 from parent1")
#
# class parent2(parent1):
#     def func2(self):
#         print("func2")
#
#     def func3(self):
#         print("func3 from parent2")
#
# class parent3(parent2):
#     def func3(self):
#         print("func3 from parent3")
#
# class child(parent3):
#     def child_func(self):
#         print("child_func")
#         self.func1()
#         self.func2()
#         self.func3()
#         super().func3()
#         parent1.func3(self)
#         parent2.func3(self)
#         parent3.func3(self)
#
# obj=child()
# obj.child_func()

########################################################
# hierarcy
# parent---> child1(obj)
# parent---> child2(obj)

# class parent:
#     def func1(self):
#         print("func1 from parent")
#
# class child1(parent):
#     def child1_func(self):
#         print("func from child1")
#
# class child2(parent):
#     def child2_func(self):
#         print("func from child2")
#
# obj1=child1()
# obj1.func1()
# obj1.child1_func()
#
# obj1=child2()
# obj1.func1()
# obj1.child2_func()

###################################################
# hybrid inherit
# parent ---> parent2---> child1(obj)--> child
# parent---> child2(obj)-->child

class parent:
    def func1(self):
        print("func1 from parent")

class child1(parent):
    def child1_func(self):
        print("func from child1")

class child2(parent):
    def child2_func(self):
        print("func from child2")


class child(child1, child2):# multiple inheritance
    def child_func(self):
        self.func1()
        self.child1_func()
        self.child2_func()
        #self.child_func()#RecursionError: maximum recursion depth exceeded while calling a Python object

obj=child()
obj.child_func()