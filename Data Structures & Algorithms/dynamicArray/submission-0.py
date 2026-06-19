class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.length=0
        self.arr=[None]*capacity


    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i]=n


    def pushback(self, n: int) -> None:
        if self.length>=self.capacity:
            self.resize()

        self.arr[self.length]=n
        self.length+=1


    def popback(self) -> int:
        result=self.arr[self.length-1]
        self.arr[self.length-1]=None
        self.length-=1
        return result
 

    def resize(self) -> None:
        self.capacity*=2
        new=[None]*self.capacity

        for i in range(self.length):
            new[i]=self.arr[i]

        self.arr=new


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
