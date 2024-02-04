
'''
statistical relatioship
process of understanding relationships between variables of a dataset
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


a= sns.load_dataset('flights')
sns.relplot(x='passengers',y="month",data=a,hue="year")

plt.show()

#a line plot
b =sns.load_dataset('tips')
sns.relplot(x="time",y ="tip",data=b,kind="line")
plt.show()

'''
plottng with categorical data
  -main variable is further divided into discrete groups
'''
#you can chooose what plot to use eg,kind= "box"or 'violin"
sns.catplot(x="day",y="total_bill",data=b)



'''
visualizing the distriibution of a dataset
 _understanding datsets wih context  to being univariate or bivariate
'''
#univariate
c= np.random.normal(loc=5,size=100,scale=2)
sns.distplot(c)

plt.show()

#bivariate

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

x = pd.DataFrame({"day": [1, 2, 3, 4, 5, 6, 7], "grocery": [30, 80, 45, 23, 51, 46, 76], "clothes": [13, 40, 34, 23, 54, 67, 90], "utensils": [12, 32, 27, 33, 61, 13, 23]})
y = pd.DataFrame({"day": [8, 9, 10, 11, 12, 13, 14], "grocery": [30, 90, 45, 23, 51, 48, 76], "clothes": [13, 49, 34, 23, 54, 67, 90], "utensils": [12, 65, 89, 54, 23, 20, 10]})

# Extract the variables you want to visualize
x_grocery = x["grocery"],['day'],["clothes"],['utensils']
y_grocery = y["grocery"],['day'],["clothes"],['utensils']

# Create a joint plot between x_grocery and y_grocery
with sns.axes_style("white"):
    sns.jointplot(x=x_grocery, y=y_grocery, kind="kde", color="b")

#for another data frame you just give new variables but to that datafrae
# x_clothes = x["clothes_x"]
# y_clothes = y["clothes_y"]
# sns.jointplot(x=x_clothes, y=y_clothes, kind="kde", color="g")


plt.show()


#creating a multiplot for the datframes

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define your DataFrames
x = pd.DataFrame({"day": [1, 2, 3, 4, 5, 6, 7], "grocery": [30, 80, 45, 23, 51, 46, 76], "clothes": [13, 40, 34, 23, 54, 67, 90], "utensils": [12, 32, 27, 33, 61, 13, 23]})
y = pd.DataFrame({"day": [8, 9, 10, 11, 12, 13, 14], "grocery": [30, 90, 45, 23, 51, 48, 76], "clothes": [13, 49, 34, 23, 54, 67, 90], "utensils": [12, 65, 89, 54, 23, 20, 10]})

# Combine the DataFrames
x["source"] = "x"
y["source"] = "y"
combined_data = pd.concat([x, y])

# Create a pairplot for multiple columns
with sns.axes_style("white"):
    sns.pairplot(data=combined_data, hue="source", markers=["o", "s"], plot_kws={"alpha": 0.7})

plt.show()


"""

#multiplot grids
#grahs plotted side by side using the same  scale and axes to aid coparison

a = sns.load_dataset("iris")
b= sns.FacetGrid(a, col="species")
b.map(plt.hist, "sepal_length")
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

a = sns.load_dataset('flights')
b = sns.PairGrid(a)
b.map(plt.scatter)

plt.show()

#asthetics
sns.set(style='white',color_codes=True)
a = sns.load_dataset('tips')
sns.boxplot(x='day',y='total_bill',data= a)
sns.despine(offset=10,trim=True)

#color palletes
c = sns.color_palette()
sns.palplot(c)
plt.show()