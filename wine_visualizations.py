
# coding: utf-8

# # Plotting with Matplotlib
# Use Matplotlib to create bar charts that visualize the conclusions you made with groupby and query.

# In[2]:


# Import necessary packages and load `winequality_edited.csv`
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd

df = pd.read_csv('winequality_edited.csv')
df.info()


# ### #1: Do wines with higher alcoholic content receive better ratings?
# Create a bar chart with one bar for low alcohol and one bar for high alcohol wine samples. This first one is filled out for you.

# In[3]:


# Use query to select each group and get its mean quality
median = df['alcohol'].median()
low = df.query('alcohol < {}'.format(median))
high = df.query('alcohol >= {}'.format(median))

mean_quality_low = low['quality'].mean()
mean_quality_high = high['quality'].mean()


# In[4]:


# Create a bar chart with proper labels
locations = [1, 2]
heights = [mean_quality_low, mean_quality_high]
labels = ['Low', 'High']
plt.bar(locations, heights, tick_label=labels)
plt.title('Average Quality Ratings by Alcohol Content')
plt.xlabel('Alcohol Content')
plt.ylabel('Average Quality Rating');


# ### #2: Do sweeter wines receive higher ratings?
# Create a bar chart with one bar for low residual sugar and one bar for high residual sugar wine samples.

# In[25]:


# Use query to select each group and get its mean quality
median = df['residual_sugar'].median()
low_s = df.query('residual_sugar < {}'.format(median))
high_s = df.query('residual_sugar >= {}'.format(median))

mean_quality_low_s = low_s['quality'].mean()
mean_quality_high_s = high_s['quality'].mean()


# In[26]:


# Create a bar chart with proper labels
locations = [1, 2]
heights = [mean_quality_low_s, mean_quality_high_s]
labels = ['Low', 'High']
plt.bar(locations, heights, tick_label=labels)
plt.title('Average Quality Ratings by Sugar Content')
plt.xlabel('Sugar Content')
plt.ylabel('Average Quality Rating');


# ### #3: What level of acidity receives the highest average rating?
# Create a bar chart with a bar for each of the four acidity levels.

# In[71]:


# Use groupby to get the mean quality for each acidity level
import numpy as np
quality_levels = df.replace(np.nan,0)
df.groupby(['acidity_levels'],as_index=False)['quality'].mean()


# In[73]:


# Create a bar chart with proper labels
locations = [ 1, 2, 3, 4]
heights = [(quality_levels)]
labels = ['Low', 'Medium','Moderately High', 'High']
plt.bar(x=locations, height=heights, tick_label=labels)
plt.title('Average Quality Ratings by Acidity Levels')
plt.xlabel('Acidity Level')
plt.ylabel('Average Quality Rating');


# ### Bonus: Create a line plot for the data in #3
# You can use pyplot's [plot](https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot) function for this.

# Compare this with the bar chart. How might showing this visual instead of the bar chart affect someone's conclusion about this data?
