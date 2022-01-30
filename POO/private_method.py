class A: 
    def fun(self):
        print("Public method")
   
    def __fun(self):
        print("Private method")
      
    def Help(self):
        self.fun()
        self.__fun()
          
# Driver's code
obj = A()
obj.Help()