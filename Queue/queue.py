class Queue:
    def __init__(self):
        self.ARR = []

    def insertItem(self, val):
        if (val):
            self.ARR.insert(0,val)
        else:
            return "Vallue is invalid"

    def popIlement(self):
        if (len(self.ARR) > 1):
            item = self.ARR[-1]
            self.ARR.pop()
            return item
        else:
            return "not {0} element left".format(len(self.ARR) > 1)

    def peek(self):
        if (len(self.ARR) > 0):
            return self.ARR[-1]

        else:
            return "No element in qeueu"

    def isEmpty(self):
        return len(self.ARR) == 0

    def size(self):
        if (len(self.ARR) > 0):
            return len(self.ARR)
        else:
            return "No element in qeueu"

    def displayQueue (self) : 
        print ("queueu: ==>{0}==> ".format(self.ARR))

q = Queue()
q.insertItem(5)
q.insertItem(6)
q.insertItem(7)
q.insertItem(8)
print(q.peek())
q.displayQueue()
