-- Channel that receives highest average views
SELECT 
	channel,
	AVG(views) AS avg_views
FROM youtube_videos
GROUP BY channel


-- 