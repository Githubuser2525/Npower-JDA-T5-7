#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDA0101ENSkillsNetwork20235326-2022-01-01" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 
# <h1 align=center><font size = 5>Data Analysis with Python</font></h1>
# 

# # House Sales in King County, USA
# 

# This dataset contains house sale prices for King County, which includes Seattle. It includes homes sold between May 2014 and May 2015.
# 

# | Variable      | Description                                                                                                 |
# | ------------- | ----------------------------------------------------------------------------------------------------------- |
# | id            | A notation for a house                                                                                      |
# | date          | Date house was sold                                                                                         |
# | price         | Price is prediction target                                                                                  |
# | bedrooms      | Number of bedrooms                                                                                          |
# | bathrooms     | Number of bathrooms                                                                                         |
# | sqft_living   | Square footage of the home                                                                                  |
# | sqft_lot      | Square footage of the lot                                                                                   |
# | floors        | Total floors (levels) in house                                                                              |
# | waterfront    | House which has a view to a waterfront                                                                      |
# | view          | Has been viewed                                                                                             |
# | condition     | How good the condition is overall                                                                           |
# | grade         | overall grade given to the housing unit, based on King County grading system                                |
# | sqft_above    | Square footage of house apart from basement                                                                 |
# | sqft_basement | Square footage of the basement                                                                              |
# | yr_built      | Built Year                                                                                                  |
# | yr_renovated  | Year when house was renovated                                                                               |
# | zipcode       | Zip code                                                                                                    |
# | lat           | Latitude coordinate                                                                                         |
# | long          | Longitude coordinate                                                                                        |
# | sqft_living15 | Living room area in 2015(implies-- some renovations) This might or might not have affected the lotsize area |
# | sqft_lot15    | LotSize area in 2015(implies-- some renovations)                                                            |
# 

# In[ ]:


#After executing the below command restart the kernel and run all cells.
get_ipython().system('pip3 install scikit-learn --upgrade --user')


# You will require the following libraries:
# 

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.linear_model import LinearRegression
get_ipython().run_line_magic('matplotlib', 'inline')


# # Module 1: Importing Data Sets
# 

# Load the csv:
# 

# In[2]:


file_name='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'
df=pd.read_csv(file_name)


# We use the method <code>head</code> to display the first 5 columns of the dataframe.
# 

# In[4]:


df.head()


# ### Question 1
# 
# Display the data types of each column using the function dtypes, then take a screenshot and submit it, include your code in the image.
# 

# In[5]:


df.dtypes


# We use the method describe to obtain a statistical summary of the dataframe.
# 

# In[6]:


df.describe()


# # Module 2: Data Wrangling
# 

# ### Question 2
# 
# Drop the columns <code>"id"</code>  and <code>"Unnamed: 0"</code> from axis 1 using the method <code>drop()</code>, then use the method <code>describe()</code> to obtain a statistical summary of the data. Take a screenshot and submit it, make sure the <code>inplace</code> parameter is set to <code>True</code>
# 

# In[7]:


df.drop(axis = 1,columns=['id','Unnamed: 0'],inplace=True)


# In[8]:


df.describe()


# We can see we have missing values for the columns <code> bedrooms</code>  and <code> bathrooms </code>
# 

# In[27]:


print("number of NaN values for the column bedrooms :", df['bedrooms'].isnull().sum())
print("number of NaN values for the column bathrooms :", df['bathrooms'].isnull().sum())


# We can replace the missing values of the column <code>'bedrooms'</code> with the mean of the column  <code>'bedrooms' </code> using the method <code>replace()</code>. Don't forget to set the <code>inplace</code> parameter to <code>True</code>
# 

# In[28]:


mean=df['bedrooms'].mean()
df['bedrooms'].replace(np.nan,mean, inplace=True)


# We also replace the missing values of the column <code>'bathrooms'</code> with the mean of the column  <code>'bathrooms' </code> using the method <code>replace()</code>. Don't forget to set the <code> inplace </code>  parameter top <code> True </code>
# 

# In[29]:


mean=df['bathrooms'].mean()
df['bathrooms'].replace(np.nan,mean, inplace=True)


# In[11]:


print("number of NaN values for the column bedrooms :", df['bedrooms'].isnull().sum())
print("number of NaN values for the column bathrooms :", df['bathrooms'].isnull().sum())


# # Module 3: Exploratory Data Analysis
# 

# ### Question 3
# 
# Use the method <code>value_counts</code> to count the number of houses with unique floor values, use the method <code>.to_frame()</code> to convert it to a dataframe.
# 

# In[30]:


df.head()


# In[31]:


df['floors'].tail()


# In[32]:


total_unique_floors = df['floors'].value_counts().to_frame()
total_unique_floors.rename(columns={'floors':'Counts'},inplace=True)
total_unique_floors


# ### Question 4
# 
# Use the function <code>boxplot</code> in the seaborn library  to  determine whether houses with a waterfront view or without a waterfront view have more price outliers.
# 

# In[15]:


sns.boxplot(x='waterfront',y='price',data=df)


