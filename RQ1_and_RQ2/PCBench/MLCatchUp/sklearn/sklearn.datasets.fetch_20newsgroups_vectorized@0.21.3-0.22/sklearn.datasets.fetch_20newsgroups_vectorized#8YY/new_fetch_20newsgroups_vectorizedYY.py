from sklearn.datasets import fetch_20newsgroups_vectorized
newsgroups_train = fetch_20newsgroups_vectorized('train', (), data_home='/home/zhang/sklearn_data', normalize=True)
