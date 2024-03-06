import matplotlib.pyplot as plt

class Apple:
    def __init__(self, model, year, price, color):
        self.__model = model
        self.__year = year
        self.__price = price
        self.__color = color

    def get_price(self):
        return self.__price
class iPhone(Apple):
    def __init__(self, model, year, price, color, camera):
        super().__init__(model, year, price, color)
        self.__camera = camera

    def display(self):
        return f"iPhone Model: {self._Apple__model}, Year: {self._Apple__year}, Camera: {self.__camera}, Color: {self._Apple__color}, Price: {self._Apple__price}"

class MacBook(Apple):
    def __init__(self, model, year, price, color, keyboard):
        super().__init__(model, year, price, color)
        self.__keyboard = keyboard

    def display(self):
        return f"MacBook Model: {self._Apple__model}, Year: {self._Apple__year}, Keyboard: {self.__keyboard}, Color: {self._Apple__color}, Price: {self._Apple__price}"

class AppleWatch(Apple):
    def __init__(self, model, year, price, color, band_material):
        super().__init__(model, year, price, color)
        self.__band_material = band_material

    def display(self):
        return f"Apple Watch Model: {self._Apple__model}, Year: {self._Apple__year}, Band Material: {self.__band_material}, Color: {self._Apple__color}, Price: {self._Apple__price}"

class AirPod(Apple):
    def __init__(self, model, year, price, color, wireless_charging):
        super().__init__(model, year, price, color)
        self.__wireless_charging = wireless_charging

    def display(self):
        charging_feature = "with" if self.__wireless_charging else "without"
        return f"AirPod Model: {self._Apple__model}, Year: {self._Apple__year}, {charging_feature} Wireless Charging, Color: {self._Apple__color}, Price: {self._Apple__price}"

def code(args):
    sum = 0
    if isinstance(args, iPhone):
        sum += 123
    elif isinstance(args, MacBook):
        sum += 456
    elif isinstance(args, AppleWatch):
        sum += 789
    elif isinstance(args, AirPod):
        sum += 1012
    return sum

# Define product instances
iphone = iPhone("iPhone 13 Pro", 2021, 999, "Graphite", "12MP triple-camera system")
macbook = MacBook("MacBook Pro 16-inch", 2021, 2499, "Space Gray", "Magic Keyboard")
apple_watch = AppleWatch("Series 7", 2021, 399, "Midnight", "Sport Band")
airpod = AirPod("AirPods Pro", 2019, 249, "White", True)

# Display each product details using the display method
print(iphone.display())
print(macbook.display())
print(apple_watch.display())
print(airpod.display())

# Print the additional code (sums) for each product type
print(f"iPhone code: {code(iphone)}")
print(f"MacBook code: {code(macbook)}")
print(f"Apple Watch code: {code(apple_watch)}")
print(f"AirPod code: {code(airpod)}")

product_names = ['iPhone', 'MacBook', 'Apple Watch', 'AirPod']
product_prices = [iphone.get_price(), macbook.get_price(), apple_watch.get_price(), airpod.get_price()]

plt.figure(figsize=(10, 6))
plt.bar(product_names, product_prices, color=['blue', 'green', 'red', 'purple'])
plt.xlabel('Product Type')
plt.ylabel('Price ($)')
plt.title('Avarage Price by Product ')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(product_names, product_prices, marker='o', linestyle='-', color='orange')
plt.xlabel('Product Type')
plt.ylabel('Price ($)')
plt.title('Price Trend by Product Type')
plt.grid(True)
plt.show()
