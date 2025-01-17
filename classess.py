class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def info(self):
        return self.title, self.author, self.year
    
book_1 = Book('Harry Potter', 'JRowling', '333')
print(book_1.info())

class Point:
    def __init__(self, x_cord, y_cord):
        self.x = x_cord
        self.y = y_cord
    
    def distance_to_zero(self):
        distance = (self.x ** 2 + self.y ** 2) ** 0.5
        return f'distance is {distance}'

point_1 = Point(4, 3)
print(point_1.distance_to_zero())

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def reset(self):
        self.value = 0

counter = Counter()
print(counter.value)
counter.increment()
counter.increment()
print(counter.value)
counter.decrement()
print(counter.value)
counter.reset()
print(counter.value)

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
class Cat(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)

class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)
    
parrot = Animal('Kesha', 'Any')
cat = Cat('meow', 'bars')

class BankAccount():
    def __init__(self):
        self.__balance = 0
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if self.__balance - amount >= 0:
            self.__balance -= amount
        else:
            return 'NOT ABLE TO WITHDRAW THIS AMOUNT'
    
    def get_balance(self):
        return self.__balance

my_acc = BankAccount()

my_acc.deposit(2000)
print(my_acc.get_balance())
print(my_acc.withdraw(3000))
my_acc.withdraw(200)
print(my_acc.get_balance())

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            return 'NO SUCH ITEM'
    
    def list_items(self):
        return self.items

store = Store('Pyaterochka')
store.add_item('Bread')
store.add_item('Milk')
print(store.list_items())
store.remove_item('Milk')
print(store.list_items())

class Shape:
    def __init__(self, value):
        self.value = value

class Circle(Shape):
    def __init__(self, value, pi=3.14):
        super().__init__(value)

        self.pi = pi

    def area(self):
        return self.pi * self.value ** 2

class Square(Shape):
    def __init__(self, value):
        super().__init__(value)

    def area(self):
        return self.value ** 2

circle = Circle(5)
square = Square(10)

print(circle.area(), square.area())

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

        if '@' not in self.email:
            raise ValueError

user_1 = User('Paul', 'Paul@gmail.com')
print(user_1.email, user_1.username)
#user_2 = User('John', 'John392.gmail.com')