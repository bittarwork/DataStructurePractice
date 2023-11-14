class TreeNode:
    def __init__(self, data):
        self.parent = None
        self.data = data
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def printTree(self):
        spaces = ' ' * self.getLevel() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printTree()

    def getLevel(self):
        counter = 0
        par = self.parent
        while (par):
            par = par.parent
            counter += 1
        return counter

    def printByLevel(self, level):
        if level == 0:
            print(self.data)
        else:
            for child in self.children:
                spaces = ' ' * self.getLevel() * 3
                prefix = spaces + "|__" if self.parent else ""
                child.printByLevel(level - 1)




