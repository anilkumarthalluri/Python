class A:
    def feature1():
        print("class A having feature1")
        
class B(A):
    def feature2():
        print("class B having feature2")
        
obj = B
obj.feature1()