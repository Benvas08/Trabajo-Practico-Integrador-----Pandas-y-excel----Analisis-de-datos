import pandas as pd


# -----------  1  -----------
# -- Leemos las hojas y las guardamos en sus respectivos dataframes --
df_1900s = pd.read_excel('data/movies.xls', sheet_name='1900s')
df_2000s = pd.read_excel('data/movies.xls', sheet_name='2000s')
df_2010s = pd.read_excel('data/movies.xls', sheet_name='2010s')

# -- Mostramos las primeras 5 filas de cada dataframe y la cantidad de filas de cada uno --
print("\nPrimeras 5 filas de la hoja 2000s:\n", df_2000s.head())
print("\nCantidad de filas de la hoja 2010s:\n", len(df_2010s))


# -----------  2  -----------
# -- Concatenamos todos los dataframes en uno solo --
df_movies = pd.concat([df_1900s, df_2000s, df_2010s], ignore_index=True)

df_movies_10_filas = df_movies.head(10)
print("\nPrimeras 10 filas de nuestro df_movies:\n", df_movies_10_filas)


# -----------  3  -----------
# -- Realizamos los análisis solicitados --
print("\nCantidad de peliculas por país en df_movies:\n", df_movies['Country'].value_counts())
print("\nTop 5 directores en 2010s:\n", df_2010s['Director'].value_counts().head(5))
print("\nPeliculas por IMBD Score:\n", df_movies["IMDB Score"].sort_values(ascending=False).head())

# -----------  4  -----------
print("\nCalculamos el promedio IMDB Score por país:\n", df_movies.groupby('Country')["IMDB Score"].mean())

def get_decade(year):
    return str(year)[:3] + "0s" if pd.notna(year) else "Unknown"
df_movies["Decade"] = df_movies["Year"].apply(get_decade)
print("\nCantidad de peliculas por década:\n", df_movies["Decade"].value_counts())

# -----------  5  -----------
print("\nInformación general de df_movies:\n")
df_movies.info()


df_limpio = df_movies.dropna(subset=['IMDB Score'])
df_limpio.to_excel('data/movies_limpio.xlsx', index=False)