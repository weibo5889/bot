class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def speak(self):
        print(f"i am {self.name}")

class Mouse(Animal):
    def __init__(self, color) -> None:
        super().__init__("老鼠")
        self.color = color

    def run(self):
        print("running.....")
        
m = Mouse(color="dark")
a = Animal("test")
a.speak()
m.speak()
m.run()
