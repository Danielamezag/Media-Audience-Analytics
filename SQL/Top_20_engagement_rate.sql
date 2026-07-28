SELECT 
	channel,
	title, 
	engagement_rate
FROM youtube_videos
WHERE views > 0
ORDER BY engagement_rate DESC
LIMIT 20

