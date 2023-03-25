import pandas as pd
text=["this is the first document from heaven","but the second document is from mars","and this is the third one from nowhere","is this the first document from nowhere?"]

#create dataframe of above sentences
textdf=pd.DataFrame({"text":text})
print(textdf)
# print(textdf.shape)

from sklearn.feature_extraction.text import CountVectorizer
countv=CountVectorizer()
x=countv.fit_transform(textdf.text).toarray()
print(x)
print(countv.get_feature_names())
print(countv.vocabulary_)


#count vectorizer with stop words
countv=CountVectorizer(stop_words=["this","and","is"])
x=countv.fit_transform(textdf.text).toarray()
print(x)
