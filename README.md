# 🧠 NSFW Text Classifier 🔞  
> Modular pipeline to detect NSFW comments using TF-IDF + Logistic Regression  

This repo contains a modular, fully configurable NSFW text classification pipeline — it can scrape, clean, label, train, and classify user-generated text. All from scratch. All with a single command.

Built for learning, usable for real-world projects.

---

## ⚡ Features

- 🧼 **Text Cleaner** — strips emojis, links, markdown, and other junk
- 🔍 **Reddit Scraper** — pulls live comments from any subreddit (via PRAW)
- 🏷️ **Auto-Labeler** — uses a trained model to tag comments as SFW/NSFW
- ✍️ **Manual Labeler** — Streamlit GUI for manually labelling weird cases
- 🧠 **Model Trainer** — trains TF-IDF + Logistic Regression model
- 🧪 **Terminal Classifier** — live classify text in the terminal
- 📁 **Fully Modular & Configurable** — all logic cleanly separated by module
- 📝 **YAML Config Driven** — Edit to your personal usecase

---

## 🚀 Quick Start (5 Steps & Done)

### 1. Clone & Enter

```bash
git clone https://github.com/Sylver-Icy/nsfw-classifier.git
cd nsfw-classifier
```

### 2. Install & Activate

```bash
python3 -m venv nsfwvenv
source nsfwvenv/bin/activate  # or use .\nsfwvenv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Configure Reddit API

Copy `.env`:

```bash
cp example.env .env
```

Edit your credentials inside `.env`:
```env
CLIENT_ID=your_reddit_app_id
CLIENT_SECRET=your_secret
USERNAME=your_username
PASSWORD=your_password
USER_AGENT=your_bot_name
```

> You can create Reddit credentials at https://www.reddit.com/prefs/apps

---

### 4. Configure Your Workflow

Edit `config.yaml` to your liking. Example:
```yaml
scraper:
  subreddit: "AskReddit"
  limit: 500
  output_path: "dataset/raw/sfw.txt"

cleaner:
  input_path: "dataset/raw/sfw.txt"
  output_path: "dataset/clean/sfw_clean.csv"
  remove_emojis: true
  minimum_comment_length: 2
  maximum_comment_length: 25
  label_value: 0
```

---

### 5. Run Any Stage with CLI

```bash
python run.py --mode scrape       # Scrape subreddit
python run.py --mode clean        # Clean raw text
python run.py --mode autolabel    # Use model to auto-label comments
python run.py --mode train        # Train the model
python run.py --mode run          # Try it in the terminal
```

### 👉 Manual Label Mode (Streamlit GUI)

```bash
streamlit run run.py -- --mode label
```

---

## 🧪 Sample Outputs (Real examples)

> “let’s play chess” → SFW (0.73)  
> “suck my d***” → NSFW (0.91)  
> “your thighs look huggable” → NSFW (0.68)  
> “I’ll bring snacks to class” → SFW (0.88)

---

## 📁 Folder Structure

```
.
├── config.yaml
├── run.py
├── scraper/
├── cleaner/
├── labeler/
├── trainer/
├── dataset/
│   ├── raw/
│   ├── clean/
├── example.env
├── requirements.txt
```

---

## 🔧 Tech Stack

- **Python 3.10+**
- scikit-learn
- pandas
- Streamlit
- TF-IDF
- PRAW (Reddit API wrapper)

---

## ⚠️ Disclaimers

- The model is trained on a tiny dataset (~1000 lines). It is not production ready.
- The purpose is to **learn, experiment, and explore** — not to judge humanity.
- Yes, you can build something better with transformers. This is intentionally simple.

---

## ✨ Future Plans

- Upgrade to SpaCy or transformer-based NLP
- HuggingFace model card + Gradio demo
- Add train/test split + metrics
- Deployable backend version with FastAPI or Flask
- Dataset expansion (Reddit, Twitter, YouTube, Discord)

---

## 💬 License
MIT — Free to use, modify, and share. Just don’t sell it as your OnlyFans detector :)

---

Star the repo if you enjoyed the project ⭐  
Pull requests and improvements are always welcome!