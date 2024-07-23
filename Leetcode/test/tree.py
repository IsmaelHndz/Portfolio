class CategoryTree:

    def __init__(self):
       self.solution = {}

    def add_category(self, category, parent):
        if category in self.solution:
            raise KeyError("Duplicate category")
        if parent is not None and parent not in self.solution:
            raise KeyError("Duplicate parent")
        
        self.solution[category] = parent
        

    def get_children(self, parent):
        child = [category for category, a in self.solution.items() if a == parent]
        return child

if __name__ == "__main__":
    c = CategoryTree()
    c.add_category('A', None)
    c.add_category('B', 'A')
    c.add_category('C', 'A')
    print(','.join(c.get_children('A') or []))