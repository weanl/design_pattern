class Person:
    def __init__(self, name: str):
        self.name = name

    def operation(self):
        print(f"Dressed-up {self.name}")


class Finery(Person):
    def __init__(self, name: str, decorator: Person = None):
        super(Finery, self).__init__(name)
        self.decorator = decorator

    def set_decorator(self, decorator: Person):
        self.decorator = decorator


class Shoes(Finery):
    def __init__(self):
        super(Shoes, self).__init__("shoes")

    def operation(self):
        print(f"Put on {self.name}")
        if self.decorator:
            self.decorator.operation()


class Tshirt(Finery):
    def __init__(self):
        super(Tshirt, self).__init__("T-shirt")

    def operation(self):
        print(f"Put on {self.name}")
        if self.decorator:
            self.decorator.operation()


if __name__ == "__main__":
    person = Person("wanchen")
    shoes = Shoes()
    tshirt = Tshirt()

    # 如何把装饰改写位 . 链式添加
    shoes.set_decorator(person)
    tshirt.set_decorator(shoes)
    tshirt.operation()
