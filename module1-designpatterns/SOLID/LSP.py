class Bird:
    pass


class FlyingBird(Bird):

    def fly(self):
        print("Flying")


class Sparrow(FlyingBird):
    pass


class Penguin(Bird):

    def swim(self):
        print("Swimming")


bird = Sparrow()
bird.fly()

penguin = Penguin()
penguin.swim()