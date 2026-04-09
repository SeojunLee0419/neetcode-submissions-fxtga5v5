class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None] * capacity;
        self.capacity = capacity
        self.size = 0
    
    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size+=1

    def popback(self) -> int:
        popped_element = self.array[self.size-1]
        self.array[self.size-1] = None
        self.size = self.size-1
        return popped_element

    def resize(self) -> None:
        new_array = [None] * self.capacity * 2
        for i in range(self.capacity):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = self.capacity*2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
