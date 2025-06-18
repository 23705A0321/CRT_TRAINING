class Qu:
    def __init__(self):
        self.qu = []
    def enqu(self , data):
        self.qu.append(data)
    def dequ(self):
        if self.is_empty() == False:
            print("remove element" , self.qu.pop(0))
    def is_empty(self):
        if len(self.qu) == 0:
            return True
        else:
            return False
obj = Qu()
obj.enqu(10)
obj.enqu(20)
obj.enqu(30)
obj.enqu(40)
obj.enqu(50)
obj.dequ()
