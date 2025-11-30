import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set(style="whitegrid")

# ===========================================================
#   📌 TANDA 1 – VISUALIZACIONES BÁSICAS (EDA GENERAL)
# ===========================================================

def plot_histogram(df, column, bins=30, save=False):
    """Histograma con KDE para ver la distribución de variables numéricas."""
    plt.figure(figsize=(8,5))
    sns.histplot(df[column].dropna(), bins=bins, kde=True)
    plt.title(f"Distribución de {column}")
    plt.xlabel(column)
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    if save:
        plt.savefig(f"../figures/hist_{column}.png")
    plt.show()

def histograms_basics(df, save=False):
    num_cols = ["duration", "gross", "budget", "imdb_score", "num_user_for_reviews"]
    for col in num_cols:
        if col in df.columns:
            plot_histogram(df, col, save=save)

def plot_bar(df, column, top=None, save=False):
    """Gráfico de barras para variables categóricas."""
    counts = df[column].value_counts()
    if top:
        counts = counts.head(top)
    plt.figure(figsize=(8,5))
    sns.barplot(x=counts.values, y=counts.index)
    plt.title(f"Frecuencia de {column}")
    plt.xlabel("Frecuencia")
    plt.ylabel(column)
    plt.tight_layout()
    if save:
        plt.savefig(f"../figures/bar_{column}.png")
    plt.show()

def barplots_basics(df, save=False):
    for col in ["main_genre", "color", "movie_type"]:
        if col in df.columns:
            plot_bar(df, col, save=save)

def plot_box(df, category_col, numeric_col, save=False):
    """Boxplot para comparar distribuciones numéricas entre categorías."""
    plt.figure(figsize=(10,5))
    sns.boxplot(x=df[category_col], y=df[numeric_col])
    plt.title(f"{numeric_col} según {category_col}")
    plt.tight_layout()
    if save:
        plt.savefig(f"../figures/box_{category_col}_{numeric_col}.png")
    plt.show()

def boxplots_basics(df, save=False):
    if "main_genre" in df.columns and "gross" in df.columns:
        plot_box(df, "main_genre", "gross", save=save)
    if "movie_type" in df.columns and "duration" in df.columns:
        plot_box(df, "movie_type", "duration", save=save)

def run_basic_visualizations(df, save=False):
    print("📊 Histogramas esenciales...")
    histograms_basics(df, save=save)

    print("📊 Barras esenciales...")
    barplots_basics(df, save=save)

    print("📊 Boxplots esenciales...")
    boxplots_basics(df, save=save)

    print("✅ Tanda 1 completada.")


# ===========================================================
#   📌 TANDA 2 – VISUALIZACIONES INTERMEDIAS (EDA GLOBAL)
# ===========================================================

def scatterplots_intermediate(df, save=False):
    pairs = [
        ("budget", "gross"),
        ("duration", "imdb_score"),
        ("imdb_score", "gross"),
    ]
    for x, y in pairs:
        if x in df.columns and y in df.columns:
            plt.figure(figsize=(8,5))
            sns.scatterplot(data=df, x=x, y=y, alpha=0.4)
            plt.title(f"Relación entre {x} y {y}")
            plt.tight_layout()
            if save:
                plt.savefig(f"../figures/scatter_{x}_{y}.png")
            plt.show()

def barplots_means_intermediate(df, save=False):
    groups = [
        ("main_genre", "gross"),
        ("movie_type", "gross"),
        ("color", "gross")
    ]
    for cat, num in groups:
        if cat in df.columns and num in df.columns:
            plt.figure(figsize=(10,5))
            sns.barplot(data=df, x=cat, y=num, estimator=np.mean)
            plt.title(f"Recaudación media según {cat}")
            plt.xticks(rotation=45)
            plt.tight_layout()
            if save:
                plt.savefig(f"../figures/mean_{cat}.png")
            plt.show()

def correlation_heatmap(df, save=False):
    corr = df.select_dtypes(include=[np.number]).corr()
    plt.figure(figsize=(10,8))
    sns.heatmap(corr, cmap="coolwarm", annot=False)
    plt.title("Mapa de correlaciones")
    plt.tight_layout()
    if save:
        plt.savefig("../figures/correlation_heatmap.png")
    plt.show()

