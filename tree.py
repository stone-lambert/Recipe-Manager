class Tree:
    def __init__(self, data, parent):
        self.children = []
        self.data = data
        self.parent = parent
        
    def add_child(self, child):
        self.children.append(child)
    
    def remove_node(self):
        if self.parent != None:
            self.parent.children.remove(self)
        self.data = None
        for child in self.children:
            child.data = None
            child.parent = None
        self.children = []
        self.parent = None
