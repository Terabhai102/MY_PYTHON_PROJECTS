import pandas as pd

# 1. Basics
# Series: 1-Dimensional array
# DataFrame: 2-Dimensional table
series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

df = pd.DataFrame({
    "name": ['rohan', 'nihal', 'shaurya'],
    "marks": [23, 45, 98]
})

# 2. Loading and Viewing Data
# df = pd.read_csv('path_to_file.csv') 
df.head()        # Returns first 5 rows
df.tail()        # Returns last 5 rows
df.describe()    # Returns statistical summary (count, mean, std, etc.)
df.info()        # Shows column data types and non-null counts

# 3. Data Selection
df["name"]              # Selects a column (returns a Series)
type(df["name"])        # Returns pandas.core.series.Series
df.iloc[0]              # Selects a row by integer position (returns a Series)

# 4. Cleaning Data
df.dropna()             # Removes rows with missing values
df.fillna(0)            # Replaces missing values (NaN) with 0
df.rename(columns={"name": "student_name"}, inplace=True) # Renames columns
df["marks"] = df["marks"].astype(int) # Converts column data type

# 5. Advanced / Utility
len(df)                 # Returns the number of rows
df["new_col"] = 0       # Efficient way to add a column of zeroes



