import sklearn  # machine learning
import numpy as np # computations
import pandas as pd # Data management

#1. Load the dataset
dataset = pd.read_csv("https://raw.githubusercontent.com/spe301/Sales-Scientist/main/datasets/check6.csv")
print(dataset.head(10))  # To view the first 10 rows


# # 2. Dimension of dataset
dataset.shape


# print("*"*50+"\n")
# describe the dataset
dataset.describe()


# # Check the variable(Numerical / categorical)
numerical_variable= dataset.columns[dataset.dtypes != 'object']
numerical = dataset[numerical_variable].head(5)
print(numerical)
print("*"*50+"\n")


categorical_variable= dataset.columns[dataset.dtypes == 'object']
categorical= dataset[categorical_variable].head(5)
print(categorical)


print("*"*50+"\n")
# Missing values

dataset.isnull().head(5)    # check all 
numerical_null = dataset[numerical_variable].isnull().head(5) # check null for numerical
categorical_null = dataset[categorical_variable].isnull().head(5) # check null for object
print(numerical_null)
print(categorical_null)

# # False = no missing value
# # True = has missing value

print("*"*50+"\n")
# Find out the percentage of missing values
len(dataset)

# dataset.isnull().sum() / len(dataset)
# dataset[numerical_variable].isnull().sum() / len(dataset)

# Replace
dataset.fillna('KIT')  # This function is going to identify the missing value and replace that missing value with your value


dataset['customer'].replace(1,3).head(5) # replace 0 by 1
dataset.replace(0,'KIT')    
dataset['customer'].replace([1,2],['KIT',0]).head(15)  # replace 0 by KIT and replace 1 bye 0


# # Create the rows and add it with the original dataset
# # Values of variable, instructions abut the variable

row_insert = pd.Series(['w3schools.com','https://www.w3schools.com/',1,'technology','software,word of mouth',70000,5000000,9000000,0.219404762,0.379880952,0.247699335,0.309339093,247,8,11,3.72,31.45,0.2165,5.74,12520000,528344,55,'youtube',1270,0.353865,30303,8958189.977,0.038501394,127.9741425,3930000,0.436666667,21736,3006.752577],index = ['name','landingPage','customer','domain','model','source','adspend','hardcosts','revenue','avg_polarity','avg_subjectivity','std_polarity','std_subjectivity','words,triggers','links','percentSocial','percentDisplay','percentSearchPaid','percentSearch','visits','monthlyVisitsChange','bounceRate','dominantPlatform','global','percentPaid','sales','adRevenue','cac','roas','profit','profitMargin','lpc','averageOrderValue'])  
 #  Series is used to create the row
dataset.append(row_insert,ignore_index=True)


# # Call the row
# # datasetname.iloc[] - we can call the specific row based on the index
dataset.iloc[1]
dataset.iloc[1:9]
dataset.iloc[ :9]


# # loc - to call the specific values,
# # index
dataset= dataset.set_index(dataset['name'])
dataset.loc['ShopaNova.com']  # call for specific information 

# Rename
dataset.rename(columns = {'name' : 'Website'}).head(5)

# Delete column
dataset.drop('model',axis = 1).head(5)
dataset.drop(dataset.columns[1],axis = 1)  # delete columns at index 1

print("*"*50+"\n")
# Delete row
# axis 0 for row , axis 1 for columns
delete_row= dataset.drop(dataset.index[1]) # delete row at index 1
print(delete_row)

print("*"*50+"\n")
dataset['model'].unique()
print("*"*50+"\n")