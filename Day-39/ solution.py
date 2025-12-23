# Implement Queue using Stacks
class MyQueue:

    def __init__(self):
        self.pvt_main=[] #primary stack
        self.hlpr=[] #helper stack
        
    def push(self, x: int) -> None:
        #add element to the main to helper stack
        # add x to main
        # add all elements back helper to main
        while len(self.pvt_main) >0:
            self.hlpr.append(self.pvt_main.pop())

        self.pvt_main.append(x)
        while self.hlpr:
            self.pvt_main.append(self.hlpr.pop())
        

    def pop(self) -> int:
        return self.pvt_main.pop()
    
        

    def peek(self) -> int:
        return self.pvt_main[-1]
        

    def empty(self) -> bool:
        return len(self.pvt_main) == 0
    
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(10)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()