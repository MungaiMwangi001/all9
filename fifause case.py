#predict the strongest 11 players taking part in the world cup
"""
-best goalkeeper(1)
-best defenders(4)
-best mid_fielders(3)
-best attackers(3)
"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
#% matplotlib inline

df = pd.read_csv("C:\\Users\\admin\\Downloads\\fifaCleanedExcel.csv")
a = df.head(7)

#visualizing the data

plt.figure(figsize=(15,32))
sns.countplot(y=df.Potential)#plot potential   on y axis
plt.show()
#ccase 2
plt.figure(figsize=(15,6))
sns.countplot(x="Age",data=df)