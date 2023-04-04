# Write a program to use Matplotlib and plot the graph.
#import pandas library
import pandas as pd
#import excel data into a pandas dataframe.
df = pd.read_excel("/Users/superyassh/Documents/Sem 8/NLP/excel-comp-data.xlsx")
df.head()
#We want to add a total column to show total sales for Jan, Feb and Mar.
df["total"] = df["Jan"] + df["Feb"] + df["Mar"]
df.head()
import matplotlib.pyplot as plt
df['total'].plot(kind="hist")
plt.xlabel("X axis label")
plt.ylabel("Y axis label")
plt.title("Histogram Plot")
plt.show()
df['total'].plot()
plt.show()
category_data = df["account"]
total_data = df["total"]
plt.pie(total_data, labels=category_data, autopct='%1.1f%%')
plt.title("% of total sales of each account")
plt.show()