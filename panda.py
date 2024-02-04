'''
DATA LIFE-CYCLE
data-datawarehousing- data analysis- data visualization

PANDAS - software library  written for the python  programming  language  for data manipulation and analysis
it is well suited  for many different kinds of data:
   - tabular data with hetergeneosly-typed columns.
   -Ordered and unordered time series  data
   - Arbitary matrix data with rows and columns labels
   - Any other form of observational/statistical data sets. The  data actually need not be labelled at all to be placed into pandas data structure

'''



import pandas as pd
xyz_web ={'day':[1,2,3,4,5,6],
          'visitors':[1000,6000,1000,400,350,300],
          'bounce_rate':[20,20,23,15,10,34]}

df = pd.DataFrame(xyz_web)
print(df)
#operation with dataframes
'''
slicing the data frame,changing the index,data conversion,joining and merging ,concantenation,,changing the column headers
'''
#slicing
print(df.head(2))
print(df.tail(2))
#merging

import pandas as pd
df1 = pd.DataFrame({'HPI':[80,90,70,60],
                    'int_rate':[2,1,2,3],
                    'ind_gdp':[50,45,45,67]},
                   index =  [2001,2002,2003,2004])

df2= pd.DataFrame({'HPI':[80,90,70,60],
                    'int_rate':[2,1,2,3],
                    'ind_gdp':[50,45,45,67]},
                   index =  [2005,2006,2007,2008])

merge = pd.merge(df1,df2)
print(merge)

#where there is only certain needed merged part
merge2 = pd.merge(df1,df2,on= 'HPI')
print(merge2)
#

#joining  the  parts
import pandas  as pd
gh = pd.DataFrame({
    'int rate': [2,3,2,2],
    'us gdp':[50,55,65,55]},
    index=[2001,2002,2003,2004]
)
hg= pd.DataFrame({
    'low tier HPI': [50,52,50,43],
    'unemployment':[7,8,9,6]},
    index=[2001,2003,2004,2005]
)

print(hg.join(gh))

#changing indexes  as columns and rows
import pandas as pd
df =pd.DataFrame({"day":[1,2,3,4], "visitors":[200,100,230,300],"bounce_rate":[20,45,68,10]})
df.set_index("day", inplace= True)
print(df)

#plotting indexes  as columns and rows
import pandas as pd
from matplotlib import  pyplot as plt
from matplotlib import  style
style.use('fivethirtyeight')
df =pd.DataFrame({"day":[1,2,3,4], "visitors":[200,100,230,300],
                  "Bounce_rate":[20,45,60,10]})
df.set_index("day",inplace=True)

df.plot ()
plt.show()

#changing the  column headers eg from visitors to users
import pandas as pd
from matplotlib import  pyplot as plt
from matplotlib import  style
style.use('fivethirtyeight')
df =pd.DataFrame({"day":[1,2,3,4], "visitors":[200,100,230,300],
                  "Bounce_rate":[20,45,60,10]})
df = df.rename(columns={"visitors": "users"})
print(df)


#concantenation
import pandas as pd
df1 = pd.DataFrame({'HPI':[80,90,70,60],
                    'int_rate':[2,1,2,3],
                    'ind_gdp':[50,45,45,67]},
                   index =  [2001,2002,2003,2004])

df2= pd.DataFrame({'HPI':[80,90,70,60],
                    'int_rate':[2,1,2,3],
                    'ind_gdp':[50,45,45,67]},
                   index =  [2005,2006,2007,2008])

concat  = pd.concat([df1, df2])
print(concat)

#data murging
import pandas as pd
country = pd.read_csv("",index_col=0)
country.to_html('index.html')

#youth unemployment data
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

country = pd.read_csv()
df = country.head(5)
df = df.set_index(['country code'])
sd = df.reindex(columns =['2010','2011'])
db = sd.diff(axis=1)

db.plot(kind = 'bar')
plt.show()


#median
from statistics import median
print(median([1,2,3,4,5]))

#mean
from statistics import mean
print(mean([1,2,3,4,5]))

#mode
from statistics import mode
print(mode([6,4,5,4,4,5,3,4,5]))

#variance
from statistics import  variance
print(variance([1,2,3,4,5]))

#PYTHON FOR HADOOP:PYDOOP
#pydoop is a  python interface to Hadoop that allows you to write MapReduce applications and interact with Hdfs in pure python

# imput---> map phase ---> reduce phase---> output
