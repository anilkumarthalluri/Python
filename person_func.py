class person:
    def __init__(self,name,country,dob):
        self.name = name
        self.country=country
        self.dob=dob
    def details(self):
        print(self.name,self.country,self.dob)
        
obj = person("tyson","IND",20)
obj.details()