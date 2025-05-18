import joblib

model = joblib.load("nsfw_classifier_v1.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def is_nsfw(text):
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]
    confidence = model.predict_proba(vec)[0]

    return prediction,confidence

while True:
    a = input()
    if a.lower() == "exit":
        break
    result,probs = is_nsfw(a)
    print("Nsfw" if result == 1 else "Sfw")
    print(f"Sfw {probs[0]:.2f}, Nsfw {probs[1]:.2f}")