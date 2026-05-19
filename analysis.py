import pandas as pd

import sqlite3

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

conn = sqlite3.connect('netflix.db')

df_clean = df.dropna(subset=["country"])
df_clean.to_sql('shows', conn, if_exists='replace', index=False)



def run_query(conn,query,title):
	result = conn.execute(query)
	print(title)
	for row in result:
		print (row)
run_query(conn,"SELECT type, COUNT(*) as count FROM shows GROUP BY type", "Filmy vs seriale")

run_query(conn,"SELECT title, release_year FROM shows WHERE country = 'United States' AND release_year >= 2015", "US Shows after 2015")

run_query(conn, "SELECT country, COUNT(*) as top FROM shows GROUP BY country ORDER BY top DESC LIMIT 5", "Top countries")


conn.close()   