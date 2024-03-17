# pkg = collection of module

# from pack1 import pack1_mod1
# from pack1 import pack1_mod2
#
# print(pack1_mod1.addition(1,2))
# print(pack1_mod2.multiply(1,2))

# from pack1.pack1_mod1 import addition
# from pack1.pack1_mod2 import multiply
#
# print(addition(1,2))
# print(multiply(1,2))

# from pack1.pack2.pack2_mod1 import subraction
#
# print(subraction(5,3))

from pkg1 import module1

obj=module1.C()
print(obj.myfunc())