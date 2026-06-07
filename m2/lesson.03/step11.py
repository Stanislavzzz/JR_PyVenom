import pandas as pd


friends = {
    'Age': [17, 25, 44, 76, 12],
    'Country': ['Spain', 'Russia', 'Germany', 'France', 'USA'],
    'Name': ['Bob', 'Ann', 'Mary', 'Stive', 'John']
}

df = pd.DataFrame(friends)
print()
print(df)
print()
print(df['Age'])
print()

print(df.Name)

print()
print(df[['Country', 'Name']])

print()
print(df[['Name', 'Country']])

print(df.columns)
print(df.index)