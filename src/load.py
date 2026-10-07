import pandas as pd
from sqlalchemy import create_engine

file_path = "data/processed/spotify_tracks_cleaned.csv"

df = pd.read_csv(file_path)

print("Cleaned data loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

connection_string = "postgresql+psycopg://postgres:Spotify%40123@localhost:5432/spotify_etl"

engine = create_engine(connection_string)

print("PostgreSQL engine created successfully!")

with engine.begin() as connection:
    connection.exec_driver_sql(
        "TRUNCATE TABLE spotify_tracks"
    )

    df.to_sql(
        "spotify_tracks",
        connection,
        if_exists="append",
        index=False
    )

print("Data loaded successfully into PostgreSQL!")

with engine.connect() as connection:
    result = connection.exec_driver_sql(
        "SELECT COUNT(*) FROM spotify_tracks"
    )
    row_count = result.scalar()

print("Rows in PostgreSQL:", row_count)


