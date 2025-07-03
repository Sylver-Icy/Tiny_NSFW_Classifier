from dotenv import load_dotenv
import os
import praw

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD"),
    user_agent=os.getenv("USER_AGENT")
)

def scrape_subreddit(subreddit_name: str, limit: int = 400):
    print(f"Scraping subreddit: r/{subreddit_name} (limit: {limit})")
    try:
        subreddit = reddit.subreddit(subreddit_name)
        comments = subreddit.comments(limit=limit)
    except Exception as e:
        print(f"Error fetching comments: {e}")
        return

    data = set()
    skipped = 0
    for comment in comments:
        if comment.author and "bot" not in comment.author.name.lower():
            body = comment.body.strip().replace('\n', ' ').lower()
            data.add(body)
        else:
            skipped += 1

    with open("nsfw_reddit.txt", "w", encoding="utf-8") as f:
        for line in data:
            f.write(line + "\n")

    print(f"Total comments written: {len(data)}")
    print(f"Total comments skipped: {skipped}")

if __name__ == "__main__":
    scrape_subreddit("sex", 400)