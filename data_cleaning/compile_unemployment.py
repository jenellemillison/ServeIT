import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize

table = pd.read_html('https://txcip.org/tac/census/morecountyinfo.php?MORE=1042', skiprows=1)

uRate = table[0]
print(uRate)
