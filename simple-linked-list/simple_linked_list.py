"""
Prompt
- Each song has a number
Given a range of numbers, Create a singly linked list

Structure: LIFO stack
"""

class EmptyListException(Exception):
    pass

class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value
    
    def next(self, next_node=None):
        if next_node is not None:
            self._next = next_node
        return self._next


class LinkedList:
    def __init__(self, values=None):
        self.top=None
        self.count = 0
        if values:
            for v in values:
                self.push(v)

    # custom Iterator logic
    def __iter__(self):
        self.iter_data = self.top
        return self
    
    def __next__(self):
        # iterates down the stack
        if self.iter_data is None:
            raise StopIteration
        return_data = self.iter_data
        self.iter_data = self.iter_data.next()
        return return_data.value()

    # defining the length condition
    def __len__(self):
        return self.count
    
    # checking if stack is empty 
    def isEmpty(self):
        return self.top is None
    
    # peek at the top of the stack
    def head(self): 
        if self.isEmpty():
            raise EmptyListException("The list is empty.")
        # return self.top.value()
        return self.top
    
    # push -> add to stack
    def push(self, value):
        temp = Node(value)
        temp.next(self.top)
        self.top = temp
        self.count += 1
        pass

    # pop -> remove from stack and return 
    def pop(self):
        if self.isEmpty():
            raise EmptyListException("The list is empty.")
        temp = self.top
        self.top = self.top.next()

        self.count -= 1
        return temp.value()
    
    # return the data in reverse order
    def reversed(self):
        return [v for v in self][::-1]

if __name__ == "__main__":
    sut = LinkedList()
    print(sut.head().value())


    st = LinkedList([1, 2, 3, 4, 5, 6, 7, 234,])

    # popping one element
    print("Popped:", st.pop())

    # checking the top element
    print("Top Element:", st.head())

    # checking if the stack is empty
    print("Is stack empty:", "Yes" if st.isEmpty() else "No")

    # Checking Current Length 
    print("Current Len:", len(st))

    # Iterating 
    print([v for v in st])

    # Reverse
    print(st.reversed())

