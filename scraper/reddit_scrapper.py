from dotenv import load_dotenv
import os
import praw

# Load environment variables from .env file (for API credentials)
load_dotenv()

# Initialize Reddit API client using PRAW and credentials from env
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD"),
    user_agent=os.getenv("USER_AGENT")
)

def scrape_subreddit(subreddit_name: str, limit: int, output_path: str):
    """
    Scrapes comments from a given subreddit using PRAW.
    Filters out bot accounts and writes the cleaned comment text to a .txt file.
    """
    print(f"Scraping subreddit: r/{subreddit_name} (limit: {limit})")
    try:
        subreddit = reddit.subreddit(subreddit_name)
        comments = subreddit.comments(limit=limit)
    except Exception as e:
        # Handle cases like invalid subreddit or network errors
        print(f"Error fetching comments: {e}")
        return

    data = set() # Using a set to automatically deduplicate comments
    skipped = 0  # Count how many comments were skipped due to bot filtering
    for comment in comments:
        # Filter out comments made by bots (common naming pattern includes 'bot')
        if comment.author and "bot" not in comment.author.name.lower():
            body = comment.body.strip().replace('\n', ' ').lower()
            data.add(body)
        else:
            skipped += 1

    with open(output_path, "w", encoding="utf-8") as f:
        for line in data:
            f.write(line + "\n")

    print(f"Total comments written: {len(data)}")
    print(f"Total comments skipped: {skipped}")