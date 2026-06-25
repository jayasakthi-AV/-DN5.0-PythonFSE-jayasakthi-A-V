class Light:

    def on(self):
        print("Light ON")

    def off(self):
        print("Light OFF")


class LightOnCommand:

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()


light = Light()

command = LightOnCommand(light)

command.execute()