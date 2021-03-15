#import packages & modules
import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import scipy as sp
import pandas as pd

#year of publication list or numpy array
year = np.array(["2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"])

#both "year" array above and "proceedings" below must have same number of items in them (same dimension)

#number of published materials by year
proceedings = np.array([2, 2, 2, 2, 0, 3, 4, 3, 6, 15, 10, 21, 11, 11, 16])

#creating subplot
plt.subplot(1, 1, 1)

#plot the bar chart of the publications
bar_chart = plt.bar(year, proceedings)

#title for the bar chart
plt.title("Journals, Proceedings, Chapter in Book")

#horizontal axis' label
plt.xlabel("Year")

#vertical axis' label
plt.ylabel("No. of papers")

#change/use style/theme of the bar chart
#option of styles/themes can be found at https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
#need to run code at least twice whenever applying/changing a theme/style
plt.style.use("ggplot")

#adjust the dimension of the whole bar chart box
plt.subplots_adjust(right = 1.4, top = 1.5)

#function to label number the corresponding number of publications on top of every bar in the bar chart
def autolabel(rects):
    """Attach a text label above each bar in *bar_chart*, displaying its height."""
    for bar in bar_chart:
        height = bar.get_height()
        plt.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
       
#execute plotting and labelling bar chart
autolabel(bar_chart)   

plt.show()