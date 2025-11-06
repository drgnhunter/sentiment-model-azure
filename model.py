import pickle
import json  # Import the json module
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# ---------------------------------
# 1. LOAD DATASET FROM JSON FILE
# ---------------------------------
print("--- 1. Loading Sample Dataset from dataset.json ---")

with open('dataset.json', 'r') as f:
    data = json.load(f)

texts = data['texts']
labels = data['labels']

print(f"Loaded {len(texts)} sample reviews from file.")


# ---------------------------------
# 2. BUILD AND TRAIN THE MODEL
# ---------------------------------
print("\n--- 2. Building and Training Model ---")

# Create the pipeline
sentiment_model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('classifier', MultinomialNB())
])

# Train the entire pipeline on our data
sentiment_model.fit(texts, labels)

print("Model training complete.")


# ---------------------------------
# 3. CREATE THE PICKLE FILE
# ---------------------------------
model_filename = 'sentiment_model.pkl'
print(f"\n--- 3. Saving Model to {model_filename} ---")

# 'wb' means 'write binary'
with open(model_filename, 'wb') as f:
    pickle.dump(sentiment_model, f)

print(f"Successfully saved model to {model_filename}")


# ---------------------------------
# 4. LOAD AND VERIFY THE PICKLE FILE
# ---------------------------------
print(f"\n--- 4. Loading Model from {model_filename} ---")

# 'rb' means 'read binary'
with open(model_filename, 'rb') as f:
    loaded_model = pickle.load(f)

print("Model loaded successfully.")

# Test the loaded model with new, unseen data
print("\n--- 5. Testing Loaded Model ---")
new_reviews = [
    "The weather is great today!",
    "I am very disappointed with this product.",
    "This was an acceptable experience."
]

predictions = loaded_model.predict(new_reviews)

for review, sentiment in zip(new_reviews, predictions):
    print(f"Review: '{review}'  ==>  Predicted Sentiment: {sentiment}")