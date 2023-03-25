from nltk.collocations import BigramCollocationFinder
from nltk.collocations import TrigramCollocationFinder
from nltk.collocations import QuadgramCollocationFinder
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation

print("THIS IS BIGRAM IN ngram")

text="I believe this would help the reader understand how tokenisation works , as well as realise its importance"
tlist=word_tokenize(text.lower())
print(tlist)

stopwordslist=list(punctuation)+stopwords.words('english')
keywordslist=[x for x in tlist if x not in stopwordslist]
print(keywordslist)

bigramofwords=BigramCollocationFinder.from_words(keywordslist)
print(list(bigramofwords.ngram_fd.items()))

bigramoftext=BigramCollocationFinder.from_words(text)
print(list(bigramoftext.ngram_fd.items()))

itemslist=list(bigramoftext.ngram_fd.items())
print(itemslist)
# for i in itemslist:
#     print(i[0][0],end="")

print("THIS IS TRIGRAM IN ngram")

trigramofwords=TrigramCollocationFinder.from_words(keywordslist)
print(list(trigramofwords.ngram_fd.items()))

trigramoftext=TrigramCollocationFinder.from_words(text)
print(list(trigramoftext.ngram_fd.items()))

itemslist=list(trigramoftext.ngram_fd.items())
print(itemslist)

trigramwordslist=[]
trigramtextlist=[]
# print(list(trigramofwords.ngram_fd.items())[0][0][0])
for i in range(len(list(trigramofwords.ngram_fd.items()))):
    tempstr=""
    for j in range(3):
        tempstr=tempstr+(list(trigramofwords.ngram_fd.items()))[i][0][j]+" "
    print(tempstr)
    trigramwordslist.append(tempstr)


for i in range(len(list(trigramoftext.ngram_fd.items()))):
    tempstr=""
    for j in range(3):
        tempstr=tempstr+(list(trigramoftext.ngram_fd.items()))[i][0][j]+" "
    print(tempstr)
    trigramtextlist.append(tempstr)

print(trigramwordslist)
print(trigramtextlist)

print("THIS IS QUADGRAM IN ngram")

quadgramofwords=QuadgramCollocationFinder.from_words(keywordslist)
print(list(trigramofwords.ngram_fd.items()))

quadgramoftext=QuadgramCollocationFinder.from_words(text)
print(list(trigramoftext.ngram_fd.items()))

itemslist=list(trigramoftext.ngram_fd.items())
print(itemslist)

# print(list(trigramofwords.ngram_fd.items())[0][0][0])
for i in range(len(list(quadgramofwords.ngram_fd.items()))):
    tempstr=""
    for j in range(4):
        tempstr=tempstr+(list(quadgramofwords.ngram_fd.items()))[i][0][j]+" "
    print(tempstr)


for i in range(len(list(quadgramoftext.ngram_fd.items()))):
    tempstr=""
    for j in range(4):
        tempstr=tempstr+(list(quadgramoftext.ngram_fd.items()))[i][0][j]+" "
    print(tempstr)