import numpy as np
import pandas as pd

#play with Pandas Series
countries = ['Mali', 'Benin', 'Mocambique', 'Senegal']
my_data = [100, 200, 400, 650]

results = pd.Series(my_data, countries)

print(results)
print('-----------------------------------------------')

my_dict = {'a':50, 'b':60, 'c': 75, 'd':90}

results = pd.Series(my_dict)
print(results)
print('-----------------------------------------------')


#play with Pandas DataFrames
df = pd.DataFrame(np.random.randn(5,4), ['A','B','C','D', 'E'], ['W','X','Y','Z'])
print(df)
print('-----------------------------------------------')

#Creating DataFrame from a dictionary of list
data = {'name': ['George', 'Anne', 'Shonda', 'Bilal', 'Damuzi'],
        'age': [40,24,31,21,45],
        'year': [1997, 1988, 2001, 1992, 1973]
        }
my_df = pd.DataFrame(data, index = ['Caretaker', 'Administrator', 'Engineer', 'HR-Manager', 'CEO'])
print(my_df)
print('-----------------------------------------------')