import pandas as pd
import numpy as np

# LECTURA DEL DATASET
df = pd.read_csv("nasa_exoplanet_intelligence.csv",sep=",")

# INFORMACIÓN ORIGINAL
print("\nDATASET ORIGINAL")

print(f"Filas originales: {df.shape[0]}")
print(f"Columnas originales: {df.shape[1]}")

# ELIMINAR COLUMNAS DUPLICADAS
df = df.loc[:, ~df.columns.duplicated()]

# LIMPIEZA DE LOS NOMBRES DE LAS COLUMNAS
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(r"[^a-zA-Z0-9_]", "", regex=True)
)

print("\nColumnas estandarizadas correctamente.")


# ELIMINAR FILAS DUPLICADAS
df.drop_duplicates(inplace=True)

# ELIMINAR FILAS COMPLETAMENTE VACÍAS
df.dropna(how="all", inplace=True)

print("\nFilas duplicadas y vacías eliminadas.")