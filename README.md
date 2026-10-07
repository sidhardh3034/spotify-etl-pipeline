# Spotify ETL Pipeline

A data engineering project that extracts Spotify track data, cleans and transforms the data using Python and Pandas, loads the processed data into PostgreSQL, and performs SQL-based analysis.

## Project Overview

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline using Spotify track data.

The pipeline:

1. Extracts raw Spotify track data from a CSV file.
2. Cleans and transforms the data using Python and Pandas.
3. Stores the processed data in PostgreSQL.
4. Performs SQL-based analysis on the processed data.
5. Automates the complete pipeline using Python.

## Technologies Used

- Python
- Pandas
- PostgreSQL
- SQL
- SQLAlchemy
- Psycopg
- Git & GitHub

## Project Structure

```text
spotify-etl-pipeline/
├── data/
│   ├── raw/
│   │   └── dataset.csv
│   └── processed/
│       └── spotify_tracks_cleaned.csv
├── sql/
│   ├── schema.sql
│   └── analysis.sql
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── run_pipeline.py
├── requirements.txt
└── README.md
```
## Pipeline Workflow

```text
Raw Spotify Dataset
        ↓
     Extract
    extract.py
        ↓
    Transform
   transform.py
        ↓
  Cleaned Dataset
        ↓
      Load
     load.py
        ↓
   PostgreSQL
        ↓
   SQL Analysis
   analysis.sql
```


## ETL Process

### 1. Extract

The raw Spotify dataset is loaded from a CSV file using Pandas.

- Input: `data/raw/dataset.csv`
- Rows: 114,000
- Columns: 21

### 2. Transform

The raw data is cleaned and transformed using Pandas.

The transformation includes:

- Removing the unnecessary `Unnamed: 0` column
- Removing records with missing track information
- Removing tracks with invalid duration values
- Removing duplicate `track_id` and `track_genre` combinations
- Cleaning text fields
- Converting genres to lowercase
- Creating `duration_min`
- Creating `popularity_level`
- Validating numerical features

After transformation:

- Rows: 113,549
- Columns: 22


### 3. Load

The processed dataset is loaded into PostgreSQL.

- Database: `spotify_etl`
- Table: `spotify_tracks`
- Rows loaded: 113,549

SQLAlchemy and Psycopg are used to connect Python with PostgreSQL.


### 4. Analysis

SQL queries are used to analyze:

- Average popularity by genre
- Popularity-level distribution
- Average track duration
- Audio features by genre
- Audio features by popularity level
- Top popular tracks
- Track distribution by genre



## Database Schema

The processed Spotify data is stored in a PostgreSQL table named `spotify_tracks`.

The table contains:

- Track information
- Artist and album information
- Spotify audio features
- Popularity information
- Genre information
- Derived transformation fields

The primary key is a composite key:

```sql
PRIMARY KEY (track_id, track_genre)



## Analysis Results

Some key findings from the SQL analysis include:

- `pop-film` had the highest average popularity among the analyzed genres, with an average popularity of 59.28.
- The dataset contained 65,000 Low-popularity tracks, 43,081 Medium-popularity tracks, and 5,468 High-popularity tracks.
- High-popularity tracks had an average duration of 3.64 minutes, compared with 3.81 minutes for Low and Medium popularity tracks.
- High-popularity tracks had average danceability of 0.62 and average energy of 0.67.
- The most popular track in the analyzed results had a popularity score of 100.
- Multiple genres contained 1,000 tracks in the processed dataset.



## How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd spotify-etl-pipeline
```
### 2. Create and activate a virtual environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

Create a PostgreSQL database named:

```text
spotify_etl
```

### 5. Run the ETL pipeline

```powershell
python run_pipeline.py
```

### 6. Run SQL analysis

```powershell
psql -U postgres -d spotify_etl -f sql/analysis.sql

```

## Future Improvements

- Schedule the ETL pipeline to run automatically.
- Add automated data quality checks.
- Add logging and monitoring for pipeline failures.
- Connect the PostgreSQL database to a visualization tool such as Power BI or Tableau.
- Build machine learning models using the processed Spotify data.



## Author

**Sidhardh S**

B.Tech in Information Technology

GitHub: [sidhardh3034](https://github.com/sidhardh3034)