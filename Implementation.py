
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Shoe:
    def __init__(self, brand, model, size, price):
        self.brand = brand
        self.model = model
        self.size = size
        self.price = price

    def display(self):
        return f"{self.brand} {self.model} Size: {self.size} Price: ฿{self.price}"


class TennisShoe(Shoe):
    def __init__(self, brand, model, size, price, court):
        super().__init__(brand, model, size, price)
        self.court = court

    def display(self):
        return f"{self.brand} {self.model} Size: {self.size} Court: {self.court} Price: ฿{self.price}"


class SoccerShoe(Shoe):
    def __init__(self, brand, model, size, price, pitch):
        super().__init__(brand, model, size, price)
        self.pitch = pitch  # The type of pitch the shoe is designed for

    def display(self):
        return f"{self.brand} {self.model} Size: {self.size} Pitch: {self.pitch} Price: ฿{self.price}"

shoe3 = Shoe("Nike", "Air Max", 42, 3200)
print(shoe3.display())

shoe2 = TennisShoe("Adidas", "CourtJam Bounce", 42, 4500, "Clay")
print(shoe2.display())

shoe1 = SoccerShoe("Puma", "Future Z 1.1", 42, 5000, "Grass")
print(shoe1.display())

shoe4= SoccerShoe("Adidas", "F50",30,8500,"Artificial grass")
print(shoe4.display())

shoe5 = Shoe("Adidas","Samba",39,8500)
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

