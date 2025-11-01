import nltk
from nltk import word_tokenize, pos_tag,ne_chunk

#Named Entity Regonition- NLP
#Sample application : Used in Resume screening
sentence_ne = "Jhon works in google in NewYork"
tokens_ne = word_tokenize(sentence_ne)
tags_ne =ne_chunk(tokens_ne)
print(tags_ne)

'''
Tagging in NLP is like giving labels to words so the computer knows what each word does in a sentence.

💬 Example sentence

"The cat is sleeping."

Tagging adds labels (or tags) to each word:

The → Determiner (a word that points to something)

cat → Noun (a thing)

is → Verb (an action or being word)

sleeping → Verb (action)

So, the computer can understand how the sentence works.

🧩 Why it’s useful

By tagging, computers can:

Understand grammar (who’s doing what) 🧱

Find important words 📌

Help in translation, question answering, and summarization

🧙‍♂️ Analogy

Imagine you’re sorting LEGO bricks:

Red = nouns

Blue = verbs

Yellow = adjectives

Tagging is like color-coding words so the computer can see the sentence’s structure!

🔖 Types of tagging

POS Tagging (Part of Speech): tells if a word is a noun, verb, adjective, etc.

NER Tagging (Named Entity Recognition): tells if a word is a person, place, date, etc.
'''