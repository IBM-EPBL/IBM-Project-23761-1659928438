# -*- coding: utf-8 -*-
"""Assignment_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/193DX-p2W95Azsem1Hz3Z-LYbgqVCbZw0

# Basic Python

## 1. Split this string
"""

s = "Hi there Sam!"

x=s.split()
print(x)

"""## 2. Use .format() to print the following string. 

### Output should be: The diameter of Earth is 12742 kilometers.
"""

planet = "Earth"
diameter = 12742

print(f'The diameter of {planet} is {diameter} kilometers.')

"""## 3. In this nest dictionary grab the word "hello"
"""

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])

"""# Numpy"""

import numpy as np

"""## 4.1 Create an array of 10 zeros? 
## 4.2 Create an array of 10 fives?
"""

arr=np.zeros(10)
print(arr)

arr=np.ones(10)*5
print(arr)

"""## 5. Create an array of all the even integers from 20 to 35"""

import numpy as np
array=np.arange(20,36,2)
print(array)

"""## 6. Create a 3x3 matrix with values ranging from 0 to 8"""

arr=np.arange(0,9).reshape(3,3)
print(arr)

"""## 7. Concatenate a and b 
## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])
"""

import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
x=np.concatenate((a,b),axis=0)
print(x)

"""# Pandas

## 8. Create a dataframe with 3 rows and 2 columns
"""

import pandas as pd

import pandas as pd
df = pd.DataFrame()
print(df)

"""## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023"""

import datetime
import pandas as pd
test_date = datetime.datetime.strptime("01-01-2023", "%d-%m-%Y")
k=41
date_generated = pd.date_range(test_date, periods=k)
print(date_generated.strftime("%d-%m-%Y"))

"""## 10. Create 2D list to DataFrame

lists = [[1, 'aaa', 22],
         [2, 'bbb', 25],
         [3, 'ccc', 24]]
"""

lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]

import pandas as pd
lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]
df = pd.DataFrame(lists, columns =['Sno', 'Name', 'Age'])
print(df)