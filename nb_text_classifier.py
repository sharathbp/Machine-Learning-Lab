from sklearn.datasets import fetch_20newsgroups
categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True)
twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True)

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
x_train_tf = count_vect.fit_transform(twenty_train.data)
x_test_tf = count_vect.transform(twenty_test.data)

from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transform = TfidfTransformer()
x_train_tfidf = tfidf_transform.fit_transform(x_train_tf)
x_test_tfidf = tfidf_transform.transform(x_test_tf)

from sklearn.naive_bayes import MultinomialNB
mnb = MultinomialNB()
mnb.fit(x_train_tfidf, twenty_train.target)
pred = mnb.predict(x_test_tfidf)

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
print("Accuracy=%.2f" % accuracy_score(twenty_test.target, pred))
print(classification_report(twenty_test.target, pred, target_names = twenty_test.target_names))
print("confusion matrix : \n", confusion_matrix(twenty_test.target, pred))