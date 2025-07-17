from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

import pandas as pd
import joblib
import glob

def train_model(output_model_path="nsfw_classifier_v1.pkl", output_vectorizer_path="vectorizer.pkl"):
    """
    Trains the logistic regression NSFW classifier using all CSV files in the dataset/clean directory.
    Saves the trained model and vectorizer as .pkl files.
    """
    all_files = glob.glob("dataset/clean/*.csv")  # looks for CSV files in the folder
    df_list = [pd.read_csv(file) for file in all_files]
    df = pd.concat(df_list, ignore_index=True)

    # Clean up text: strip whitespace and remove duplicates
    df['text'] = df['text'].str.strip()
    df = df.drop_duplicates()
    
    #Parameters for standard Tf-IDF vectorizer edit them if you wanna tweak the model 
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=10000,
        min_df=2,
        strip_accents="unicode",
        sublinear_tf=True,
        stop_words=None
    )

    # Transform text into vectorized format and extract labels
    X = vectorizer.fit_transform(df.text)
    y = df.label

    # Train model on vectorized text
    model = LogisticRegression()
    model.fit(X, y)

    # Save model and vectorizer
    joblib.dump(model, output_model_path)
    joblib.dump(vectorizer, output_vectorizer_path)

def run_terminal_classifier(model_path="nsfw_classifier_v1.pkl", vectorizer_path="vectorizer.pkl"):
    """
    Loads trained model and vectorizer and lets you test predictions via terminal
    """
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)

    while True:
        user_input = input("Enter text to classify (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        user_vec = vectorizer.transform([user_input])
        prediction = model.predict(user_vec)[0]
        probs = model.predict_proba(user_vec)[0]
        print("NSFW" if prediction == 1 else "SFW")
        print(f"Confidence — SFW: {probs[0]:.2f}, NSFW: {probs[1]:.2f}")