dict = {"country": ["Brazil", "Russia", "India","China","South Africa"],
        "capital": ["Brasilia", "Moscow", "New Delhi","Beijing", "Pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.22],
        "population": [200.4, 143.5, 1252, 1357, 52.98]}

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

# Changing index from 0,1,2 .. to something else.

brics.index = ["BR", "RS", "IN", "CN", "SA"]

print(brics)


# Importing .csv

dic = pd.read_csv('/filepath/filename.csv', index_col = 0) #index_col determines which column acts as index.

# Use of .loc & .iloc filtering
# .loc is label based 
# .iloc is integer based

print(brics.iloc[3])            # Prints entry China with all the informat
print(brics.loc["BR"])          # Prints entry with index "BR" i.e Brazil

