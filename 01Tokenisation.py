#Manual word tokenisation

text="I believe this would help the reader understand how tokenisation works , as well as realise its importance"

wlis=text.split()
print("This is word tokenisation")
print(wlis)

slis=text.split(",")
print("This is sentence tokenisation")
print(slis)
swlis=[]
for i in slis:
    swlis.append(i.split())

print("This is word sentence tokenisation")
print(swlis)


swlis1=[x.split() for x in slis]
print("This is word sentence tokenisation using list comprehension")
print(swlis1)


#Tokenisation with the help of nltk library
from nltk.tokenize import word_tokenize,sent_tokenize
print("\n\n\n\n\n\n")
text1="I believe this would help the reader understand how tokenisation works . as well as realise its importance"

wtoken=word_tokenize(text1)
print(wtoken)
stoken=sent_tokenize(text1)
print(stoken)

stokenlcomp=[word_tokenize(x) for x in stoken]
print(stokenlcomp)

