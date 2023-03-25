from nltk.corpus import wordnet #wordnet is a library for context of words 
# import nltk 
# nltk.download('wordnet')
# import nltk 
# nltk.download('omw-1.4')

for i in wordnet.synsets("Live"):
    print(i,i.definition())

from nltk.wsd import lesk #lesk internally uses wordnet, nltk.corpus-wordnet helps us to get all meanings and contexts of the word 
#but nltk.wsd library helps to get the meaning of the word in the sentence according to its context 

context1=lesk("My name is prathamesh patil,i am 20 years old,i use a mouse","mouse")
print(context1,context1.definition())