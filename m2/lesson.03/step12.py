import pandas as pd


friends = {
    'Age': [17, 25, 44, 76, 12],
    'Country': ['Spain', 'Russia', 'Germany', 'France', 'USA'],
    'Name': ['Bob', 'Ann', 'Mary', 'Stive', 'John']
}

df = pd.DataFrame(friends, index=[5, 7, 4 ,2, 3])
print()
print(df)

df.index = [15, 27, 34 , 72, 43]
print()
print(df)