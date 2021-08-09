from typing import Dict
from bs4 import BeautifulSoup
import lxml.html as lh
import requests
import pandas as pd
import re

DK_MLB_URL = "https://sportsbook.draftkings.com/leagues/baseball/88670847?category=game-lines&subcategory=game"
NUMBERS = "0123456789"
DAY_LETTERS ="MTWFS"

try: 
    page = requests.get(DK_MLB_URL)
except:
    print("An error occured.")

# Holds the page content
doc = lh.fromstring(page.content)

# all of the table rows
tr_elements = doc.xpath('//tr')

# columns
col = []
i = 0

col.append(('TIME', []))

# loop through the headers of the table rows adding to the columns list
for t in tr_elements[0]:
    i+=1
    name = t.text_content()
    col.append((name, []))

pattern = r'.*[PA]M'
regex = re.compile(pattern)

count = 0

for j in range(1, len(tr_elements)):
    T=tr_elements[j]

    if len(T) != 4:
        break

    i = 1
    
    # Handles the time column
    for t in T.iterchildren():
        if i == 1:
            data = t.text_content()
            time = re.findall(regex, data)
            if len(time) > 0:
                col[0][1].append(time)
            if (len(data) > 4) and (data[0] in DAY_LETTERS) and (data != "MONEYLINE") and (data != "TOTAL"):
                col[0][1].append("NA") 

    # adds the values to the rows
    for t in T.iterchildren():
        data=t.text_content()
        col[i][1].append(data)
        i += 1

Dict={title:column for (title,column) in col}
df = pd.DataFrame(Dict)

print(df)
