import matplotlib.pyplot as plt

class Apple:
    def __init__(self, model, year, price, color):
        self.model = model
        self.year = year
        self.price = price
        self.color = color

class iPhone(Apple):
    def __init__(self, model, year, price, color, camera):
        super().__init__(model, year, price, color)
        self.camera = camera

    def display(self):
        return f"iPhone Model: {self.model}, Year: {self.year}, Camera: {self.camera}, Color: {self.color}, Price: {self.price}"

class MacBook(Apple):
    def __init__(self, model, year, price, color, keyboard):
        super().__init__(model, year, price, color)
        self.keyboard = keyboard

    def display(self):
        return f"MacBook Model: {self.model}, Year: {self.year}, Keyboard: {self.keyboard}, Color: {self.color}, Price: {self.price}"

class AppleWatch(Apple):
    def __init__(self, model, year, price, color, band_material):
        super().__init__(model, year, price, color)
        self.band_material = band_material

    def display(self):
        return f"Apple Watch Model: {self.model}, Year: {self.year}, Band Material: {self.band_material}, Color: {self.color}, Price: {self.price}"

class AirPod(Apple):
    def __init__(self, model, year, price, color, wireless_charging):
        super().__init__(model, year, price, color)
        self.wireless_charging = wireless_charging

    def display(self):
        charging_feature = "with" if self.wireless_charging else "without"
        return f"AirPod Model: {self.model}, Year: {self.year}, {charging_feature} Wireless Charging, Color: {self.color}, Price: {self.price}"

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
product_prices = [iphone.price, macbook.price, apple_watch.price, airpod.price]

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
