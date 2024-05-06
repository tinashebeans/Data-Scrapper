
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://weatherandclimate.com/harare/december-2010"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

table_yedu = soup.find_all("table", class_= "tb7")

#print(table_yedu) ##

column_titles = soup.find("table", class_= "tb7").find_all("th")
data_title_names = [title.text.strip() for title in column_titles]
#print(data_title_names)

df = pd.DataFrame(columns= data_title_names)

#print(df)

column_data = soup.find("table", class_= "tb7").find_all("tr")


for row in column_data[1:]:
    row_data = row.find_all("td")
    individual_row_data = [data.text.strip() for data in row_data]

    #print(individual_row_data)

    length = len(df)
    df.loc[length] = individual_row_data

print(df)
df.to_csv(r'C:\Users\User\Desktop\project\2010\December_data.csv', index = False)

print("data collected and csv is saved successfully!!")

#commit changes