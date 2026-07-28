DROP TABLE IF EXISTS youtube_videos;

CREATE TABLE youtube_videos (
    channel TEXT,
    video_id TEXT,
    title TEXT,
    published_at TIMESTAMPTZ,
    description TEXT,
    tags TEXT,
    category_id INT,
    views BIGINT,
    likes BIGINT,
    comments BIGINT,
    engagement_rate FLOAT
);