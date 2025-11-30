import pandas as pd
import numpy as np

# -----------------------------------------------------------
# 1. Estandarizar nombres de columnas
# -----------------------------------------------------------

def clean_column_names(df):
    """
    Normaliza los nombres de columnas:
    - minúsculas
    - sin espacios
    - sin caracteres especiales
    """
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^a-z0-9_]", "", regex=True)
    )
    return df


# -----------------------------------------------------------
# 2. Estandarizar todas las columnas por tipo de dato
# -----------------------------------------------------------

def standardize_all_columns(df):
    """
    Estandariza columnas según su tipo:
    - columnas de texto (excepto content_rating): strip + title()
    - columnas numéricas: conversión segura a numérico
    """
    df = df.copy()

    # Columnas de texto excepto content_rating
    text_cols = [
        col for col in df.columns
        if df[col].dtype == "object" and col != "content_rating"
    ]

    for col in text_cols:
        df[col] = df[col].astype(str).str.strip().str.title()

    # Columnas numéricas
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


# -----------------------------------------------------------
# 3. Eliminar duplicados
# -----------------------------------------------------------

def remove_duplicates(df):
    """Elimina duplicados completos."""
    df = df.copy()
    return df.drop_duplicates()


# -----------------------------------------------------------
# 4. Manejo de valores nulos
# -----------------------------------------------------------

def handle_missing_values(df):
    """
    Manejo razonado de nulos:
    - language: imputación mediante la moda (English)
    - country: imputación mediante la moda (USA)
    """

    df = df.copy()

    # Justificación:
    # (1) Dominancia estadística: English y USA son valores predominantes.
    # (2) Coherencia contextual: idioma y país están correlacionados.
    # (3) Evitar eliminar registros válidos por falta de estos datos.

    if "language" in df.columns:
        df["language"] = df["language"].fillna(df["language"].mode()[0])

    if "country" in df.columns:
        df["country"] = df["country"].fillna(df["country"].mode()[0])

    return df


# -----------------------------------------------------------
# 5. Normalizar categorías de content_rating
# -----------------------------------------------------------

def normalize_categories(df):
    """
    Normalización manual de content_rating:
    - strip + upper
    - unificación de equivalentes
    """
    df = df.copy()

    if "content_rating" not in df.columns:
        return df

    df["content_rating"] = df["content_rating"].astype(str).str.strip().str.upper()

    replacements = {
        "PG 13": "PG-13",
        "PG13": "PG-13",
        "NOT RATED": "UNRATED",
        "UN-RATED": "UNRATED",
        "X": "NC-17",
    }

    df["content_rating"] = df["content_rating"].replace(replacements)
    return df


# -----------------------------------------------------------
# 6. Extraer main_genre
# -----------------------------------------------------------

def extract_main_genre(df):
    """Extrae el primer género de la columna genres."""
    df = df.copy()

    if "genres" in df.columns:
        df["main_genre"] = df["genres"].str.split("|").str[0]

    return df


# -----------------------------------------------------------
# 7. Crear movie_type
# -----------------------------------------------------------

def create_movie_type(df):
    """
    Define categorías:
    - <60  -> Cortometraje
    - 60-120 -> Pelicula
    - >120 -> Pelicula_Larga
    """
    df = df.copy()

    if "duration" not in df.columns:
        return df

    def classify(t):
        if pd.isna(t):
            return np.nan
        if t < 60:
            return "Cortometraje"
        elif t <= 120:
            return "Pelicula"
        else:
            return "Pelicula_Larga"

    df["movie_type"] = df["duration"].apply(classify)
    return df


# -----------------------------------------------------------
# 8. Corregir outliers de title_year
# -----------------------------------------------------------

def fix_year_outliers(df):
    """Mantiene años entre 1920 y 2025."""
    df = df.copy()

    if "title_year" not in df.columns:
        return df

    mask = (df["title_year"].isna()) | (
        (df["title_year"] >= 1920) & (df["title_year"] <= 2025)
    )
    return df[mask]


# -----------------------------------------------------------
# 9. Ajuste final de tipos (incluye convertir 'color' a category)
# -----------------------------------------------------------

def fix_dtypes(df):
    """
    Ajuste de tipos:
    - title_year como Int32
    - columnas categóricas clave convertidas a category
    - NO convertir identificadores (nombres, URLs, títulos)
    """
    df = df.copy()

    # Años como enteros
    if "title_year" in df.columns:
        df["title_year"] = (
            pd.to_numeric(df["title_year"], errors="coerce").astype("Int32")
        )

    # Columnas categóricas reales
    categorical_cols = [
        "country",
        "language",
        "content_rating",
        "main_genre",
        "movie_type",
        "color",  # se añade color como categoría real
    ]

    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].astype("category")

    return df


# -----------------------------------------------------------
# 10. ORDENAR DATASET POR RECAUDACIÓN (gross)
# -----------------------------------------------------------

def sort_by_gross(df):
    """
    Ordena el dataset por la variable 'gross' de mayor a menor.
    Este paso se incluye porque puede facilitar análisis posteriores.
    """
    df = df.copy()

    if "gross" in df.columns:
        df = df.sort_values(by="gross", ascending=False)

    return df


# -----------------------------------------------------------
# 11. PIPELINE COMPLETO
# -----------------------------------------------------------

def clean_data(df):
    """
    Ejecuta TODA LA LIMPIEZA sobre una copia del dataset.
    Incluye:
    - estandarización general
    - manejo de nulos
    - creación de columnas
    - normalización de categorías
    - conversión de tipos
    - ordenación por recaudación
    """
    df = df.copy()

    df = clean_column_names(df)
    df = standardize_all_columns(df)
    df = remove_duplicates(df)

    df = extract_main_genre(df)
    df = handle_missing_values(df)
    df = normalize_categories(df)
    df = create_movie_type(df)

    df = standardize_all_columns(df)  # estandariza también columnas nuevas
    df = fix_dtypes(df)
    df = fix_year_outliers(df)

    df = sort_by_gross(df)  # *** Orden final por recaudación ***

    return df




    
