import pandas as pd
import numpy as np
from datetime import datetime

ARCHIVO_ENTRADA = "nasa_exoplanet_intelligence.csv"
ARCHIVO_SALIDA = "nasa_exoplanet_intelligence_clean.csv"
REPORTE_LIMPIEZA = "dataset_limpio.txt"

print("\n================ CARGANDO DATASET ================\n")

df = pd.read_csv(
    ARCHIVO_ENTRADA,
    sep=","
)

filas_originales = df.shape[0]
columnas_originales = df.shape[1]

print("=============== DATASET ORIGINAL ===============")
print(f"Filas originales: {filas_originales}")
print(f"Columnas originales: {columnas_originales}")

df = df.loc[:, ~df.columns.duplicated()]

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(r"[^a-zA-Z0-9_]", "", regex=True)
)

print("\nColumnas estandarizadas correctamente.")

filas_antes = len(df)

df.drop_duplicates(inplace=True)
df.dropna(how="all", inplace=True)

filas_eliminadas = filas_antes - len(df)

print("\nFilas duplicadas y vacías eliminadas.")
print(f"Filas eliminadas: {filas_eliminadas}")

columnas_texto = df.select_dtypes(include="object").columns

for col in columnas_texto:

    df[col] = df[col].astype(str)

    df[col] = df[col].str.strip()

    df[col] = df[col].str.lower()

    df[col] = df[col].replace(
        ["", " ", "nan", "none", "null"],
        np.nan
    )

print("\nTexto normalizado correctamente.")

columnas_antes = len(df.columns)

df.dropna(axis=1, how="all", inplace=True)

columnas_vacias_eliminadas = columnas_antes - len(df.columns)

print(f"\nColumnas vacías eliminadas: {columnas_vacias_eliminadas}")

columnas_eliminadas = []

for col in df.columns:

    if df[col].nunique(dropna=True) <= 1:

        columnas_eliminadas.append(col)

if columnas_eliminadas:

    df.drop(columns=columnas_eliminadas, inplace=True)

    print("\nColumnas eliminadas por poca utilidad:")

    for col in columnas_eliminadas:
        print(f"- {col}")

print("\n================ VALORES NULOS ================\n")

print(df.isnull().sum())

limite_nulos = len(df) * 0.70

columnas_antes_nulos = len(df.columns)

df = df.loc[:, df.isnull().sum() < limite_nulos]

columnas_nulos_eliminadas = columnas_antes_nulos - len(df.columns)

print("\nTratamiento de nulos finalizado.")
print(f"Columnas eliminadas por exceso de nulos: {columnas_nulos_eliminadas}")

df = df.reindex(
    sorted(df.columns),
    axis=1
)

df.reset_index(
    drop=True,
    inplace=True
)

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

df.to_csv(
    ARCHIVO_SALIDA,
    index=False
)

print("\nDataset limpio exportado correctamente.")

with open(REPORTE_LIMPIEZA, "w", encoding="utf-8") as archivo:

    archivo.write("=====================================\n")
    archivo.write("      REPORTE DE LIMPIEZA DATASET\n")
    archivo.write("=====================================\n\n")

    archivo.write(f"Fecha: {datetime.now()}\n\n")

    archivo.write("INFORMACIÓN ORIGINAL\n")
    archivo.write(f"Filas originales: {filas_originales}\n")
    archivo.write(f"Columnas originales: {columnas_originales}\n\n")

    archivo.write("INFORMACIÓN FINAL\n")
    archivo.write(f"Filas finales: {df.shape[0]}\n")
    archivo.write(f"Columnas finales: {df.shape[1]}\n\n")

    archivo.write("COLUMNAS ELIMINADAS\n")

    if columnas_eliminadas:
        for col in columnas_eliminadas:
            archivo.write(f"- {col}\n")
    else:
        archivo.write("No se eliminaron columnas.\n")

    archivo.write("\nDataset limpio correctamente.\n")

print("\nReporte generado: dataset_limpio.txt")
