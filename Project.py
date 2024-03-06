
import pandas as pd

import matplotlib.pyplot as plt


class Shoe:
    def __init__(self, brand, model, size, price, discount):
        self.brand = brand
        self.model = model
        self.size = size
        self.price = price
        self.__discount = 1000

    def get_discount(self):
        """Getter method to access the private discount attribute."""
        return self.__discount


    def display(self):
        final_price = self.price - self.get_discount()  # Apply discount to price
        return (f"Brand: {self.brand}, Model: {self.model}, Size: {self.size}, "
                f"Original Price: ฿{self.price}, Discount: ฿{self.get_discount()}, "
                f"Final Price: ฿{final_price}")

class TennisShoe(Shoe):
    def __init__(self, brand, model, size, price, discount, court):
        super().__init__(brand, model, size, price, discount)
        self.court = court

    def display(self):
        final_price = self.price - self.get_discount()
        return (f"Brand: {self.brand}, Model: {self.model}, Size: {self.size}, "
                f"Court: {self.court}, Original Price: ฿{self.price}, "
                f"Discount: ฿{self.get_discount()}, Final Price: ฿{final_price}")

class SoccerShoe(Shoe):
    def __init__(self, brand, model, size, price, discount, pitch):
        super().__init__(brand, model, size, price, discount)
        self.pitch = pitch  # The type of pitch the shoe is designed for

    def display(self):
        final_price = self.price - self.get_discount()
        return (f"Brand: {self.brand}, Model: {self.model}, Size: {self.size}, "
                f"Pitch: {self.pitch}, Original Price: ฿{self.price}, "
                f"Discount: ฿{self.get_discount()}, Final Price: ฿{final_price}")

shoe3 = Shoe("Nike", "Air Max", 42, 60000,1000)
print(shoe3.display())

shoe2 = TennisShoe("Adidas", "CourtJam Bounce", 42, 4500, 1000,"Clay")
print(shoe2.display())

shoe1 = SoccerShoe("Puma", "Future Z 1.1", 42, 5000, 10000,"Grass")
print(shoe1.display())

shoe4= SoccerShoe("Adidas", "F50",30,2000,8500,"Artificial grass")
print(shoe4.display())

shoe5 = Shoe("Adidas","Samba",39,10000,2000)
print(shoe5.display())

# Simulating data creation from the instances of Shoe, TennisShoe, and SoccerShoe
data = [
    {"Brand": "Nike", "Model": "Air Max", "Size": 42, "Price": 3200, "Type": "General"},
    {"Brand": "Adidas", "Model": "CourtJam Bounce", "Size": 42, "Price": 4500, "Type": "Tennis", "Court": "Clay"},
    {"Brand": "Puma", "Model": "Future Z 1.1", "Size": 42, "Price": 5000, "Type": "Soccer", "Pitch": "Grass"},
    {"Brand": "Adidas", "Model": "F50", "Size": 30, "Price": 8500, "Type": "Soccer", "Pitch": "Artificial grass"},
    {"Brand": "Adidas", "Model": "Samba", "Size": 39, "Price": 8500, "Type": "General"}
]
# Create a DataFrame
df = pd.DataFrame(data)

print(df)

tennis_shoes = df[df['Court'].notna()]
print("Tennis Shoes:\n", tennis_shoes)

soccer_shoes = df[df['Pitch'].notna()]
print("Soccer Shoes:\n", soccer_shoes)

average_price = df['Price'].mean()
print(f"Average Price of Shoes: ฿{average_price:.2f}")

average_price_by_brand = df.groupby('Brand')['Price'].mean().sort_values(ascending=False).reset_index()






# Plotting
plt.figure(figsize=(10, 6))  # Optional: Adjust the figure size
plt.bar(average_price_by_brand['Brand'], average_price_by_brand['Price'], color='skyblue')
plt.xlabel('Brand')
plt.ylabel('Average Price')
plt.title('Average Shoe Price by Brand (Highest to Lowest)')
plt.xticks(rotation=45)  # Rotate brand names for better readability


plt.show()

