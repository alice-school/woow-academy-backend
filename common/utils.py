# resume_classifier/utils.py
import joblib
import nltk
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Preprocess text function
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    tokens = [word.lower() for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# Prediction function
def get_predicted_industry(student_details):
    
    # Define the path to the model file
    model_path = os.path.join(os.path.dirname(__file__), 'industry_model.pkl')
    trained_model = joblib.load(model_path)

    # Load the TF-IDF vectorizer
    vectorizer_path = os.path.join(os.path.dirname(__file__), 'tfidf_vectorizer.pkl')
    tfidf_vectorizer = joblib.load(vectorizer_path)

    # Extract features from the input resume
    about_text = student_details["cvProfile"]["about"]
    work_experience_text = " ".join([exp["jobDescription"] for exp in student_details["workExperience"]])
    skills_text = " ".join([skill["skillName"] for skill in student_details["skills"]])

    # Combine all relevant text data
    resume_text = " ".join([about_text, work_experience_text, skills_text])

    # Preprocess the combined text
    preprocessed_text = preprocess_text(resume_text)

    # Transform the preprocessed text into TF-IDF vectors
    preprocessed_text_tfidf = tfidf_vectorizer.transform([preprocessed_text])

    return trained_model.predict(preprocessed_text_tfidf)[0]
