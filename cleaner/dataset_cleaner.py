import pandas as pd
import re
import emoji

def clean_text(text, remove_emojis):
    """
    Cleans a single text input based on rules like lowercasing, emoji stripping,
    markdown cleanup, and word count filtering.
    
    Returns a list of clean strings (chunks), coz some long texts get split.
    """
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
        chunks = [chunk for chunk in chunks if len(chunk.split()) >= 2]
        return chunks if chunks else []

    return [text]

def clean_dataset(input_file, output_file, label_value, remove_emojis):
    """
    Reads a .txt file, cleans each line of text using clean_text(), 
    explodes chunked results into rows, assigns labels, and exports to CSV
    """
    with open(input_file, "r") as f:
        lines = f.readlines()

    df=pd.DataFrame({"text": [line.strip() for line in lines if line.strip()]})

    df["text"] = df["text"].apply(lambda x: clean_text(x, remove_emojis=remove_emojis))
    df = df.explode("text")
    df = df[df.text != ""]
    df["label"] = label_value
    df.to_csv(output_file, index=False)
    print(f"Cleaned {len(df)} lines from {input_file}")
