from sklearn.feature_extraction.text import HashingVectorizer
import pandas as pd
text=["this is the first document from heaven","but the second document is from mars","and this is the third one from nowhere","is this the first document from nowhere?"]
text1=pd.DataFrame({"Text":text})

hashvectorizer=HashingVectorizer(n_features=15,alternate_sign=False,norm=None)


print(hashvectorizer.fit_transform(text1.Text).toarray())
