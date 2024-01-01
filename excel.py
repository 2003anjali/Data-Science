import pandas as pd
#read excel file
df=pd.read_excel('data.xlsx')

#display first few rows
print("First few rows: ")
print(df.head())

#get summary statistics
print("\nSummary statistics:")
print(df.describe())

#filter data
filtered_data=df[df['Age']>30]
print("\nFiltered data (Age >30):")
print(filtered_data)

#sort data
sorted_data=df.sort_values(by ='Salary'.ascending=False)
print("\n Sorted data (by salary):")
print(sorted_data)

#add a new column
df['Bonus']=df['Salary']*0.1
print(\n Data with new column(Bonus):)
print(df)

#write to excel file
df.to_excel('output.xlsx',index=False)
print("Data written to output.xlsx")