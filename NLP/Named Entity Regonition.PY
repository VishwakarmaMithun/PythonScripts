import nltk
from nltk import word_tokenize, pos_tag,ne_chunk

#Named Entity Regonition- NLP
#Sample application : Used in Resume screening
sentence_ne = "Jhon works in google in NewYork"
tokens_ne = word_tokenize(sentence_ne)
tags_ne =ne_chunk(tokens_ne)
print(tags_ne)

