-- Channel that recieves highest average likes
SELECT 
	channel, 
	AVG(likes) as avg_likes
FROM youtube_videos
GROUP BY channel
ORDER BY avg_likes DESC