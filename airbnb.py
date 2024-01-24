# -*- coding: utf-8 -*-
"""

####Importing Libraries
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %matplotlib inline

# Commented out IPython magic to ensure Python compatibility.
# %lsmagic

"""####Mounting Google Drive"""

from google.colab import drive
drive.mount('/content/drive/')

path = '/content/drive/My Drive/'

"""####Importing Dataset From Drive

"""

df = pd.read_csv(path + 'Airbnb NYC 2019.csv')

df.info()

df.describe()

df.head()

df.isnull().sum()

df.columns

"""###Taking Necessary Columns Only"""

new_df = df[['id','name','host_id','host_name','neighbourhood_group','neighbourhood','room_type','price','minimum_nights',
             'number_of_reviews','calculated_host_listings_count','availability_365']]
new_df.head(5)

"""##1. What can we learn about different hosts and areas?"""

hosts_areas = new_df.groupby(['host_name','neighbourhood_group'])['calculated_host_listings_count'].max().reset_index()
hosts_areas.sort_values(by='calculated_host_listings_count', ascending=False).head(5)

"""##As we can see most number of listings are from **Manhattan** created Sonder (NYC), Blueground, Michael, David

##2. What can we learn from predictions? (ex: locations, prices, reviews, etc)
"""

areas_reviews = new_df.groupby(['neighbourhood_group'])['number_of_reviews'].max().reset_index()
areas_reviews

area = areas_reviews['neighbourhood_group']
review = areas_reviews['number_of_reviews']

fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(area, review, color ='maroon',
        width = 0.4)

plt.xlabel("area")
plt.ylabel("review")
plt.title("Area vs Number of reviews")
plt.show()

price_area = new_df.groupby(['price'])['number_of_reviews'].max().reset_index()
price_area.head(5)

area = price_area['price']
price = price_area['number_of_reviews']

fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.scatter(area, price)

plt.xlabel("Price")
plt.ylabel("Number of Review")
plt.title("Price vs Number of Reviews")
plt.show()

"""##From the above Analysis we can say that most people prefer to stay in place where price is less.

##3.Which hosts are the busiest and why?
"""

busiest_hosts = new_df.groupby(['host_name','host_id','room_type'])['number_of_reviews'].max().reset_index()
busiest_hosts = busiest_hosts.sort_values(by='number_of_reviews', ascending=False).head(10)
busiest_hosts

name = busiest_hosts['host_name']
reviews = busiest_hosts['number_of_reviews']

fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(name, reviews, color ='maroon',
        width = 0.4)

plt.xlabel("Name of the Host")
plt.ylabel("Number of Reviews")
plt.title("Busiest Hosts")
plt.show()

"""##Busiest hosts are:
1. Dona
2. Ji
3. Maya
4. Carol
5. Danielle

##Because these hosts listed room type as Entire home and Private room which is preferred by most number of people.

##4. Is there any noticeable difference of traffic among different areas and what could be the reason for it?
"""

traffic_areas = new_df.groupby(['neighbourhood_group','room_type'])['minimum_nights'].count().reset_index()
traffic_areas = traffic_areas.sort_values(by='minimum_nights', ascending=False)
traffic_areas

room_type = traffic_areas['room_type']
stayed = traffic_areas['minimum_nights']

fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(room_type, stayed, color ='maroon',
        width = 0.4)

plt.xlabel("Room Type")
plt.ylabel("Minimum number of nights stayed")
plt.title("Traffic Areas")
plt.show()

"""###From the Above Analysis We can Stay that People are preferring Entire home/apt or Private room which are present in Manhattan, Brooklyn, Queens and people are preferring listings which are less in price.

##Conclusion:
###1. The people who prefer to stay in Entire home or  Apartment they are going to stay bit longer in that particular Neighbourhood only.
###2. The people who prefer to stay in Private room they won't stay longer as compared to Home or Apartment.
###3. Most people prefer to pay less price.
###4. If there are more number of Reviews for particular Neighbourhood group that means that place is a tourist place.
###5. If people are not staying more then one night means they are travellers.

---


#Thanks
"""
