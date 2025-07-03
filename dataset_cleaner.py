import pandas as pd
import re
import emoji

def clean_text(text, remove_emojis):
    """Cleans dataset"""
    if not isinstance(text, str):
        return []

    # Lowercase everything
    text = text.lower()

    # Remove URLs (http, https, www)
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)

    # Remove markdown links [text](link)
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)

    # Remove emojis
    if remove_emojis:
        text = emoji.replace_emoji(text, replace='')

    # Remove special characters (keep letters, numbers, spaces)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    # Remove extra spaces
    text = ' '.join(text.split())

    # Word count filter
    word_count = len(text.split())

    #  Skip short
    if word_count < 2:
        return []

    # Split long ones
    if word_count > 25:
        words = text.split()
        chunks = [' '.join(words[i:i+50]) for i in range(0, len(words), 50)]
        return chunks

    return [text]

input_file="nsfw_reddit.txt"
output_file="nsfw_sex_reddit.csv"
label_value = 1
remove_emojis = True

with open(input_file, "r") as f:
    lines = f.readlines()

df=pd.DataFrame({"text": [line.strip() for line in lines if line.strip()]})

df["text"] = df["text"].apply(lambda x: clean_text(x, remove_emojis=remove_emojis))
df = df.explode("text")
df = df[df.text != ""]
df["label"] = label_value
df.to_csv(output_file, index=False)
print(f"Cleaned {len(df)} lines from {input_file}")
