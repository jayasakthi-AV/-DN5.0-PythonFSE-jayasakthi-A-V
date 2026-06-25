
def stars(fn):
    def wrap():
        print("***")
        fn()
        print("***")
    return wrap
@stars
def greet(): print("Hello")
greet()