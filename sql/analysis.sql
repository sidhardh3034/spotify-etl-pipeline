-- 1. Top 10 genres by average popularity

SELECT
    track_genre,
    ROUND(AVG(popularity)::numeric, 2) AS average_popularity
FROM spotify_tracks
GROUP BY track_genre
ORDER BY average_popularity DESC
LIMIT 10;


-- 2. Number of tracks by popularity level

SELECT
    popularity_level,
    COUNT(*) AS track_count
FROM spotify_tracks
GROUP BY popularity_level
ORDER BY track_count DESC;


-- 3. Average track duration by popularity level

SELECT
    popularity_level,
    ROUND(AVG(duration_min)::numeric, 2) AS average_duration_min
FROM spotify_tracks
GROUP BY popularity_level
ORDER BY average_duration_min DESC;

-- 4. Average audio features of the most popular genres

SELECT
    track_genre,
    ROUND(AVG(popularity)::numeric, 2) AS avg_popularity,
    ROUND(AVG(danceability)::numeric, 2) AS avg_danceability,
    ROUND(AVG(energy)::numeric, 2) AS avg_energy
FROM spotify_tracks
GROUP BY track_genre
ORDER BY avg_popularity DESC
LIMIT 10;

-- 5. Compare audio features by popularity level

SELECT
    popularity_level,
    COUNT(*) AS track_count,
    ROUND(AVG(danceability)::numeric, 2) AS avg_danceability,
    ROUND(AVG(energy)::numeric, 2) AS avg_energy,
    ROUND(AVG(duration_min)::numeric, 2) AS avg_duration_min
FROM spotify_tracks
GROUP BY popularity_level
ORDER BY
    CASE popularity_level
        WHEN 'High' THEN 1
        WHEN 'Medium' THEN 2
        WHEN 'Low' THEN 3
    END;

-- 6. Top 20 most popular tracks

SELECT
    track_name,
    artists,
    popularity,
    track_genre
FROM spotify_tracks
ORDER BY popularity DESC
LIMIT 20;


-- 7. Number of tracks in each genre

SELECT
    track_genre,
    COUNT(*) AS track_count
FROM spotify_tracks
GROUP BY track_genre
ORDER BY track_count DESC;

