#!/usr/bin/env python
import matplotlib.pyplot as plt

# Average pricing data
categories = ["Small", "Medium", "Large", "XL"]
ceramic_categories = ["Level 1", "Level 2", "Level 3"]

interior_avg = [197.25, 239.75, 277.25, 318.50]
exterior_avg = [174.75, 208.50, 244.75, 280.00]
full_detail_avg = [253.50, 299.75, 349.75, 393.50]
ceramic_coating_avg = [672.50, 1022.50, 1347.50]

plt.figure(figsize=(8,6))

plt.plot(categories, interior_avg, marker='o', label="Interior")
plt.plot(categories, exterior_avg, marker='s', label="Exterior")
plt.plot(categories, full_detail_avg, marker='^', label="Full Detail")
plt.plot(ceramic_categories, ceramic_coating_avg, marker='d', label="Ceramic Coating")

plt.xlabel("Category")
plt.ylabel("Average Price ($)")
plt.title("Average Pricing Chart")
plt.legend()
plt.grid(True)

# Save the chart as an image
plt.savefig("average_pricing_chart.png", dpi=300)  # Change to .jpg or .jpeg if needed
plt.show()
