from abc import ABC, abstractmethod


class Workable(ABC):

    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):

    @abstractmethod
    def eat(self):
        pass


class Human(Workable, Eatable):

    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")


class Robot(Workable):

    def work(self):
        print("Robot working")


robot = Robot()
robot.work()

human = Human()
human.work()
human.eat()