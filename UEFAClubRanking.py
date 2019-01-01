#UEFA Club Ranking Complete Code

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.uefa.com'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
html_structure = soup.find_all('div',class_='ranking-card')


container = html_structure[0].ul
data = []
#ul_list = container.ul.li
#print(ul_list)



name = container.find_all('span', class_='ranking-name')
value = container.find_all('span', class_='ranking-value')

#print(name.text,"",value.text)

for i,j in zip(name,value):
    x = i.text
    y=j.text
    data.append([str(x),str(y)])
print(data)
df = pd.DataFrame(data,columns=("Name","Value"))
print(df)
                
