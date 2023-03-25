from sklearn.feature_extraction.text import TfidfVectorizer

text=["this is the first document from heaven","but the second document is from mars","and this is the third one from nowhere","is this the first document from nowhere?"]

vectorizer=TfidfVectorizer()
vectorizer.fit(text)
print(vectorizer.vocabulary_)
print(vectorizer.idf_)