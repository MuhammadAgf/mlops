from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib
from sklearn import metrics
import os
from gcs import GCS


MODEL_FILE_NAME = os.environ['MODEL_FILE_NAME'] # text-clf.joblib
BUCKET_NAME = os.environ['BUCKET_NAME'] # morgana-mlops
REMOTE_FILE_NAME = os.environ['REMOTE_FILE_NAME'] # demo/text-clf.joblib
PROJECT_NAME = os.environ['PROJECT_NAME']


categories = ["sci.electronics", "sci.med", "sci.space"]

def main():
    twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
    gcs_service = GCS(PROJECT_NAME)
    try:
        gcs_service.download_blob(BUCKET_NAME, MODEL_FILE_NAME, REMOTE_FILE_NAME)
        text_clf = joblib.load(MODEL_FILE_NAME)
    except Exception as e:
        print('err',str(e))
        text_clf = Pipeline([
            ('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', MultinomialNB()),
        ])
    text_clf.fit(twenty_train.data, twenty_train.target)

    twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)
    docs_test = twenty_test.data
    predicted = text_clf.predict(docs_test)

    print(metrics.classification_report(twenty_test.target, predicted, target_names=twenty_test.target_names))
    joblib.dump(text_clf, MODEL_FILE_NAME)
    gcs_service.upload_blob(BUCKET_NAME, MODEL_FILE_NAME, REMOTE_FILE_NAME)

if __name__ == "__main__":
    main()