def run_intermediate_visualizations(df, save=False):
    print("📍 Scatterplots...")
    scatterplots_intermediate(df, save=save)

    print("📍 Gráficos de medias por categoría...")
    barplots_means_intermediate(df, save=save)

    print("📍 Mapa de correlaciones...")
    correlation_heatmap(df, save=save)

    print("✅ Tanda 2 completada.")


# ===========================================================
#   📌 TANDA 3 – VISUALIZACIONES AVANZADAS (EDA PROFESIONAL)
# ===========================================================

def pairplot_advanced(df, save=False):
    cols = ["budget", "gross", "imdb_score", "duration"]
    cols = [c for c in cols if c in df.columns]
    sns.pairplot(df[cols].dropna(), diag_kind="kde")
    if save:
        plt.savefig("../figures/pairplot.png")
    plt.show()

def violinplots_advanced(df, save=False):
    if "main_genre" in df.columns and "imdb_score" in df.columns:
        plt.figure(figsize=(12,5))
        sns.violinplot(data=df, x="main_genre", y="imdb_score", inner="quartile")
        plt.xticks(rotation=45)
        plt.title("Distribución de IMDB por género")
        plt.tight_layout()
        if save:
            plt.savefig("../figures/violin_imdb_genre.png")
        plt.show()

    if "color" in df.columns and "gross" in df.columns:
        plt.figure(figsize=(10,5))
        sns.violinplot(data=df, x="color", y="gross", inner="quartile")
        plt.title("Distribución de gross por color")
        plt.tight_layout()
        if save:
            plt.savefig("../figures/violin_gross_color.png")
        plt.show()

def log_distributions(df, save=False):
    for col in ["gross", "budget", "num_voted_users"]:
        if col in df.columns:
            plt.figure(figsize=(8,5))
            sns.histplot(np.log1p(df[col].dropna()), bins=40, kde=True)
            plt.title(f"Distribución logarítmica de {col}")
            plt.tight_layout()
            if save:
                plt.savefig(f"../figures/logdist_{col}.png")
            plt.show()

def run_advanced_visualizations(df, save=False):
    print("🔬 Pairplot avanzado…")
    pairplot_advanced(df, save=save)

    print("🔬 Violinplots avanzados…")
    violinplots_advanced(df, save=save)

    print("🔬 Distribuciones logarítmicas…")
    log_distributions(df, save=save)

    print("✅ Tanda 3 completada.")


# ===========================================================
#   🎯 TANDA 4 – VISUALIZACIONES PARA EL OBJETIVO DEL PROYECTO
# ===========================================================

# OBJETIVO:
# ¿Según el país, la recaudación se ve afectada por el género y la clasificación por edades?

def gross_by_country(df, save=False):
    plt.figure(figsize=(12,6))
    sns.boxplot(data=df, x="country", y="gross")
    plt.xticks(rotation=45)
    plt.title("Recaudación por país")
    plt.tight_layout()
    if save:
        plt.savefig("../figures/gross_by_country.png")
    plt.show()

def genre_by_country(df, save=False):
    plt.figure(figsize=(14,6))
    sns.barplot(data=df, x="main_genre", y="gross", hue="country", estimator=np.mean)
    plt.xticks(rotation=45)
    plt.title("Recaudación media por género y país")
    plt.tight_layout()
    if save:
        plt.savefig("../figures/genre_by_country.png")
    plt.show()

def rating_by_country(df, save=False):
    plt.figure(figsize=(12,6))
    sns.barplot(data=df, x="content_rating", y="gross", hue="country", estimator=np.mean)
    plt.xticks(rotation=45)
    plt.title("Recaudación media por clasificación y país")
    plt.tight_layout()
    if save:
        plt.savefig("../figures/rating_by_country.png")
    plt.show()

def full_interaction(df, save=False):
    g = sns.catplot(
        data=df,
        x="main_genre",
        y="gross",
        hue="content_rating",
        col="country",
        kind="bar",
        col_wrap=3,
        height=5
    )
    g.fig.subplots_adjust(top=0.9)
    g.fig.suptitle("Interacción país × género × clasificación")
    if save:
        g.savefig("../figures/full_interaction.png")
    plt.show()

