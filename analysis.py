import pandas as pd

df = pd.read_csv('netflix_titles.csv')

print("Wymiary:", df.shape)
print("\nKolumny:", df.columns.tolist())
print("\nPuste wartości:\n", df.isnull().sum())

# Ile filmow vs seriali?
print("\nTypy treści:\n", df['type'].value_counts())

# Top 10 krajów
print("\nTop 10 krajów:\n", df['country'].value_counts().head(10))

# Filmy dodane po 2019
nowe = df[df['release_year'] > 2019]
print("\nFilmy po 2019:", len(nowe))

import sqlite3

conn = sqlite3.connect('netflix.db')
df.to_sql('shows', conn, if_exists='replace', index=False)

# Zapytanie 1 - ile filmow vs seriali
result = conn.execute("SELECT type, COUNT(*) as count FROM shows GROUP BY type")
print("\nSQL - typy:\n")
for row in result:
    print(row)


result = conn.execute('SELECT title, release_year FROM shows WHERE country = "United States" AND release_year >= 2015')
for row in result:
    print(row)

    result = conn.execute('SELECT country, COUNT(*) as top FROM shows WHERE country IS NOT NULL GROUP BY country ORDER BY top DESC LIMIT 5')
for row in result:
    print(row)


conn.close()   