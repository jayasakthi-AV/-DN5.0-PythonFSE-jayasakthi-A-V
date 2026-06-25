
class Legacy:
    def old(self): print("Old API")
class Adapter:
    def __init__(self,obj): self.obj=obj
    def new(self): self.obj.old()
Adapter(Legacy()).new()