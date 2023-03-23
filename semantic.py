import spacy  # importing spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

"""

Cat and monkey have a higher similarity because they are both animals.
Banana and monkey have a significant similarity, probably beacuse monkey is associated often with banana.
Banana does not have any significant similarity with cat.

"""
import spacy  # importing spacy
nlp = spacy.load('en_core_web_sm') 

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

"""

Cat and monkey have a higher similarity but it is lower than that between banana and monkey.
Banana and monkey have the highest similarity.
The interesting thing is that also Banana have a significant similarity with cat.
Overall in this model all words seem to have a higher similarity to each other than in the model above.

"""

"""

Overall in en_core_web_sm  model, banana, cat and monkey seem to have a higher similarity to each other than in the model en_core_web_sm.

"""


