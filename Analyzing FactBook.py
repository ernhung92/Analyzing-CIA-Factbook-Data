
# coding: utf-8

# # Overview of the Data

# In[6]:


# Importing the pandas and sqlite libraries
import pandas
import sqlite3

# Connecting to the database
conn = sqlite3.connect("factbook.db")

# Finds the tables from the database
query1 = "select * from sqlite_master WHERE type='table';"
pandas.read_sql_query(query1, conn)


# There are two tables on the database

# In[7]:


# Displays the first 5 rows of table "facts"
query2 = "select * from facts limit 5;"
pandas.read_sql_query(query2, conn)


# # Summary Statistics

# In[9]:


query3 = "SELECT MIN(population) as min_population, MAX(population) as max_population, MIN(population_growth) as min_pop_growth, MAX(population_growth) as max_pop_growth FROM facts;"
pandas.read_sql_query(query3, conn)


# # Exploring Outliers

# In[11]:


query4 = "SELECT * FROM facts WHERE population==(SELECT MIN(population) FROM facts);"
pandas.read_sql_query(query4, conn)


# The Antarctica is the country with a population of 0

# In[12]:


query5 = "SELECT * FROM facts WHERE population==(SELECT MAX(population) FROM facts);"
pandas.read_sql_query(query5, conn)


# There seems to be a row of data with a total population of 7256490011 people, meaning that this is the total number of people in the world

# # Histograms

# In[15]:


import matplotlib.pyplot as plt
import seaborn 
get_ipython().magic('matplotlib inline')

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

query6 = "SELECT population, population_growth, birth_rate, death_rate FROM facts WHERE population!=(SELECT MIN(population) FROM facts) and population!=(SELECT MAX(population) FROM facts);"
pandas.read_sql_query(query6, conn).hist(ax=ax)


# # Which Countries have the highest population density

# In[16]:


query7 = "SELECT name, CAST(population as float)/CAST(area_land as float) density FROM facts ORDER BY density DESC LIMIT 10;"
pandas.read_sql_query(query7, conn)

