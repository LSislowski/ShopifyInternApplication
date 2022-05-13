from statistics import median
import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats


# Import the csv file into the notebook
df = pd.read_csv("/Users/lsislowski/GitHub/Shopify/ShopifyInternApplication/2019_Winter_Data_Science_Intern_Challenge_Data_Set_Sheet1.csv")

# Calculates the median order value 
median_orders = df['order_amount'].median()

# This answers question 1
text_block = """When we are looking at the calculation for the Mean of sales amounts,
this is an inaccurate value to use since the distribution of the sales 
amounts are right skewed. Looking through the exploratory Jupyter Notebook, 
we can see that the largest buyer of shoes spent over $11mm over the 30 day 
window. This drastically affected the Average Order Value.  The Median Order 
Value (MOV) in this instance is $284 which is a more accurate value to describe 
what types of purchases are generally being made for shoes in this dataset. 
Additionally, the Interquartile Range is a good method to show the spread of the 
data after removing outliers.  If the data was more evenly distributed a z-score 
would be fine, but this does not work when the data is skewed."""


# Tools to help explore the dataset 
def removeoutliers(DataFrame):
    """
    This function takes in a dataframe and removes the outliers and filters the dataframe
    the process for outlier selection and data exploration can be found in question1.ipynb
    included in this repo
    
    This function is specific for the dataset imported above
    """
    # Creates the Quartile range to remove outliers
    # IQR method is more appropriate than z-score since the data is right-skewed
    Q1 = df['order_amount'].quantile(0.25)
    Q3 = df['order_amount'].quantile(0.75)
    IQR = Q3 - Q1
    
    # Filters data to only include values inside IQR
    df_remove_outlier = df['order_amount'].loc[
        (df['order_amount'] > (Q1 - 1.5 * IQR)) & 
        (df['order_amount'] < (Q3 + 1.5 * IQR))
        ]

    return df_remove_outlier

def create_viz(data1, data2):
    """
    This function takes two dataframe inputs (with and without outliers)
    and creates a scatterplot for the given data.

    data1 = with outliers
    data2 = without outliers
    
    We will create two scatterplots to show what the data
    looks like before and after the outliers are removed
    """

    with_outlier = sns.scatterplot(x= df.index, y= 'order_amount', data= data1)
    without_outlier = sns.scatterplot(data= data2)

    return with_outlier, without_outlier


if __name__ == "__main__":

    print(f'The median order amount is {median_orders}')
    print()
    print(text_block)






