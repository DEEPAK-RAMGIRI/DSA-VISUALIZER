class Queue:
    def __init__(self):
        self.queue = []
        # self.front = -1
        # self.rear = -1       
    
    def enque(self, value):
        self.queue.append(value)
    
    def deque(self):
        if self.isempty():
            return None
        return self.queue.pop(0)
    
    def peek(self):
        if self.isempty():
            return None
        return self.queue[0]
    
    def clear(self):
        self.queue = []
    
    def size(self):
        return len(self.queue)
    
    def isempty(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)

    def __iter__(self):
        return iter(self.queue)
