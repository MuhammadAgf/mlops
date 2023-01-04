from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib
from sklearn import metrics

categories = ["sci.electronics", "sci.med", "sci.space"]
twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', MultinomialNB()),
])
text_clf.fit(twenty_train.data, twenty_train.target)

print(twenty_train.data[0])

twenty_test = fetch_20newsgroups(subset='test',
    categories=categories, shuffle=True, random_state=42)
docs_test = twenty_test.data
predicted = text_clf.predict(docs_test)

print(metrics.classification_report(twenty_test.target, predicted,
    target_names=twenty_test.target_names))


model_file_name = "text-clf.joblib"
joblib.dump(text_clf, model_file_name)
