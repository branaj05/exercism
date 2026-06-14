# https://www.geeksforgeeks.org/dsa/implement-a-stack-using-singly-linked-list/
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class myStack:
    def __init__(self):
        self.top=None
        self.count = 0

    def push(self, x):
        temp = Node(x)
        temp.next = self.top
        self.top=temp
        self.count += 1
    
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            return -1
        
        temp = self.top
        self.top = self.top.next
        val = temp.data

        self.count -= 1
        return val
    
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
            return -1
        
        return self.top.data
    
    def isEmpty(self):
        return self.top is None
    
    def size(self):
        return self.count
if __name__ == "__main__":
    st = myStack()
    
    # Push Elements
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    st.push(5)

    # popping one element
    print("Popped:", st.pop())

    # checking the top element
    print("Top Element:", st.peek())

    # checking if the stack is empty
    print("Is stack empty:" "Yes" if st.isEmpty() else "No")

    # checking current size
    print("Current Size:", st.size())
