import pandas as pd
import numpy as np

# LECTURA DEL DATASET
df = pd.read_csv("nasa_exoplanet_intelligence.csv",sep=",")

# INFORMACIÓN ORIGINAL
print("\nDATASET ORIGINAL")

print(f"Filas originales: {df.shape[0]}")
print(f"Columnas originales: {df.shape[1]}")
