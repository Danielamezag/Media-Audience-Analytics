-- Channel that recieves highest average comments
SELECT 
	channel, 
	AVG(comments) as avg_comments
FROM youtube_videos
GROUP BY channel
ORDER BY avg_comments DESC