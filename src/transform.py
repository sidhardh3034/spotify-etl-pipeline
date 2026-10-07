import pandas as pd

file_path = "data/raw/dataset.csv"

df = pd.read_csv(file_path)

print("Raw data loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))


df = df.drop(columns=["Unnamed: 0"])

print("\nRemoved 'Unnamed: 0' column.")
print("Rows:", len(df))
print("Columns:", len(df.columns))

df = df.dropna(
    subset=["track_id", "artists", "album_name", "track_name"]
)

df = df[df["duration_ms"] > 0]

print("\nRemoved invalid track records.")
print("Rows:", len(df))
print("Columns:", len(df.columns))


df = df.drop_duplicates(
    subset=["track_id", "track_genre"]
)

print("\nRemoved duplicate track_id + genre records.")
print("Rows:", len(df))
print("Columns:", len(df.columns))

text_columns = [
    "artists",
    "album_name",
    "track_name",
    "track_genre"
]

for column in text_columns:
    df[column] = df[column].str.strip()

print("\nText columns cleaned.")



df["duration_min"] = df["duration_ms"] / 60000

print("\nCreated duration_min column.")

df["duration_min"] = df["duration_min"].round(2)

print("Duration rounded to 2 decimal places.")

print("\nDuration examples:")
print(
    df[["track_name", "duration_ms", "duration_min"]].head(10)
)

def classify_popularity(score):
    if score < 40:
        return "Low"
    elif score < 70:
        return "Medium"
    else:
        return "High"


df["popularity_level"] = df["popularity"].apply(classify_popularity)

print("\nCreated popularity_level column.")
print("\nPopularity examples:")
print(
    df[["track_name", "popularity", "popularity_level"]].head(10)
)

print("\nValidation checks:")

print(
    "Invalid popularity values:",
    ((df["popularity"] < 0) | (df["popularity"] > 100)).sum()
)

print(
    "Invalid danceability values:",
    ((df["danceability"] < 0) | (df["danceability"] > 1)).sum()
)

print(
    "Invalid energy values:",
    ((df["energy"] < 0) | (df["energy"] > 1)).sum()
)

print(
    "Invalid duration values:",
    (df["duration_min"] <= 0).sum()
)

audio_features = [
    "danceability",
    "energy",
    "speechiness",
    "acousticness",
    "instrumentalness",
    "liveness",
    "valence"
]

for column in audio_features:
    invalid_count = (
        (df[column] < 0) | (df[column] > 1)
    ).sum()

    print(
        f"Invalid {column} values:",
        invalid_count
    )



print("\nOther numerical validations:")

print(
    "Invalid key values:",
    ((df["key"] < 0) | (df["key"] > 11)).sum()
)

print(
    "Invalid mode values:",
    (~df["mode"].isin([0, 1])).sum()
)

print(
    "Invalid time_signature values:",
    ((df["time_signature"] < 0) | (df["time_signature"] > 5)).sum()
)

print(
    "Invalid tempo values:",
    (df["tempo"] < 0).sum()
)

print("\nFinal dataset summary:")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nFinal columns:")
print(df.columns.tolist())

output_path = "data/processed/spotify_tracks_cleaned.csv"

df.to_csv(
    output_path,
    index=False
)

print("\nTransformed data saved successfully!")
print("File:", output_path)


saved_df = pd.read_csv(output_path)

print("\nSaved file verification:")
print("Rows:", len(saved_df))
print("Columns:", len(saved_df.columns))

print("\nFirst 5 rows:")
print(saved_df.head())