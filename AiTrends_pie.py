from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')


url = 'https://aitrends.com'
page = urlopen(url)

soup = BeautifulSoup(page,'html.parser')

page_structure = soup.find_all('div', class_='td_module_10 td_module_wrap td-animation-stack')
topic = []
category = []
time = []
content = []

for container in page_structure:
    post_topic = container.h3.a.text
    x=container.find_all('div',class_='td-module-meta-info')
    post_category = x[0].a.text
    post_time = x[0].span.time.text
    y = container.find_all('div',class_='td-excerpt')
    post_content = y[0].text
    topic.append(post_content)
    category.append(post_category)
    time.append(post_time)
    content.append(post_content)

df = pd.DataFrame({'Date':time,'Topic':topic,'Category':category,'Content':content})
df=df.drop_duplicates(['Content'])
post_category=df.groupby(['Category'])['Date'].count()

def post_category_pie_chart(post_category):
    fig,ax=plt.subplots()
    explodex=[]
    for i in np.arange(len(post_category)):
        explodex.append(0.05)

    ax=post_category.plot(kind='pie',colors=['red','gold','skyblue','green','orange','teal','cyan','lime','orangered','aqua','blue','blue'],fontsize=12,autopct='%1.1f%%',startangle=180,pctdistance=0.85,explode=explodex)
    inner_circle=plt.Circle((0,0),0.70,fc='white')
    fig=plt.gcf()
    fig.gca().add_artist(inner_circle)
    ax.axis('equal')
    ax.set_title("Post Categories\n",fontsize=18)
    plt.tight_layout()
    plt.show()

print(post_category)


post_category_pie_chart(post_category)


