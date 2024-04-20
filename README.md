# Introduction
Have fun scrapping real websites for faster data retrieval using **Python(Pandas)** and **BeautifulSoup** 

# Background
This project is a web scrapper that is used I used to scrape weather data (temperature, rainfall amount, humidity...etc), for my Final Year Project from the website: https://weatherandclimate.com

Here is the code: [data_scrapper](/data%20scrapper/)

# Tools I Used
These are the tools i used :

- **Python (Pandas):**  for data manipulation.
- **BeautifulSoup**: Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.
- **VS Code**: Code Editor

# The Scrapping
Here is how i went about it:

## Importing the necessary Libraries
```python
import requests #for making HTTP requests
from bs4 import BeautifulSoup
import pandas as pd
```

## Getting the web url
I used the **get** method from the **requests** library to retrieve the content of the webpage specified in the **url** variable.
The downloaded content of the webpage is then stored in the variable named **page**.

```python
url = "https://weatherandclimate.com/manicaland/march-2017"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
```

## Searching for the table i wanted
I used the **class** tag to find the exact table with the data I wanted.

```python
table_yedu = soup.find_all("table", class_= "tb7")
```

## Getting the column names of the table

```python
column_titles = soup.find("table", class_= "tb7").find_all("th")
data_title_names = [title.text.strip() for title in column_titles]
print(data_title_names)
```

the code iterates through the list stored in column_titles. For each table header element **(title)** in the list, it extracts the text content using the **.text** attribute. This retrieves the text displayed within the table header.

The **.strip()** method is then used to remove any leading or trailing whitespace characters from the extracted text.

Finally, the cleaned text is stored in a new list named **data_title_names**. 

## Creating a dataframe and assigning the extracted column names

```python
df = pd.DataFrame(columns= data_title_names)
```
## Finding all table rows
Used the function **find_all("tr")** to retrieve all  **<tr** elements (table row elements) within **tb7** and storing them  in the list named **column_data**.

```python
column_data = soup.find("table", class_= "tb7").find_all("tr")
```

##  Extracting individual data points
Start by finding data cells within each row and storing the data in the list **row_data**. And iterate though the created list cleaning the data and storing it in the list **individual_row_data**.

```python
for row in column_data[1:]:
    row_data = row.find_all("td")
    individual_row_data = [data.text.strip() for data in row_data]
```

## Assigning data to the DataFrame
Use the **len()** function to count the number of rows currently in the DataFrame and assign the data in **individual_row_data**  to a new row in the DataFrame.

```python
length = len(df)
    df.loc[length] = individual_row_data
```

## Storing the DataFrame Locally as a .csv file

```python
df.to_csv(r'C:\Users\User\Desktop\project\2017\March_data.csv', index = False)

print("data collected and csv is saved successfully!!")
```