class fruits:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color
    def onyesha(self):
        print(f"My favorite fruit is {self.name}"
              f"and it costs {self.price}"
              f"and it's {self.color} in color")
myobj=fruits("Apples",50,"green or red")
myobj.onyesha()

myobj=fruits("Oranges",30,"orange")
myobj=fruits("cherry",100,"red")
myobj.onyesha()