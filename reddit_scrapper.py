from dotenv import load_dotenv
import os
import praw

load_dotenv()  # Load .env file

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD"),
    user_agent=os.getenv("USER_AGENT")
)

subreddit = reddit.subreddit('sex')
comments = subreddit.comments(limit=400)

data = []
for comment in comments:
    if comment.author and "bot" not in comment.author.name.lower():
        data.append(comment.body)

with open("nsfw_reddit.txt", "w", encoding="utf-8") as f:
    for line in data:
        f.write(line.replace('\n', ' ') + "\n")