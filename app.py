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

for col in df.select_dtypes(include="object"):

    # Convertir a string
    df[col] = df[col].astype(str)

    # Eliminar espacios innecesarios
    df[col] = df[col].str.strip()

    # Convertir texto a minúsculas
    df[col] = df[col].str.lower()

    # Reemplazar valores vacíos por NaN
    df[col] = df[col].replace(
        ["", " ", "nan", "none", "null"],
        np.nan
    )

print("\nTexto normalizado correctamente.")


# Eliminar columnas completamente vacías
df.dropna(axis=1, how="all", inplace=True)

# Eliminar columnas con un único valor
for col in df.columns:

    if df[col].nunique(dropna=True) <= 1:

        print(f"\nColumna eliminada por poca utilidad: {col}")

        df.drop(columns=col, inplace=True)

# Mostrar valores nulos
print("\n================ VALORES NULOS ================\n")

print(df.isnull().sum())

# Eliminar columnas con más del 70% de nulos
limite_nulos = len(df) * 0.70

df = df.loc[:, df.isnull().sum() < limite_nulos]

print("\nTratamiento de nulos finalizado.")

# Ordenar columnas alfabéticamente
df = df.reindex(sorted(df.columns), axis=1)

# Reiniciar índices
df.reset_index(drop=True, inplace=True)

# INFORMACIÓN FINAL
print("\n================ DATASET LIMPIO ================")

print("\nDimensiones finales:")
print(df.shape)

print("\nTipos de datos:")
print(df.dtypes)

print("\nPrimeras filas:")
print(df.head())

print("\nÚltimas filas:")
print(df.tail())

print("\nInformación general:")
print(df.info())

# EXPORTAR DATASET LIMPIO
df.to_csv(
    "nasa_exoplanet_intelligence_clean.csv",
    index=False
)

print(
    "\nDataset limpio y estandarizado guardado correctamente."
)
