import argparse
import yaml

# === Load all function imports ===
from scraper.reddit_scrapper import scrape_subreddit
from cleaner.dataset_cleaner import clean_dataset
from labeler.autolabel import auto_label_data
from labeler.manual_label import launch_manual_label_app
from trainer.nsfw_classifier import train_model, run_terminal_classifier

# === Load Config ===
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# === Parse CLI args ===
parser = argparse.ArgumentParser(description="NSFW Classifier Control Center")
parser.add_argument(
    "--mode",
    choices=["scrape", "clean", "autolabel", "label", "train", "run"],
    required=True,
    help="Choose which module to run."
)
args = parser.parse_args()

# === Route to correct function ===
if args.mode == "scrape":
    scraper_cfg = config["scraper"]
    scrape_subreddit(
        subreddit_name=scraper_cfg["subreddit"],
        limit=scraper_cfg["limit"],
        output_path=scraper_cfg["output_path"]
    )

elif args.mode == "clean":
    cleaner_cfg = config["cleaner"]
    clean_dataset(
        input_file=cleaner_cfg["input_path"],
        output_file=cleaner_cfg["output_path"],
        label_value=cleaner_cfg["label_value"],
        remove_emojis=cleaner_cfg["remove_emojis"]
    )

elif args.mode == "autolabel":
    auto_cfg = config["auto_label"]
    auto_label_data(
        input_csv=auto_cfg["input_path"],
        threshold=auto_cfg["threshold"],
        output_nsfw=auto_cfg["nsfw_output_path"],
        output_sfw=auto_cfg["sfw_output_path"]
    )

elif args.mode == "label":
    manual_cfg = config["manual_label"]
    launch_manual_label_app(
        data_file=manual_cfg["input_path"],
        labeled_file=manual_cfg["output_path"]
    )

elif args.mode == "train":
    train_model()

elif args.mode == "run":
    run_terminal_classifier()

else:
    print("❌ Unknown mode. This should be impossible if argparse did its job.")