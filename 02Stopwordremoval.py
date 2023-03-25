from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
# import nltk
# nltk.download('stopwords')
print(list(punctuation))
print(stopwords.words("english"))
englishstopwords=stopwords.words("english")
text="I believe this would help the reader understand how tokenisation works , as well as realise its importance"
texttoken=text.lower().split()
stopwordslist=(list(punctuation)+englishstopwords)
print(stopwordslist)
keywords=[x for x in texttoken if x not in stopwordslist]
print(keywords)

