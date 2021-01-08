# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 13:18:28 2021

@author: Sunidhi Thakur
"""

from matplotlib import pyplot as plt

# Ques 6 - Pie Chart

activities = ["Sleeping", "Eating", "Studying","Coding", "Playing"]
slices = [6, 1, 13, 2, 2]
cols = ["orange", "g", "c", "r", "b"]

plt.pie(slices, labels = activities, colors = cols, startangle = 90, shadow = True, explode = (0, 0, 0.05, 0.05, 0), autopct = "%1.1f%%")

plt.title("PIE CHART")

plt.legend()
plt.show()

# # Ques 5 - Plotting Scatter Plot
# x = [1,2,3,4,5,6,7,8,9,10,11, 12]
# y1 = [7, 1, 4, 3, 5, 2, 8, 11, 7, 12, 1, 7]
# y2 = [1, 3, 5, 7, 9, 9, 9, 7, 5, 3, 1, 9]

# plt.scatter(x,y1, label = 'Scatter 1', color = "r", s = 65, marker = "d")
# plt.scatter(x,y2, label = 'Scatter 2', color = "b", s = 65, marker = "X")

# plt.title("SCATTERED PLOT")
# plt.xlabel("Age")  
# plt.ylabel("Frequency")  
# plt.legend()
# plt.show()


# Ques 4 - Plotting Histogram
# plt.figure(figsize=(10,6))
# ax = plt.axes()
# ax.set_facecolor("grey")
# population = [5, 10,45, 36, 98, 44, 78, 23, 20, 21, 18, 11, 20, 30, 40, 14, 66, 5, 50, 60, 72, 47, 80, 90, 100, 110]
# bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

# plt.hist(population, bins, histtype = "bar", rwidth = 0.8, color="k")
# plt.title("HISTOGRAM")
# plt.xlabel("Age")  # Assume Product IDs(cyan = Haircare products, blue = Skincare Products)
# plt.ylabel("Frequency")  # Profit
# plt.legend()
# plt.show()



# #Ques 3 - Plotting Bar Graphs

# plt.bar([2001, 2003, 2005, 2007, 2009],[7, 5, 2, 4, 6], label = "Product X", color = 'b')
# plt.bar([2002, 2004, 2006, 2008, 2010],[6, 4, 2, 5, 7], label = "Product Y", color = 'c')

# plt.title("BAR GRAPHS")
# plt.xlabel("X-axis")  # Assume Product IDs(cyan = Haircare products, blue = Skincare Products)
# plt.ylabel("Y-axis")  # Profit
# plt.legend()
# plt.show()


# Ques 2 - Plotting Two lines Together

# from matplotlib import pyplot as plt
# from matplotlib import style

# x1 = [6,9,11]
# y1 = [6,10,7]
# x2 = [5,8,10]
# y2 = [2,16,6]

# plt.plot(x1,y1,"g", label="Line 1", linewidth = 5)
# plt.plot(x2,y2,"r", label="Line 2", linewidth = 5)

# plt.title("INFO")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.legend()
# plt.grid(True, color = "k")

# plt.show()


# Ques 1 - Plotting a simple line

# from matplotlib import pyplot as plt

# plt.plot([1,2,3],[4,5,6])

# plt.title("info")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")

# plt.show()
