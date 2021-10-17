from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize

URL = "https://www.arts.texas.gov/initiatives/rural-initiatives/rural-texas-counties/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="dalist")
results = results.text.strip()

buffer = ""
counties = []
for ch in results:
    if ch == "\n":
        counties.append(buffer)
        buffer = ""

    else:
        buffer += '' + ch

df = pd.DataFrame(counties, columns=["Counties"])
df.to_csv('../cleaned_data/rural-counties.csv', index=False)








