-- Day with the highest views
SELECT
    TO_CHAR(published_at, 'Day') AS day_of_week,
    AVG(views) AS avg_views
FROM youtube_videos
GROUP BY day_of_week
ORDER BY avg_views DESC