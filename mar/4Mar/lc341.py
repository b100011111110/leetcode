class NestedIterator:
    def __init__(self, nestedList):
        self.nestedList = nestedList        
        self.flattenedList = []        
        self.currentIndex = 0
        def flatten(currentList):
            for item in currentList:
                if item.isInteger():
                    self.flattenedList.append(item.getInteger())
                else:
                    flatten(item.getList())        
        flatten(self.nestedList)
    def next(self):
        number = self.flattenedList[self.currentIndex]
        self.currentIndex += 1
        return number
    def hasNext(self):
        return self.currentIndex < len(self.flattenedList)