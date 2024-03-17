import os

import sys
#C:\Users\user\PycharmProjects\pythonProject_WEMorning_dec\day3\mod_and_pkg\pkg1
#C:\Users\user\PycharmProjects\pythonProject_WEMorning_dec\day3\mod_and_pkg\
#C:\Users\user\PycharmProjects\pythonProject_WEMorning_dec\day3\mod_and_pkg\pack1\pack2


# sys.path.append(r"C:\Users\user\PycharmProjects\pythonProject_WEMorning_dec\day3")
# from day3.mod_and_pkg.pack1.pack2 import pack2_mod1
# from ..pack1.pack2 import pack2_mod1

# from ..pack1.pack1_mod1 import A2
from day3.mod_and_pkg.pack1.pack1_mod1 import A2
class C:
    def myfunc(self):
        obj=A2()
        var1, var2 = obj.func1()
        print("this is myfunc from class c", var1,var2)

obj=C()
obj.myfunc()

