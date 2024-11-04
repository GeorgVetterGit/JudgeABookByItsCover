import requests
import pandas as pd
from bs4 import BeautifulSoup

#Get html source code from web page
r = requests.get('https://de.wikipedia.org/wiki/Liste_der_meistverkauften_Belletristikb%C3%BCcher_in_Deutschland')
html = r.text

#Parse HTML site to text
parsed_html = BeautifulSoup(html,'html.parser')
site = parsed_html.get_text()

#Define relevant decades
decade_list = ['1961', '1971', '1981', '1991', '2001', '2011', '2021']

#Set initial values for loop
year = 1960
tuple_list = []
for idx, decade in enumerate(decade_list):
    
    #Check if the last entry is reached
    if idx == len(decade_list) - 1:
        break
    
    #get indexes an select relevant decade string
    first_idx = site.find(decade_list[idx] + ' ff.[Bearbeiten | Quelltext bearbeiten]')
    second_idx = site.find(decade_list[idx + 1] + ' ff.[Bearbeiten | Quelltext bearbeiten]')
    decade_string = site[first_idx:second_idx]
    decade_string_split = decade_string.split('\n')

    #Initial values for decade loop
    add_next = False
    empty_count = 0
    
    #loop over decade entries
    for row in decade_string_split:

        if add_next:
            tuple_list.append((first_entry, row, year))
            add_next = False

        if len(row) > 4:

            #if empty_count >= 2:
            #    year += 1
            #empty_count = 0

            if row[0] not in '0123456789':
                if empty_count >= 2:
                    year += 1
                empty_count = 0
                first_entry = row
                add_next = True
        else:
            empty_count += 1

df_books = pd.DataFrame(tuple_list, columns=['title', 'time_range', 'year'])

df_books.to_excel('books.xlsx')