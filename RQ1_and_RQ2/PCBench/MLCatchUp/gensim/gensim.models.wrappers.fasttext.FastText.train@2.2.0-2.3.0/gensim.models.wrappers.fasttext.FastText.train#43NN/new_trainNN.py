from gensim.models.wrappers import FastText
ft_path = '/home/zhang/fastText/build/fasttext'
corpus_file = '/home/zhang/corpus.txt'
output_file = '/home/zhang/'
model = FastText.train(ft_path, corpus_file, output_file, 'cbow', 100, 0.025, 5, 1, 'ns', word_ngrams=1)
