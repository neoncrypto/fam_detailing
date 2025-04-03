#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

# Sservice categories and prices
categories = ["Express Full", "Full Detail", "Interior", "Exterior", "Ceramic Coating"]

x = np.arange(len(categories))  # Bar positions

# Regular Prices
car_prices = [99, 255, 200, 175, 675]
suv_prices = [119, 300, 240, 210, 1025]
truck_2dr_prices = [109, 350, 180, 175, 1350]
truck_4dr_prices = [129, 395, 280, 250, 1500]

# Discounted Prices
car_discount = [69, 175, 140, 125, 450]
suv_discount = [89, 200, 170, 150, 700]
truck_2dr_discount = [79, 225, 125, 125, 900]
truck_4dr_discount = [99, 275, 200, 180, 1000]

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 7))
width = 0.2  # Bar width

# Plot bars
bars1 = ax.bar(x - width*1.5, car_prices, width, label="Car (Regular)", color="#4c72b0")
bars2 = ax.bar(x - width/2, suv_prices, width, label="SUV (Regular)", color="#55a868")
bars3 = ax.bar(x + width/2, truck_2dr_prices, width, label="Truck 2dr (Regular)", color="#c44e52")
bars4 = ax.bar(x + width*1.5, truck_4dr_prices, width, label="Truck 4dr (Regular)", color="#8172b3")

# Plot discount bars
bars1_d = ax.bar(x - width*1.5, car_discount, width, label="Car (Discount)", color="#4c72b0", alpha=0.5, hatch="//")
bars2_d = ax.bar(x - width/2, suv_discount, width, label="SUV (Discount)", color="#55a868", alpha=0.5, hatch="//")
bars3_d = ax.bar(x + width/2, truck_2dr_discount, width, label="Truck 2dr (Discount)", color="#c44e52", alpha=0.5, hatch="//")
bars4_d = ax.bar(x + width*1.5, truck_4dr_discount, width, label="Truck 4dr (Discount)", color="#8172b3", alpha=0.5, hatch="//")

# Add labels above bars
for bars in [bars1, bars2, bars3, bars4]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 20, f"${height}", ha='center', fontsize=10, fontweight='bold')

# Labels, title, and legend
ax.set_title("Regular vs Discounted Pricing", fontsize=14, fontweight='bold')
ax.set_xlabel("Service Category", fontsize=12, fontweight='bold')
ax.set_ylabel("Price", fontsize=12, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=10)
ax.legend()

# Save chart as an image file.
plt.savefig("sparkleco_pricing_chart.png", dpi=300, bbox_inches="tight")

# Show the chart
plt.show()
