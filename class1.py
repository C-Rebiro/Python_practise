class employees:
    def __init__(self, name, age, salary):
        self.name = name
        self.age= age
        self.salary= salary

    def show(self):
        print(f"My name is {self.name}."
              f" I'm {self.age} years"
              f" and I earn {self.salary} in a month.")

myobj= employees("Liam", 24,35700)
myobj.show()
myobj= employees("Charles",32,45200)
myobj.show()
myobj= employees("Mae",28,34000)
myobj.show()