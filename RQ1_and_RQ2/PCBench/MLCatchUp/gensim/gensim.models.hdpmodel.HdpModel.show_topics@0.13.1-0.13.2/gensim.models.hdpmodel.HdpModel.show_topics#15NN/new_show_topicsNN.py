from gensim.models import HdpModel
from gensim.corpora import Dictionary
documents = [['cat', 'dog', 'mouse'], ['dog', 'wolf', 'rabbit'], ['fish', 'shark', 'whale']]
dictionary = Dictionary(documents)
corpus = [dictionary.doc2bow(doc) for doc in documents]
hdp = HdpModel(corpus=corpus, id2word=dictionary)
topics = hdp.show_topics(log=False, formatted=True, num_topics=20, num_words=20)
