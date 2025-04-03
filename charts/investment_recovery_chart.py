#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

# Initial investment
initial_investment = 1338.91

# Services and prices (Regular and Discounted)
services = ["Express Full Service", "Full Detail", "Interior Detailing", "Exterior Detailing", "Ceramic Coating"]
regular_prices = [99, 255, 200, 175, 675]
discount_prices = [69, 175, 140, 125, 450]

# Calculate the number of services needed to break even
services_needed_regular = [np.ceil(initial_investment / price) for price in regular_prices]
services_needed_discount = [np.ceil(initial_investment / price) for price in discount_prices]

# Plot settings
x = np.arange(len(services))
width = 0.4

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, services_needed_regular, width, label='Regular Pricing', color='blue', alpha=0.7)
rects2 = ax.bar(x + width/2, services_needed_discount, width, label='Discount Pricing', color='green', alpha=0.7)

# Labels and title
ax.set_xlabel("Service Type")
ax.set_ylabel("Number of Services Needed")
ax.set_title("Estimated Number of Services to Recover Investment ($1338.91)")
ax.set_xticks(x)
ax.set_xticklabels(services, rotation=20, ha="right")
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Annotate bars with actual values
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{int(height)}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 5),  # Offset text above bars
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, fontweight='bold')

add_labels(rects1)
add_labels(rects2)

# Save the figure
plt.tight_layout()
plt.savefig("roi_chart.png", dpi=300)
plt.show()
