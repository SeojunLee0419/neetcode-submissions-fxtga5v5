class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for i in range(index):
            if curr == None:
                return -1
            curr = curr.next
        return curr.value if curr else -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val, self.head)
        self.head = new_node
        if self.size == 0:
            self.tail = new_node
        self.size += 1
        
    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size+=1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False

        if self.size ==1:
            self.head = None
            self.tail = None
            self.size-=1
            return True
        if index == 0:
            self.head = self.head.next
            self.size-=1
            return True
        

        curr_node = self.head
        for i in range(index-1):
            curr_node = curr_node.next

        if index == self.size - 1:
            self.tail = curr_node

        curr_node.next = curr_node.next.next

        self.size-=1
        return True


    def getValues(self) -> List[int]:
        values_in_list = []
        temp_node = self.head
        while temp_node:
            values_in_list.append(temp_node.value)
            temp_node = temp_node.next
        return values_in_list



class Node: 

    def __init__(self, value, next=None):
        self.value = value
        self.next = next