def run_objective_visualizations(df, save=False):
    print("🎯 Recaudación por país…")
    gross_by_country(df, save=save)

    print("🎯 Género × país…")
    genre_by_country(df, save=save)

    print("🎯 Clasificación × país…")
    rating_by_country(df, save=save)

    print("🎯 Interacción completa país × género × clasificación…")
    full_interaction(df, save=save)

    print("🎯 Tanda específica del objetivo completada.")


# ===========================================================
# 19. Visualizaciones orientadas al objetivo del estudio
#     (país × género × clasificación × recaudación)
# ===========================================================

def recaudacion_por_pais(df, save=False):
    """ Boxplot de recaudación por país. """
    plt.figure(figsize=(12,6))
    sns.boxplot(data=df, x="country", y="gross")
    plt.title("Recaudación por país")
    plt.xticks(rotation=45)
    plt.tight_layout()
    if save:
        plt.savefig("../figures/recaudacion_pais.png")
    plt.show()

def recaudacion_por_genero_pais(df, save=False):
    """
    Gráfico SIEMPRE FUNCIONAL de recaudación global por género.
    - Si df tiene 'country', no importa.
    - Si df NO está agrupado, agrupo adentro.
    - Nunca produce gráfico vacío.
    """

    # Si la columna main_genre no existe → no hay nada que graficar
    if "main_genre" not in df.columns:
        print("⚠️ El dataframe no contiene 'main_genre'. No se puede graficar.")
        return

    # Si NO está agregada la recaudación, la agregamos aquí
    if "country" in df.columns or df["gross"].count() != df.shape[0]:
        df_group = (
            df.groupby("main_genre")["gross"]
            .sum()
            .reset_index()
            .sort_values("gross", ascending=False)
        )
    else:
        # ya está agrupado (df_group)
        df_group = df.copy()

    # Si todo es cero → mostramos aviso
    if df_group["gross"].sum() == 0:
        print("⚠️ Todas las recaudaciones son 0. Gráfico vacío.")
        return
    
    # Gráfico
    plt.figure(figsize=(14,6))
    sns.barplot(data=df_group, x="main_genre", y="gross")
    plt.xticks(rotation=45)
    plt.title("Recaudación global por género")
    plt.tight_layout()

    if save:
        plt.savefig("../figures/recaudacion_genero_pais.png")

    plt.show()

def recaudacion_por_clasificacion_pais(df, save=False):
    """ Recaudación por clasificación de edades dentro de cada país. """
    plt.figure(figsize=(14,6))
    sns.barplot(data=df, x="content_rating", y="gross", hue="country", errorbar=None)
    plt.title("Recaudación según clasificación y país")
    plt.xticks(rotation=45)
    plt.tight_layout()
    if save:
        plt.savefig("../figures/recaudacion_clasificacion_pais.png")
    plt.show()

def interaccion_pais_genero_clasificacion(df, save=False):
    """ 
    Visualización completa: país × género × clasificación × recaudación.
    Esta es la visualización clave del objetivo.
    """
    g = sns.catplot(
        data=df,
        x="main_genre",
        y="gross",
        hue="content_rating",
        col="country",
        kind="bar",
        col_wrap=3,
        height=4,
        sharey=False
    )
    g.fig.suptitle("Interacción entre país, género, clasificación y recaudación", y=1.02)
    
    if save:
        plt.savefig("../figures/interaccion_objetivo.png")

    plt.show()

def run_objetivo_visualizations(df, save=False):
    """ Runner general de visualizaciones enfocadas al objetivo del estudio. """
    print("➡ Recaudación por país")
    recaudacion_por_pais(df, save=save)

    print("➡ Recaudación global por género")
    recaudacion_por_genero_pais(df, save=save)

    print("➡ Recaudación por clasificación según país")
    recaudacion_por_clasificacion_pais(df, save=save)

    print("➡ Interacción país × género × clasificación × recaudación")
    interaccion_pais_genero_clasificacion(df, save=save)

    print("✔ Visualizaciones orientadas al objetivo completadas.")
