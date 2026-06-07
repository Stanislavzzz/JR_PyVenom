import pandas as pd


nums = pd.Series([11,21,33,44,55,67])
print(nums)
print(type(nums))


# companies = ['Apple', 'Apple', 'HP', 'Dell']

# nums = pd.Series([11,21,33,44,55,67], index=['a', 'b', 'c', 'd', 'e', 'f'])
nums = pd.Series([11,21,33,44,55,67])
print(nums)
print(type(nums))

print(nums.index)
print(type(nums.index))

print(nums.values)
print(type(nums.values))

x = nums[1]
print(x)