from abc import ABC,abstractmethod
class Base(ABC):
    @abstractmethod
    def abs(self):
        print("Abstract method ")
    
    def conc(self):
        print("Concrete method")

class Derived(Base):
    def abs(self):
        #print("Derived cls method ")
        super().abs()
        

d=Derived()
d.abs()
d.conc()
