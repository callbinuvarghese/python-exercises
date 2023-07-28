#!pip install anonymizedf

import pandas as pd
from anonymizedf.anonymizedf import anonymize

# Import the data
df = pd.read_csv("https://query.data.world/s/shcktxndtu3ojonm46tb5udlz7sp3e")

