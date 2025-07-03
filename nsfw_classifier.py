from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

import pandas as pd
import joblib

df = pd.read_csv("nsfw_dataset_500.csv")
df['text'] = df['text'].str.strip()
df = df.drop_duplicates()
# print(df.head())
# print(df['label'].value_counts())

# df.text=df.text.str.lower().str.strip()

vectorizer=TfidfVectorizer()
X = vectorizer.fit_transform(df.text)
y = df.label

model=LogisticRegression()
model.fit(X,y)

# preds = model.predict(X)

# while True:
#     user_input = input("Enter text to classify (or 'exit' to quit): ")
#     if user_input.lower() == "exit":
#         break
#     user_vec = vectorizer.transform([user_input])
#     prediction = model.predict(user_vec)[0]
#     probs = model.predict_proba(user_vec)[0]
#     print("NSFW" if prediction == 1 else "SFW")
#     print(f"Confidence — SFW: {probs[0]:.2f}, NSFW: {probs[1]:.2f}")

joblib.dump(model,"nsfw_classifier_v1.pkl")
joblib.dump(vectorizer,"vectorizer.pkl")