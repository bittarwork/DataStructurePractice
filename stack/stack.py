class Stack:
    def __init__(self ):
        self.ARR = []

    def push(self , val):
        self.ARR.append(val)

    def pop(self ):
        item = self.ARR[-1]
        self.ARR.pop()
        return item
        
    def peek (self ) : 
        return self.ARR[-1]

    def size (self ) : 
        return len(self.ARR)

    def isEmpty (self) : 
        return len(self.ARR)==0

    def printStack(self ):
        return print(self.ARR)

    def delete (self) : 
        self.ARR = [None for i in range(self.MAX)]


def reversUseingStack (strign) : 
    stk = Stack()
    for letter in strign:
        stk.push(letter) 
    reve = []
    for i in range (stk.size()) : 
        reve.append(stk.pop())
    return reve

