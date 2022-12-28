#In this example i will show as convert Bytes to GB in Python:

import pandas as pd

# Charge dataframe with data
df = pd.read_csv("datos.csv")

# Create function for conversion Bytes to Gigabytes
def convertir_a_gb(valor_bytes):
  return valor_bytes / (1024**3)

# Apply the function for each value in column
df["columna_gb"] = df["columna_bytes"].apply(convertir_a_gb)

# we must see a new column with name "columna_gb" with applied conversion
