a=1# global
class myclass:
    a=10# class
    @staticmethod
    def func1():
        a=100# local
        print("class method", a,myclass.a, globals()['a'])

myclass().func1()
print(myclass().a)