class File:
    def open(self): print("Opening file")
class SecureProxy:
    def __init__(self): self.f=File()
    def open(self):
        print("Permission granted")
        self.f.open()
SecureProxy().open()