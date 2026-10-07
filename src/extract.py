import pandas as pd

file_path=r'data\raw\dataset.csv'
df=pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("Number of rows:", len(df))
print("Number of columns:", len(df.columns))

print("\nColumns:")
print(df.columns.tolist())


print("\nFirst 5 rows:")
print(df.head())


print('\nData types:')
print(df.dtypes)

print('\nMissing values:')
print(df.isnull().sum())


print("\nNumber of duplicate rows:", df.duplicated().sum())

print("Number of duplicate track IDs:", df["track_id"].duplicated().sum())

print("\nNumerical statistics:")
print(df.describe())



print("\nRows with missing values:")
print(df[df.isnull().any(axis=1)])


print("\nTracks with zero duration:")
print(df[df["duration_ms"] == 0][
    ["track_id", "track_name", "artists", "duration_ms"]
])

print("\nNumber of tracks with zero duration:")
print((df["duration_ms"] == 0).sum())

print("\nExample duplicate track IDs:")
duplicate_ids = df[df["track_id"].duplicated(keep=False)]

print(
    duplicate_ids[
        ["track_id", "track_name", "artists", "track_genre"]
    ].head(20)
)

print("\nDuplicate track_id + genre combinations:")
print(
    df.duplicated(
        subset=["track_id", "track_genre"]
    ).sum()
)

duplicate_combinations = df[
    df.duplicated(
        subset=["track_id", "track_genre"],
        keep=False
    )
]

print("\nDuplicate track_id + genre records:")
print(
    duplicate_combinations[
        [
            "track_id",
            "track_name",
            "artists",
            "track_genre",
            "popularity",
            "duration_ms"
        ]
    ].sort_values(
        ["track_id", "track_genre"]
    ).head(30)
)