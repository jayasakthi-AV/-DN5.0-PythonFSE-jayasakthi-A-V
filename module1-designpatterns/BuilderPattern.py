class Laptop:

    def __init__(self):
        self.ram = None
        self.storage = None

    def __str__(self):
        return f"RAM={self.ram}, Storage={self.storage}"


class LaptopBuilder:

    def __init__(self):
        self.laptop = Laptop()

    def add_ram(self):
        self.laptop.ram = "16GB"
        return self

    def add_storage(self):
        self.laptop.storage = "512GB SSD"
        return self

    def build(self):
        return self.laptop


laptop = LaptopBuilder().add_ram().add_storage().build()

print(laptop)