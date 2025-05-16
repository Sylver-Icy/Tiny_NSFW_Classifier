# NSFW Text Classifier 🔞

This is my first ever machine learning project — a custom NSFW text classifier that flags inappropriate messages based on language content. It’s trained on a **tiny dataset (160 samples)** and still manages to perform surprisingly well.  

> “mommy cuddle me” → NSFW (0.81)  
> “let’s play chess” → SFW (0.73)  
> “i sleep on monday” → SFW (0.55)  
> “suck my d***” → NSFW (0.54)  

---

## 🧠 Model Details
- **Type**: Logistic Regression  
- **Vectorizer**: TF-IDF  
- **Language**: Python  
- **Libraries**: scikit-learn, pandas  
- **Interface**: Terminal-based input (for now)

---

### 📝 Note on Dataset Splitting

I intentionally didn’t split the dataset into train/test sets because the total sample size is very small (just 160 entries for now).  
This project was meant to validate the pipeline (TF-IDF + Logistic Regression) and test how it performs with limited data — not to optimize metrics.  

In future versions, once the dataset is expanded, proper train/test (and even validation) splits will be added.