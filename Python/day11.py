'''
Encapsulation and Access Modifiers
Encapsulationo isthe packing of data and methods into a class so that you can hide the information and restriction.

Public Access Modifier (self.Normal);all
Private Access Modifier (self.__doubleUnderScore); Parent only but not child; it can be access _class__attribute also called as name mangling.
Protected Access Modifier (self._SingleUnderScore); Parent and child.
'''

class Person():
    def __init__(self,name, age, s_code):
        self.name = name
        self._age = age
        self.__s_code = s_code
    
    def publicMethod(self):
        print(self.name)
        print(self._age)
        print(self.__s_code)
    
    def _protectedMethod(self):
        print('\nProtected Method')
        print(self.name)
        print(self._age)
        print(self.__s_code)
    
    def __privateMethod(self):
        print('\nPrivate Method')
        print(self.name)
        print(self._age)
        print(self.__s_code)

p1 = Person('Bikash Chaudhary', 19, 12345)


# p1.publicMethod()
# p1._protectedMethod()

class Person2(Person):
    def __init__(self,name, age, s_code):
        super(Person2,self).__init__(name, age, s_code)
    
    def acccessing_test1(self):
        print('\nTest-1, Trying to access from parent class')
        print(self.name)
        print(self._age)
        # print(self.__s_code)
    
    def callingProtectedMethod(self):
        Person._protectedMethod(self)

p2 = Person2('Bikash', 19, 12345)
Person2.acccessing_test1(p2)
Person2.callingProtectedMethod(p2)
    



