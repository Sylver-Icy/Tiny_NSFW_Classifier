import pandas as pd
import joblib

# Load model and vectorizer
model = joblib.load("nsfw_classifier_v1.pkl") # The actual brain that predicts NSFW-ness
vectorizer = joblib.load("vectorizer.pkl")   # Turns words into numbers the model can understand

def auto_label_data(input_csv, threshold, output_nsfw, output_sfw):
    """Auto-labels a dataset based on NSFW probability using a pre-trained model."""
    # Load the cleaned input CSV
    df = pd.read_csv(input_csv)

    # Drop NaNs (to avoid crash)
    df = df.dropna(subset=['text'])

    # Vectorize and predict
    X = vectorizer.transform(df['text'])
    probs = model.predict_proba(X)

    # Split based on threshold
    nsfw_rows = [] #For spicy stuff
    sfw_rows = [] #For sweet stuff??

    for i, prob in enumerate(probs):
        if prob[1] > threshold:
            nsfw_rows.append(df.iloc[i])
        else:
            sfw_rows.append(df.iloc[i])

    # Convert back to DataFrame
    nsfw_df = pd.DataFrame(nsfw_rows)
    sfw_df = pd.DataFrame(sfw_rows)
    nsfw_df['label'] = 1
    sfw_df['label'] = 0
    nsfw_df.to_csv(output_nsfw, index=False)
    sfw_df.to_csv(output_sfw, index=False)

    print("✅ Auto-labeling done.")