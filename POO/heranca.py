class Base: 
    def fun(self):
        print("Public method")
  
    def __fun(self):
        print("Private method")
  
class Derived(Base): 
    def __init__(self): 
        Base.__init__(self) 
          
    def call_public(self):
        print("\nInside derived class")
        self.fun()
          
    def call_private(self):
        self.__fun()
  
obj1 = Base()

obj1.fun()
  
obj2 = Derived()
obj2.call_public()