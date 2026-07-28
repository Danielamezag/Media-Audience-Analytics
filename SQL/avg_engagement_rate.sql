-- Highest average engagement rate
SELECT
	channel,
	AVG(engagement_rate) AS avg_engagement_rate
FROM youtube_videos
WHERE views >0
GROUP BY channel
ORDER BY avg_engagement_rate DESC

