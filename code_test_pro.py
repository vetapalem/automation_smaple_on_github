import time as tt
from tqdm import tqdm
class mike: 
    __er=8
    def ____init__(ki):
        ki.ma='mike class'
        ki.__na='inint'
    
    # def eri(self):
    #     self.er=1
    #     return self.__na

    def __eri(self):
        self.er=1
        return self.__na
    
    @property
    def encap(self):
        # print(self.__na,mike.__er)
        print(mike.__er)
        # return self.__eri
    @encap.deleter
    def encap(self):
        print('recycleben...')
        for a in range(5):

            print("|",flush=True,end="")
    @classmethod
    def __ring(cls):
        cls.re=1
        print(cls.re)

    @staticmethod
    def __round():
        mike.__ring()


class runner(mike):
    def __init__(self):
        # super().__init__()
        mike.__init__(self)
        self.__ma=23
        print(mike.__na)
    

obj1=mike()
obj1.ma=45
# print(obj1.__round())

# print(obj1.__ring())
# print(obj1.round())
# print(obj1.encap())
# del obj1.encap
# print(obj1.encap())
# print(obj1.__eri)
# print(obj1.ma)
# print('encapsulation..')
# print(obj1.__na)
# print(obj1.__er)

# print('inheritance of class..')
# obj2=runner()
# print(obj2.ma)
# print(dir(obj1))
# print(obj1.__annotations__)
# print(obj2)


class progress_bar():
    def ri(li):
        for a in range(101):
            tt.sleep(2)
            print("||",end="",flush=True)
    def bar(le):
        for a in tqdm(range(99+1)):
            tt.sleep(0.0002)
# obj3=progress_bar()
# obj3.ri()
# obj3.bar()