# ### Question 5
# 
# Use the function <code>regplot</code>  in the seaborn library  to  determine if the feature <code>sqft_above</code> is negatively or positively correlated with price.
# 

# In[33]:


sns.regplot(x='sqft_above',y='price',data=df,scatter_kws={'s':15},color='green')
plt.ylim(0,)
plt.title('Relation between sq-ft and price!!! ',color='Blue')
#positively correlated


# We can use the Pandas method <code>corr()</code>  to find the feature other than price that is most correlated with price.
# 

# In[34]:


df.corr()['price'].sort_values()


# # Module 4: Model Development
# 

# We can Fit a linear regression model using the  longitude feature <code>'long'</code> and  caculate the R^2.
# 

# In[35]:


X = df[['long']]
Y = df['price']
lm = LinearRegression()
lm.fit(X,Y)
lm.score(X, Y)


# ### Question  6
# 
# Fit a linear regression model to predict the <code>'price'</code> using the feature <code>'sqft_living'</code> then calculate the R^2. Take a screenshot of your code and the value of the R^2.
# 

# In[36]:


X = df[['sqft_living']]
Y = df['price']
lm = LinearRegression()
lm.fit(X,Y)
r2 = lm.score(X,Y)
print("R-Square is : ",r2)


# ### Question 7
# 
# Fit a linear regression model to predict the <code>'price'</code> using the list of features:
# 

# In[37]:


features =df[["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]]
y = df['price']


# Then calculate the R^2. Take a screenshot of your code.
# 

# In[38]:


lm.fit(features,Y)
r2 = lm.score(features,Y)

print("R-Square is : ",r2)


# ### This will help with Question 8
# 
# Create a list of tuples, the first element in the tuple contains the name of the estimator:
# 
# <code>'scale'</code>
# 
# <code>'polynomial'</code>
# 
# <code>'model'</code>
# 
# The second element in the tuple  contains the model constructor
# 
# <code>StandardScaler()</code>
# 
# <code>PolynomialFeatures(include_bias=False)</code>
# 
# <code>LinearRegression()</code>
# 

# In[39]:


Input=[('scale',StandardScaler()),('polynomial', PolynomialFeatures(include_bias=False)),('model',LinearRegression())]


# ### Question 8
# 
# Use the list to create a pipeline object to predict the 'price', fit the object using the features in the list <code>features</code>, and calculate the R^2.
# 

# In[40]:


pipe = Pipeline(Input)

pipe.fit(features,Y)

pipe.predict(features)


# In[81]:


R = pipe.score(features,Y)
print("R^2 VALUE IS ",R)


# # Module 5: Model Evaluation and Refinement
# 

# Import the necessary modules:
# 

# In[41]:


from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
print("done")


# We will split the data into training and testing sets:
# 

# In[42]:


features =["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]    
X = df[features]
Y = df['price']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, random_state=1)


print("number of test samples:", x_test.shape[0])
print("number of training samples:",x_train.shape[0])


# ### Question 9
# 
# Create and fit a Ridge regression object using the training data, set the regularization parameter to 0.1, and calculate the R^2 using the test data.
# 

# In[43]:


from sklearn.linear_model import Ridge


# In[44]:


ridge=Ridge(alpha=0.1)
ridge.fit(x_train,y_train)


# In[45]:


ridge.predict(x_test)


# In[46]:


#y_test


# In[47]:


test_r2 = ridge.score(x_test,y_test)
print('R^2 using the test data :',test_r2)


# ### Question 10
# 
# Perform a second order polynomial transform on both the training data and testing data. Create and fit a Ridge regression object using the training data, set the regularisation parameter to 0.1, and calculate the R^2 utilising the test data provided. Take a screenshot of your code and the R^2.
# 

# In[48]:


pr = PolynomialFeatures(degree=2)
X_train_trans = pr.fit_transform(x_train)
x_test_trans = pr.fit_transform(x_test)

ridge.fit(X_train_trans,y_train)
ridge.score(x_test_trans,y_test)


# <h2>About the Authors:</h2> 
# 
# <a href="https://www.linkedin.com/in/joseph-s-50398b136/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDA0101ENSkillsNetwork20235326-2022-01-01">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.
# 

# Other contributors: <a href="https://www.linkedin.com/in/michelleccarey/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDA0101ENSkillsNetwork20235326-2022-01-01">Michelle Carey</a>, <a href="https://www.linkedin.com/in/jiahui-mavis-zhou-a4537814a?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDA0101ENSkillsNetwork20235326-2022-01-01">Mavis Zhou</a>
# 

# ## Change Log
# 
# | Date (YYYY-MM-DD) | Version | Changed By      | Change Description                           |
# | ----------------- | ------- | --------------- | -------------------------------------------- |
# | 2022-07-29        | 2.3     | Lakshmi Holla | Added library import |
# | 2020-12-01        | 2.2     | Aije Egwaikhide | Coverted Data describtion from text to table |
# | 2020-10-06        | 2.1     | Lakshmi Holla   | Changed markdown instruction of Question1    |
# | 2020-08-27        | 2.0     | Malika Singla   | Added lab to GitLab                          |
# 
# <hr>
# 
# ## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>
# 
# <p>
# 
