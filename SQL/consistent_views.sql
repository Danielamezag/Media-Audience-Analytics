-- Consistent Performance 
SELECT 
	channel,
	STDDEV(views) AS consistent_views
FROM youtube_videos
GROUP BY channel
ORDER BY consistent_views