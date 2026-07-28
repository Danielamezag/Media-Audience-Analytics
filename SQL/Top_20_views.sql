SELECT 
	channel,
	title, 
	views
FROM youtube_videos
ORDER BY views DESC
LIMIT 20