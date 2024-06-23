class A:
    def __init__(self):
        print("in A init")
    
    def feature1(self):
        print("class A having feature1")
        
class B(A):
    
    def __init__(self):
        super().__init__()
        print("in B init")
    def feature2(self):
        print("class B having feature2")
        
obj = B()