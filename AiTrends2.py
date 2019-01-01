from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
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
post_date=df.groupby(['Date'])['Date'].count()

def post_bar_chart(post_date):
    ax=post_date.plot(kind='bar',color=['red','gold','skyblue','green','orange','teal','cyan','lime','orangered','aqua','blue','white'],fontsize=12)
    ax.set_title("Post Date\n", fontsize=18)
    ax.set_xlabel("Date",fontsize=12)
    ax.set_ylabel("Posts",fontsize=12)
    plt.show()
    print(post_date)


post_bar_chart(post_date)


