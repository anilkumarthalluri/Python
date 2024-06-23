class A:
    def feature1():
        print("class A having feature1")
        
class B(A):
    def feature2():
        print("class B having feature2")
        
class C(B):
    def feature3():
        print("class C having feature3")
        
obj = C
obj.feature1()
obj.feature2()
obj.feature3()