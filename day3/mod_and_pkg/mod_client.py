
# module - collection of func and classes


#appr 1
# import mod1
# import mod2
# #
# # print(mod1.addition(1,2))
# # print(mod2.multiply(3,4))
#
# obj=mod1.A()
# var=obj.func1()
# print(var)
#
# obj=mod2.B()
# var=obj.func2()
# print(var)


#appr 2

# from mod1 import addition, A
# from mod2 import multiply, B
# #
# print(addition(1,2))
# print(multiply(3,4))

# obj=A()
# var=obj.func1()
# print(var)
#
# obj=B()
# var=obj.func2()
# print(var)

#appr 3

import mod1
import mod2
#
# mod1.fun1("python")
# mod2.fun1("java")

# obj=mod1.A()
# var=obj.func3()
# print(var)
#
# obj=mod2.B()
# var=obj.func3()
# print(var)

# obj=mod1.A1()
# var=obj.func1()
# print(var)
#
# obj=mod2.A1()
# var=obj.func1()
# print(var)


# appr4

from mod2 import fun1, B, A1
from mod1 import fun1 ,A, A1
# #
# # fun1("python")
# # fun1("java")
#
# obj=A()
# var=obj.func3()
# print(var)
#
# obj=B()
# var=obj.func3()
# print(var)

obj=A1()
var=obj.func1()
print(var)