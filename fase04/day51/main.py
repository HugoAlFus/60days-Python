# spam_classifier.py
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

texts = [
    "Free money now!!!",
    "Congratulations, you've won a free ticket!",
    "Call this number now to claim your prize",
    "Hi John, are we still meeting later?",
    "Don't forget the meeting at 10am",
    "Can you send me the report?",
    "Win a brand new car",
    "Hey, how was your day?",
    "Important update regarding your bank account",
    "Let's catch up soon!"
]
labels = [1, 1, 1, 0, 0, 0, 1, 0, 1, 0]

X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.3, random_state=42)

model = make_pipeline(CountVectorizer(), MultinomialNB())

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Reporte de clasificación:\n", metrics.classification_report(y_test, y_pred))


def classify_text(text):
    pred = model.predict([text])[0]
    return "Spam" if pred == 1 else "No Spam"


print(classify_text("Congratulations, you’ve won a prize!"))
print(classify_text("Hey, are we still on for lunch?"))
