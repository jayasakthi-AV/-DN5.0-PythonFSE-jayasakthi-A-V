class Subscriber:

    def update(self, message):
        print(message)


class YouTube:

    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def upload(self, video):

        for subscriber in self.subscribers:
            subscriber.update(f"New video uploaded: {video}")


user1 = Subscriber()
user2 = Subscriber()

channel = YouTube()

channel.subscribe(user1)
channel.subscribe(user2)

channel.upload("Python Design Patterns")