'''
Task 2 : Data manipulation with Pandas
Date:29-06-2024
Description: This task involves using the Pandas
library to manipulate data.

Responsibility: Load a CSV file into a Pandas
DataFrame. Perform operations like
filtering data based on conditions, handling
missing values, and calculating summary
statistics.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
df=pd.read_csv("D:\Python\Datasets\DataCleaningandPreprocessing.csv")
#Printing the type of df variable
print("Type of df variable  is :",type(df)) #Output : <class 'pandas.core.frame.DataFrame'>

#Printing Conise summary of Dataset :
print("Printing Information of the dataset : \n")
print(df.info()) #Output: RangeIndex: 324 entries, 0 to 323 | Data columns (total 23 columns):

#Deleting Duplicate Rows
df=df.drop_duplicates()
print("After Dropping the Duplicates values: \n")
print(df.info()) #Output : Index: 301 entries, 0 to 307  | Data columns (total 23 columns):

#Descriptive Statistics
print("Descriptive Statistics : \n")
print(df.describe())

#Checking Null Values
print("Checking NULL Values")
print(df.isnull())

print("Printing the Sum of Null Values present in each column : ")
print(df.isnull().sum())

# Note- To check Not Null values use .notnull() function in place of .isnull()

#Printing Total NUll Values present in th dataset
print("Total Null Values Present in Dataset :",df.isnull().sum().sum())
#Output: Total Null Values Present in Dataset : 352

#Handling the Null Values

#  1. Filling with zero
df2=df.fillna(value=0) #Making new Dataframe df2 so that we can apply other handling techniques on orignal df
print("Printing after filling na with zero")
print(df2)

# 2.Forward Filling
df3=df.fillna(method='pad')
print("Printing after applying Forward filling ")
print(df3)

# 3.Backward Filling
df4=df.fillna(method='bfill')
print("Printing after applying backward filling")
print(df4)

#Droping column
df2.drop('Observation',axis=1,inplace=True)
print(df2.columns) 

#Detecting outlier 
q1=df2.quantile(0.25)
q3=df2.quantile(0.75)
IQR=q3-q1
print(IQR) #Inter Quatile Range

df2=df2[~((df2<(q1-1.5*IQR))|(df2>(q3+1.5*IQR))).any(axis=1)]
print("Printing the pre-processed dataset :")
print(df2)