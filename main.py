import numpy as np  
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import plotly.express as px    
shop = pd.read_csv('shopping_trends_updated.csv')
shop.shape
shop.head()
shop.dtypes
shop.columns
shop.info()
shop.shape
shop.isnull().sum()
print(f"The unique values of the 'Gender' column are: {shop['Gender'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Category' column are: {shop['Category'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Size' column are: {shop['Size'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Subscription Status' column are: {shop['Subscription Status'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Shipping Type' column are: {shop['Shipping Type'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Discount Applied' column are: {shop['Discount Applied'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Promo Code Used' column are: {shop['Promo Code Used'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Payment Method' column are: {shop['Payment Method'].unique()}")
shop['Age'].value_counts() #name of datframe[column].value_counts()
shop['Age'].mean()
shop['Gender'].unique()
shop['Age_category'] = pd.cut(shop['Age'], bins= [0,15, 18 , 30 , 50 , 70] , labels= ['child' , 'teen' , 'Young Adults' ,'Middle-Aged Adults','old'])
fig = px.histogram(shop , y = 'Age' , x = 'Age_category')
fig.show()
shop.columns

shop['Category'].unique()
shop[['Category','Purchase Amount (USD)']]
shop.groupby('Category')['Purchase Amount (USD)'].sum()

shop.groupby('Category')['Purchase Amount (USD)'].mean()
shop.columns
sns.barplot(shop , x = 'Gender' , y = 'Purchase Amount (USD)')
shop.columns
shop.groupby('Category')['Item Purchased'].value_counts()
fig = px.histogram(shop , x = 'Item Purchased' , color = 'Category')
fig.show()
shop['Season'].unique()
shop['Season'].value_counts()
fig = px.histogram(shop , x = 'Season' , range_y= [800 , 1200] )

fig.show()
shop.groupby('Category')['Review Rating'].mean()
shop_groupby = shop.groupby('Category')['Review Rating'].mean().reset_index()
print(shop_groupby)
fig = px.bar(shop_groupby ,x= 'Category' , y = 'Review Rating' )
fig.show()
shop.columns
shop['Subscription Status'].value_counts()
sns.barplot(shop  , x = 'Subscription Status' , y = 'Purchase Amount (USD)')
shop['Purchase Amount (USD)'].sum()
shop.groupby('Subscription Status')['Purchase Amount (USD)'].mean()
shop.groupby('Payment Method')['Purchase Amount (USD)'].mean().sort_values(ascending= False)

shop_groupby = shop.groupby('Payment Method')['Purchase Amount (USD)'].mean().reset_index()
fig = px.bar(shop_groupby , x = 'Payment Method' , y = 'Purchase Amount (USD)')
fig.show()
sns.barplot(shop ,x='Payment Method' , y = 'Purchase Amount (USD)')
plt.show()
shop_groupby  = shop.groupby('Promo Code Used')['Purchase Amount (USD)'].sum().reset_index()
fig = px.sunburst(shop , path=['Gender' , 'Promo Code Used'] , values='Purchase Amount (USD)')
fig.show()
fig  =  px.bar(shop_groupby , x= 'Promo Code Used' , y = 'Purchase Amount (USD)')
fig.show()
shop[['Age' , 'Age_category']]
shop['Age_category'].unique()
shop_group = shop.groupby('Frequency of Purchases')['Age'].sum()

px.sunburst(shop , path=['Frequency of Purchases','Age_category'] , values='Age')
shop.columns
shop_group = shop.groupby('Size')['Purchase Amount (USD)'].sum().reset_index()
fig  = px.bar(shop_group , x = 'Size' , y ='Purchase Amount (USD)'  )
fig.show()
shop.groupby('Category')['Shipping Type'].value_counts().sort_values(ascending= False)
shop['Category'].unique()
shop.columns
shop_group = shop.groupby('Discount Applied')['Purchase Amount (USD)'].sum().reset_index()

px.histogram(shop_group , x = 'Discount Applied' , y = 'Purchase Amount (USD)')
fig = px.sunburst(shop , path = ['Gender' , 'Discount Applied'], values='Purchase Amount (USD)' , color= 'Gender')

fig.show()
px.histogram(shop , x = 'Color')
shop['Color'].value_counts().nlargest(5)
shop['Previous Purchases'].mean()
shop.groupby('Location')['Purchase Amount (USD)'].mean().sort_values(ascending = False)
shop_group = shop.groupby('Location')['Purchase Amount (USD)'].mean().reset_index()
fig = px.bar(shop_group, x = 'Location' , y = 'Purchase Amount (USD)')
fig.show()
shop_group = shop.groupby('Category')['Age'].mean().reset_index()

fig = px.bar(shop_group ,y = 'Age' , x= 'Category')
fig.show()
shop_group = shop.groupby('Gender')['Purchase Amount (USD)'].sum().reset_index()
fig = px.bar(shop_group , x = 'Gender' , y = 'Purchase Amount (USD)')
fig.show()
px.sunburst(data_frame= shop , path = ['Gender' ,'Age_category'] , values='Purchase Amount (USD)')